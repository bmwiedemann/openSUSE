#
# spec file for package hamster-time-tracker
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global ext_version 0.10.0

# ext_gnome_version: latest GNOME shell version supported
# min_gnome_version: earliest GNOME shell version supported
%if 0%{?suse_version} >= 1550
%global ext_gnome_version 44
%global min_gnome_version 3.34
%else
%if 0%{?sle_version} >= 150400
%global ext_gnome_version 41
%global min_gnome_version 3.34
%else
%if 0%{?sle_version} >= 150200
%global ext_gnome_version 3.34
%global min_gnome_version 3.32
%else
%global ext_gnome_version 3.30
%global min_gnome_version 3.10
%endif
%endif
%endif

%global ext_uuid contact@projecthamster.org
%bcond_without extension

Name:           hamster-time-tracker
Version:        3.0.3~20
Release:        0
Summary:        A time tracker for GNOME
License:        CC-BY-SA-3.0 AND GPL-3.0-or-later
Group:          Productivity/Other
URL:            https://github.com/projecthamster/hamster
Source:         hamster-time-tracker-%{version}.tar.xz
# Pulled from github, see _service
Source1:        hamster-shell-extension-%{ext_version}.tar.gz
# necessary for GNOME < 3.32
Source2:        https://gitlab.gnome.org/GNOME/gnome-shell-extensions/raw/gnome-3-30/lib/convenience.js
# avoid rpm error: env-script-interpreter
Patch1:         replace-env-python-invocation-by-direct-call.patch
Patch2:         waf-skip-gsettings-schema-compilation.patch
# Patches for GNOME extension
# GNOME up to 3.30
Patch101:       0101-Don-t-try-to-access-controller.activities-before-it-.patch
Patch102:       0102-Fix-disable-callback-gnome-shell-3.30-compatibility.patch
Patch103:       0103-convenience.js-has-been-removed-in-GNOME-extensions-.patch
Patch104:       0104-Makefile-allow-shipping-convenience.js.patch
Patch105:       0105-metadata.json-mark-GNOME-3.30-as-supported.patch
Patch106:       0106-Fix-installation-instructions-matches-Ubuntu-18.04-T.patch
Patch107:       0107-metadata.json-remove-version-field.patch
# GNOME 3.32
Patch108:       0108-drop-convenience.js.patch
Patch109:       0109-make-test-style-set-esversion-to-6-for-GNOME-3.32.patch
Patch110:       0110-Mark-GNOME-3.32-as-supported-all-others-as-unsupport.patch
Patch111:       0111-Port-GObject-classes-to-JS6-classes.patch
Patch112:       0112-add-jshint-validthis-to-silence-warnings-about-stric.patch
Patch113:       0113-todaysFactsWidget-add-missing-bind.patch
Patch114:       0114-replace-Lang.bind-with-function-.bind.patch
Patch115:       0115-Port-non-GObject-class-to-JS6.patch
Patch116:       0116-extension.js-add-jshint-validthis-hints.patch
Patch117:       0117-extension.js-fix-indentation-after-previous-change.patch
Patch118:       0118-Don-t-log-ACTIVITIES-at-every-refresh.patch
Patch119:       0119-doc-remove-broken-link-to-usejsdoc.org.patch
# GNOME 3.34
Patch120:       0120-factsBox-use-GObject.registerClass.patch
Patch121:       0121-panelWidget-fix-object.actor-is-deprecated-warning.patch
Patch122:       0122-metadata.json-mark-GNOME-3.34-as-supported.patch
Patch123:       0123-Makefile-don-t-fail-if-zip-is-unavailable.patch
Patch124:       0124-Makefile-collect-must-depend-on-build.patch
# GNOME 3.36
Patch125:       0125-todaysFactsWidget-replace-Clutter.TableLayout-with-C.patch
Patch126:       0126-Fix-GNOME-shell-error-message-about-factsBox.FactsBo.patch
Patch127:       0127-Makefile-configurable-extension-UUID.patch
Patch128:       0128-metadata.json.in-mark-GNOME-3.36-supported.patch
Patch129:       0129-README.rst-mention-the-GNOME-extensions-tool.patch
Patch130:       0130-README.rst-Add-a-section-about-UUID-changing.patch
Patch131:       0131-metadata.json.in-fix-json-syntax-error.patch
Patch132:       0132-Update-README.st.patch
Patch133:       0133-Bump-latest-validated-gnome-shell-version-1.patch
Patch134:       0134-README-mention-GNOME-shell-compatibility-of-this-ver.patch
Patch135:       0135-README.rst-document-GNOME-shell-compatibility.patch
Patch136:       0136-ongoingFactEntry-stop-using-deprecated-Clutter-key-s.patch
Patch137:       0137-README.rst-update-GNOME-shell-compatibility-informat.patch
Patch138:       0138-Makefile-Add-install-user-target.patch
Patch139:       0139-Makefile-Add-install-target.patch
Patch140:       0140-README-Add-description-of-install-targets.patch
Patch141:       0141-Update-reST-syntax.patch
Patch142:       0142-Update-reST-syntax-take-2.patch
# GNOME 3.38
Patch143:       0143-Document-GNOME-3.38-compatibility.patch
Patch144:       0144-panelWidget-Remove-show-method.patch
Patch145:       0145-panelWidget-Rename-toggle-to-toggle_menu.patch
# GNOME 3.40
Patch146:       0146-Makeing-it-work-with-Gnome-40.-340.patch
Patch147:       0147-fixup-Makeing-it-work-with-Gnome-40.-340.patch
Patch148:       0148-display-total-time-for-the-day.patch
Patch149:       0149-Extension-configuration-add-a-new-option-center-with.patch
Patch150:       0150-Improve-description-of-center-positioning.patch
Patch151:       0151-Default-shortcut-Super-t.patch
# GNOME 41-44
Patch152:       0152-metadata.json-add-support-for-GNOME-41.patch
Patch153:       0153-metadata.json.in-add-support-for-GNOME-42.patch
Patch154:       0154-prefs.js-handle-different-return-values-of-Gtk.accel.patch
Patch155:       0155-Use-of-ellipsis-instead-of-tripledot.patch
Patch156:       0156-Use-ellipsis-instead-of-triple-dot-.-in-translations.patch
Patch157:       0157-Add-Gnome-Shell-43-compatibility.patch
Patch158:       0158-Add-basic-gnome-44-support.patch
Patch159:       0159-Report-errors-in-DBUS-calls.patch
Patch160:       0160-Report-errors-on-initial-DBUS-connection.patch
Patch161:       0161-Gracefully-handle-hamster-DBUS-disappearing.patch

