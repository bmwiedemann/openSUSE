#
# spec file for package thin-provisioning-tools
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%global debug_package %{nil}
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define origname thin-provisioning-tools
Name:           %{origname}%{psuffix}
Version:        1.3.3
Release:        0
Summary:        Thin Provisioning Tools
# Legal-Review-Notice: upstream itself is GPL-3.0-only (COPYING), but every
# shipped tool is a symlink to one statically linked Rust binary
# (pdata_tools), so the binary also contains the vendored crates.
# Re-derived on this re-vendor with "cargo tree --offline -p thinp -e normal"
# over the refreshed vendor.tar.zst: 77 of the 212 vendored crates are
# actually linked. Build-only and dev-only crates are deliberately excluded
# because their code is not in the binary - notably bindgen (BSD-3-Clause),
# clang-sys (Apache-2.0) and libloading (ISC), which devicemapper-sys uses
# only to generate FFI bindings at build time, and r-efi, whose
# LGPL-2.1-or-later option is UEFI-target-only and absent from the Linux
# graph.
# Where a crate offers a choice we elect MIT: it is on offer from every
# dual/multi-licensed crate in the linked set, so a single election covers
# all of them and no Zlib, 0BSD, BSD-2-Clause, Unlicense or BSL-1.0
# obligation is taken on. Only the unavoidable licences are declared:
#  - GPL-3.0-only  upstream itself
#  - MIT           12 crates offering nothing else (console, data-encoding,
#                  indicatif, libudev-sys, nix, nom, quick-xml, retry,
#                  simd-adler32, strsim, udev, unit-prefix), plus every
#                  crate for which MIT was elected
#  - Apache-2.0    exitcode 1.1.2, which offers no alternative
#  - MPL-2.0       devicemapper 0.34.8 and devicemapper-sys 0.3.3, reached
#                  through the thin_migrate tool
#  - Unicode-3.0   unicode-ident 1.0.24, whose expression is an AND
# Compatibility, flagged rather than silently assumed: Apache-2.0 and
# MPL-2.0 are each one-way compatible with GPLv3, so the combined binary is
# distributable and is effectively GPL-3.0-only as a whole; the reverse
# direction is not claimed. MPL-2.0 section 3.2 source availability is
# satisfied because the complete vendor.tar.zst ships in the src.rpm.
# The licence text of every linked crate that ships one is installed below
# %%{_defaultlicensedir} (crc32c 0.6.8 declares MIT OR Apache-2.0 but ships
# no licence file of its own).
License:        Apache-2.0 AND GPL-3.0-only AND MIT AND MPL-2.0 AND Unicode-3.0
URL:            https://github.com/jthornber/thin-provisioning-tools/
Source0:        %{origname}-%{version}.tar.zst
Source1:        vendor.tar.zst
# PATCH-FIX-UPSTREAM thin-provisioning-tools-tests-clap-single-alias.patch gh#jthornber/thin-provisioning-tools#328
# clap 4.6.2 renders "alias" rather than "aliases" for an option with
# exactly one alias, and tests/thin_delta.rs hardcodes the old wording.
# Upstream CI never sees it because it builds from the committed
# Cargo.lock, which pins clap 4.6.1; we re-resolve (cargo_vendor
# update=true), so we get the newer clap and the two help assertions fail.
Patch0:         thin-provisioning-tools-tests-clap-single-alias.patch
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(devmapper)
BuildRequires:  pkgconfig(libudev)
# Everything below is main-flavour only. The test flavour builds no binary
# package at all, so guard the declarations themselves and not just %%files:
# rpmbuild would drop a package that has no %%files, but OBS reads the
# declarations when it schedules, and an unguarded one would advertise a
# competing provider of thin-provisioning-tools from the test flavour.
%if %{without test}
BuildRequires:  fdupes
BuildRequires:  suse-module-tools
Requires(post): coreutils
Requires(postun): coreutils
Conflicts:      device-mapper < 1.02.115
%endif

%description
A suite of tools for thin provisioning on Linux.

%prep
%autosetup -p1 -a1 -n %{origname}-%{version}

%build
%if %{without test}
%{cargo_build}
%endif

%if %{with test}
%check
# %%check was 267s of a 376s build (71%%), and 88 packages build-depend on
# this, so a test flake stalled a large fan-out. It now runs in its own
# flavour, which builds no binary package. Note there is no %%build here on
# purpose: cargo test compiles in the test profile anyway, so running
# %%cargo_build first would only add a throwaway release compile.
%{cargo_test}
%endif

