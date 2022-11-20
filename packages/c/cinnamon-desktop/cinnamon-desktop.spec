#
# spec file for package cinnamon-desktop
#
# Copyright (c) 2022 SUSE LLC
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


%define soname  libcinnamon-desktop
%define sover   4
%define soname_cvc libcvc
%define sover_cvc 0
%define typelib typelib-1_0-CinnamonDesktop-3_0
%define typelib_cvc typelib-1_0-Cvc-1_0
Name:           cinnamon-desktop
Version:        5.4.2
Release:        0
Summary:        Libcinnamon-desktop API
License:        GPL-2.0-or-later AND MIT
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/cinnamon-desktop
Source:         https://github.com/linuxmint/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# Some documentation for people writing branding packages, shipped in the branding-upstream package.
Source1:        README.Gsettings-overrides
Source2:        baselibs.conf
# PATCH-FIX-OPENSUSE cinnamon-desktop-correct-background-path.patch sor.alexi@meowr.ru -- Fix path to Adwaita background.
Patch0:         %{name}-correct-background-path.patch
# PATCH-FIX-UPSTREAM fix_return_value_void.patch andythe_great@pm.me -- Fix return with a value in a void function gh#linuxmint/cinnamon-desktop#225
Patch1:         fix_return_value_void.patch
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.22.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.37.3
BuildRequires:  pkgconfig(glib-2.0) >= 2.37.3
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.7
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10.0
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(xext) >= 1.1
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xrandr) >= 1.3

%description
cinnamon-desktop contains the libcinnamon-desktop library, the
cinnamon-about program as well as some desktop-wide documents.

The libcinnamon-desktop library provides API shared by several
applications on the desktop, but that cannot live in the platform
for various reasons. There is no API or ABI guarantee, although we
are doing our best to provide stability. Documentation for the API
is available with gtk-doc.

%package -n %{soname}%{sover}
Summary:        Libcinnamon-desktop API
Group:          System/Libraries
Requires:       %{soname}-data >= %{version}
Provides:       %{name} = %{version}
Provides:       %{soname} = %{version}
Obsoletes:      %{name} < %{version}

%description -n %{soname}%{sover}
cinnamon-desktop contains the libcinnamon-desktop library, the
cinnamon-about program as well as some desktop-wide documents.

The libcinnamon-desktop library provides API shared by several
applications on the desktop, but that cannot live in the platform
for various reasons. There is no API or ABI guarantee, although we
are doing our best to provide stability. Documentation for the API
is available with gtk-doc.

%lang_package -n %{soname}

%package -n %{soname}-data
Summary:        Libcinnamon-desktop API -- Common Files
Group:          System/GUI/Other
Requires:       %{soname}-data-branding = %{version}
Requires:       pam
Requires:       python3-gobject
Recommends:     %{soname}-lang
# cinnamon-desktop-lang was last used in openSUSE 13.2.
Provides:       %{name}-lang = %{version}
Obsoletes:      %{name}-lang < %{version}
%glib2_gsettings_schema_requires

%description -n %{soname}-data
cinnamon-desktop contains the libcinnamon-desktop library, the
cinnamon-about program as well as some desktop-wide documents.

This package includes files that are shared between several
Cinnamon applications (configuration schemas).

%package -n %{soname}-data-branding-upstream
Summary:        Upstream definitions of default settings and applications
Group:          System/GUI/Other
Requires:       %{soname}-data = %{version}
Requires:       gnome-backgrounds
Requires:       metatheme-adwaita-common
Supplements:    (%{soname}-data and branding-upstream)
Conflicts:      %{soname}-data-branding
Provides:       %{soname}-data-branding = %{version}
BuildArch:      noarch
#BRAND: A /usr/share/glib-2.0/schemas/$NAME.gschema.override file can
#BRAND: be used to override the default value for GSettings keys. See
#BRAND: README.Gsettings-overrides for more details. The branding
#BRAND: package should then have proper Requires for features changed
#BRAND: with such an override file.

%description -n %{soname}-data-branding-upstream
This package provides upstream defaults for settings stored with
GSettings and applications used by the MIME system.

%package -n %{typelib}
Summary:        Libcinnamon-desktop API -- Introspection bindings
Group:          System/Libraries

