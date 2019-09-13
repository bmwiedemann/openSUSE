#
# spec file for package quazip
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


%define so_ver 1
Name:           quazip
Version:        0.8.1
Release:        0
Summary:        C++ wrapper for ZIP/UNZIP
License:        GPL-2.0-or-later OR LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/stachenov/quazip
Source:         https://github.com/stachenov/quazip/archive/v%{version}.tar.gz#/quazip-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM quazip-0.8.1_pkgconfig.patch
Patch0:         quazip-0.8.1_pkgconfig.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
BuildRequires:  graphviz-gnome
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(zlib)

%description
A C++ wrapper for the Gilles Vollant's ZIP/UNZIP C package, using Qt5 toolkit.
Useful to access ZIP archives from Qt5 programs.

%package -n libquazip5-%{so_ver}
Summary:        C++ wrapper for ZIP/UNZIP
Group:          Development/Libraries/C and C++
Provides:       libquazip%{so_ver} = %{version}
Obsoletes:      libquazip%{so_ver} < %{version}

%description -n libquazip5-%{so_ver}
A C++ wrapper for the Gilles Vollant's ZIP/UNZIP C package, using Qt5 toolkit.
Useful to access ZIP archives from Qt5 programs.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libquazip5-%{so_ver} = %{version}-%{release}
Requires:       pkgconfig(Qt5Core)
Provides:       libquazip-qt5-devel = %{version}
Obsoletes:      libquazip-qt5-devel < %{version}
Provides:       quazip-qt5-devel = %{version}
Obsoletes:      quazip-qt5-devel < %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Documentation for quazip, a C++ wrapper for ZIP/UNZIP
Group:          Documentation/HTML
Provides:       libquazip-qt5-doc = %{version}
Obsoletes:      libquazip-qt5-doc < %{version}
Provides:       quazip-qt5-doc = %{version}
Obsoletes:      quazip-qt5-doc < %{version}

%description doc
A C++ wrapper for the Gilles Vollant's ZIP/UNZIP C package, using Qt5 toolkit.
Useful to access ZIP archives from Qt5 programs.

%prep
%setup -q -n quazip-%{version}
%patch0 -p1

%build
%cmake
%make_jobs
cd ..

sed -i 's/HTML_TIMESTAMP\s*= YES/HTML_TIMESTAMP=NO/' Doxyfile
doxygen -u
doxygen

%install
%cmake_install
rm %{buildroot}/%{_libdir}/libquazip5.a
# install docs
mkdir -pv %{buildroot}%{_defaultdocdir}/quazip-doc
cp -r doc/html %{buildroot}%{_defaultdocdir}/quazip-doc/
%fdupes -s %{buildroot}%{_defaultdocdir}/quazip-doc

%post -n libquazip5-%{so_ver} -p /sbin/ldconfig
%postun -n libquazip5-%{so_ver} -p /sbin/ldconfig

%files -n libquazip5-%{so_ver}
%license COPYING*
%doc NEWS.txt README*
%{_libdir}/libquazip5.so.%{so_ver}*

%files devel
%license COPYING*
%{_datadir}/cmake/Modules/FindQuaZip5.cmake
%{_includedir}/quazip5/
%{_libdir}/libquazip5.so
%{_libdir}/pkgconfig/quazip.pc

%files doc
%doc %{_defaultdocdir}/quazip-doc

%changelog
