#
# spec file for package iverilog
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


Name:           iverilog
Version:        11.0
Release:        0
%define major_ver 11
Summary:        Simulation and synthesis tool for IEEE-1364
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            http://iverilog.icarus.com/
Source:         ftp://icarus.com/pub/eda/verilog/v%{major_ver}/verilog-%{version}.tar.gz
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  libbz2-devel
BuildRequires:  readline-devel
BuildRequires:  zlib-devel

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

%build
%configure
%make_build

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
