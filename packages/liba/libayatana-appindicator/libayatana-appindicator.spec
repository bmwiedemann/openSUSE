#
# spec file for package libayatana-appindicator
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


%define sover 1
%if %{undefined with_mono}
%bcond_without mono
%endif
%bcond_with mono
Name:           libayatana-appindicator
Version:        0.5.3
Release:        0
Summary:        Ayatana application indicators library
License:        LGPL-2.0-only AND LGPL-3.0-only AND GPL-3.0-only
Group:          System/GUI/Other
URL:            https://github.com/AyatanaIndicators/libayatana-appindicator
Source:         https://github.com/AyatanaIndicators/libayatana-appindicator/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM libayatana-appindicator-disable-werror.patch dimstar@opensuse.org -- Don't add -Werror on build: the code is aging and does not keep up.
Patch0:         libayatanaappindicator-disable-werror.patch
# PATCH-FIX-OPENSUSE libayatana-appindicator-fix-mono-dir.patch hrvoje.senjan@gmail.com -- Fix location of .pc files.
Patch1:         libayatana-appindicator-fix-mono-dir.patch
BuildRequires:  fdupes
BuildRequires:  mate-common
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  vala
BuildRequires:  pkgconfig(ayatana-indicator-0.4)
BuildRequires:  pkgconfig(ayatana-indicator3-0.4)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dbusmenu-glib-0.4)
BuildRequires:  pkgconfig(dbusmenu-gtk-0.4)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(pygtk-2.0)
%if %{with mono}
BuildRequires:  pkgconfig(gapi-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(mono-nunit)
%endif

%description
A library to allow applications to add an icon into the
StatusNotifier-compatible notification area. If none are available,
it also provides an XEmbed-tray fallback.

%package -n libayatana-appindicator%{sover}
Summary:        Ayatana application indicators library
Group:          System/Libraries

%description -n libayatana-appindicator%{sover}
A library to allow applications to add an icon into the
StatusNotifier-compatible notification area. If none are available,
it also provides an XEmbed-tray fallback.

%package -n typelib-1_0-AyatanaAppIndicator-0_1
Summary:        Ayatana application indicators library
Group:          System/Libraries

%description -n typelib-1_0-AyatanaAppIndicator-0_1
This package contains the GObject Introspection bindings for the
ayatana appindicator library.

%package devel
Summary:        Development files for libayatana-appindicator
Group:          Development/Libraries/C and C++
Requires:       libayatana-appindicator%{sover} = %{version}

%description devel
This package contains the development files for the ayatana
appindicator library.

%package -n libayatana-appindicator3-%{sover}
Summary:        Ayatana application indicators library for GTK+3
Group:          System/Libraries

%description -n libayatana-appindicator3-%{sover}
A library to allow applications to add an icon into the
StatusNotifier-compatible notification area. If none are available,
it also provides an XEmbed-tray fallback.

This package contains the GTK+ 3 version of the library.

%package -n typelib-1_0-AyatanaAppIndicator3-0_1
Summary:        Ayatana application indicators library
Group:          System/Libraries

%description -n typelib-1_0-AyatanaAppIndicator3-0_1
This package contains the GObject Introspection bindings for the ayatana
appindicator library.

%package -n libayatana-appindicator3-devel
Summary:        Development files for libayatana-appindicator3
Group:          Development/Libraries/C and C++
Requires:       libayatana-appindicator3-%{sover} = %{version}

%description -n libayatana-appindicator3-devel
This package contains the development files for the ayatana
appindicator3 library.

%package doc
Summary:        Documentation for libayatana-appindicator and libayatana-appindicator3
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains the documentation for the ayatana
appindicator and appindicator3 libraries.

%if %{with mono}
%package -n ayatana-appindicator-sharp
Summary:        Ayatana application indicators library for C#
Group:          System/Libraries

%description -n ayatana-appindicator-sharp
This package provides the ayatana-appindicator-sharp assembly that
allows CLI (.NET) applications to take menus from applications and
place them in the panel.

This package provides assemblies to be used by applications.

%package -n ayatana-appindicator-sharp-devel
Summary:        Development files for libayatana-appindicator-sharp
Group:          Development/Libraries/Other
Requires:       ayatana-appindicator-sharp = %{version}

%description -n ayatana-appindicator-sharp-devel
This package contains the development files for the
ayatana-appindicator-sharp library.
%endif

%if 0%{?suse_version} >= 1500
%package -n python2-ayatana-appindicator
%else
%package -n python-ayatana-appindicator
%endif
Summary:        Python 2 bindings for libayatana-appindicator
Group:          Development/Languages/Python
Requires:       libayatana-appindicator%{sover} = %{version}
%if 0%{?suse_version} >= 1500
# python-ayatana-appindicator was last used in openSUSE Leap 42.3.
Provides:       python-ayatana-appindicator = %{version}-%{release}
Obsoletes:      python-ayatana-appindicator < %{version}-%{release}

%description -n python2-ayatana-appindicator
%else

%description -n python-ayatana-appindicator
%endif
This package contains the Python 2 bindings for the
ayatana appindicator library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%if %{with mono}
export CSC=%{_bindir}/gmcs
%endif
%global _configure ../configure
for ver in 2 3; do
    mkdir build-gtk$ver
    pushd build-gtk$ver
    %configure \
      --disable-static    \
      --disable-gtk-doc   \
      --disable-mono-test \
      --with-gtk=$ver
    make -j1 V=1
    popd
done

%install
%make_install -C build-gtk2
%make_install -C build-gtk3
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{python_sitearch}

%post -n libayatana-appindicator%{sover} -p /sbin/ldconfig

%postun -n libayatana-appindicator%{sover} -p /sbin/ldconfig

%post -n libayatana-appindicator3-%{sover} -p /sbin/ldconfig

%postun -n libayatana-appindicator3-%{sover} -p /sbin/ldconfig

%files -n libayatana-appindicator%{sover}
%license COPYING*
%doc README
%{_libdir}/libayatana-appindicator.so.%{sover}*

%files -n typelib-1_0-AyatanaAppIndicator-0_1
%license COPYING*
%doc README
%{_libdir}/girepository-1.0/AyatanaAppIndicator-0.1.typelib

%files devel
%license COPYING*
%doc README
%{_includedir}/libayatana-appindicator-0.1/
%{_libdir}/libayatana-appindicator.so
%{_libdir}/pkgconfig/ayatana-appindicator-0.1.pc
%{_datadir}/gir-1.0/AyatanaAppIndicator-0.1.gir
%{_datadir}/vala/vapi/ayatana-appindicator-0.1.vapi
%{_datadir}/vala/vapi/ayatana-appindicator-0.1.deps

%files -n libayatana-appindicator3-%{sover}
%license COPYING*
%doc README
%{_libdir}/libayatana-appindicator3.so.%{sover}*

%files -n typelib-1_0-AyatanaAppIndicator3-0_1
%license COPYING*
%doc README
%{_libdir}/girepository-1.0/AyatanaAppIndicator3-0.1.typelib

%files -n libayatana-appindicator3-devel
%license COPYING*
%doc README
%{_includedir}/libayatana-appindicator3-0.1/
%{_libdir}/libayatana-appindicator3.so
%{_libdir}/pkgconfig/ayatana-appindicator3-0.1.pc
%{_datadir}/gir-1.0/AyatanaAppIndicator3-0.1.gir
%{_datadir}/vala/vapi/ayatana-appindicator3-0.1.*

%if %{with mono}
%files -n ayatana-appindicator-sharp
%license COPYING*
%doc README
%{_libdir}/ayatana-appindicator-sharp-0.1/
%{_libexecdir}/mono/ayatana-appindicator-sharp/
%{_libexecdir}/mono/gac/ayatana-appindicator-sharp/
%{_libexecdir}/mono/gac/policy.0.0.ayatana-appindicator-sharp/

%files -n ayatana-appindicator-sharp-devel
%license COPYING*
%doc README
%{_libdir}/pkgconfig/ayatana-appindicator-sharp-0.1.pc
%endif

%if 0%{?suse_version} >= 1500
%files -n python2-ayatana-appindicator
%else
%files -n python-ayatana-appindicator
%endif
%license COPYING*
%doc README
%dir %{python_sitearch}/ayatana_appindicator/
%{python_sitearch}/ayatana_appindicator/__init__.py*
%{python_sitearch}/ayatana_appindicator/_ayatana_appindicator.so
%dir %{_datadir}/pygtk/
%dir %{_datadir}/pygtk/2.0/
%dir %{_datadir}/pygtk/2.0/defs/
%{_datadir}/pygtk/2.0/defs/ayatana_appindicator.defs

%changelog
