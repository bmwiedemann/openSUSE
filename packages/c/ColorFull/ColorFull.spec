#
# spec file for package ColorFull
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


%define shlib lib%{name}0
Name:           ColorFull
Version:        1.1
Release:        0
Summary:        C++ library for calculations in QCD (SU(Nc)) color space
License:        GPL-2.0
Group:          Productivity/Scientific/Physics
Url:            http://colorfull.hepforge.org/
Source0:        http://colorfull.hepforge.org/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM ColorFull-install-pkgconfig-file.patch badshah400@gmail.com -- Add a pkgconfig file and modify the autotool files to install it to an appropriate location
Patch2:         ColorFull-install-pkgconfig-file.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
%{name} is a C++ library for calculations in QCD (SU(Nc)) color space. It can
* Square any QCD color amplitude and calculate any interference.
* Create a trace type basis for any number of quarks and gluons.
* Read in and write out color bases.
* Calculate scalar product matrices, i.e., the matrices of scalar products
  between the basis vectors.
* Describe the effect of gluon exchange, including calculating the color
  soft anomalous dimension matrices.
* Describe the effect of gluon emission.
* Be interfaced to Herwig++ (>= 2.7) via Matchbox.

%package -n %{shlib}
Summary:        C++ library for calculations in QCD (SU(Nc)) color space
Group:          System/Libraries

%description -n %{shlib}
%{name} is a C++ library for calculations in QCD (SU(Nc)) color space. It can
* Square any QCD color amplitude and calculate any interference.
* Create a trace type basis for any number of quarks and gluons.
* Read in and write out color bases.
* Calculate scalar product matrices, i.e., the matrices of scalar products
  between the basis vectors.
* Describe the effect of gluon exchange, including calculating the color
  soft anomalous dimension matrices.
* Describe the effect of gluon emission.
* Be interfaced to Herwig++ (>= 2.7) via Matchbox.

This package provides the shared library for %{name}.

%package devel
Summary:        Development files for ColorFull, a library for calculations in QCD color space
Group:          Development/Libraries/C and C++
Requires:       %{shlib} = %{version}

%description devel
%{name} is a C++ library for calculations in QCD (SU(Nc)) color space. It can
* Square any QCD color amplitude and calculate any interference.
* Create a trace type basis for any number of quarks and gluons.
* Read in and write out color bases.
* Calculate scalar product matrices, i.e., the matrices of scalar products
  between the basis vectors.
* Describe the effect of gluon exchange, including calculating the color
  soft anomalous dimension matrices.
* Describe the effect of gluon emission.
* Be interfaced to Herwig++ (>= 2.7) via Matchbox.

This package provides the headers and source files needed for developing applications using %{name}.

%prep
%setup -q
%patch2 -p1

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

find %{buildroot} -type f -name "*.la" -delete -print

# DON'T INSTALL TEST/EXAMPLE BINARIES, PKG THE CODES AS DOC INSTEAD
rm %{buildroot}%{_bindir}/{ColorFull_test,ColorPlay}

# MOVE LIBS INSTALLED TO STD LIBDIR
mv %{buildroot}%{_libdir}/%{name}/* %{buildroot}%{_libdir}/
rm -fr %{buildroot}%{_libdir}/%{name}/

%post -n %{shlib} -p /sbin/ldconfig
%postun -n %{shlib} -p /sbin/ldconfig

%files -n %{shlib}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS ChangeLog README COPYING
%doc Test/*.cc Examples/*.cc
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/

%changelog
