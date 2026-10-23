#
# spec file for package verilator
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        5.052
Release:        0
Summary:        Compiling Verilog HDL simulator
License:        Artistic-2.0 OR LGPL-3.0-only
Group:          Productivity/Scientific/Electronics
URL:            https://verilator.org/
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  bison
# Required by the CMake integration examples run by make test.
BuildRequires:  cmake >= 3.19
BuildRequires:  flex
BuildRequires:  gcc-c++ >= 10
BuildRequires:  help2man
BuildRequires:  jemalloc-devel
BuildRequires:  perl
BuildRequires:  python3-base >= 3.9
BuildRequires:  python3-distro
BuildRequires:  z3
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-devel = %{version}-%{release}
Requires:       perl
Requires:       z3

%description
Verilator compiles synthesizable Verilog (not test-bench code), plus
some PSL, SystemVerilog and Synthesis assertions into an optimized
model which is in turn wrapped inside a C++/SystemC module for faster
execution.

%package devel
Summary:        Verilator library header files
Group:          Development/Languages/C and C++
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gcc-c++ >= 10
Requires:       make
Requires:       pkgconfig(liblz4)
Requires:       pkgconfig(zlib)

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
sed -i '1s@/usr/bin/env @/usr/bin/@' bin/*

%build
export VERILATOR_SRC_VERSION=v%{version}
autoconf
%configure --disable-partial-static
%make_build

%install
%make_install pkgconfigdir=%{_libdir}/pkgconfig
install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/verilator/examples %{buildroot}%{_docdir}/%{name}/

%check
export DEBUGINFOD_URLS=""
make test

%files
%license LICENSE LICENSES
%doc Changes README.rst
%{_bindir}/verilator*
%dir %{_datadir}/verilator
%{_datadir}/verilator/bin
%{_mandir}/man1/verilator*.1%{?ext_man}

%files devel
%{_datadir}/verilator/include
%{_datadir}/verilator/verilator-config*.cmake
%{_libdir}/pkgconfig/verilator.pc

%files examples
%doc %{_docdir}/%{name}/examples/

%changelog
