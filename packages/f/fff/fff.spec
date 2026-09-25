#
# spec file for package fff
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


Name:           fff
Version:        0.11.0
Release:        0
Summary:        Fuzzy file finder library with a C ABI
License:        MIT AND Apache-2.0 AND BSL-1.0 AND CC0-1.0 AND ISC AND MPL-2.0 AND OLDAP-2.8 AND Unicode-3.0
# Legal-Review-Notice: 155 crates are statically linked into libfff_c (cargo
# tree -e normal -p fff-c). Beyond MIT and the dual
# MIT/Apache-2.0 majority: Apache-2.0 only from lmdb-master-sys, BSL-1.0 from
# xxhash-rust, CC0-1.0 from notify, ISC from inotify and inotify-sys, MPL-2.0
# from option-ext (vendor.tar.zst in the src.rpm carries its source), and
# Unicode-3.0 from the icu_* family. lmdb-master-sys compiles LMDB itself,
# hence OLDAP-2.8 and the bundled() provide below; libgit2 is the system one.
URL:            https://github.com/dmtrKovalenko/fff
Source0:        https://github.com/dmtrKovalenko/fff/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  pkgconfig(libgit2) >= 1.9
Provides:       bundled(lmdb) = 0.9.70
ExclusiveArch:  %{rust_tier1_arches}

%description
fff indexes a directory tree once, then answers fuzzy queries ranked by
match quality and by how recently and how often a file was opened. This
package contains libfff_c, the C ABI of the search engine, in a private
directory for programs that load it through their own FFI (opencode's
file search does).

%prep
%autosetup -p1 -a1
rm -f rust-toolchain.toml

%build
# The workspace asks git2 for its vendored libgit2 sources; libgit2-sys
# honours this variable and links the distribution's libgit2 instead.
export LIBGIT2_NO_VENDOR=1
# Upstream's release profile strips DWARF at link time, which would leave
# the debuginfo package empty.
export CARGO_PROFILE_RELEASE_STRIP=none
# Upstream's binaries enable the zlob feature, a glob matcher compiled with
# Zig at build time; without it the crate uses globset, its pure-Rust path.
%{cargo_build} -p fff-c

%install
install -Dpm 0755 target/release/libfff_c.so %{buildroot}%{_libdir}/%{name}/libfff_c.so

%check
# fff-c's own tests: accessor behaviour and the layout of the versioned
# options struct. fff-core's integration tests (git watcher, LMDB locking,
# fuzzing against real repositories) need a writable checkout and time
# budgets a build host cannot promise, so they are not run.
%{cargo_test} -p fff-c
# The versioned constructor is the entry point FFI consumers call first;
# its presence proves the cdylib exported the C ABI rather than an empty rlib.
nm -D %{buildroot}%{_libdir}/%{name}/libfff_c.so | grep -q ' T fff_create_instance_with$'
ldd %{buildroot}%{_libdir}/%{name}/libfff_c.so | grep -q 'libgit2\.so'

%files
%license LICENSE
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libfff_c.so

%changelog
