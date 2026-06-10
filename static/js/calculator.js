/**
 * Gravel Calculator Pro — Client-Side Calculator
 * All calculations run in the browser. No data is sent to the server.
 *
 * Conversion pipeline (SRS Section 11):
 *   1. Convert all inputs to meters
 *   2. Compute area (m²)
 *   3. Volume (m³) = area × depth
 *   4. Weight (kg) = volume × density × 1000  [density in tons/m³ → ×1000 = kg/m³]
 *   5. Convert to display units
 *   6. Cost = weight/volume × price per unit
 */

(function () {
    'use strict';

    // ─── Conversion factors to meters ────────────────────────────────────────
    const TO_METERS = { ft: 0.3048, yd: 0.9144, 'in': 0.0254, m: 1, cm: 0.01 };
    const TO_METERS_SQ = { ft2: 0.092903, yd2: 0.836127, m2: 1 };

    // ─── State ────────────────────────────────────────────────────────────────
    let currentShape = 'rectangle';

    // ─── DOM refs ─────────────────────────────────────────────────────────────
    const shapeTabs        = document.querySelectorAll('.shape-tab');
    const calculateBtn     = document.getElementById('calculateBtn');
    const resetBtn         = document.getElementById('resetBtn');
    const gravelTypeSelect = document.getElementById('gravelType');
    const customDensityGrp = document.getElementById('customDensityGroup');
    const customDensityInp = document.getElementById('customDensity');
    const circleMode       = document.getElementById('circleMode');
    const circleValueLabel = document.getElementById('circleValueLabel');
    const resultsPlaceholder = document.getElementById('resultsPlaceholder');
    const resultsContent   = document.getElementById('resultsContent');
    const costCard         = document.getElementById('costCard');
    const faqButtons       = document.querySelectorAll('.faq-question');

    // ─── Shape tab switching ──────────────────────────────────────────────────
    shapeTabs.forEach(function (tab) {
        tab.addEventListener('click', function () {
            shapeTabs.forEach(function (t) {
                t.classList.remove('active');
                t.setAttribute('aria-selected', 'false');
            });
            this.classList.add('active');
            this.setAttribute('aria-selected', 'true');
            currentShape = this.dataset.shape;

            document.querySelectorAll('.shape-inputs').forEach(function (el) {
                el.classList.add('hidden');
            });
            var target = document.getElementById('inputs-' + currentShape);
            if (target) target.classList.remove('hidden');
            clearErrors();
        });
    });

    // ─── Circle mode label ────────────────────────────────────────────────────
    if (circleMode) {
        circleMode.addEventListener('change', function () {
            if (circleValueLabel) circleValueLabel.textContent = this.value === 'diameter' ? 'Diameter' : 'Radius';
        });
    }

    // ─── Custom gravel density ────────────────────────────────────────────────
    if (gravelTypeSelect) {
        gravelTypeSelect.addEventListener('change', function () {
            if (this.value === 'custom') {
                customDensityGrp.classList.remove('hidden');
            } else {
                customDensityGrp.classList.add('hidden');
            }
        });
    }

    // ─── Calculate ────────────────────────────────────────────────────────────
    if (calculateBtn) {
        calculateBtn.addEventListener('click', calculate);
    }

    function calculate() {
        clearErrors();
        var areaM2 = getAreaInM2();
        if (areaM2 === null) return;

        var depthM = getDepthInM();
        if (depthM === null) return;

        var density = getDensity();
        if (density === null) return;

        // Volume
        var volumeM3    = areaM2 * depthM;
        var volumeYd3   = volumeM3 * 1.30795;
        var volumeFt3   = volumeM3 * 35.3147;

        // Weight (density is in tons/m³, ×1000 = kg/m³)
        var weightKg    = volumeM3 * density * 1000;
        var weightTons  = weightKg / 1000;
        var weightLb    = weightKg * 2.20462;

        // Cost
        var cost = null;
        var priceVal = parseFloat(document.getElementById('price').value);
        if (!isNaN(priceVal) && priceVal >= 0) {
            var priceUnit = document.getElementById('priceUnit').value;
            cost = computeCost(priceVal, priceUnit, weightTons, weightKg, weightLb, volumeM3, volumeYd3, volumeFt3);
        } else if (document.getElementById('price').value !== '') {
            setError('err-price', 'Price must be a positive number.');
            return;
        }

        showResults(areaM2, volumeM3, volumeYd3, volumeFt3, weightKg, weightTons, weightLb, cost);
    }

    // ─── Area calculation ─────────────────────────────────────────────────────
    function getAreaInM2() {
        if (currentShape === 'rectangle') {
            var len = getPositiveFloat('length', 'err-length', 'Please enter a valid length greater than zero.');
            var wid = getPositiveFloat('width', 'err-width', 'Please enter a valid width greater than zero.');
            if (len === null || wid === null) return null;
            var lenM = len * TO_METERS[document.getElementById('lengthUnit').value];
            var widM = wid * TO_METERS[document.getElementById('widthUnit').value];
            return lenM * widM;
        }
        if (currentShape === 'circle') {
            var val = getPositiveFloat('circleValue', 'err-circle', 'Please enter a valid radius or diameter.');
            if (val === null) return null;
            var unit = document.getElementById('circleUnit').value;
            var mode = document.getElementById('circleMode').value;
            var radius = (mode === 'diameter' ? val / 2 : val) * TO_METERS[unit];
            return Math.PI * radius * radius;
        }
        if (currentShape === 'triangle') {
            var base = getPositiveFloat('base', 'err-base', 'Please enter a valid base.');
            var height = getPositiveFloat('triHeight', 'err-triHeight', 'Please enter a valid height.');
            if (base === null || height === null) return null;
            var baseM   = base   * TO_METERS[document.getElementById('baseUnit').value];
            var heightM = height * TO_METERS[document.getElementById('triHeightUnit').value];
            return (baseM * heightM) / 2;
        }
        if (currentShape === 'direct') {
            var areaVal = getPositiveFloat('area', 'err-area', 'Please enter a valid area.');
            if (areaVal === null) return null;
            return areaVal * TO_METERS_SQ[document.getElementById('areaUnit').value];
        }
        return null;
    }

    // ─── Depth ────────────────────────────────────────────────────────────────
    function getDepthInM() {
        var d = getPositiveFloat('depth', 'err-depth', 'Please enter a valid depth greater than zero.');
        if (d === null) return null;
        return d * TO_METERS[document.getElementById('depthUnit').value];
    }

    // ─── Density ──────────────────────────────────────────────────────────────
    function getDensity() {
        var val = gravelTypeSelect ? gravelTypeSelect.value : null;
        if (!val) { setError('err-gravelType', 'Please select a gravel type.'); return null; }
        if (val === 'custom') {
            var custom = getPositiveFloat('customDensity', 'err-customDensity', 'Please enter a valid density value.');
            return custom;
        }
        return parseFloat(val);
    }

    // ─── Cost ─────────────────────────────────────────────────────────────────
    function computeCost(price, unit, tons, kg, lb, m3, yd3, ft3) {
        switch (unit) {
            case 'ton':  return price * tons;
            case 'm3':   return price * m3;
            case 'yd3':  return price * yd3;
            case 'ft3':  return price * ft3;
            case 'kg':   return price * kg;
            case 'lb':   return price * lb;
            default:     return null;
        }
    }

    // ─── Display results ──────────────────────────────────────────────────────
    function showResults(areaM2, volM3, volYd3, volFt3, kg, tons, lb, cost) {
        var areaFt2 = areaM2 * 10.7639;
        setText('resArea', fmt(areaM2, 2) + ' m²  (' + fmt(areaFt2, 1) + ' ft²)');
        setText('resVolM3',   fmt(volM3, 3) + ' m³');
        setText('resVolYd3',  fmt(volYd3, 3) + ' yd³');
        setText('resVolFt3',  fmt(volFt3, 2) + ' ft³');
        setText('resWeightTons', fmt(tons, 2) + ' tons');
        setText('resWeightKg',   fmt(kg, 0) + ' kg');
        setText('resWeightLb',   fmt(lb, 0) + ' lbs');

        if (cost !== null) {
            setText('resCost', '$' + fmt(cost, 2));
            costCard.classList.remove('hidden');
        } else {
            costCard.classList.add('hidden');
        }

        resultsPlaceholder.classList.add('hidden');
        resultsContent.classList.remove('hidden');
    }

    // ─── Reset ────────────────────────────────────────────────────────────────
    if (resetBtn) {
        resetBtn.addEventListener('click', function () {
            document.getElementById('calcForm').reset();
            clearErrors();
            if (customDensityGrp) customDensityGrp.classList.add('hidden');
            resultsContent.classList.add('hidden');
            resultsPlaceholder.classList.remove('hidden');
            costCard.classList.add('hidden');
        });
    }

    // ─── FAQ accordion ────────────────────────────────────────────────────────
    faqButtons.forEach(function (btn) {
        btn.addEventListener('click', function () {
            var expanded = this.getAttribute('aria-expanded') === 'true';
            faqButtons.forEach(function (b) {
                b.setAttribute('aria-expanded', 'false');
                b.nextElementSibling.style.display = 'none';
            });
            if (!expanded) {
                this.setAttribute('aria-expanded', 'true');
                this.nextElementSibling.style.display = 'block';
            }
        });
    });

    // ─── Smooth scroll for anchor links ──────────────────────────────────────
    document.querySelectorAll('a[href^="#"]').forEach(function (link) {
        link.addEventListener('click', function (e) {
            var target = document.querySelector(this.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // ─── Helpers ──────────────────────────────────────────────────────────────
    function getPositiveFloat(id, errId, msg) {
        var el = document.getElementById(id);
        if (!el) return null;
        var val = parseFloat(el.value);
        if (isNaN(val) || val <= 0) {
            setError(errId, msg);
            el.focus();
            return null;
        }
        return val;
    }

    function setError(id, msg) {
        var el = document.getElementById(id);
        if (el) el.textContent = msg;
    }

    function clearErrors() {
        document.querySelectorAll('.field-error').forEach(function (el) { el.textContent = ''; });
    }

    function setText(id, text) {
        var el = document.getElementById(id);
        if (el) el.textContent = text;
    }

    function fmt(num, decimals) {
        return parseFloat(num.toFixed(decimals)).toLocaleString('en-US', {
            minimumFractionDigits: 0,
            maximumFractionDigits: decimals
        });
    }

})();