BuildRequires:  fdupes
BuildRequires:  intltool
# For detecting typelib() dependencies
BuildRequires:  gobject-introspection
# "waf configure" checks for these
BuildRequires:  dbus-1-glib-devel
BuildRequires:  glib2-devel
# for help files
BuildRequires:  itstool
# for the python3_sitelib macro
BuildRequires:  python3-devel
# For suse_update_desktop_file
BuildRequires:  update-desktop-files
# For ownership on icon directories
BuildRequires:  hicolor-icon-theme
%if %{with extension}
BuildRequires:  zip
%endif
# Note:
# - we do not have the gnomeapplet bindings anymore (it doesn't work with
#   GNOME 3), so we don't add a Requires/Recommends for it.
# - the gnome python module is needed only for the applet, and since we don't
#   have it, we don't need a dependency on python-gnome
Requires:       intltool
Requires:       python3-cairo
Requires:       python3-dbus-python
Requires:       python3-gobject-Gdk
Requires:       python3-pyxdg

%if 0%{?suse_version} < 1330
# see https://en.opensuse.org/openSUSE:Packaging_Conventions_RPM_Macros
Requires(post): update-desktop-files
Requires(postun):update-desktop-files
Requires(post): gtk3-tools
Requires(postun):gtk3-tools
%endif

Recommends:     %{name}-lang
# hamster-time-tracker used to be developed as hamster-applet. Last ever release was 2.91.2
Obsoletes:      docky-hamster-applet < 2.91.2
Obsoletes:      hamster-applet < 2.91.2
Provides:       docky-hamster-applet = 2.91.2
Provides:       hamster-applet = 2.91.2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Project Hamster is a time tracker for keeping track on how much time
is spent during the day on activities that are set up.

%lang_package

