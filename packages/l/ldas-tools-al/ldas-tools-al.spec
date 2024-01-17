#
# spec file for package ldas-tools-al
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


%define shlib libldastoolsal7
Name:           ldas-tools-al
Version:        2.6.4
Release:        0
Summary:        LDAS (LIGO Data Analysis System) tools abstraction toolkit
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Physics
URL:            https://wiki.ligo.org/Computing/LDASTools
Source:         http://software.ligo.org/lscsoft/source/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libboost_headers-devel
BuildRequires:  libopenssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ldastoolscmake)
BuildRequires:  pkgconfig(zlib)

%description
LDAS (LIGO Data Analysis System) is a collection of libraries and executables
aid in the processing of gravitation wave data sets. %{name} provides the
tools abstraction toolkit for LDAS.

%package -n %{shlib}
Summary:        Shared lib for %{name} - LDAS tools abstraction toolkit
Group:          Productivity/Scientific/Physics

%description -n %{shlib}
This package provides the shared library for %{name} - LDAS tools abstraction toolkit.

%package devel
Summary:        Headers and source files for developing with %{name}
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}

%description devel
This package provides the headers and sources needed for developing programs using %{name} - LDAS tools abstraction toolkit.

%prep
%autosetup -p1

%build
# FIXME: HAVE_PROC_SYS IS NOT CORRECTLY DETERMINED FOR openSUSE >= 1550, FORCE IT MANUALLY
%cmake \
%if 0%{?suse_version} >= 1550
  -DHAVE_PROCFS_STAT=1 \
%endif
  -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}

%cmake_build

%install
%cmake_install

find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot}%{_libdir} -name "*.a" -delete -print

%fdupes %{buildroot}%{_docdir}/ldas-tools-al/

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%{_libdir}/*.so.*

%files devel
%{_includedir}/ldastoolsal
%{_libdir}/*.so
%{_libdir}/pkgconfig/ldastoolsal.pc
%{_docdir}/ldas-tools-al/

%changelog
