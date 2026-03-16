#
# spec file for package killport
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


Name:           killport
Version:        2.0.0
Release:        0
Summary:        A tool to easily kill processes running on a specified port
License:        MIT
Group:          System/Console
URL:            https://github.com/jkfran/killport
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source3:        killport.1
BuildRequires:  cargo-packaging

%description
A command-line utility for killing processes listening on specific ports.
It's designed to be simple, fast, and effective.

Features:
- Kill processes by port number
- Supports multiple port numbers
- Verbosity control

%prep
%autosetup -a1

%build
%{cargo_build}

%install
%{cargo_install}
install -d %{buildroot}/%{_mandir}/man1
install -m 0644 %{_sourcedir}/killport.1 %{buildroot}/%{_mandir}/man1

%check
cargo test -- --test-threads=1

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
# Manpages
%{_mandir}/man1/killport*

%changelog
