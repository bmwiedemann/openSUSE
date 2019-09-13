#
# spec file for package telepathy-qt5
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define         libname libtelepathy-qt5
%define         major   0

# SLE12 does not have farstream support in ppc64le but openSUSE Factory and Ports does
%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
%ifnarch ppc64le
%define with_farstream 1
%endif
%else
%define with_farstream 1
%endif

Name:           telepathy-qt5
Version:        0.9.7
Release:        0
Summary:        Qt5 bindings for the Telepathy Library
License:        LGPL-2.1+
Group:          Development/Tools/Other
Url:            http://telepathy.freedesktop.org/
Source:         http://telepathy.freedesktop.org/releases/telepathy-qt/telepathy-qt-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake >= 2.8.12
BuildRequires:  dbus-1-python
BuildRequires:  fdupes
# FIXME patch, or make upstream look for qhelpgenerator-qt5 first
#BuildRequires:  libqt5-qttools-devel
#BuildRequires:  doxygen
BuildRequires:  libxml2-devel
BuildRequires:  python-xml
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
%if 0%{?with_farstream}
BuildRequires:  pkgconfig(farstream-0.2)
BuildRequires:  pkgconfig(telepathy-farstream)
%endif
BuildRequires:  pkgconfig(telepathy-glib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Telepathy-Qt5 is a high-level binding for Telepathy, similar to telepathy-glib but for Qt 5.

%package -n %{libname}-%{major}
Summary:        Qt5 bindings for the Telepathy Library
Group:          Development/Tools/Other

%description -n %{libname}-%{major}
Telepathy-Qt5 is a high-level binding for Telepathy, similar to telepathy-glib but for Qt 5.


%package -n %{libname}-service%{major}
Summary:        Qt5 bindings for the Telepathy Library
Group:          Development/Tools/Other

%description -n %{libname}-service%{major}
Service library for the Qt5 telepathy binding.

%if 0%{?with_farstream}
%package -n %{libname}-farstream%{major}
Summary:        Qt5 bindings for the Telepathy Library
Group:          Development/Tools/Other

%description -n %{libname}-farstream%{major}
Telepathy-Qt5-farstream is a high-level binding for Telepathy, similar to telepathy-glib but for Qt 5.
%endif

%package devel
Summary:        Header files, libraries and development documentation for %{name}
Group:          Development/Libraries/C and C++
Provides:       %{name}-service-devel-static = %{version}
Requires:       %{libname}-%{major} = %{version}
Requires:       %{libname}-service%{major} = %{version}
%if 0%{?with_farstream}
Requires:       %{libname}-farstream%{major} = %{version}
%endif
Requires:       pkgconfig(gstreamer-1.0)
Requires:       pkgconfig(gstreamer-plugins-base-1.0)

%description devel
This package contains the header files, static libraries and development documentation for %{name}. If you like to develop programs using %{name}, you will need to install %{name}-devel.

%prep
%setup -q -n telepathy-qt-%{version}

%build
if [ %{_lib} = lib64 ]; then
  EXTRA_FLAGS="$EXTRA_FLAGS -DLIB_SUFFIX=64"
fi
mkdir build
cd build
cmake -DCMAKE_BUILD_TYPE=release \
      -DCMAKE_INSTALL_PREFIX=/usr \
      -DCMAKE_C_FLAGS="%{optflags}" \
      -DCMAKE_CXX_FLAGS="%{optflags}" \
      -DENABLE_TESTS=FALSE \
      -DENABLE_EXAMPLES=FALSE \
      -DENABLE_FARSIGHT=FALSE \
%if 0%{?with_farstream}
      -DENABLE_FARSTREAM=TRUE \
%endif
      -DDISABLE_WERROR=TRUE \
      -DDESIRED_QT_VERSION=5 $EXTRA_FLAGS ..

make %{?_smp_mflags}

%install
%makeinstall -C build
%fdupes %{buildroot}

%post -n %{libname}-%{major} -p /sbin/ldconfig

%postun -n %{libname}-%{major} -p /sbin/ldconfig

%post -n %{libname}-service%{major} -p /sbin/ldconfig

%postun -n %{libname}-service%{major} -p /sbin/ldconfig

%if 0%{?with_farstream}
%post -n %{libname}-farstream%{major} -p /sbin/ldconfig

%postun -n %{libname}-farstream%{major} -p /sbin/ldconfig
%endif

%files -n %{libname}-%{major}
%defattr(-,root,root)
%{_libdir}/libtelepathy-qt5.so.*

%files -n %{libname}-service%{major}
%defattr(-,root,root)
%{_libdir}/libtelepathy-qt5-service.so.*

%if 0%{?with_farstream}
%files -n %{libname}-farstream%{major}
%defattr(-,root,root)
%{_libdir}/libtelepathy-qt5-farstream.so.*
%endif

%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog README COPYING HACKING NEWS
%{_includedir}/telepathy-qt5/
%{_libdir}/libtelepathy-qt5*.so
%{_libdir}/pkgconfig/TelepathyQt5*.pc
%{_libdir}/cmake/TelepathyQt5*/

%changelog
