#
# spec file for package ttyper
#
# Copyright (c) 2024 mantarimay
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


%bcond_without test
Name:           ttyper
Version:        1.5.0
Release:        0
Summary:        Terminal-based typing test
License:        MIT
URL:            https://github.com/max-niederman/ttyper
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging

%description
ttyper is a terminal-based typing test built with Rust and tui-rs.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
install -Dm755 target/release/%{name} -t %{buildroot}%{_bindir}

%check
%if %{with test}
%{cargo_test}
%endif

%files
%license LICENSE*
%doc README*
%{_bindir}/%{name}

%changelog
