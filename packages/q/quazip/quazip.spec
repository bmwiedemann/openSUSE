#
# spec file for package quazip
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


%global quazip_flavor @BUILD_FLAVOR@%{nil}
%if "%{quazip_flavor}" == ""
ExclusiveArch:  do_not_build
%endif
%define no_pkgconfig 0
%if "%{quazip_flavor}" == "qt6"
%define qt6 1
%define pkg_suffix -qt6
# No pkgconfig file before 6.3.1
%if %{pkg_vcmp cmake(Qt6Core) <= 6.3.0}
%define no_pkgconfig 1
%endif
%endif
%if "%{quazip_flavor}" == "qt5"
%define qt5 1
%define pkg_suffix -qt5
%endif
%define so_ver 1
%define lib_ver 1_4_0
Name:           quazip%{?pkg_suffix}
Version:        1.4
Release:        0
Summary:        C++ wrapper for ZIP/UNZIP
License:        GPL-2.0-or-later OR LGPL-2.1-or-later
URL:            https://github.com/stachenov/quazip
Source:         https://github.com/stachenov/quazip/archive/v%{version}.tar.gz#/quazip-%{version}.tar.gz
BuildRequires:  cmake >= 3.15
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)
%if 0%{?qt5}
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  graphviz-gnome
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
%endif
%if 0%{?qt6}
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Test)
%endif

%description
A C++ wrapper for the Gilles Vollant's ZIP/UNZIP C package, using Qt toolkit.
Useful to access ZIP archives from Qt programs.

%package -n libquazip%{so_ver}-%{quazip_flavor}-%{lib_ver}
Summary:        C++ wrapper for ZIP/UNZIP
%if 0%{?qt5}
Provides:       libquazip%{so_ver} = %{version}
Obsoletes:      libquazip%{so_ver} < %{version}
Provides:       libquazip5-%{so_ver} = %{version}
Obsoletes:      libquazip5-%{so_ver} < %{version}
%endif

%description -n libquazip%{so_ver}-%{quazip_flavor}-%{lib_ver}
A C++ wrapper for the Gilles Vollant's ZIP/UNZIP C package, using Qt toolkit.
Useful to access ZIP archives from Qt programs.

%package        devel
Summary:        Development files for %{name}
Requires:       libquazip%{so_ver}-%{quazip_flavor}-%{lib_ver} = %{version}
Requires:       pkgconfig(bzip2)
Requires:       pkgconfig(zlib)
%if 0%{?qt5}
Requires:       cmake(Qt5Core)
Provides:       libquazip-qt5-devel = %{version}
Obsoletes:      libquazip-qt5-devel < %{version}
Provides:       quazip-devel = %{version}
Obsoletes:      quazip-devel < %{version}
%endif
%if 0%{?qt6}
Requires:       cmake(Qt6Core)
Requires:       cmake(Qt6Core5Compat)
%endif

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use quazip.

# Only build the doc package once
%if 0%{?qt5}
%package -n quazip-doc
Summary:        Documentation for quazip, a C++ wrapper for ZIP/UNZIP
Provides:       libquazip-qt5-doc = %{version}
Obsoletes:      libquazip-qt5-doc < %{version}
Provides:       quazip-qt5-doc = %{version}
Obsoletes:      quazip-qt5-doc < %{version}
BuildArch:      noarch

%description -n quazip-doc
A C++ wrapper for the Gilles Vollant's ZIP/UNZIP C package, using Qt toolkit.
Useful to access ZIP archives from Qt programs.

This package contains documentation for quazip.
%endif

%prep
%autosetup -p1 -n quazip-%{version}

%build
%if 0%{?qt6}
%cmake_qt6
%qt6_build
%endif
%if 0%{?qt5}
%cmake
%cmake_build
cd ..
sed -i 's/HTML_TIMESTAMP\s*= YES/HTML_TIMESTAMP=NO/' Doxyfile
doxygen -u
doxygen
%endif

%install
%if 0%{?qt6}
%qt6_install
%endif
%if 0%{?qt5}
%cmake_install

# install docs
mkdir -pv %{buildroot}%{_defaultdocdir}/quazip-doc
cp -r doc/html %{buildroot}%{_defaultdocdir}/quazip-doc/
%fdupes -s %{buildroot}%{_defaultdocdir}/quazip-doc
%endif

%if %{no_pkgconfig}
rm %{buildroot}%{_libdir}/pkgconfig/quazip%{so_ver}-qt6.pc
%endif

%post -n libquazip%{so_ver}-%{quazip_flavor}-%{lib_ver} -p /sbin/ldconfig
%postun -n libquazip%{so_ver}-%{quazip_flavor}-%{lib_ver} -p /sbin/ldconfig

%files -n libquazip%{so_ver}-%{quazip_flavor}-%{lib_ver}
%license COPYING*
%doc NEWS.txt README*
%{_libdir}/libquazip%{so_ver}-%{quazip_flavor}.so.%{so_ver}*

%files devel
%license COPYING*
%doc QuaZip-1.x-migration.md
%if 0%{?qt5}
%{_includedir}/QuaZip-Qt5-%{version}
%{_libdir}/cmake/QuaZip-Qt5-%{version}
%endif
%if 0%{?qt6}
%{_includedir}/QuaZip-Qt6-%{version}
%{_libdir}/cmake/QuaZip-Qt6-%{version}
%endif
%{_libdir}/libquazip%{so_ver}-%{quazip_flavor}.so
%if !%{no_pkgconfig}
%{_libdir}/pkgconfig/quazip%{so_ver}-%{quazip_flavor}.pc
%endif

%if 0%{?qt5}
%files -n quazip-doc
%doc %{_defaultdocdir}/quazip-doc
%endif

%changelog
