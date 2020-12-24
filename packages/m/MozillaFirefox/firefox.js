pref("intl.locale.requested", "");
pref("geo.wifi.uri", "https://location.services.mozilla.com/v1/geolocate?key=%MOZILLA_API_KEY%");
/* Disable DoH by default */
pref("network.trr.mode", 5);
// do not disable any scope
pref("extensions.autoDisableScopes", 0);
pref("extensions.shownSelectionUI", true);
pref("extensions.langpacks.signatures.required", false);
// enable D-Bus inteface for Gnome Shell search
pref("browser.gnome-search-provider.enabled", true);
