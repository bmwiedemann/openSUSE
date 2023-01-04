#
# spec file for package ginac
#
# Copyright (c) 2023 SUSE LLC
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

%global srcname ginac

%if "%{flavor}" == "doc"
%bcond_without doc
%define pkg_suffix -doc
%endif

%if "%{flavor}" == ""
%bcond_with doc
%endif

%define library_version 11
Name:           %{srcname}%{?pkg_suffix}
Version:        1.8.5
Release:        0
Summary:        C++ library for symbolic calculations
License:        GPL-2.0-only
URL:            https://www.ginac.de/
Source0:        https://www.ginac.de/%{srcname}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM ginac-fix-makeindex.patch badshah400@gmail.com -- Fix input file path when running makeindex which does not like absolute paths
Patch0:         ginac-fix-makeindex.patch
# PATCH-FIX-UPSTREAM ginac-cmake-install-doc.patch badshah400@gmail.com -- Install man and other documentation files when cmake is used for building
Patch1:         ginac-cmake-install-doc.patch
BuildRequires:  bison
BuildRequires:  cln-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  readline-devel
# SECTION Requirements for building documentation
%if %{with doc}
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  texinfo
BuildRequires:  texlive-courier
BuildRequires:  texlive-dvips-bin
BuildRequires:  texlive-helvetic
BuildRequires:  texlive-latex-bin
BuildRequires:  texlive-makeindex-bin
BuildRequires:  texlive-metafont-bin
BuildRequires:  texlive-wasy
BuildRequires:  transfig
BuildRequires:  tex(adjustbox.sty)
BuildRequires:  tex(alphalph.sty)
BuildRequires:  tex(caption.sty)
BuildRequires:  tex(changepage.sty)
BuildRequires:  tex(colortbl.sty)
BuildRequires:  tex(enumitem.sty)
BuildRequires:  tex(etoc.sty)
BuildRequires:  tex(fancyhdr.sty)
BuildRequires:  tex(fancyvrb.sty)
BuildRequires:  tex(float.sty)
BuildRequires:  tex(hanging.sty)
BuildRequires:  tex(helvet.sty)
BuildRequires:  tex(multirow.sty)
BuildRequires:  tex(natbib.sty)
BuildRequires:  tex(newunicodechar.sty)
BuildRequires:  tex(sectsty.sty)
BuildRequires:  tex(stackengine.sty)
BuildRequires:  tex(tabu.sty)
BuildRequires:  tex(tocloft.sty)
BuildRequires:  tex(ulem.sty)
BuildRequires:  tex(wasysym.sty)
%endif
# /SECTION

%description
GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra System)") is an
open framework for symbolic computation within the C++ programming language.

%package -n libginac%{library_version}
Summary:        C++ library for symbolic calculations

%description -n libginac%{library_version}
GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra System)") is an
open framework for symbolic computation within the C++ programming language.

%package devel
Summary:        GiNaC development libraries and header files
Requires:       cln-devel
Requires:       libginac%{library_version} = %{version}
Provides:       lib%{name}-devel = %{version}
Obsoletes:      lib%{name}-devel < %{version}
%if 0%{?suse_version} < 1550
Requires(pre):  %{install_info_prereq}
Requires(preun):%{install_info_prereq}
%endif
Recommends:     ginac-doc-tutorial

%description devel
GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra System)") is an
open framework for symbolic computation within the C++ programming language.

This package contains the libraries, include files and other resources you
use to develop GiNaC applications.

%if "%{flavor}" == "doc"
%package pdf
Summary:        API documentation for GiNaC in PDF format
BuildArch:      noarch

%description pdf
GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra System)") is an
open framework for symbolic computation within the C++ programming language.

This package provides the API documentation for GiNaC in PDF format.

%package html
Summary:        API documentation for GiNaC in HTML format
BuildArch:      noarch

%description html
GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra System)") is an
open framework for symbolic computation within the C++ programming language.

This package provides the API documentation for GiNaC in HTML format.

%package tutorial
Summary:        The GiNaC tutorial in PDF format
BuildArch:      noarch

%description tutorial
GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra System)") is an
open framework for symbolic computation within the C++ programming language.

This package provides a tutorial file for GiNaC in PDF format.

%endif

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
export LDFLAGS="-Wl,--no-undefined"
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON \
       -DCMAKE_INSTALL_LIBEXECDIR:PATH=%{_libexecdir} \
       -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name}

%if "%{flavor}" == "doc"
# Build just the reference doc for the "doc" flavour
pushd doc/reference
%cmake_build pdf_dox html_dox
popd
pushd doc/tutorial
%cmake_build pdf_ginac_tutorial
popd
%else
%cmake_build
%endif

%install
%if "%{flavor}" == "doc"
pushd build/doc/reference
%make_install
popd
%else
%cmake_install
%endif

find %{buildroot} -type f -name "*.la" -delete -print

%fdupes %{buildroot}%{_docdir}/%{name}/html/

# SECTION Unflavoured Pkg
%if "%{flavor}" == ""
%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
%cmake_build check

%post -n libginac%{library_version} -p /sbin/ldconfig
%postun -n libginac%{library_version} -p /sbin/ldconfig

%if 0%{?suse_version} < 1550
%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/ginac.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/ginac-examples.info.gz

%preun devel
%install_info_delete  --info-dir=%{_infodir} %{_infodir}/ginac.info.gz
%install_info_delete  --info-dir=%{_infodir} %{_infodir}/ginac-examples.info.gz
%endif

%files -n libginac%{library_version}
%{_libdir}/libginac.so.%{library_version}*

%files devel
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so
%{_libdir}/pkgconfig/ginac.pc
%{_libdir}/cmake/ginac/
%{_includedir}/ginac/
%{_infodir}/*.info%{?ext_info}

%files
%{_bindir}/ginsh
%{_bindir}/viewgar
%{_libexecdir}/ginac-excompiler
%{_mandir}/man1/ginsh.1%{?ext_man}
%{_mandir}/man1/viewgar.1%{?ext_man}
%endif
# /SECTION

# SECTION doc flavoured pkg
%if "%{flavor}" == "doc"
%files pdf
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/reference.pdf

%files html
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/html/

%files tutorial
%doc %__builddir/doc/tutorial/ginac.pdf
%endif
# /SECTION

%changelog
