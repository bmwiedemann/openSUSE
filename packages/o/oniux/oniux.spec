#
# spec file for package oniux
#
# Copyright (c) 2026 onlyJak0b onlyJak0b@mailbox.org
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           oniux
Version:        0.12.0~0
Release:        0
Summary:        Isolate an arbitrary application over the Tor network
License:        Apache-2.0 OR MIT
URL:            https://gitlab.torproject.org/tpo/core/oniux
Source0:        %{name}-%{version}.tar.zst
Source1:        registry.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
# Exclude 32bit archs to prevent oom during compilation
ExcludeArch:    armv6l armv7hl i586

%description
This is still considered experimental software!
oniux is a tool that utilizes various Linux namespaces(7) in order to isolate
an arbitrary application over the Tor network. To achieve this, it makes heavy
use of the onionmasq, which offers a TUN device to send Tor traffic through.

%prep
%autosetup -p1 -a1

%build
export CARGO_HOME=$PWD/.cargo
%{cargo_build}

%install
export CARGO_HOME=$PWD/.cargo
%{cargo_install}

%check
export CARGO_HOME=$PWD/.cargo
%{cargo_test}

%files
%doc README.md
%license LICENSE-APACHE LICENSE-MIT
%{_bindir}/%{name}

%changelog
