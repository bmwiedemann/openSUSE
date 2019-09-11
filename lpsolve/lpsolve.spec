#
# spec file for package lpsolve
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define libname liblpsolve55-0
Name:           lpsolve
Version:        5.5.2.0
Release:        0
Summary:        A Mixed Integer Linear Programming (MILP) Solver
License:        LGPL-2.0+
Group:          Productivity/Scientific/Math
Url:            http://sourceforge.net/projects/lpsolve
Source:         http://dev.gentooexperimental.org/~scarabeus/%{name}_bundled_colamd-%{version}.tar.xz
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Mixed Integer Linear Programming (MILP) solver lpsolve solves pure
linear, (mixed) integer/binary, semi-continuous and special ordered
sets (SOS) models.

%package -n %{libname}
Summary:        A Mixed Integer Linear Programming (MILP) Solver Library
Group:          Productivity/Scientific/Math
Provides:       liblpsolve55 = %{version}
Obsoletes:      liblpsolve55 < %{version}

%description -n %{libname}
Mixed Integer Linear Programming (MILP) solver library lpsolve solves
pure linear, (mixed) integer/binary, semi-continuous and special
ordered sets (SOS) models.

%package devel
Summary:        Files for Developing with lpsolve
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
Includes and definitions for developing with the lpsolve library.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -Icolamd/"
%configure \
	--disable-static \
	--docdir="%{_docdir}/%{name}"
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ./bfp/bfp_LUSOL/LUSOL/LUSOL_LGPL.txt ./bfp/bfp_LUSOL/LUSOL/LUSOL_README.txt ./bfp/bfp_LUSOL/LUSOL/LUSOL-overview.txt README.txt
%{_bindir}/*

%files -n %{libname}
%defattr(-,root,root,-)
%{_libdir}/*.so.0*

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/*.so

%changelog
