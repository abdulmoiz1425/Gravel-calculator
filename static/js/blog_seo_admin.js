document.addEventListener('DOMContentLoaded', function () {
    var titleInput = document.getElementById('id_meta_title');
    var descInput = document.getElementById('id_meta_description');
    var kwTitleInput = document.getElementById('id_focus_keyword_title');
    var kwDescInput = document.getElementById('id_focus_keyword_description');

    if (!titleInput || !descInput) {
        return;
    }

    function insertStatus(input) {
        var el = document.createElement('div');
        el.className = 'seo-counter';
        input.insertAdjacentElement('afterend', el);
        return el;
    }

    var titleCounter = insertStatus(titleInput);
    var descCounter = insertStatus(descInput);
    var kwTitleStatus = kwTitleInput ? insertStatus(kwTitleInput) : null;
    var kwDescStatus = kwDescInput ? insertStatus(kwDescInput) : null;

    function statusColor(length, min, max) {
        if (length > max) return 'red';
        if (length >= min && length <= max) return 'green';
        return 'orange';
    }

    function statusLabel(color) {
        if (color === 'green') return '✅ Good';
        if (color === 'red') return '⚠️ Too long';
        return '⚠️ Too short';
    }

    function updateCounter(el, input, min, max) {
        var length = input.value.length;
        var color = statusColor(length, min, max);
        el.textContent = length + '/' + max + ' — ' + statusLabel(color);
        el.className = 'seo-counter seo-' + color;
    }

    function updateKeywordStatus(el, keywordInput, targetInput, targetLabel) {
        if (!el) return;
        var keyword = keywordInput.value.trim().toLowerCase();

        if (!keyword) {
            el.textContent = 'Enter a keyword to check presence in the ' + targetLabel + '.';
            el.className = 'seo-counter seo-neutral';
            return;
        }

        var found = targetInput.value.toLowerCase().indexOf(keyword) !== -1;
        el.textContent = found ? '✅ Found' : '⚠️ Missing';
        el.className = 'seo-counter ' + (found ? 'seo-green' : 'seo-red');
    }

    function refresh() {
        updateCounter(titleCounter, titleInput, 50, 60);
        updateCounter(descCounter, descInput, 140, 155);
        updateKeywordStatus(kwTitleStatus, kwTitleInput, titleInput, 'SEO title');
        updateKeywordStatus(kwDescStatus, kwDescInput, descInput, 'meta description');
    }

    titleInput.addEventListener('input', refresh);
    descInput.addEventListener('input', refresh);
    if (kwTitleInput) kwTitleInput.addEventListener('input', refresh);
    if (kwDescInput) kwDescInput.addEventListener('input', refresh);

    refresh();
});
