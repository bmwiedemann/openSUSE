#
# spec file for package iverilog
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


Name:           iverilog
Version:        10.2
Release:        0
%define major_ver 10
Summary:        Simulation and synthesis tool for IEEE-1364
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
Url:            http://iverilog.icarus.com/
Source:         ftp://icarus.com/pub/eda/verilog/v%{major_ver}/verilog-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/steveicarus/iverilog/commit/5bb6c7f53a6ab5b44c282ba5b118927fd4f17e4f.patch
Patch0:         Fix-makefile-rules-for-header-files-generated-by-bison.patch
# PATCH-FIX-UPSTREAM https://patch-diff.githubusercontent.com/raw/steveicarus/iverilog/pull/257.patch
Patch1:         fix-cfparse-include-order-causing-lto-type-mismatch.patch
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Icarus Verilog is a Verilog compiler that generates a variety of
engineering formats, including simulation. It strives to be true
to the IEEE-1364 standard.

%package        devel
Summary:        Icarus Verilog development files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description    devel
This package contains necessary header files for Icarus Verilog

%prep
%setup -q -n verilog-%{version}
%patch0 -p1
%patch1 -p1

%build
%configure
# Can not use make_build here, as the V=1 overwrites a Makefile variable
# https://github.com/steveicarus/iverilog/issues/256
make %{_smp_mflags}

%install
%make_install
rm %{buildroot}/%{_libdir}/*.a
%fdupes -s %{buildroot}/%{_libdir}/ivl/

%check
make check

%files
%license COPYING
%doc README.txt BUGS.txt QUICK_START.txt ieee1364-notes.txt
%doc swift.txt netlist.txt t-dll.txt vpi.txt tgt-fpga/fpga.txt
%doc cadpli/cadpli.txt xilinx-hint.txt examples
%{_mandir}/man1/*
%{_bindir}/*
%{_libdir}/ivl/

%files devel
%{_includedir}/*

%changelog
