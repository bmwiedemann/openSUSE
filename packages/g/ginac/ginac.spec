#
# spec file for package ginac
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


%define library_version 6
Name:           ginac
Version:        1.7.8
Release:        0
Summary:        C++ library for symbolic calculations
License:        GPL-2.0-only
Group:          Development/Libraries/C and C++
URL:            https://www.ginac.de/
Source0:        https://www.ginac.de/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM ginac-check-for-python3.patch badshah400@gmail.com -- Check for python3 if python not found during configure.
Patch0:         ginac-check-for-python3.patch
BuildRequires:  bison
BuildRequires:  cln-devel
BuildRequires:  doxygen
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  readline-devel
BuildRequires:  texinfo
BuildRequires:  texlive-dvips-bin
BuildRequires:  texlive-latex-bin
BuildRequires:  transfig
BuildRequires:  tex(newunicodechar.sty)

%description
GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra System)") is an
open framework for symbolic computation within the C++ programming language.

%package -n libginac%{library_version}
Summary:        C++ library for symbolic calculations
Group:          System/Libraries

%description -n libginac%{library_version}
GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra System)") is an
open framework for symbolic computation within the C++ programming language.

%package devel
Summary:        GiNaC development libraries and header files
Group:          Development/Libraries/C and C++
Requires:       cln-devel
Requires:       libginac%{library_version} = %{version}
Requires(pre):  %{install_info_prereq}
Requires(preun): %{install_info_prereq}
Provides:       lib%{name}-devel = %{version}
Obsoletes:      lib%{name}-devel < %{version}

%description devel
GiNaC (which stands for "GiNaC is Not a CAS (Computer Algebra System)") is an
open framework for symbolic computation within the C++ programming language.

This package contains the libraries, include files and other resources you
use to develop GiNaC applications.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fvi
%configure --docdir=%{_docdir}/%{name} --disable-static --disable-rpath
make %{?_smp_mflags}
make %{?_smp_mflags} html

%install
%make_install install-html
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n libginac%{library_version} -p /sbin/ldconfig
%postun -n libginac%{library_version} -p /sbin/ldconfig

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/ginac.info.gz
%preun devel
%install_info_delete  --info-dir=%{_infodir} %{_infodir}/ginac.info.gz

%files -n libginac%{library_version}
%{_libdir}/libginac.so.%{library_version}*

%files devel
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so
%{_libdir}/pkgconfig/ginac.pc
%dir %{_includedir}/ginac
%{_includedir}/ginac/*.h
%{_infodir}/*.info%{?ext_info}
%{_docdir}/%{name}/

%files
%{_bindir}/ginsh
%{_bindir}/viewgar
%{_libexecdir}/ginac-excompiler
%{_mandir}/man1/ginsh.1%{?ext_man}
%{_mandir}/man1/viewgar.1%{?ext_man}

%changelog
