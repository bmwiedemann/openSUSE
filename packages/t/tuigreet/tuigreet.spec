#
# spec file for package tuigreet
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


Name:           tuigreet
Version:        0.11.1
Release:        0
Summary:        Graphical console greeter for greetd
License:        GPL-3.0-only
Group:          System/Management
URL:            https://github.com/tuigreet/tuigreet
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  cargo-packaging
Recommends:     greetd

%description
Graphical console UI greeter for greetd (using tui-rs)

%prep
%autosetup -p1 -a1

%build
%{cargo_build} -p tuigreet

%install
cargo install --offline --path crates/tuigreet --root %{buildroot}/usr
rm -f %{buildroot}/usr/.crates.toml %{buildroot}/usr/.crates2.json

%check
cargo test -p tuigreet

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
