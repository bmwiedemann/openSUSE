#
# spec file for package udunits2
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


%define soname 0

Name:           udunits2
Version:        2.2.28
Release:        0
Summary:        A library for manipulating units of physical quantities
License:        MIT
Group:          Productivity/Scientific/Math
URL:            https://www.unidata.ucar.edu/software/udunits/
Source0:        ftp://ftp.unidata.ucar.edu/pub/udunits/udunits-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  info
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version}
BuildRequires:  CUnit-devel
BuildRequires:  expat-devel
%define ext_info .gz
%else
BuildRequires:  cunit-devel
BuildRequires:  libexpat-devel
%endif

%description
The Unidata units utility, udunits, supports conversion of unit specifications
between formatted and binary forms, arithmetic manipulation of unit
specifications, and conversion of values between compatible scales of
measurement. A unit is the amount by which a physical quantity is measured. For
example:

                  Physical Quantity   Possible Unit
                  _________________   _____________
                        time              weeks
                      distance         centimeters
                        power             watts

This utility works interactively and has two modes. In one mode, both an input
and output unit specification are given, causing the utility to print the
conversion between them. In the other mode, only an input unit specification is
given. This causes the utility to print the definition -- in standard units --
of the input unit.

%package -n lib%{name}-%{soname}
Summary:        Libraries for %{name}
Group:          Development/Libraries/C and C++

%package devel
Summary:        Headers and development libraries for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Conflicts:      udunits < %{version}

%package -n udunits-compat
Summary:        Udunits2 compatibility layer for udunits v1 API
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}-%{release}
Obsoletes:      udunits < %{version}
Provides:       udunits = %{version}

%package -n udunits-compat-devel
Summary:        Udunits2 compatibility layer for udunits v1 API
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}-%{release}
Requires:       udunits-compat = %{version}-%{release}
Obsoletes:      udunits-devel < %{version}
Provides:       udunits-devel = %{version}

%description -n lib%{name}-%{soname}
This package contains the runtime libraries for %{name}.

%description devel
This package contains the files needed for compiling programs using
the %{name} library.

%description -n udunits-compat
A compatibility layer allowing applications written for libudunits to
work with libudunits2.

%description -n udunits-compat-devel
This package contains the files needed for compiling programs using
the udunits2 compatibility library.

%prep
%setup -q -n udunits-%{version}

%build
%configure --docdir=%{_docdir}/%{name} --disable-static
%make_build

%install
%make_install install-html install-pdf

# Install info file
mkdir -p %{buildroot}%{_infodir}/
install -p -m0644 %{name}.info %{buildroot}%{_infodir}

#---Installation with custom docdir does not really work:
pushd %{buildroot}%{_docdir}/%{name}
rm -f *.xml
for f in %{buildroot}%{_datadir}/udunits/*.xml; do
  ln -sr "$f" .
done
popd
#---We provide compat symlinks to provide udunits v1 API:
pushd %{buildroot}%{_libdir}
for f in libudunits2.so*; do
  ln -s "$f" "libudunits.so${f#*.so}"
done
popd
#---cleanup
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_infodir}/dir

%check
%make_build check

%post
install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%post   -n lib%{name}-%{soname} -p /sbin/ldconfig
%postun -n lib%{name}-%{soname} -p /sbin/ldconfig
%post   -n udunits-compat       -p /sbin/ldconfig
%postun -n udunits-compat       -p /sbin/ldconfig
%preun
if [ $1 = 0 ] ; then
  install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files
%{_bindir}/%{name}
%{_datadir}/udunits/
%{_infodir}/%{name}*.info%{?ext_info}
%{_docdir}/%{name}

%files -n lib%{name}-%{soname}
%license COPYRIGHT
%{_libdir}/libudunits2.so.*

%files devel
%{_includedir}/converter.h
%{_includedir}/udunits2.h
%{_libdir}/libudunits2.so

%files -n udunits-compat
%{_libdir}/libudunits.so.*

%files -n udunits-compat-devel
%{_includedir}/udunits.h
%{_libdir}/libudunits.so

%changelog
