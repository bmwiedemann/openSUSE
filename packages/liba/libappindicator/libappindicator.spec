#
# spec file for package libappindicator
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
%define _version 12.10.1+17.04.20170215
%if %{undefined with_mono}
%bcond_without mono
%endif
%bcond_with mono
Name:           libappindicator
Version:        12.10.1+bzr20170215
Release:        0
Summary:        Application indicators library
License:        LGPL-2.0-only AND LGPL-3.0-only AND GPL-3.0-only
Group:          System/Libraries
URL:            https://launchpad.net/libappindicator
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{_version}.orig.tar.gz
# PATCH-FIX-UPSTREAM 0001_Fix_mono_dir.patch hrvoje.senjan@gmail.com -- Fix location of .pc files.
Patch0:         0001_Fix_mono_dir.patch
# PATCH-FIX=UPSTREAM libappindicator-no-Werror.patch dimstar@opensuse.org -- Don't add -Werror on build: the code is aging and does not keep up
Patch2:         libappindicator-no-Werror.patch
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(dbusmenu-glib-0.4)
BuildRequires:  pkgconfig(dbusmenu-gtk-0.4)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(indicator-0.4)
BuildRequires:  pkgconfig(indicator3-0.4)
BuildRequires:  pkgconfig(pygtk-2.0)
%if %{with mono}
BuildRequires:  pkgconfig(gapi-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(mono-nunit)
%endif

%description
A library to allow applications to export a menu into the Unity Menu bar. Based
on KSNI it also works in KDE and will fallback to generic Systray support if
none of those are available.

%package -n python2-appindicator
Summary:        Python 2 bindings for libappindicator
Group:          Development/Languages/Python
Requires:       libappindicator%{sover} = %{version}
# python-appindicator was last used in openSUSE Leap 42.2.
Provides:       python-appindicator = %{version}
Obsoletes:      python-appindicator < %{version}

%description -n python2-appindicator
This package contains the Python 2 bindings for the appindicator library.

%package -n libappindicator%{sover}
Summary:        Application indicators library
Group:          System/Libraries

%description -n libappindicator%{sover}
A library to allow applications to export a menu into the Unity Menu bar. Based
on KSNI it also works in KDE and will fallback to generic Systray support if
none of those are available.

%package -n typelib-1_0-AppIndicator-0_1
Summary:        Application indicators library
Group:          System/Libraries

%description -n typelib-1_0-AppIndicator-0_1
This package contains the GObject Introspection bindings for the appindicator
library.

%package devel
Summary:        Development files for libappindicator
Group:          Development/Libraries/C and C++
Requires:       libappindicator%{sover} = %{version}

%description devel
This package contains the development files for the appindicator library.

%package -n libappindicator3-%{sover}
Summary:        Application indicators library for GTK+3
Group:          System/Libraries

%description -n libappindicator3-%{sover}
A library to allow applications to export a menu into the Unity Menu bar. Based
on KSNI it also works in KDE and will fallback to generic Systray support if
none of those are available.

This package contains the GTK+ 3 version of this library.

%package -n typelib-1_0-AppIndicator3-0_1
Summary:        Application indicators library
Group:          System/Libraries

%description -n typelib-1_0-AppIndicator3-0_1
This package contains the GObject Introspection bindings for the appindicator
library.

%package -n libappindicator3-devel
Summary:        Development files for libappindicator3
Group:          Development/Libraries/C and C++
Requires:       libappindicator3-%{sover} = %{version}

%description -n libappindicator3-devel
This package contains the development files for the appindicator3 library.

%package doc
Summary:        Documentation for libappindicator and libappindicator3
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains the documentation for the appindicator and appindicator3
libraries.

%if %{with mono}
%package -n appindicator-sharp
Summary:        Application indicators library for C#
Group:          System/Libraries

%description -n appindicator-sharp
This package provides the appindicator-sharp assembly that allows CLI (.NET)
programs to take menus from applications and place them in the panel.

This package provides assemblies to be used by applications

%package -n appindicator-sharp-devel
Summary:        Development files for libappindicator-sharp
Group:          Development/Libraries/Other
Requires:       appindicator-sharp = %{version}

%description -n appindicator-sharp-devel
This package contains the development files for the appindicator-sharp library.
%endif

%prep
%setup -q -c
%patch0 -p1
%patch2 -p1

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

%post -n libappindicator%{sover} -p /sbin/ldconfig

%postun -n libappindicator%{sover} -p /sbin/ldconfig

%post -n libappindicator3-%{sover} -p /sbin/ldconfig

%postun -n libappindicator3-%{sover} -p /sbin/ldconfig

%files -n python2-appindicator
%license COPYING COPYING.LGPL.2.1
%doc README
%dir %{python_sitearch}/appindicator/
%{python_sitearch}/appindicator/__init__.py*
%{python_sitearch}/appindicator/_appindicator.so
%dir %{_datadir}/pygtk/
%dir %{_datadir}/pygtk/2.0/
%dir %{_datadir}/pygtk/2.0/defs/
%{_datadir}/pygtk/2.0/defs/appindicator.defs

%files -n libappindicator%{sover}
%license COPYING COPYING.LGPL.2.1
%doc README
%{_libdir}/libappindicator.so.%{sover}*

%files -n typelib-1_0-AppIndicator-0_1
%license COPYING COPYING.LGPL.2.1
%doc README
%{_libdir}/girepository-1.0/AppIndicator-0.1.typelib

%files devel
%license COPYING COPYING.LGPL.2.1
%doc README
%dir %{_includedir}/libappindicator-0.1/
%dir %{_includedir}/libappindicator-0.1/libappindicator/
%{_includedir}/libappindicator-0.1/libappindicator/*.h
%{_libdir}/libappindicator.so
%{_libdir}/pkgconfig/appindicator-0.1.pc
%{_datadir}/gir-1.0/AppIndicator-0.1.gir
%{_datadir}/vala/vapi/appindicator-0.1.vapi
%{_datadir}/vala/vapi/appindicator-0.1.deps

%files -n libappindicator3-%{sover}
%license COPYING COPYING.LGPL.2.1
%doc README
%{_libdir}/libappindicator3.so.%{sover}*

%files -n typelib-1_0-AppIndicator3-0_1
%license COPYING COPYING.LGPL.2.1
%doc README
%{_libdir}/girepository-1.0/AppIndicator3-0.1.typelib

%files -n libappindicator3-devel
%license COPYING COPYING.LGPL.2.1
%doc README
%dir %{_includedir}/libappindicator3-0.1/
%dir %{_includedir}/libappindicator3-0.1/libappindicator/
%{_includedir}/libappindicator3-0.1/libappindicator/*.h
%{_libdir}/libappindicator3.so
%{_libdir}/pkgconfig/appindicator3-0.1.pc
%{_datadir}/gir-1.0/AppIndicator3-0.1.gir
%{_datadir}/vala/vapi/appindicator3-0.1.vapi
%{_datadir}/vala/vapi/appindicator3-0.1.deps

%if %{with mono}
%files -n appindicator-sharp
%license COPYING COPYING.LGPL.2.1
%doc README
%dir %{_libdir}/appindicator-sharp-0.1/
%{_libdir}/appindicator-sharp-0.1/appindicator-sharp.dll
%{_libdir}/appindicator-sharp-0.1/appindicator-sharp.dll.config
%{_libdir}/appindicator-sharp-0.1/policy.0.0.appindicator-sharp.config
%{_libdir}/appindicator-sharp-0.1/policy.0.0.appindicator-sharp.dll
%{_libdir}/appindicator-sharp-0.1/policy.0.1.appindicator-sharp.config
%{_libdir}/appindicator-sharp-0.1/policy.0.1.appindicator-sharp.dll
%dir %{_libexecdir}/mono/appindicator-sharp/
%{_libexecdir}/mono/appindicator-sharp/appindicator-sharp.dll
%{_libexecdir}/mono/appindicator-sharp/policy.0.0.appindicator-sharp.dll
%dir %{_libexecdir}/mono/gac/appindicator-sharp/
%dir %{_libexecdir}/mono/gac/appindicator-sharp/*/
%{_libexecdir}/mono/gac/appindicator-sharp/*/appindicator-sharp.dll
%{_libexecdir}/mono/gac/appindicator-sharp/*/appindicator-sharp.dll.config
%dir %{_libexecdir}/mono/gac/policy.0.0.appindicator-sharp/
%dir %{_libexecdir}/mono/gac/policy.0.0.appindicator-sharp/*/
%{_libexecdir}/mono/gac/policy.0.0.appindicator-sharp/*/policy.0.0.appindicator-sharp.config
%{_libexecdir}/mono/gac/policy.0.0.appindicator-sharp/*/policy.0.0.appindicator-sharp.dll

%files -n appindicator-sharp-devel
%license COPYING COPYING.LGPL.2.1
%doc README
%{_libdir}/pkgconfig/appindicator-sharp-0.1.pc
%endif

%changelog
