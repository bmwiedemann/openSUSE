#
# spec file for package cargo-auditable
#
# Copyright (c) 2023 SUSE LLC
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


%define __rustflags -Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=2 -C incremental=false
%define __cargo CARGO_FEATURE_VENDORED=1 RUSTFLAGS="%{__rustflags}" %{_bindir}/cargo
%define __cargo_common_opts %{?_smp_mflags}

Name:           cargo-auditable
Version:        0.6.0~0
Release:        0
Summary:        A tool to embed auditing information in ELF sections of rust binaries
#               If you know the license, put it's SPDX string here.
#               Alternately, you can use cargo lock2rpmprovides to help generate this.
License:        (Apache-2.0 OR MIT) AND Unicode-DFS-2016 AND (0BSD OR MIT OR Apache-2.0) AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (Apache-2.0 OR Apache-2.0 WITH LLVM-exception OR MIT) AND (Apache-2.0 OR MIT OR Zlib) AND (Apache-2.0 OR MIT OR Zlib) AND (MIT OR Unlicense) AND (Apache-2.0 OR Zlib OR MIT) AND MIT
#               Select a group from this link:
#               https://en.opensuse.org/openSUSE:Package_group_guidelines
Group:          Development/Languages/Rust
URL:            https://github.com/rust-secure-code/cargo-auditable
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
# We can't dep on cargo-packaging because we would create a dependency loop.
# BuildRequires:  cargo-packaging
BuildRequires:  cargo
BuildRequires:  zstd
Requires:       cargo

%description
Know the exact crate versions used to build your Rust executable. Audit binaries for known bugs or
security vulnerabilities in production, at scale, with zero bookkeeping. This works by embedding
data about the dependency tree in JSON format into a dedicated linker section of the compiled
executable.

%prep
%autosetup -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
unset LIBSSH2_SYS_USE_PKG_CONFIG
%{__cargo} build \
    %{__cargo_common_opts} \
    --offline --release

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/cargo-auditable %{buildroot}%{_bindir}/cargo-auditable

%files
%{_bindir}/cargo-auditable

%changelog
