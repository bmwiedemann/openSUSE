#
# spec file for package dwarf2json
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 LISA GmbH, Bingen, Germany
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


Name:           dwarf2json
Version:        0.6.0~git.20200714T092604.d1b08fe
Release:        0
Summary:        Generate ELF/DWARF symbol and type information for volatility3
License:        BSD-2-Clause-Patent
URL:            https://github.com/volatilityfoundation/dwarf2json
Source:         %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
BuildRequires:  golang-packaging

%description
%{name} is a Go utility that processes files containing symbol and type
information to generate Volatilty3 Intermediate Symbol File (ISF) JSON output
suitable for Linux and macOS analysis.

%prep
%setup -q
%setup -q -T -D -a 1

%build
export GOFLAGS="-trimpath -mod=vendor"
%goprep github.com/volatilityfoundation/dwarf2json 
%gobuild

%install
%goinstall

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/%{name}

%changelog
