#
# spec file for package bun-pty
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


Name:           bun-pty
Version:        0.4.8
Release:        0
Summary:        Pseudo-terminal library for Bun FFI consumers
License:        MIT
# Legal-Review-Notice: 45 crates are statically linked (cargo tree -e normal
# on rust-pty, minus the proc-macro closure); every one is MIT or MIT OR
# Apache-2.0, so the tag is upstream's own licence.
URL:            https://github.com/sursaone/bun-pty
Source0:        https://github.com/sursaone/bun-pty/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
bun-pty spawns processes on a pseudo-terminal from Bun through bun:ffi.
The TypeScript half ships with each consumer; this package builds the
native half, librust_pty (a thin C ABI over portable-pty), into a private
directory for those consumers to load. The npm package carries only a
binary of it.

%prep
%autosetup -p1 -a1

%build
# Upstream's release profile strips the library at link time, which would
# leave the debuginfo package empty.
export CARGO_PROFILE_RELEASE_STRIP=none
# The vendor tarball unpacks next to the crate, so cargo has to run there
# to see its .cargo/config.toml; the macro still writes to ../target.
cd rust-pty
%{cargo_build}

%install
install -Dpm 0755 target/release/librust_pty.so \
    %{buildroot}%{_libdir}/%{name}/librust_pty.so

%check
# All eight entry points the TypeScript side dlopens.
for sym in spawn read write resize kill close get_pid get_exit_code; do
    nm -D %{buildroot}%{_libdir}/%{name}/librust_pty.so | grep -q " T bun_pty_$sym$"
done

%files
%license LICENSE
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/librust_pty.so

%changelog
