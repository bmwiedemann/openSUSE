#
# spec file for package boulette
#
# Copyright (c) 2025 SUSE LLC
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


Name:           boulette
Version:        0.2.3
Release:        0
Summary:        Terminal confirmation prompt that prevents you from shutting down remote hosts
License:        MIT
URL:            https://github.com/pipelight/boulette
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.82.0
BuildRequires:  cargo-packaging
BuildRequires:  zstd

%description
Boulette prevents you from accidentally damaging remote hosts by raising a
warning prompt on dangerous commands. The prompt simply asks for user
confirmation, and can also enforce a challenge resolution to decide whether to
resume(or abort) the command.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%check
%{cargo_test}

%files
# examples directory is not included in latest release...
%doc README.md
%license LICENSE
%{_bindir}/boulette

%changelog
