#
# spec file for package wlgreet
#
# Copyright (c) 2020 SUSE LLC
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

Name:           wlgreet
Version:        0.2
Release:        0
Summary:        Raw wayland greeter for greetd
License:        GPL-3.0
Group:          System/Management
URL:            https://git.sr.ht/~kennylevinsen/wlgreet
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        cargo_config
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  rust-packaging
Recommends:     greetd

%description
Raw wayland greeter for greetd, to be run under sway or similar. 
Note that cage is currently not supported due to it lacking wlr-layer-shell-unstable support.

%prep
%setup -qa1
%cargo_prep
cp %{SOURCE2} .cargo/config

%build
%cargo_build

%install

install -D -p -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
