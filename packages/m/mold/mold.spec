#
# spec file for package mold
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


Name:           mold
Version:        3.0.0
Release:        0
Summary:        A Modern Linker (mold)
License:        MIT
URL:            https://github.com/rui314/mold
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo
BuildRequires:  clang
BuildRequires:  diffutils
BuildRequires:  gawk
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel-static
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.95
BuildRequires:  tar
BuildRequires:  zstd
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
Suggests:       update-alternatives
OrderWithRequires(pre): update-alternatives

%description
mold is a faster drop-in replacement for existing Unix linkers.
It is several times faster than LLVM lld linker, the second-fastest
open-source linker.
mold is created for increasing developer productivity by reducing
build time especially in rapid debug-edit-rebuild cycles.

%prep
%autosetup -p1 -a1

%build
# mold embeds the wrapper library dir at compile time (default
# /usr/local/lib); openSUSE uses lib64, so export it for both
# the build and the install below.
export MOLD_LIBDIR=%{_libdir}
export ZSTD_SYS_USE_PKG_CONFIG=1
cargo build --release --offline --features system-allocator

%install
export MOLD_LIBDIR=%{_libdir}
# install-mold.sh hardcodes PREFIX/share/doc, not the distro docdir, so install
# the same layout by hand into the openSUSE paths.
install -D -m 0755 target/release/mold %{buildroot}%{_bindir}/mold
ln -sf mold %{buildroot}%{_bindir}/ld.mold
install -D -m 0755 target/release/mold-wrapper.so %{buildroot}%{_libdir}/mold/mold-wrapper.so
install -d %{buildroot}%{_libexecdir}/mold
ln -sf ../../bin/mold %{buildroot}%{_libexecdir}/mold/ld
install -D -m 0644 docs/mold.1 %{buildroot}%{_mandir}/man1/mold.1
ln -sf mold.1 %{buildroot}%{_mandir}/man1/ld.mold.1
install -D -m 0644 LICENSE %{buildroot}%{_docdir}/mold/LICENSE

%check
export MOLD_LIBDIR=%{_libdir}
export ZSTD_SYS_USE_PKG_CONFIG=1
# Full suite: unit tests plus the shell integration tests. Targets without
# a compiler+QEMU pair in the buildroot are skipped by the runner, so this
# exercises every native case with no cross toolchain needed.
cargo test --release --offline --features system-allocator

%pre
if [ $1 -eq 2 ] && [ -f %{_sbindir}/update-alternatives ] && [ -f %{_sysconfdir}/alternatives/ld ] ; then
  "%{_sbindir}/update-alternatives" --remove ld "%{_bindir}/ld.mold"
fi

%files
%{_bindir}/mold
%{_bindir}/ld.mold
%dir %{_libdir}/mold
%{_libexecdir}/mold/ld
%dir %{_libexecdir}/mold
%{_libdir}/mold/mold-wrapper.so
%{_mandir}/man1/mold.1%{?ext_man}
%{_mandir}/man1/ld.mold.1%{?ext_man}
%dir %{_docdir}/mold
%license %{_docdir}/mold/LICENSE

%changelog
