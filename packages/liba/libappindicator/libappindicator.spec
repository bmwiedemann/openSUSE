#
# spec file for package libappindicator
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "gtk2"
%global gtkver 2
%bcond_without mono
%endif
%if "%{flavor}" == "gtk3"
%global psuffix 3
%global gtkver 3
%bcond_with mono
%endif
%define sover 1
%define _version 12.10.1+20.10.20200706.1
Name:           libappindicator
Version:        12.10.1~bzr20200706.298
Release:        0
Summary:        Application indicators library
License:        GPL-3.0-only AND LGPL-2.0-only AND LGPL-3.0-only
Group:          System/GUI/Other
URL:            https://launchpad.net/libappindicator
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{_version}.orig.tar.gz
# PATCH-FIX-UPSTREAM 0001_Fix_mono_dir.patch hrvoje.senjan@gmail.com -- Fix location of .pc files.
Patch0:         0001_Fix_mono_dir.patch
# PATCH-FIX-OPENSUSE make_gtk_doc_optional.patch -- Do not require macros from gtk-doc
Patch1:         make_gtk_doc_optional.patch
# PATCH-FIX-OPENSUSE xappstatusicon.patch maurizio.galli@gmail.com -- Original patch by Linux Mint. Include support for XAppStatusIcon by Linux Mint
Patch2:         xappstatusicon.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%if "%{flavor}" == ""
ExclusiveArch:  do-not-build
%endif
%if "%{flavor}" == "gtk2"
BuildRequires:  pkgconfig(dbusmenu-gtk-0.4)
BuildRequires:  pkgconfig(gtk+-2.0)
%if %{with mono}
BuildRequires:  pkgconfig(gapi-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(nunit)
%endif
%else
BuildRequires:  vala
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gtk+-3.0)
#BuildRequires:  pkgconfig(xapp) >= 1.5.0
%endif
Provides:       libappindicator-gtk3

%description
A library to allow applications to export a menu into the Unity Menu bar. Based
on KSNI it also works in KDE and will fallback to generic Systray support if
none of those are available.

%package -n libappindicator%{?psuffix:%{psuffix}-}%{sover}
Summary:        Application indicators library
Group:          System/Libraries
# Fedora and friends compatibility symbol
%if "%{flavor}" == "gtk2"
Provides:       libappindicator = %{version}
%else
Provides:       libappindicator-gtk3 = %{version}
%endif

%description -n libappindicator%{?psuffix:%{psuffix}-}%{sover}
A library to allow applications to export a menu into the Unity Menu bar. Based
on KSNI it also works in KDE and will fallback to generic Systray support if
none of those are available.

%if "%{flavor}" != "gtk2"
%package -n typelib-1_0-AppIndicator%{?psuffix}-0_1
Summary:        Application indicators library
Group:          System/Libraries

%description -n typelib-1_0-AppIndicator%{?psuffix}-0_1
This package contains the GObject Introspection bindings for the appindicator
library.

%else

%package -n appindicator%{?psuffix}-sharp
Summary:        Application indicators library for C#
Group:          System/Libraries

%description -n appindicator%{?psuffix}-sharp
This package provides the appindicator-sharp assembly that allows CLI (.NET)
programs to take menus from applications and place them in the panel.

This package provides assemblies to be used by applications.

%package -n appindicator%{?psuffix}-sharp-devel
Summary:        Development files for libappindicator-sharp
Group:          Development/Libraries/Other
Requires:       appindicator%{?psuffix}-sharp = %{version}

%description -n appindicator%{?psuffix}-sharp-devel
This package contains the development files for the appindicator-sharp library.
%endif

%package -n libappindicator%{?psuffix}-devel
Summary:        Development files for libappindicator
Group:          Development/Libraries/C and C++
Requires:       libappindicator%{?psuffix:%{psuffix}-}%{sover} = %{version}

%description -n libappindicator%{?psuffix}-devel
This package contains the development files for the appindicator%{?psuffix} library.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
#%%patch2 -p1

%build
# Create dummy file, to avoid dependency on gtk-doc
echo "EXTRA_DIST = " >> gtk-doc.make
autoreconf -vfi
%if %{with mono}
export CSC=%{_bindir}/gmcs
%endif

%configure \
  --disable-static    \
  --disable-gtk-doc   \
  --disable-mono-test \
  --with-gtk=%{gtkver}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%if "%{flavor}" == "gtk2"
rm %{buildroot}%{_libdir}/girepository-1.0/AppIndicator3-0.1.typelib
rm %{buildroot}%{_datadir}/gir-1.0/AppIndicator3-0.1.gir
%endif

%post -n libappindicator%{?psuffix:%{psuffix}-}%{sover} -p /sbin/ldconfig

%postun -n libappindicator%{?psuffix:%{psuffix}-}%{sover} -p /sbin/ldconfig

%files -n libappindicator%{?psuffix:%{psuffix}-}%{sover}
%license COPYING COPYING.LGPL.2.1
%doc README
%{_libdir}/libappindicator%{?psuffix}.so.%{sover}*

%if "%{flavor}" == "gtk2"
# Only for GTK 2
%if %{with mono}
%files -n appindicator%{?psuffix}-sharp
%license COPYING COPYING.LGPL.2.1
%doc README
%{_libdir}/appindicator%{?psuffix}-sharp-0.1/
%{_prefix}/lib/mono/appindicator%{?psuffix}-sharp/
%{_prefix}/lib/mono/gac/appindicator%{?psuffix}-sharp/
%{_prefix}/lib/mono/gac/policy.0.0.appindicator%{?psuffix}-sharp/

%files -n appindicator%{?psuffix}-sharp-devel
%license COPYING COPYING.LGPL.2.1
%doc README
%{_libdir}/pkgconfig/appindicator%{?psuffix}-sharp-0.1.pc
%endif

%else

# Only for GTK 3+
%files -n typelib-1_0-AppIndicator%{?psuffix}-0_1
%license COPYING COPYING.LGPL.2.1
%doc README
%{_libdir}/girepository-1.0/AppIndicator%{?psuffix}-0.1.typelib

%endif

%files -n libappindicator%{?psuffix}-devel
%license COPYING COPYING.LGPL.2.1
%doc README
%{_includedir}/libappindicator%{?psuffix}-0.1/
%{_libdir}/libappindicator%{?psuffix}.so
%{_libdir}/pkgconfig/appindicator%{?psuffix}-0.1.pc
%if "%{flavor}" != "gtk2"
%{_datadir}/gir-1.0/AppIndicator%{?psuffix}-0.1.gir
%{_datadir}/vala/vapi/appindicator%{?psuffix}-0.1.*
%endif

%changelog
