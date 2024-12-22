#
# spec file for package bluetui
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


Name:           bluetui
Version:        0.6
Release:        0
Summary:        TUI for managing bluetooth devices
License:        GPL-3.0-or-later
Group:          Hardware/Other
URL:            https://github.com/pythops/bluetui
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  dbus-1-devel
BuildRequires:  rust >= 1.75.0
Requires:       bluez

%description
bluetui is a TUI-based bluetooth connection manager written in Rust.
Which can interact with bluetooth adapters and devices. It aims to be 
an alternative to most bluetooth managers, like blueman.

%prep
%autosetup -a1 -p1

%build
%{cargo_build}

%install
install -Dm755 target/release/%{name} -t %{buildroot}%{_bindir}

%files
%license LICEN*
%doc Readme.md Release.md
%{_bindir}/%{name}

%changelog
