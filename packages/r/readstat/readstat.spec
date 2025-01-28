#
# spec file for package readstat
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

%if 0%{?sle_version} == 150000 || 0%{?suse_version} >= 1550
%bcond_without libcsv
%else
%bcond_with    libcsv
%endif

%define major 1
%define libname lib%{name}
%define libname_ver %{libname}%{major}
Name:           readstat
Version:        %{major}.1.9
Release:        0
Summary:        Command-line tool (+ C library) for converting SAS, Stata, and SPSS files
License:        MIT
URL:            https://github.com/WizardMac/ReadStat
Source0:        https://github.com/WizardMac/ReadStat/archive/v%{version}.tar.gz#/ReadStat-%{version}.tar.gz
# PATCH-FIX-UPSTREAM
Patch0:         0001-Fix-use-after-free.patch
BuildRequires:  autoconf
BuildRequires:  automake
%if %{with libcsv}
BuildRequires:  libcsv-devel
%endif
BuildRequires:  libtool
BuildRequires:  zlib-devel

%description
ReadStat is a command-line tool and C library for reading 
files from popular stats packages. Supported data formats include:

  - SAS: SAS7BDAT (binary file) and XPORT (transport file)
  - Stata: DTA (binary file) versions 104-119
  - SPSS: POR (portable file), SAV (binary file), and ZSAV (compressed binary)

Supported metadata formats include:

  - SAS: SAS7BCAT (catalog file) and .sas (command file)
  - Stata: .dct (dictionary file)
  - SPSS: .sps (command file)

There is also write support for all the data formats, but not the metadata
formats. The produced SAS7BDAT files still cannot be read by SAS.

%package -n    %{libname_ver}
Summary:        Command-line tool (+ C library) for converting SAS, Stata, and SPSS files

%description -n    %{libname_ver}
ReadStat is a command-line tool and C library for reading 
files from popular stats packages. Supported data formats include:

  - SAS: SAS7BDAT (binary file) and XPORT (transport file)
  - Stata: DTA (binary file) versions 104-119
  - SPSS: POR (portable file), SAV (binary file), and ZSAV (compressed binary)

Supported metadata formats include:

  - SAS: SAS7BCAT (catalog file) and .sas (command file)
  - Stata: .dct (dictionary file)
  - SPSS: .sps (command file)

There is also write support for all the data formats, but not the metadata
formats. The produced SAS7BDAT files still cannot be read by SAS.

%package devel
Summary:        Development files for %{name}
Requires:       %{libname_ver} = %{version}

%description devel
ReadStat is a command-line tool and C library for reading 
files from popular stats packages. Supported data formats include:

  - SAS: SAS7BDAT (binary file) and XPORT (transport file)
  - Stata: DTA (binary file) versions 104-119
  - SPSS: POR (portable file), SAV (binary file), and ZSAV (compressed binary)

Supported metadata formats include:

  - SAS: SAS7BCAT (catalog file) and .sas (command file)
  - Stata: .dct (dictionary file)
  - SPSS: .sps (command file)

There is also write support for all the data formats, but not the metadata
formats. The produced SAS7BDAT files still cannot be read by SAS.

This package contains files for development.

%prep
%autosetup -p1 -n ReadStat-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure
%make_build
# Build tests without executing
%make_build check TESTS=""

%install
%make_install

rm %{buildroot}%{_libdir}/%{libname}.la

%check
%make_build check

%post -n %{libname_ver} -p /sbin/ldconfig
%postun -n %{libname_ver} -p /sbin/ldconfig

%files devel
%doc README.md
%{_bindir}/extract_metadata
%{_bindir}/%{name}
%{_includedir}/%{name}.h
%{_libdir}/%{libname}.so
%{_mandir}/man1/extract_metadata.1%{?ext_man}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files -n %{libname_ver}
%license LICENSE
%{_libdir}/%{libname}.so.*

%changelog
