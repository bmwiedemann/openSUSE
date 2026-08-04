#
# spec file for package zlib-rs
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


# Upstream sets the C API version to the zlib API level it implements
# ([package.metadata.capi.library] version in libz-rs-sys-cdylib/Cargo.toml),
# so the library is libz_rs.so.1.3.0 with an soname of libz_rs.so.1.
%define sover 1
Name:           zlib-rs
Version:        0.6.7
Release:        0
Summary:        Memory-safe zlib implementation written in Rust
License:        Zlib
URL:            https://github.com/trifectatechfoundation/zlib-rs
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-c >= 0.10.12
BuildRequires:  cargo-packaging
# MSRV declared by the workspace (rust-version = "1.75").
BuildRequires:  rust >= 1.75

%description
zlib-rs is an implementation of the zlib compression algorithms written in
Rust. It provides the standard zlib C API, so it can be used by existing C
programs, while avoiding the classes of memory-safety bugs that affect
implementations written in C.

The library is installed as libz_rs, next to and independently of the system
zlib. It is not a file-level replacement for it: programs opt in by linking
against libz_rs explicitly.

%package -n libz_rs%{sover}
Summary:        Memory-safe zlib implementation written in Rust

%description -n libz_rs%{sover}
zlib-rs is an implementation of the zlib compression algorithms written in
Rust, exposing the standard zlib C API.

This package provides the shared library.

%package devel
Summary:        Development files for zlib-rs
Requires:       libz_rs%{sover} = %{version}
# The library is API-compatible with zlib and deliberately ships no headers of
# its own, so that it cannot collide with zlib-devel; build against the system
# zlib.h and link with -lz_rs.
Requires:       pkgconfig(zlib)

%description devel
zlib-rs is an implementation of the zlib compression algorithms written in
Rust, exposing the standard zlib C API.

This package contains the files needed to build applications against it.

%prep
%autosetup -p1 -a1

%build
export RUSTFLAGS="%{build_rustflags}"
# The cdylib is listed under [workspace] exclude and has its own lockfile, so
# it is built from its own directory. The vendored sources and the generated
# .cargo/config.toml sit at the tree root; cargo finds them by walking up.
#
# Features: the defaults (c-allocator, std) keep allocation on libc malloc/free
# and enable runtime SIMD detection. gz adds the gz* family of entry points,
# without which a consumer calling gzopen() and friends would fail to link.
#
# gzprintf is deliberately NOT enabled: it is gated on #![feature(c_variadic)],
# which is not available on the stable Rust we build with. gzprintf() is
# therefore absent from this library; everything else in the gz* API is present.
cd libz-rs-sys-cdylib
CFLAGS="%{optflags}" cargo cbuild \
    --offline \
    --release \
    --features gz \
    --library-type cdylib \
    --prefix=%{_prefix} \
    --libdir=%{_libdir}

%install
export RUSTFLAGS="%{build_rustflags}"
cd libz-rs-sys-cdylib
cargo cinstall \
    --offline \
    --release \
    --features gz \
    --library-type cdylib \
    --destdir=%{buildroot} \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --pkgconfigdir=%{_libdir}/pkgconfig

%check
# Exercise the library we actually ship, rather than the Rust crate behind it:
# build upstream's zpipe.c example against the installed shared object and
# round-trip a file through deflate and inflate.
cd libz-rs-sys-cdylib
gcc %{optflags} -o zpipe zpipe.c -I include \
    -L %{buildroot}%{_libdir} -lz_rs
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./zpipe < Cargo.toml > compressed.bin
LD_LIBRARY_PATH=%{buildroot}%{_libdir} ./zpipe -d < compressed.bin > roundtrip.toml
cmp Cargo.toml roundtrip.toml

%ldconfig_scriptlets -n libz_rs%{sover}

%files -n libz_rs%{sover}
%license LICENSE
%{_libdir}/libz_rs.so.%{sover}
%{_libdir}/libz_rs.so.%{sover}.*

%files devel
%license LICENSE
%doc README.md
%{_libdir}/libz_rs.so
%{_libdir}/pkgconfig/libz_rs.pc

%changelog
