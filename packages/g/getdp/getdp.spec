#
# spec file for package getdp
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           getdp
Version:        2.11.2
Release:        0
%define lib_ver 2_11
Url:            http://geuz.org/getdp/
Summary:        A general finite element solver
License:        GPL-2.0+
Group:          Productivity/Scientific/Math
Source0:        http://geuz.org/getdp/src/getdp-%{version}-source.tgz
# PATCH-FIX-UPSTREAM http://gitlab.onelab.info/getdp/getdp/commit/c53529ffaa4c42130c2b6799441cf8d164f85343
Patch0:         getdp-2.11.2-reproducible-date.patch
%if 0%{?suse_version} <= 120300
# PATCH-FIX-OPENSUSE fix command line options for makeinfo on OpenSuSE <= Leap 42.3
Patch1:         getdp-2.11.2-fix-doc-build.patch
%endif
BuildRequires:  arpack-devel
BuildRequires:  bison
BuildRequires:  blas-devel
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gsl-devel
BuildRequires:  lapack-devel
%if 0%{?suse_version} == 1110
BuildRequires:  texlive-latex
%endif
BuildRequires:  texinfo
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
GetDP is a general finite element solver using mixed elements to discretize
de Rham-type complexes in one, two and three dimensions. The main feature of
GetDP is the closeness between the input data defining discrete problems
(written by the user in ASCII data files) and the symbolic mathematical 
expressions of these problems.  

%package     -n libGetDP%{lib_ver}
Summary:        A general finite element solver
Group:          System/Libraries
Provides:       libGetDP = %{version}
Obsoletes:      libGetDP < %{version}

%description -n libGetDP%{lib_ver}
GetDP is a general finite element solver using mixed elements to discretize
de Rham-type complexes in one, two and three dimensions. The main feature of
GetDP is the closeness between the input data defining discrete problems
(written by the user in ASCII data files) and the symbolic mathematical 
expressions of these problems.  

%package        devel
Summary:        Header files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libGetDP = %{version}

%description    devel
This package contains libraries and header files for getdb.

%package        doc
Summary:        A general finite element solver
Group:          Documentation/Other
%if 0%{?suse_version} > 1110
BuildArch:      noarch
%endif

%description    doc
GetDP is a general finite element solver using mixed elements to discretize
de Rham-type complexes in one, two and three dimensions. The main feature of
GetDP is the closeness between the input data defining discrete problems
(written by the user in ASCII data files) and the symbolic mathematical 
expressions of these problems.

This package contains the documentation files (pdf and html) and some examples
files.

%prep
%setup -q -n %{name}-%{version}-source
%patch0 -p1
%if 0%{?suse_version} <= 120300
%patch1 -p1
%endif

sed -i "s/\${GETDP_LIB}/\${LIB_DIR}/" CMakeLists.txt

%build
%cmake \
    -DENABLE_BUILD_SHARED:BOOL=ON \
    -DLIB_DIR:PATH=%{_lib}

make %{?_smp_mflags}
make doc

%install
%cmake_install

# documentation
rm -rf %{buildroot}%{_datadir}/doc/%{name}
pushd build
tar xzf %{name}-%{version}-doc.tgz
popd

%post -n libGetDP%{lib_ver} -p /sbin/ldconfig
%postun -n libGetDP%{lib_ver} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc LICENSE.txt CHANGELOG.txt README.txt
%{_bindir}/*
%{_mandir}/man1/*

%files -n libGetDP%{lib_ver}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/
%{_libdir}/*.so

%files doc
%defattr(-,root,root)
%doc build/doc/texinfo/getdp.html
%doc build/doc/texinfo/getdp.pdf
%doc demos/

%changelog
