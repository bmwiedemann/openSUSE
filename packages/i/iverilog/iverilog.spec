#
# spec file for package iverilog
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


Name:           iverilog
Version:        13.0
Release:        0
%define major_ver 13
Summary:        Simulation and synthesis tool for IEEE-1364
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Electronics
URL:            https://steveicarus.github.io/iverilog/
Source:         https://altushost-swe.dl.sourceforge.net/project/iverilog/iverilog/%{version}/%{name}-%{major_ver}_0.tar.gz
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  libbz2-devel
BuildRequires:  python3-Sphinx
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
%setup -q -n %{name}-%{major_ver}_0

%build
%configure
%make_build

#build docs
cd Documentation
make text
cd ..

%install
%make_install
rm %{buildroot}/%{_libdir}/*.a
%fdupes -s %{buildroot}/%{_libdir}/ivl/

#install docs
mkdir -p %{buildroot}/%{_docdir}/%{name}
cp -r Documentation/_build/text/* %{buildroot}/%{_docdir}/%{name}

%check
make check

%files
%license COPYING
%doc README.md
%doc examples
%{_docdir}/%{name}/*
%{_bindir}/iverilog
%{_bindir}/iverilog-vpi
%{_bindir}/vvp
%{_libdir}/ivl
%{_mandir}/man1/iverilog*
%{_mandir}/man1/vvp*

%files devel
%{_includedir}/iverilog

%changelog
