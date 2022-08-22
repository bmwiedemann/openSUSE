#
# spec file for package gnuprumcu-devel
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


Name:           gnuprumcu
Version:        0.8.0
Release:        0
Summary:        Linker scripts and device specs for PRU MCU variants
License:        BSD-2-Clause
URL:            https://github.com/dinuxbg/gnuprumcu
Source:         https://github.com/dinuxbg/gnuprumcu/releases/download/v%{version}/gnuprumcu-%{version}.tar.gz
BuildRequires:  cross-pru-binutils >= 2.37
BuildRequires:  cross-pru-gcc%{gcc_version}
BuildRequires:  cross-pru-newlib-devel
BuildRequires:  fdupes
BuildArch:      noarch

%description
This package contains the linker scripts, device specs and I/O headers for the
different PRU variants in different TI SoCs. Install this package to allow the
"-mmcu=" GCC compiler option to pick the correct settings for your board.

%prep
%setup -q -n gnuprumcu-%{version}

%build
./configure --prefix=%{_prefix} --host=pru
%make_build

%install
%make_install

%fdupes %{buildroot}

%files
%license COPYING
%doc README.md AUTHORS
%dir %{_prefix}/pru
%dir %{_prefix}/pru/include
%dir %{_prefix}/pru/include/pru
%{_prefix}/pru/include/pru/*
%dir %{_prefix}/pru/lib
%dir %{_prefix}/pru/lib/device-specs
%{_prefix}/pru/lib/device-specs/*

%changelog
