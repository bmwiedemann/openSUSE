#
# spec file for package telepathy-qt5
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


%define         libname libtelepathy-qt5
%define         soversion         0
%define         service_soversion 1
# SLE12 does not have farstream support in ppc64le but openSUSE Factory and Ports does
%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
%ifnarch ppc64le
%define with_farstream 1
%endif
%else
%define with_farstream 1
%endif
Name:           telepathy-qt5
Version:        0.9.8
Release:        0
Summary:        Qt5 bindings for the Telepathy Library
License:        LGPL-2.1-or-later
Group:          Development/Tools/Other
URL:            https://telepathy.freedesktop.org/
Source:         https://telepathy.freedesktop.org/releases/telepathy-qt/telepathy-qt-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake >= 3.5
BuildRequires:  fdupes
# FIXME patch, or make upstream look for qhelpgenerator-qt5 first
#BuildRequires:  libqt5-qttools-devel
#BuildRequires:  doxygen
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(telepathy-glib)
%if 0%{?with_farstream}
BuildRequires:  pkgconfig(farstream-0.2)
BuildRequires:  pkgconfig(telepathy-farstream)
%endif

%description
Telepathy-Qt5 is a high-level binding for Telepathy, similar to telepathy-glib but for Qt 5.

%package -n %{libname}-%{soversion}
Summary:        Qt5 bindings for the Telepathy Library
Group:          Development/Tools/Other

%description -n %{libname}-%{soversion}
Telepathy-Qt5 is a high-level binding for Telepathy, similar to telepathy-glib but for Qt 5.

%package -n %{libname}-service%{service_soversion}
Summary:        Qt5 bindings for the Telepathy Library
Group:          Development/Tools/Other

%description -n %{libname}-service%{service_soversion}
Service library for the Qt5 telepathy binding.

%if 0%{?with_farstream}
%package -n %{libname}-farstream%{soversion}
Summary:        Qt5 bindings for the Telepathy Library
Group:          Development/Tools/Other

%description -n %{libname}-farstream%{soversion}
Telepathy-Qt5-farstream is a high-level binding for Telepathy, similar to telepathy-glib but for Qt 5.
%endif

%package devel
Summary:        Header files, libraries and development documentation for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname}-%{soversion} = %{version}
Requires:       %{libname}-service%{service_soversion} = %{version}
Requires:       pkgconfig(gstreamer-1.0)
Requires:       pkgconfig(gstreamer-plugins-base-1.0)
Provides:       %{name}-service-devel-static = %{version}
%if 0%{?with_farstream}
Requires:       %{libname}-farstream%{soversion} = %{version}
%endif

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
%make_install -C build
%fdupes %{buildroot}

%post -n %{libname}-%{soversion} -p /sbin/ldconfig
%postun -n %{libname}-%{soversion} -p /sbin/ldconfig
%post -n %{libname}-service%{service_soversion} -p /sbin/ldconfig
%postun -n %{libname}-service%{service_soversion} -p /sbin/ldconfig

%if 0%{?with_farstream}
%post -n %{libname}-farstream%{soversion} -p /sbin/ldconfig
%postun -n %{libname}-farstream%{soversion} -p /sbin/ldconfig
%endif

%files -n %{libname}-%{soversion}
%license COPYING
%{_libdir}/libtelepathy-qt5.so.*

%files -n %{libname}-service%{service_soversion}
%license COPYING
%{_libdir}/libtelepathy-qt5-service.so.*

%if 0%{?with_farstream}
%files -n %{libname}-farstream%{soversion}
%license COPYING
%{_libdir}/libtelepathy-qt5-farstream.so.*
%endif

%files devel
%license COPYING
%doc AUTHORS ChangeLog README HACKING NEWS
%{_includedir}/telepathy-qt5/
%{_libdir}/libtelepathy-qt5*.so
%{_libdir}/pkgconfig/TelepathyQt5*.pc
%{_libdir}/cmake/TelepathyQt5*/

%changelog
