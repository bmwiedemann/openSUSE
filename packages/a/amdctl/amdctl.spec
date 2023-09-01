#
# spec file for package amdctl
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


Name:           amdctl
Version:        0.11
Release:        0
Summary:        Set P-State voltages and clock speeds on recent AMD CPUs on Linux
License:        GPL-3.0-only
URL:            https://github.com/kevinlekiller/amdctl
Source:         amdctl-%{version}.tar.gz

%description
Set P-State voltages and clock speeds on recent AMD CPUs on Linux.

%prep
%autosetup -p1

%build
%make_build

%check
# check if binary is working
#amdctl --help

%install
install -Dm 755 amdctl %{buildroot}/%{_bindir}/amdctl

%files
%license LICENSE
%doc README.md
%{_bindir}/amdctl

%changelog
