#
# spec file for package image-janitor
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           image-janitor
Version:        0.3.0
Release:        0
Summary:        Cleans up unused kernel drivers and firmware
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/image-janitor
Source0:        image-janitor-%{version}.tar.zst
Source1:        registry.tar.zst

BuildRequires:  cargo
BuildRequires:  cargo-packaging

%description
A simple tool to cleanup unused kernel drivers and firmware files.

%prep
%autosetup -p1 -a1

%build
export CARGO_HOME=$PWD/.cargo
%{cargo_build}

%install
export CARGO_HOME=$PWD/.cargo
%{cargo_install}
mkdir -p %{buildroot}/%{_datadir}/%{name}
install -m644 data/module.list* %{buildroot}/%{_datadir}/%{name}

%check
export CARGO_HOME=$PWD/.cargo
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
