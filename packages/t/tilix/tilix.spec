#
# spec file for package tilix
#
# Copyright (c) 2020 SUSE LLC
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


%define gtkd_version 3.8.5
# DMD is available only on x86*. Use LDC with dub otherwise.
# For Tumbleweed move to only use LDC
%if 0%{?suse_version} < 1550
%ifarch %{ix86} x86_64
%bcond_without dcompiler_dmd
%else
%bcond_with dcompiler_dmd
%endif
%endif
Name:           tilix
Version:        1.9.3
Release:        0
Summary:        A tiling terminal emulator based on GTK+ 3
License:        MPL-2.0 AND LGPL-3.0-only
URL:            https://github.com/gnunn1/tilix
Source0:        https://github.com/gnunn1/tilix/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# See https://github.com/dlang/dub/issues/838 on why we need to have the full source code as dependency
Source1:        https://github.com/gtkd-developers/GtkD/archive/v%{gtkd_version}.tar.gz#/GtkD-%{gtkd_version}.tar.gz
# PATCH-FIX-OPENSUSE gnome-ssh-agent.patch gh#gnunn1/tilix#870
Patch0:         gnome-ssh-agent.patch
Patch1:         dynamic-link.patch
Patch2:         fix-ldc-link.patch
# PATCH-FIX-UPSTREAM fix-meson-build.patch
Patch3:         fix-meson-build.patch
# PATCH-FIX-UPSTREAM 0001-Avoid-calling-values-on-a-shared-object.patch gh#gnunn1/tilix#1733
Patch4:         0001-Avoid-calling-values-on-a-shared-object.patch
BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig
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
BuildRequires:  pkgconfig(libunwind)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(x11)
Conflicts:      nautilus-extension-terminix
Conflicts:      terminix
%if 0%{?suse_version} > 1500
BuildRequires:  ldc
BuildRequires:  ldc-phobos-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gtkd-3) >= 3.8.5
BuildRequires:  pkgconfig(vted-3) >= 3.8.5
%else
BuildRequires:  dub
%endif
%if 0%{?suse_version} < 1550
%if %{with dcompiler_dmd}
BuildRequires:  dmd
BuildRequires:  phobos-devel
%else
BuildRequires:  ldc
BuildRequires:  ldc-phobos-devel
%endif
%endif

%description
A tiling terminal emulator for Linux using GTK+ 3

%package -n nautilus-extension-tilix
Summary:        Nautilus Extension to Open Tilix in Folders
Supplements:    (nautilus and %{name})
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
Requires:       python3-nautilus
%else
Requires:       python-nautilus
%endif

%description -n nautilus-extension-tilix
This is a Nautilus extension that allows you to open tilix in
arbitrary folders.

%lang_package

%prep
%setup -q -a 1
%patch0 -p 1
%patch4 -p 1
%if 0%{?suse_version} < 1550
%if %{with dcompiler_dmd}
%patch1 -p 1
%else
%patch2 -p 1
%endif
%endif
%if 0%{?suse_version} > 1500
%patch3 -p 1
%endif

%build
%if 0%{?suse_version} > 1500
%meson
%meson_build
%else
# Register local GtkD repository in dub
dub add-local GtkD-%{gtkd_version} %{gtkd_version}

# Build tilix
dub build --build=release

# De-register local GtkD repository in dub
dub remove-local GtkD-%{gtkd_version}
%endif
# Rename license files so that we can include them in %%license
# Both x11 and icons use LGPL-3.0-only.
cp -a data/icons/LICENSE LICENSE-data-icons
cp -a source/x11/LICENSE LICENSE-source-x11

%install
%if 0%{?suse_version} > 1500
%meson_install
%else
./install.sh %{buildroot}%{_prefix}
rm %{buildroot}%{_datadir}/glib-2.0/schemas/gschemas.compiled
%endif

%find_lang %{name} %{?no_lang_C}

%files
%license LICENSE*
%doc README.md
%{_bindir}/tilix
%{_datadir}/applications/com.gexperts.Tilix.desktop
%if 0%{?sle_version} == 120300 && 0%{?is_opensuse}
%dir %{_datadir}/metainfo
%endif
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
%{_datadir}/tilix/schemes/solarized-light.json
%{_datadir}/tilix/schemes/tango.json
%dir %{_datadir}/tilix/scripts
%{_datadir}/tilix/scripts/tilix_int.sh
%{_datadir}/icons/hicolor/scalable/apps/com.gexperts.Tilix.svg
%if 0%{?suse_version} > 1500
%{_datadir}/icons/hicolor/symbolic/apps/com.gexperts.Tilix-symbolic.svg
%else
%{_datadir}/icons/hicolor/scalable/apps/com.gexperts.Tilix-symbolic.svg
%{_datadir}/tilix/schemes/yaru.json
%endif
%{_mandir}/man1/tilix.1%{?ext_man}
%{_datadir}/glib-2.0/schemas/com.gexperts.Tilix.gschema.xml
%{_datadir}/dbus-1/services/com.gexperts.Tilix.service

%files -n nautilus-extension-tilix
%dir %{_datadir}/nautilus-python
%dir %{_datadir}/nautilus-python/extensions
%{_datadir}/nautilus-python/extensions/open-tilix.py

%files lang -f %{name}.lang

%changelog