%prep
%setup -q -n hamster-time-tracker-%{version} -a1
%patch1 -p1
%patch2 -p1
%if %{with extension}
cd hamster-shell-extension-%{ext_version}
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch107 -p1
# SLE15-SP2 / Leap 15.2:
# GNOME 3.34 support for shell extension
# https://github.com/projecthamster/hamster-shell-extension/pull/316
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
%patch108 -p1
%patch109 -p1
%patch110 -p1
%patch111 -p1
%patch112 -p1
%patch113 -p1
%patch114 -p1
%patch115 -p1
%patch116 -p1
%patch117 -p1
%patch118 -p1
%patch119 -p1
%patch120 -p1
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1
# TW / 15.4: GNOME 41+ support
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
%patch125 -p1
%patch126 -p1
%patch127 -p1
%patch128 -p1
%patch129 -p1
%patch130 -p1
%patch131 -p1
%patch132 -p1
%patch133 -p1
%patch134 -p1
%patch135 -p1
%patch136 -p1
%patch137 -p1
%patch138 -p1
%patch139 -p1
%patch140 -p1
%patch141 -p1
%patch142 -p1
%patch143 -p1
%patch144 -p1
%patch145 -p1
%patch146 -p1
%patch147 -p1
%patch148 -p1
%patch149 -p1
%patch150 -p1
%patch151 -p1
%patch152 -p1
%patch153 -p1
%patch154 -p1
%patch155 -p1
%patch156 -p1
%patch157 -p1
%patch158 -p1
%patch159 -p1
%patch160 -p1
%patch161 -p1
%endif
%endif

mkdir build
cp %{SOURCE2} build
%endif

%build
./waf --prefix=%{_prefix} --libdir=%{_libdir} --libexecdir=%{_libexecdir} \
      --skip-icon-cache-update configure build
%if %{with extension}
cd hamster-shell-extension-%{ext_version}
make dist
%endif

%install
./waf install --destdir=%{buildroot}
%find_lang hamster %{?no_lang_C}
%suse_update_desktop_file org.gnome.Hamster.GUI TimeUtility

%if %{with extension}
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{ext_uuid}
tar xz -f hamster-shell-extension-%{ext_version}/dist/%{ext_uuid}.tar.gz \
    -C %{buildroot}%{_datadir}/gnome-shell/extensions/%{ext_uuid}
%endif

%fdupes %{buildroot}

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-, root, root)
%license COPYING
%doc AUTHORS NEWS.md README.md MAINTAINERS
%{_bindir}/hamster
%{_datadir}/applications/org.gnome.Hamster.GUI.desktop
%{_datadir}/dbus-1/services/org.gnome.Hamster.service
%{_datadir}/dbus-1/services/org.gnome.Hamster.WindowServer.service
%{_datadir}/dbus-1/services/org.gnome.Hamster.GUI.service
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/hamster/
%{_libexecdir}/hamster/
%{python3_sitelib}/hamster/
%{_datadir}/bash-completion/completions/hamster.bash
%{_datadir}/metainfo/org.gnome.Hamster.GUI.metainfo.xml
%{_datadir}/glib-2.0/schemas/org.gnome.hamster.gschema.xml
%{_datadir}/help/C/hamster

# Derive "next higher" GNOME version to be able to use "<" in Requires
%define next_higher() %{lua: x = tonumber(rpm.expand('%1'))
   if x < 4 then print(string.format("%.02f", x + 0.01)) else print(x + 1) end}

%package -n gnome-shell-extension-hamster-time-tracker
Version:        3.0.3~20_%{ext_version}_%{ext_gnome_version}
Release:        0
Summary:        Hamster time tracker extension for GNOME Shell
License:        GPL-3.0-only
Group:          System/GUI/GNOME
Requires:       %{name}
Requires:       gnome-shell < %{next_higher %{ext_gnome_version}}
Requires:       gnome-shell >= %{min_gnome_version}
Supplements:    packageand(gnome-shell:%{name})
# The predecessor package had a broken version number.
Obsoletes:      gnome-shell-extension-hamster < 2.2.20.10.1
Provides:       gnome-shell-extension-hamster = 2.2.20.10.1

%description -n gnome-shell-extension-hamster-time-tracker

GNOME Shell extension to track activities in hamster via the main
GNOME shell menu. Packaged for openSUSE Factory because the
upstream version on extensions.gnome.org often leaks behind current
GNOME shell development.

%files lang -f hamster.lang

%if %{with extension}
%files -n gnome-shell-extension-hamster-time-tracker
%defattr(-, root, root)
%dir %{_datadir}/gnome-shell
%{_datadir}/gnome-shell/extensions
%license hamster-shell-extension-%{ext_version}/LICENSE
%doc hamster-shell-extension-%{ext_version}/README.rst
%doc hamster-shell-extension-%{ext_version}/HISTORY.rst
%doc hamster-shell-extension-%{ext_version}/AUTHORS.rst
%doc hamster-shell-extension-%{ext_version}/CONTRIBUTING.rst
%endif

%changelog
