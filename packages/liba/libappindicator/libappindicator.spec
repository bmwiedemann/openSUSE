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

%global flavor @BUILD_FLAVOR@%{nil}
%global sname libappindicator
%if "%{flavor}" == ""
ExclusiveArch: do-not-build
%endif


%if "%{flavor}" == "gtk2"
%bcond_without mono
%bcond_without python
%global gtkver 2
%endif
%if "%{flavor}" == "gtk3"
%bcond_with mono
%bcond_with python
%global psuffix 3
%global gtkver 3
%endif

%define sover 1
%define _version 12.10.1+17.04.20170215
Name:           libappindicator%{?psuffix}
Version:        12.10.1+bzr20170215
Release:        0
Summary:        Application indicators library
License:        LGPL-2.0-only AND LGPL-3.0-only AND GPL-3.0-only
Group:          System/Libraries
URL:            https://launchpad.net/libappindicator
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{sname}_%{_version}.orig.tar.gz
# PATCH-FIX-UPSTREAM 0001_Fix_mono_dir.patch hrvoje.senjan@gmail.com -- Fix location of .pc files.
Patch0:         0001_Fix_mono_dir.patch
# PATCH-FIX=UPSTREAM libappindicator-no-Werror.patch dimstar@opensuse.org -- Don't add -Werror on build: the code is aging and does not keep up
Patch2:         libappindicator-no-Werror.patch
# PATCH-FIX-OPENSUSE only_require_python_for_gtk2.patch -- Only require Python when building for GTK2
Patch3:         only_require_python_for_gtk2.patch
# PATCH-FIX-OPENSUSE make_gtk_doc_optional.patch -- Do not require macros from gtk-doc
Patch4:         make_gtk_doc_optional.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  vala
BuildRequires:  pkgconfig(gobject-introspection-1.0)
%if "%{flavor}" == "gtk2"
BuildRequires:  pkgconfig(dbusmenu-gtk-0.4)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(indicator-0.4)
%if %{with python}
BuildRequires:  pkgconfig(pygtk-2.0)
%endif
%if %{with mono}
BuildRequires:  pkgconfig(gapi-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(mono-nunit)
%endif
%else
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(indicator3-0.4)
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
Requires:       libappindicator%{?psuffix:%{psuffix}-}%{sover} = %{version}

%description devel
This package contains the development files for the appindicator%{?psuffix} library.

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

%package doc
Summary:        Documentation for libappindicator and libappindicator3
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This package contains the documentation for the appindicator and appindicator3
libraries.

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

%prep
%setup -q -c
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

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
make -j1 V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}%{python_sitearch}

%post -n libappindicator%{sover} -p /sbin/ldconfig

%postun -n libappindicator%{sover} -p /sbin/ldconfig

%post -n libappindicator3-%{sover} -p /sbin/ldconfig

%postun -n libappindicator3-%{sover} -p /sbin/ldconfig

%if %{with python}
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
%endif

%if "%{flavor}" == "gtk2"
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

%else
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
%endif

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
