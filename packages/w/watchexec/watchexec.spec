#
# spec file for package watchexec
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


Name:           watchexec
Version:        1.22.0
Release:        0
Summary:        Watches a path and runs a command whenever it detects modifications.
License:        Apache-2.0
Group:          Productivity/Other
URL:            https://github.com/watchexec/watchexec
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
BuildRequires:  cargo-packaging

%description
A simple, standalone tool that watches a path and runs a command
whenever it detects modifications.

%prep
%autosetup -a1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
%{cargo_build}

%install
# binary
install -Ddm 0755 %{buildroot}%{_bindir}
strip %{_builddir}/%{name}-%{version}/target/release/watchexec
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/watchexec %{buildroot}%{_bindir}/watchexec

# manpages
install -Dd %{buildroot}/%{_mandir}/man1
install -m 0644 doc/watchexec.1 %{buildroot}%{_mandir}/man1/watchexec.1

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%doc doc/watchexec.1.md
%doc doc/watchexec.1.pdf
%{_mandir}/man1/watchexec.1%{?ext_man}
%{_bindir}/watchexec

%changelog
