#
# spec file for package wiremix
#
# Copyright (c) 2026 Jakob onlyjak0b@mailbox.org
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

Name:           wiremix
Version:        0.10.0~0
Release:        0
Summary:        Simple TUI audio mixer for PipeWire
License:        MIT OR Apache-2.0
Url:            https://github.com/tsowell/wiremix
Source0:        %{name}-%{version}.tar.zst
Source1:        registry.tar.zst
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(libpipewire-0.3)

%description
wiremix is a simple TUI audio mixer for PipeWire.
You can use it to adjust volumes, route audio
between devices and applications, and configure
audio device settings like input/output ports and
profiles.

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
%license LICENSE-MIT
%license LICENSE-APACHE
%{_bindir}/%{name}

%changelog
