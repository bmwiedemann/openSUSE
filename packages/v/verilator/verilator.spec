#
# spec file for package verilator
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


Name:           verilator
Version:        4.010
Release:        0
Summary:        Compiling Verilog HDL simulator
License:        Artistic-2.0 OR LGPL-3.0-only
Group:          Productivity/Scientific/Electronics
Url:            https://www.veripool.org/projects/verilator/wiki/Intro
Source0:        https://www.veripool.org/ftp/%{name}-%{version}.tgz
Source1:        verilator-rpmlintrc
Patch0:         add-shebangs.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gdb
BuildRequires:  perl
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

%package        doc
Summary:        Documentation for verilator in HTML format
Group:          Documentation/HTML
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    doc
Verilator is a compiling Verilog HDL simulator.

This package contains documentation for verilator in HTML format.

%package        doc-pdf
Summary:        Documentation for verilator in PDF format
Group:          Documentation/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description    doc-pdf
Verilator is a compiling Verilog HDL simulator.

This package contains documentation for verilator in PDF format.

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
# Put real perl binary location into the patch
sed -e 's:%%__perl:%__perl:' %{PATCH0} | patch -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install

# install documentation
install -d %{buildroot}%{_docdir}/%{name}/
install -Dm644 *.html %{buildroot}%{_docdir}/%{name}/
install -Dm644 *.pdf %{buildroot}%{_docdir}/%{name}/

# install examples
mv %{buildroot}%{_datadir}/verilator/examples %{buildroot}%{_docdir}/%{name}/examples

# fix install of devel files
mkdir -p %{buildroot}%{_includedir}/
mv %{buildroot}%{_datadir}/verilator/include/ %{buildroot}%{_includedir}/verilator

%check
make test

%files
%license Artistic COPYING.LESSER
%doc Changes README
%exclude %{_docdir}/%{name}/*.html
%exclude %{_docdir}/%{name}/*.pdf
%exclude %{_docdir}/%{name}/examples/
%{_bindir}/verilator
%{_bindir}/verilator_bin
%{_bindir}/verilator_bin_dbg
%{_bindir}/verilator_coverage
%{_bindir}/verilator_coverage_bin_dbg
%{_bindir}/verilator_gantt
%{_bindir}/verilator_profcfunc
%{_datadir}/verilator
%{_mandir}/man1/verilator.1.gz
%{_mandir}/man1/verilator_coverage.1.gz
%{_mandir}/man1/verilator_gantt.1.gz
%{_mandir}/man1/verilator_profcfunc.1.gz

%files devel
%{_datadir}/pkgconfig/verilator.pc
%{_includedir}/verilator

%files doc
%{_docdir}/%{name}/*.html

%files doc-pdf
%{_docdir}/%{name}/*.pdf

%files examples
%doc %{_docdir}/%{name}/examples/

%changelog
