#
# spec file for package verilator
#
# Copyright (c) 2022 SUSE LLC
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


Name:           verilator
Version:        4.228
Release:        0
Summary:        Compiling Verilog HDL simulator
License:        Artistic-2.0 OR LGPL-3.0-only
Group:          Productivity/Scientific/Electronics
URL:            https://www.veripool.org/projects/verilator/wiki/Intro
Source0:        https://github.com/verilator/verilator/archive/refs/tags/v%{version}.tar.gz#/verilator-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  perl
BuildRequires:  pkgconfig

%description
Verilator compiles synthesizable Verilog (not test-bench code), plus
some PSL, SystemVerilog and Synthesis assertions into an optimized
model which is in turn wrapped inside a C++/SystemC module for faster
execution.

%package devel
Summary:        Verilator library header files
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
BuildArch:      noarch

%description devel
Development files for Verilator, a compiling Verilog HDL simulator.
It includes header files and a pkgconfig file.

%package        examples
Summary:        Examples for verilator
Group:          Documentation/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    examples
Verilator is a compiling Verilog HDL simulator.

This package contains examples of using verilator.

%prep
%setup -q
# Use real path in she-bangs
sed -i -e '1 s@bin/env perl@bin/perl@' bin/*
sed -i -e '1 s@bin/env python3@bin/python3@' bin/*

%build
autoconf
%configure
%make_build

%install
%make_install

# install examples
install -d %{buildroot}%{_docdir}/%{name}/
mv %{buildroot}%{_datadir}/verilator/examples %{buildroot}%{_docdir}/%{name}/examples

# fix install of devel files
mkdir -p %{buildroot}%{_includedir}/
mv %{buildroot}%{_datadir}/verilator/include/ %{buildroot}%{_includedir}/verilator

%check
mkdir -p "~/.config/gdb/"
echo "set auto-load safe-path /" > "~/.config/gdb/gdbinit"
export DEBUGINFOD_URLS=""
make test

%files
%license Artistic LICENSE
%doc Changes README.rst
%exclude %{_docdir}/%{name}/examples/
%{_bindir}/verilator
%{_bindir}/verilator_bin
%{_bindir}/verilator_bin_dbg
%{_bindir}/verilator_coverage
%{_bindir}/verilator_coverage_bin_dbg
%{_bindir}/verilator_gantt
%{_bindir}/verilator_profcfunc
%{_datadir}/verilator
%{_mandir}/man1/verilator.1%{?ext_man}
%{_mandir}/man1/verilator_coverage.1%{?ext_man}

%files devel
%{_datadir}/pkgconfig/verilator.pc
%{_includedir}/verilator

%files examples
%doc %{_docdir}/%{name}/examples/

%changelog