%if %{without test}
%install
make install STRIP="/bin/true" MANPATH=%{buildroot}%{_mandir} BINDIR=%{buildroot}%{_sbindir}

# The binary statically links the vendored crates, and MIT and Apache-2.0
# both require their notice to travel with it, while upstream's COPYING
# covers only the GPL-3.0 part. Ship the licence text of each crate that is
# genuinely linked; the list is derived at build time so it cannot go stale
# across a re-vendor. Installed straight into the buildroot rather than
# staged for %%license, so that %%fdupes can collapse the many byte-identical
# copies of the stock Apache-2.0 and MIT texts (~500 KB of pure duplication
# otherwise, which rpmlint scores as files-duplicated-waste).
install -Dpm 0644 COPYING %{buildroot}%{_defaultlicensedir}/%{origname}/COPYING
cargo tree --offline --quiet -e normal --prefix none \
    | awk 'NF >= 2 { print $1 "-" substr($2, 2) }' | sort -u > vendor-licenses.list
test -s vendor-licenses.list
while read -r crate; do
    test -d "vendor/$crate" || continue
    for f in "vendor/$crate"/LICENSE* "vendor/$crate"/COPYING* \
             "vendor/$crate"/NOTICE* "vendor/$crate"/UNLICENSE*; do
        test -f "$f" && install -Dpm 0644 "$f" \
            "%{buildroot}%{_defaultlicensedir}/%{origname}/vendor/$crate/${f##*/}"
    done
done < vendor-licenses.list
%fdupes %{buildroot}%{_defaultlicensedir}/%{origname}/vendor

%post
%{?regenerate_initrd_post}

%postun
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%files
%doc README.md
%license %{_defaultlicensedir}/%{origname}
%{_sbindir}/cache_check
%{_sbindir}/cache_dump
%{_sbindir}/cache_metadata_size
%{_sbindir}/cache_repair
%{_sbindir}/cache_restore
%{_sbindir}/cache_writeback
%{_sbindir}/era_check
%{_sbindir}/era_dump
%{_sbindir}/era_invalidate
%{_sbindir}/era_restore
%{_sbindir}/pdata_tools
%{_sbindir}/thin_check
%{_sbindir}/thin_delta
%{_sbindir}/thin_dump
%{_sbindir}/thin_ls
%{_sbindir}/thin_metadata_pack
%{_sbindir}/thin_metadata_size
%{_sbindir}/thin_metadata_unpack
%{_sbindir}/thin_migrate
%{_sbindir}/thin_repair
%{_sbindir}/thin_restore
%{_sbindir}/thin_rmap
%{_sbindir}/thin_trim
%{_mandir}/man8/cache_check.8%{?ext_man}
%{_mandir}/man8/cache_dump.8%{?ext_man}
%{_mandir}/man8/cache_metadata_size.8%{?ext_man}
%{_mandir}/man8/cache_repair.8%{?ext_man}
%{_mandir}/man8/cache_restore.8%{?ext_man}
%{_mandir}/man8/cache_writeback.8%{?ext_man}
%{_mandir}/man8/era_check.8%{?ext_man}
%{_mandir}/man8/era_dump.8%{?ext_man}
%{_mandir}/man8/era_invalidate.8%{?ext_man}
%{_mandir}/man8/era_restore.8%{?ext_man}
%{_mandir}/man8/thin_check.8%{?ext_man}
%{_mandir}/man8/thin_delta.8%{?ext_man}
%{_mandir}/man8/thin_dump.8%{?ext_man}
%{_mandir}/man8/thin_ls.8%{?ext_man}
%{_mandir}/man8/thin_metadata_pack.8%{?ext_man}
%{_mandir}/man8/thin_metadata_size.8%{?ext_man}
%{_mandir}/man8/thin_metadata_unpack.8%{?ext_man}
%{_mandir}/man8/thin_migrate.8%{?ext_man}
%{_mandir}/man8/thin_repair.8%{?ext_man}
%{_mandir}/man8/thin_restore.8%{?ext_man}
%{_mandir}/man8/thin_rmap.8%{?ext_man}
%{_mandir}/man8/thin_trim.8%{?ext_man}
%endif

%changelog
