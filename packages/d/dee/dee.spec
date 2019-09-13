#
# spec file for package dee
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define soname  libdee
%define sover   1_0-4
%define _version 1.2.7+17.10.20170616
Name:           dee
Version:        1.2.7+bzr20170616
Release:        0
Summary:        Library that uses D-Bus to provide objects
License:        LGPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://launchpad.net/dee
Source:         https://launchpad.net/ubuntu/+archive/primary/+files/%{name}_%{_version}.orig.tar.gz
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  libicu-devel >= 4.6
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  python3
BuildRequires:  vala
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
Libdee is a library that uses D-Bus to provide objects allowing one
to create Model-View-Controller type applications across D-Bus.
It also consists of utility objects which extend D-Bus allowing
peer-to-peer discoverability of known objects without needing a
central registrar.

%package -n %{soname}-%{sover}
Summary:        Library that uses D-Bus to provide objects
Group:          System/Libraries

%description -n %{soname}-%{sover}
Libdee is a library that uses D-Bus to provide objects allowing one
to create Model-View-Controller type applications across D-Bus.
It also consists of utility objects which extend D-Bus allowing
peer-to-peer discoverability of known objects without needing a
central registrar.

%package -n typelib-1_0-Dee-1_0
Summary:        Introspection bindings for the dee library 
Group:          System/Libraries

%description -n typelib-1_0-Dee-1_0
Libdee is a library that uses D-Bus to provide objects allowing one
to create Model-View-Controller type applications across D-Bus.
It also consists of utility objects which extend D-Bus allowing
peer-to-peer discoverability of known objects without needing a
central registrar.

This package provides the GObject Introspection bindings for libdee.

%if 0%{?suse_version} > 1320 || 0%{?sle_version} > 120200
%package -n python2-gobject-Dee
%else
%package -n python-gobject-Dee
%endif
Summary:        Python bindings for GObject/Dee
Group:          Development/Languages/Python
Requires:       %{soname}-%{sover} = %{version}
# python-dee was last used in openSUSE Leap 14.3.
Provides:       python-dee = %{version}
Obsoletes:      python-dee < %{version}
%if 0%{?suse_version} > 1320
Requires:       python2-gobject
Supplements:    packageand(python2-gobject:%{soname}-%{sover})
%else
Requires:       python-gobject
Supplements:    packageand(python-gobject:%{soname}-%{sover})
%endif
%if 0%{?suse_version} > 1320 || 0%{?sle_version} > 120200
# python-gobject-Dee was last used in openSUSE Leap 14.2.
Provides:       python-gobject-Dee = %{version}
Obsoletes:      python-gobject-Dee < %{version}
%endif

%if 0%{?suse_version} > 1320 || 0%{?sle_version} > 120200
%description -n python2-gobject-Dee
%else
%description -n python-gobject-Dee
%endif
Libdee is a library that uses D-Bus to provide objects allowing one
to create Model-View-Controller type applications across D-Bus.
It also consists of utility objects which extend D-Bus allowing
peer-to-peer discoverability of known objects without needing a
central registrar.

This package contains the Python Dee bindings for GObject.

%package -n python3-gobject-Dee
Summary:        Python bindings for GObject/Dee
Group:          Development/Languages/Python
Requires:       %{soname}-%{sover} = %{version}
Requires:       python3-gobject
Supplements:    packageand(python3-gobject:%{soname}-%{sover})

%description -n python3-gobject-Dee
Libdee is a library that uses D-Bus to provide objects allowing one
to create Model-View-Controller type applications across D-Bus.
It also consists of utility objects which extend D-Bus allowing
peer-to-peer discoverability of known objects without needing a
central registrar.

This package contains the Python Dee bindings for GObject.

%package devel
Summary:        Development files for dee
Group:          Development/Libraries/C and C++
Requires:       %{soname}-%{sover} = %{version}
Requires:       python3-gobject-Dee = %{version}
Requires:       typelib-1_0-Dee-1_0 = %{version}
%if 0%{?suse_version} > 1320 || 0%{?sle_version} > 120200
Requires:       python2-gobject-Dee = %{version}
%else
Requires:       python-gobject-Dee = %{version}
%endif

%description devel
This package provides the development files for dee.

Libdee is a library that uses D-Bus to provide objects allowing one
to create Model-View-Controller type applications across D-Bus.
It also consists of utility objects which extend D-Bus allowing
peer-to-peer discoverability of known objects without needing a
central registrar.

%prep
%setup -q -c

%build
NOCONFIGURE=1 gnome-autogen.sh
%global _configure ../configure
for pyver in %{py_ver} %{py3_ver}; do
    mkdir -p "build-py$pyver"
    pushd "build-py$pyver"
    export PYTHON="python$pyver"
    %configure \
      --disable-static           \
      --disable-maintainer-flags \
      --enable-introspection
    make %{?_smp_mflags} V=1
    popd
done

%install
%make_install -C build-py%{py_ver}
%make_install -C build-py%{py3_ver}

%fdupes %{buildroot}%{python_sitearch}/
%fdupes %{buildroot}%{python3_sitearch}/
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{soname}-%{sover} -p /sbin/ldconfig

%postun -n %{soname}-%{sover} -p /sbin/ldconfig

%files -n %{soname}-%{sover}
%doc ChangeLog README COPYING
%{_libdir}/libdee-1.0.so.*

%files -n typelib-1_0-Dee-1_0
%{_libdir}/girepository-1.0/Dee-1.0.typelib

%if 0%{?suse_version} > 1320 || 0%{?sle_version} > 120200
%files -n python2-gobject-Dee
%else
%files -n python-gobject-Dee
%endif
%dir %{python_sitearch}/gi/
%dir %{python_sitearch}/gi/overrides/
%{python_sitearch}/gi/overrides/*

%files -n python3-gobject-Dee
%dir %{python3_sitearch}/gi/
%dir %{python3_sitearch}/gi/overrides/
%{python3_sitearch}/gi/overrides/*

%files devel
%{_bindir}/dee-tool
%{_includedir}/dee-1.0/
%{_libdir}/libdee-1.0.so
%{_libdir}/pkgconfig/dee-1.0.pc
%{_libdir}/pkgconfig/dee-icu-1.0.pc
%{_datadir}/gir-1.0/Dee-1.0.gir
%dir %{_datadir}/vala/
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/dee-1.0.deps
%{_datadir}/vala/vapi/dee-1.0.vapi

%changelog
