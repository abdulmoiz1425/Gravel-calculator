// Cookie consent for Google Analytics. Nothing from Google is requested until the
// visitor presses Accept. The choice is kept in localStorage (no cookie).
(function () {
    var GA_ID = 'G-KVPEYSQ98D';
    var KEY = 'gyc_analytics_consent';
    var banner = document.getElementById('consentBanner');
    if (!banner) return;

    function getChoice() {
        try { return localStorage.getItem(KEY); } catch (e) { return null; }
    }
    function setChoice(value) {
        try { localStorage.setItem(KEY, value); } catch (e) { /* choice just won't persist */ }
    }

    function loadAnalytics() {
        window['ga-disable-' + GA_ID] = false;
        if (window.__gaLoaded) return;
        window.__gaLoaded = true;
        window.dataLayer = window.dataLayer || [];
        window.gtag = function () { window.dataLayer.push(arguments); };
        var s = document.createElement('script');
        s.async = true;
        s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
        document.head.appendChild(s);
        window.gtag('js', new Date());
        window.gtag('config', GA_ID);
    }

    function clearAnalyticsCookies() {
        var host = location.hostname;
        var domains = ['', host, '.' + host];
        document.cookie.split(';').forEach(function (c) {
            var name = c.split('=')[0].trim();
            if (name.indexOf('_ga') !== 0) return;
            domains.forEach(function (d) {
                document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/' +
                    (d ? '; domain=' + d : '');
            });
        });
    }

    function hide() { banner.hidden = true; }
    function show() {
        banner.hidden = false;
        var accept = document.getElementById('consentAccept');
        if (accept) accept.focus();
    }

    document.getElementById('consentAccept').addEventListener('click', function () {
        setChoice('granted');
        loadAnalytics();
        hide();
    });
    document.getElementById('consentDeny').addEventListener('click', function () {
        setChoice('denied');
        window['ga-disable-' + GA_ID] = true;
        clearAnalyticsCookies();
        hide();
    });
    var settings = document.getElementById('cookieSettings');
    if (settings) settings.addEventListener('click', show);

    var choice = getChoice();
    if (choice === 'granted') {
        loadAnalytics();
    } else if (choice !== 'denied') {
        banner.hidden = false;
    }
})();
