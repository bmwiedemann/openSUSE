#
# spec file for package tuigreet
#
# Copyright (c) 2024 SUSE LLC
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
Version:        0.9.1
Release:        0
Summary:        Graphical console greeter for greetd
License:        GPL-3.0-only
Group:          System/Management
URL:            https://github.com/apognu/tuigreet
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  cargo-packaging
Recommends:     greetd

%description
Graphical console UI greeter for greetd (using tui-rs)

%prep
%autosetup -p1 -a1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
