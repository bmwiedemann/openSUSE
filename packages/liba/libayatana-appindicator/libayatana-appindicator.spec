#
# spec file for package libayatana-appindicator
#
# Copyright (c) 2024 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "gtk3"
%global psuffix 3
%endif
%define sover 1
%bcond_with mono
Name:           libayatana-appindicator
Version:        0.5.93
Release:        0
Summary:        Ayatana application indicators library
License:        GPL-3.0-only AND LGPL-2.0-only AND LGPL-3.0-only
Group:          System/GUI/Other
URL:            https://github.com/AyatanaIndicators/libayatana-appindicator
Source:         https://github.com/AyatanaIndicators/libayatana-appindicator/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE libayatana-appindicator-fix-mono-dir.patch hrvoje.senjan@gmail.com -- Fix location of .pc files.
Patch0:         libayatana-appindicator-fix-mono-dir.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%if "%{flavor}" == ""
ExclusiveArch:  do-not-build
%endif
%if "%{flavor}" == "gtk2"
BuildRequires:  pkgconfig(ayatana-indicator-0.4) >= 0.8.4
BuildRequires:  pkgconfig(dbusmenu-gtk-0.4)
BuildRequires:  pkgconfig(gtk+-2.0)
%else
BuildRequires:  vala
BuildRequires:  pkgconfig(ayatana-indicator3-0.4) >= 0.8.4
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gtk+-3.0)
%endif
%if %{with mono}
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(nunit)
%if "%{flavor}" == "gtk2"
BuildRequires:  pkgconfig(gapi-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
%else
BuildRequires:  pkgconfig(gapi-3.0)
BuildRequires:  pkgconfig(gtk-sharp-3.0)
%endif
%endif

%description
A library to allow applications to add an icon into the
StatusNotifier-compatible notification area. If none are available,
it also provides an XEmbed-tray fallback.

%package -n libayatana-appindicator%{?psuffix:%{psuffix}-}%{sover}
Summary:        Ayatana application indicators library
Group:          System/Libraries
Provides:       libayatana-appindicator%{?psuffix} = %{version}

%description -n libayatana-appindicator%{?psuffix:%{psuffix}-}%{sover}
A library to allow applications to add an icon into the
StatusNotifier-compatible notification area. If none are available,
it also provides an XEmbed-tray fallback.

%package -n typelib-1_0-AyatanaAppIndicator%{?psuffix}-0_1
Summary:        Ayatana application indicators library
Group:          System/Libraries

%description -n typelib-1_0-AyatanaAppIndicator%{?psuffix}-0_1
This package contains the GObject Introspection bindings for the
ayatana appindicator library.

%package -n ayatana-appindicator%{?psuffix}-sharp
Summary:        Ayatana application indicators library for C#
Group:          System/Libraries

%description -n ayatana-appindicator%{?psuffix}-sharp
This package provides the ayatana-appindicator%{?psuffix}-sharp assembly that
allows CLI (.NET) applications to take menus from applications and
place them in the panel.

This package provides assemblies to be used by applications.

%package -n ayatana-appindicator%{?psuffix}-sharp-devel
Summary:        Development files for libayatana-appindicator%{?psuffix}-sharp
Group:          Development/Libraries/Other
Requires:       ayatana-appindicator%{?psuffix}-sharp = %{version}

%description -n ayatana-appindicator%{?psuffix}-sharp-devel
This package contains the development files for the
ayatana-appindicator%{?psuffix}-sharp library.

%package -n libayatana-appindicator%{?psuffix}-devel
Summary:        Development files for libayatana-appindicator%{?psuffix}
Group:          Development/Libraries/C and C++
Requires:       libayatana-appindicator%{?psuffix:%{psuffix}-}%{sover} = %{version}

%description -n libayatana-appindicator%{?psuffix}-devel
This package contains the development files for the ayatana
appindicator%{?psuffix} library.

%prep
%autosetup -p1

%build
%cmake \
  -DENABLE_GTKDOC=OFF \
%if "%{flavor}" == "gtk2"
  -DFLAVOUR_GTK2=ON \
%else
  -DFLAVOUR_GTK3=ON \
%endif
%if %{without mono}
  -DENABLE_BINDINGS_MONO=OFF \
%endif
  -DENABLE_MONO_TESTS=OFF
%cmake_build

%install
%cmake_install

%post -n libayatana-appindicator%{?psuffix:%{psuffix}-}%{sover} -p /sbin/ldconfig

%postun -n libayatana-appindicator%{?psuffix:%{psuffix}-}%{sover} -p /sbin/ldconfig

%files -n libayatana-appindicator%{?psuffix:%{psuffix}-}%{sover}
%license COPYING*
%doc README.md ChangeLog
%{_libdir}/libayatana-appindicator%{?psuffix}.so.%{sover}*

%files -n typelib-1_0-AyatanaAppIndicator%{?psuffix}-0_1
%license COPYING*
%doc README.md
%{_libdir}/girepository-1.0/AyatanaAppIndicator%{?psuffix}-0.1.typelib

%if %{with mono}
%files -n ayatana-appindicator%{?psuffix}-sharp
%license COPYING*
%doc README.md
%{_libdir}/ayatana-appindicator%{?psuffix}-sharp-0.1/

%files -n ayatana-appindicator%{?psuffix}-sharp-devel
%license COPYING*
%doc README.md
%{_libdir}/pkgconfig/ayatana-appindicator%{?psuffix}-sharp-0.1.pc
%endif

%files -n libayatana-appindicator%{?psuffix}-devel
%license COPYING*
%doc README.md
%{_includedir}/libayatana-appindicator%{?psuffix}-0.1/
%{_libdir}/libayatana-appindicator%{?psuffix}.so
%{_libdir}/pkgconfig/ayatana-appindicator%{?psuffix}-0.1.pc
%{_datadir}/gir-1.0/AyatanaAppIndicator%{?psuffix}-0.1.gir
%if "%{flavor}" != "gtk2"
%{_datadir}/vala/vapi/ayatana-appindicator%{?psuffix}-0.1.vapi
%{_datadir}/vala/vapi/ayatana-appindicator%{?psuffix}-0.1.deps
%endif

%changelog
