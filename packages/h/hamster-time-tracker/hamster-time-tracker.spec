#
# spec file for package hamster-time-tracker
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%global ext_uuid contact@projecthamster.org
%bcond_without extension

Name:           hamster-time-tracker
Version:        2.2.2
Release:        0
Summary:        A time tracker for GNOME
License:        GPL-3.0-or-later AND CC-BY-SA-3.0
Group:          Productivity/Other
Url:            https://github.com/projecthamster/hamster
Source:         %{name}-%{version}.tar.xz
# https://github.com/projecthamster/hamster-shell-extension/archive/0.10.0.tar.gz
Source1:        hamster-shell-extension-%{ext_version}.tar.gz
Source2:        https://gitlab.gnome.org/GNOME/gnome-shell-extensions/raw/gnome-3-30/lib/convenience.js
# PATCH-FEATURE-UPSTREAM https://github.com/projecthamster/hamster/pull/336
Patch0:         appdata.patch
# avoid rpm error: env-script-interpreter
Patch1:         env-script-interpreter.patch
Patch2:         0002-Overview-fix-gtk.show_uri-call.patch
Patch3:         0003-Overview-add-help-menu-entry.patch
Patch4:         0004-waf-install-help-files-into-usr-share-help.patch
Patch5:         0005-wscript-install-bash-completion-to-usr-share-bash-co.patch
Patch6:         0006-Overview-show-error-window-if-opening-help-fails.patch
# Patches for GNOME extension
Patch101:       0001-Don-t-try-to-access-controller.activities-before-it-.patch
Patch102:       0002-Fix-disable-callback-gnome-shell-3.30-compatibility.patch
Patch103:       0003-convenience.js-has-been-removed-in-GNOME-extensions-.patch
Patch104:       0004-metadata.json-mark-GNOME-3.30-as-supported.patch
Patch105:       0005-Makefile-allow-shipping-convenience.js.patch
Patch106:       0006-Makefile-don-t-zip.patch
Patch107:       0007-drop-convenience.js.patch
Patch108:       0008-make-test-style-set-esversion-to-6-for-GNOME-3.32.patch
Patch109:       0009-Mark-GNOME-3.32-as-supported-all-others-as-unsupport.patch
Patch110:       0010-Port-GObject-classes-to-JS6-classes.patch
Patch111:       0011-add-jshint-validthis-to-silence-warnings-about-stric.patch
Patch112:       0012-todaysFactsWidget-add-missing-bind.patch
Patch113:       0013-replace-Lang.bind-with-function-.bind.patch
Patch114:       0014-Port-non-GObject-class-to-JS6.patch
Patch115:       0015-extension.js-add-jshint-validthis-hints.patch
Patch116:       0016-extension.js-fix-indentation-after-previous-change.patch
Patch117:       0017-Don-t-log-ACTIVITIES-at-every-refresh.patch
Patch118:       0018-doc-remove-broken-link-to-usejsdoc.org.patch
BuildRequires:  fdupes
BuildRequires:  intltool
# For detecting typelib() dependencies
BuildRequires:  gobject-introspection
# waf requires python2
BuildRequires:  python
# "waf configure" checks for these
BuildRequires:  dbus-1-glib-devel
BuildRequires:  glib2-devel
# for help files
BuildRequires:  xml2po
# for gconf-related rpm macros
BuildRequires:  gconf2-devel
# for the python3_sitelib macro
BuildRequires:  python3-devel
# For suse_update_desktop_file
BuildRequires:  update-desktop-files
# For ownership on icon directories
BuildRequires:  hicolor-icon-theme
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
%gconf_schemas_requires

%if 0%{?suse_version} < 1330
# see https://en.opensuse.org/openSUSE:Packaging_Conventions_RPM_Macros
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
Requires(post):	gtk3-tools
Requires(postun): gtk3-tools
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
%setup -q -n %{name}-%{version} -a1
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%if %{with extension}
cd hamster-shell-extension-%{ext_version}
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1
%patch106 -p1
# Tumbleweed: GNOME 3.32 support for shell extension
# https://github.com/projecthamster/hamster-shell-extension/pull/312
%if 0%{?suse_version} >= 1550
%patch107 -p1
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
%endif
mkdir build
cp %{SOURCE2} build
%endif

%build
./waf --prefix=%{_prefix} configure build
%if %{with extension}
cd hamster-shell-extension-%{ext_version}
make dist
%endif

%install
./waf install --destdir=%{buildroot} --libdir=%{_libdir} --libexecdir=%{_libexecdir}
# hack: waf installs in the python2 directory, but hamster should be in python3 now
mkdir -p %{buildroot}%{python3_sitelib}
mv %{buildroot}%{python_sitelib}/hamster %{buildroot}%{python3_sitelib}
%find_gconf_schemas
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file hamster-time-tracker X-SuSE-TimeUtility
%suse_update_desktop_file hamster-time-tracker-overview X-SuSE-TimeUtility

%if %{with extension}
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{ext_uuid}
tar xz -f hamster-shell-extension-%{ext_version}/dist/%{ext_uuid}.tgz \
    -C %{buildroot}%{_datadir}/gnome-shell/extensions/%{ext_uuid}
%endif

%fdupes %{buildroot}

%pre -f %{name}.schemas_pre

%preun -f %{name}.schemas_preun

%posttrans -f %{name}.schemas_posttrans

%if 0%{?suse_version} < 1330

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%endif

%files -f %{name}.schemas_list
%defattr(-, root, root)
%license COPYING
%doc AUTHORS NEWS README.md MAINTAINERS
%{_bindir}/hamster
%{_datadir}/applications/hamster-time-tracker.desktop
%{_datadir}/applications/hamster-time-tracker-overview.desktop
%{_datadir}/applications/hamster-windows-service.desktop
%{_datadir}/dbus-1/services/org.gnome.hamster.service
%{_datadir}/dbus-1/services/org.gnome.hamster.Windows.service
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/*.svg
%{_datadir}/%{name}/
%{_libexecdir}/%{name}/
%{python3_sitelib}/hamster/
%{_datadir}/bash-completion/completions/hamster.bash
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.appdata.xml
%dir %{_datadir}/help
%{_datadir}/help/C

%package -n gnome-shell-extension-hamster
Version:        2.2.2%{ext_version}
Release:        0
Summary:        Hamster time tracker for GNOME Shell status menu
License:        GPL-3.0-only
Group:          System/GUI/GNOME
%if 0%{?suse_version} >= 1550
Requires:       gnome-shell >= 3.32
%else
Requires:       gnome-shell < 3.32
Requires:       gnome-shell >= 3.10
%endif
Requires:       %{name}
Supplements:    packageand(gnome-shell:%{name})

%description -n gnome-shell-extension-hamster
GNOME Shell extension to track activities quickly and efficiently via
the main GNOME shell menu. Packaged for openSUSE Factory because the
upstream version on extensions.gnome.org often leaks behind current
GNOME shell development.

%files lang -f %{name}.lang

%if %{with extension}
%files -n gnome-shell-extension-hamster
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
