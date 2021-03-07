#
# spec file for package tilix
#
# Copyright (c) 2021 SUSE LLC
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


#
%define _lto_cflags %{nil}
Name:           tilix
Version:        1.9.4
Release:        0
Summary:        A tiling terminal emulator based on GTK+ 3
License:        MPL-2.0 AND LGPL-3.0-only
URL:            https://github.com/gnunn1/tilix
Source0:        https://github.com/gnunn1/tilix/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
%if 0%{?suse_version} < 1550 
Source1:        com.gexperts.Tilix.appdata.xml
%endif
# PATCH-FIX-OPENSUSE gnome-ssh-agent.patch gh#gnunn1/tilix#870
Patch0:         gnome-ssh-agent.patch
# PATCH-FIX-UPSTREAM tilix-1.9.4-localized-man.patch -- https://github.com/gnunn1/tilix/pull/2006
Patch1:         tilix-1.9.4-localized-man.patch
%if 0%{?suse_version} < 1550 
# PATCH-FIX-OPENSUSE 0001-Don-t-generate-appstream-meta-data-on-older-versions.patch -- Provide appdata.xml instead of generating one since we have to old version of appstream in Leap releases
Patch2:         0001-Don-t-generate-appstream-meta-data-on-older-versions.patch
%endif
BuildRequires:  AppStream
BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  ldc
BuildRequires:  ldc-phobos-devel
%if 0%{?suse_version} < 1550 
BuildRequires:  librsvg-devel
%endif
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  po4a
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dconf)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gmodule-no-export-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkd-3) >= 3.8.5
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(vted-3) >= 3.8.5
BuildRequires:  pkgconfig(x11)
Conflicts:      nautilus-extension-terminix
Conflicts:      terminix

%description
A tiling terminal emulator for Linux using GTK+ 3

%package -n nautilus-extension-tilix
Summary:        Nautilus Extension to Open Tilix in Folders
Requires:       python3-nautilus
Supplements:    (nautilus and %{name})

%description -n nautilus-extension-tilix
This is a Nautilus extension that allows you to open tilix in
arbitrary folders.

%lang_package

%prep
%autosetup -p 1

%build
%meson
%meson_build

# Rename license files so that we can include them in %%license
# Both x11 and icons use LGPL-3.0-only.
cp -a data/icons/LICENSE LICENSE-data-icons
cp -a source/x11/LICENSE LICENSE-source-x11

%install
%meson_install

%if 0%{?suse_version} < 1550 
mkdir -p %{buildroot}%{_datadir}/metainfo/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/com.gexperts.Tilix.appdata.xml
%endif

%find_lang %{name} %{?no_lang_C} --with-man

# Some localized man directories are not provided by filesystem package yet
for locale in uk en_GB hr nb_NO oc pt_PT ro sr tr zh_Hant; do
  echo "%%dir %{_mandir}/${locale}" >> %{name}.lang
  echo "%%dir %{_mandir}/${locale}/man1" >> %{name}.lang
done

%check
%meson_test

%files
%license LICENSE*
%doc README.md
%{_bindir}/tilix
%{_datadir}/applications/com.gexperts.Tilix.desktop
%{_datadir}/metainfo/com.gexperts.Tilix.appdata.xml
%dir %{_datadir}/tilix
%dir %{_datadir}/tilix/resources
%{_datadir}/tilix/resources/tilix.gresource
%dir %{_datadir}/tilix/schemes
%{_datadir}/tilix/schemes/base16-twilight-dark.json
%{_datadir}/tilix/schemes/linux.json
%{_datadir}/tilix/schemes/material.json
%{_datadir}/tilix/schemes/monokai.json
%{_datadir}/tilix/schemes/orchis.json
%{_datadir}/tilix/schemes/solarized-dark.json
%{_datadir}/tilix/schemes/yaru.json
%{_datadir}/tilix/schemes/solarized-light.json
%{_datadir}/tilix/schemes/tango.json
%dir %{_datadir}/tilix/scripts
%{_datadir}/tilix/scripts/tilix_int.sh
%{_datadir}/icons/hicolor/scalable/apps/com.gexperts.Tilix.svg
%{_datadir}/icons/hicolor/symbolic/apps/com.gexperts.Tilix-symbolic.svg
%{_mandir}/man1/tilix.1%{?ext_man}
%{_datadir}/glib-2.0/schemas/com.gexperts.Tilix.gschema.xml
%{_datadir}/dbus-1/services/com.gexperts.Tilix.service

%files -n nautilus-extension-tilix
%dir %{_datadir}/nautilus-python
%dir %{_datadir}/nautilus-python/extensions
%{_datadir}/nautilus-python/extensions/open-tilix.py

%files lang -f %{name}.lang

%changelog
