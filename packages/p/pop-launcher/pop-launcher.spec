#
# spec file for package pop-launcher
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


Name:           pop-launcher
Version:        1.2.4
Release:        0
Summary:        Modular IPC-based desktop launcher service
License:        MPL-2.0
URL:            https://github.com/pop-os/launcher
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(xkbcommon)

%description
Modular IPC-based desktop launcher service, written in Rust. Desktop launchers
may interface with this service via spawning the pop-launcher process and
communicating to it via JSON IPC over the stdin and stdout pipes. The launcher
service will also spawn plugins found in plugin directories on demand, based on
the queries sent to the service.

Using IPC enables each plugin to isolate their data from other plugin processes
and frontends that are interacting with them. If a plugin crashes, the launcher
will continue functioning normally, gracefully cleaning up after the crashed
process. Frontends and plugins may also be written in any language. The
pop-launcher will do its part to schedule the execution of these plugins in
parallel, on demand.

%prep
%autosetup -p1 -a1

%build
export RUSTFLAGS="-C codegen-units=1"
just build-release

%install
just rootdir=%{buildroot} install

%check
%{cargo_test}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_prefix}/lib/%{name}

%changelog
