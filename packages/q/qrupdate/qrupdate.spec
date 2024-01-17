#
# spec file for package qrupdate
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           qrupdate
Version:        1.1.2
Release:        0
Summary:        Fortran library for fast updates of QR and Cholesky decompositions
License:        GPL-3.0+
Group:          Productivity/Scientific/Math
Url:            http://qrupdate.sourceforge.net/
Source0:        qrupdate-%{version}.tar.gz

BuildRequires:  blas-devel
BuildRequires:  gcc-fortran
BuildRequires:  lapack-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
qrupdate is a Fortran library for fast updates of QR and Cholesky decompositions

%package -n libqrupdate1
Summary:        Fortran library for fast updates of QR and Cholesky decompositions
Group:          Productivity/Scientific/Math

%description -n libqrupdate1
qrupdate is a Fortran library for fast updates of QR and Cholesky decompositions

%package devel
Summary:        Development files for qrupdate library
Group:          Development/Libraries/C and C++
Requires:       libqrupdate1 = %{version}

%description devel
This package contains the development files for the qrupdate libraries.

%package static
Summary:        Static version of qrupdate library
Group:          Development/Libraries/C and C++

%description static
This package contains the static version of the qrupdate libraries.

%prep
%setup -q -n qrupdate-%{version}

%build
make lib FFLAGS=-g
make solib FFLAGS=-g

%install
make install PREFIX=%{buildroot}/usr
test %{_libdir} = /usr/lib || mv %{buildroot}%{_prefix}/lib %{buildroot}%{_libdir}

%clean
rm -rf %{buildroot}

%post -n libqrupdate1 -p /sbin/ldconfig

%postun -n libqrupdate1 -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README COPYING

%files -n libqrupdate1
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_libdir}/lib*.so

%files static
%defattr(-,root,root)
%{_libdir}/lib*.a

%changelog