%description -n %{typelib}
cinnamon-desktop contains the libcinnamon-desktop library, the
cinnamon-about program as well as some desktop-wide documents.

This package provides the GObject Introspection bindings for
libcinnamon-desktop.

%package -n %{soname}-devel
Summary:        Libcinnamon-desktop API -- Development Files
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}
Requires:       %{typelib} = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(gtk+-3.0)
Requires:       pkgconfig(xkbfile)
# cinnamon-desktop-devel was last used in openSUSE 12.3.
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}

%description -n %{soname}-devel
cinnamon-desktop contains the libcinnamon-desktop library, the
cinnamon-about program as well as some desktop-wide documents.

This package contains development files for libcinnamon-desktop.

%package -n %{soname_cvc}%{sover_cvc}
Summary:        LibCVC API
Group:          System/Libraries

%description -n %{soname_cvc}%{sover_cvc}
Utility library for volume control of pulseaudio from gobject-based
Cinnamon modules/applications.

%package -n %{typelib_cvc}
Summary:        LibCVC API -- Introspection bindings
Group:          System/Libraries

%description -n %{typelib_cvc}
Utility library for volume control of pulseaudio from gobject-based
Cinnamon modules/applications.

This package provides the GObject Introspection bindings for libcvc.

%package -n %{soname_cvc}-devel
Summary:        LibCVC API -- Development Files
Group:          Development/Libraries/C and C++
Requires:       %{soname_cvc}%{sover_cvc} = %{version}
Requires:       %{typelib_cvc} = %{version}
Requires:       pkgconfig
Requires:       pkgconfig(libpulse)
Requires:       pkgconfig(libpulse-mainloop-glib)

%description -n %{soname_cvc}-devel
Utility library for volume control of pulseaudio from gobject-based
Cinnamon modules/applications.

This package contains development files for libcvc.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
cp -a %{SOURCE1} .

%build
%if 0%{?suse_version} < 1500
mkdir -p bin
cat > bin/g-ir-scanner << EOF
#!/bin/sh
# This breaks the build. There are also useless entries in shared-library= in
# .gir files but that doesn't seem to have any actual implications here.
export SUSE_ASNEEDED=0
exec %{_bindir}/g-ir-scanner "\$%{nil}@"
EOF
chmod a+x bin/g-ir-scanner

export PATH="$PWD/bin:$PATH"
%endif
%meson
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}

%if 0%{?suse_version} < 1500
%post -n %{soname}-data
%glib2_gsettings_schema_post

%postun -n %{soname}-data
%glib2_gsettings_schema_postun
%endif

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%post -n %{soname_cvc}%{sover_cvc} -p /sbin/ldconfig

%postun -n %{soname_cvc}%{sover_cvc} -p /sbin/ldconfig

%files -n %{soname}%{sover}
%license COPYING*
%doc AUTHORS README debian/changelog
%{_libdir}/%{soname}.so.%{sover}*

%files -n %{soname}-lang -f %{name}.lang

%files -n %{soname}-data
%license COPYING*
%doc AUTHORS README debian/changelog
#%%{_bindir}/cinnamon-desktop-migrate-mediakeys
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/%{soname}/

%files -n %{soname}-data-branding-upstream
%doc README.Gsettings-overrides

%files -n %{typelib}
%{_libdir}/girepository-1.0/CinnamonDesktop-3.0.typelib
%{_libdir}/girepository-1.0/CDesktopEnums-3.0.typelib

%files -n %{soname}-devel
%{_includedir}/%{name}/
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{soname}.so
%{_datadir}/gir-1.0/CinnamonDesktop-3.0.gir
%{_datadir}/gir-1.0/CDesktopEnums-3.0.gir

%files -n %{soname_cvc}%{sover_cvc}
%license COPYING*
%doc AUTHORS README debian/changelog
%{_libdir}/%{soname_cvc}.so.%{sover_cvc}*

%files -n %{typelib_cvc}
%{_libdir}/girepository-1.0/Cvc-1.0.typelib

%files -n %{soname_cvc}-devel
%{_libdir}/pkgconfig/cvc.pc
%{_libdir}/%{soname_cvc}.so
%{_datadir}/gir-1.0/Cvc-1.0.gir

%changelog
