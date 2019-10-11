pref("intl.locale.requested", "");
pref("geo.wifi.uri", "https://location.services.mozilla.com/v1/geolocate?key=%MOZILLA_API_KEY%");
/* Disable DoH by default */
pref("network.trr.mode", 5);
// do not disable system-global or app-global extensions
pref("extensions.autoDisableScopes", 3);
pref("extensions.shownSelectionUI", true);
