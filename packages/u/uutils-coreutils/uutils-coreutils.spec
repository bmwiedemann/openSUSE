#
# spec file for package uutils-coreutils
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


%define gnu_version 9.12
Name:           uutils-coreutils
Version:        0.13.0
Release:        0
Summary:        Rust rewrite of the GNU coreutils
# Legal-Review-Notice: License is MIT only.
# - Linked crates (~206) all permissive (MIT/Apache/BSD/ISC/etc).
# - self_cell is Apache-2.0 OR GPL-2.0-only; Apache-2.0 applies.
# - colored (MPL-2.0) and r-efi (LGPL) vendored but NOT linked.
# - vendor.tar.zst in src.rpm satisfies source availability.
License:        MIT
URL:            https://github.com/uutils/coreutils
Source0:        coreutils-%{version}.tar.zst
Source1:        vendor.tar.zst
# Source-Binary-Exception: vendor.tar.zst:vendor/winapi-*-pc-windows-gnu-*/lib/* -- other-platform: Windows import libraries never used on Linux
# Source-Binary-Exception: vendor.tar.zst:vendor/aws-lc-sys-*/builder/prebuilt-nasm/* -- other-platform: Windows COFF objects for builds without nasm
# Source-Binary-Exception: vendor.tar.zst:vendor/libloading-*/tests/*.dll -- other-platform: Windows test DLLs never loaded on Linux
BuildRequires:  cargo >= 1.89
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  memory-constraints
BuildRequires:  pkgconfig
BuildRequires:  rust >= 1.89
BuildRequires:  xz
BuildRequires:  pkgconfig(libselinux)
# No Obsoletes: replacing GNU coreutils happens only when the user
# explicitly installs this package (Conflicts then resolves it).
Conflicts:      coreutils
Conflicts:      coreutils-single
Conflicts:      coreutils-systemd
Provides:       coreutils = %{gnu_version}
Provides:       coreutils-single = %{gnu_version}
Provides:       coreutils-systemd = %{gnu_version}
Provides:       fileutils = %{gnu_version}
Provides:       mktemp = %{gnu_version}
Provides:       sh-utils = %{gnu_version}
Provides:       stat = %{gnu_version}
Provides:       textutils = %{gnu_version}
ExclusiveArch:  %{rust_tier1_arches}

%description
uutils aims to be a drop-in replacement for the GNU utils.
Differences with GNU are treated as bugs.

This package can replace GNU coreutils (Conflicts/Provides);
without Obsoletes the switch happens only on explicit install.
It installs the standard %{_bindir} utilities, man pages and
completions.

%package doc
Summary:        Documentation for uutils-coreutils
Conflicts:      coreutils-doc
Conflicts:      coreutils-systemd-doc
Provides:       coreutils-doc = %{gnu_version}
Provides:       coreutils-systemd-doc = %{gnu_version}
BuildArch:      noarch

%description doc
Man pages for uutils-coreutils.

%package bash-completion
Summary:        Bash completions for uutils-coreutils
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completions for uutils-coreutils.

%package zsh-completion
Summary:        Zsh completions for uutils-coreutils
Requires:       %{name} = %{version}
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh completions for uutils-coreutils.

%package fish-completion
Summary:        Fish completions for uutils-coreutils
Requires:       %{name} = %{version}
Supplements:    (%{name} and fish)
BuildArch:      noarch

%description fish-completion
Fish completions for uutils-coreutils.

%prep
%autosetup -a1 -p1 -n coreutils-%{version}
# cargo_vendor writes cross linkers (aarch64-linux-gnu-gcc, *-redox-gcc)
# that do not exist on openSUSE native builders; drop those sections,
# keeping [source.*] replacements and rustflags.
sed -i -e '/^\[target\.aarch64-unknown-linux-gnu\]/,/^$/d' -e '/^\[target\..*-redox\]/,/^$/d' .cargo/config.toml

%build
%limit_build -m 2000
export CARGO_NET_OFFLINE=true
PROFILE=release SELINUX_ENABLED=1 MULTICALL=n %make_build build

%install
export CARGO_NET_OFFLINE=true
PROFILE=release SELINUX_ENABLED=1 MULTICALL=n \
  make install PREFIX=%{_prefix} LIBSTDBUF_DIR=%{_libexecdir}/%{name} \
  SKIP_UTILS="hostname more kill" PROG_PREFIX= PROFILE=release MULTICALL=n \
  DATAROOTDIR=%{_datadir} DESTDIR=%{buildroot}
# Upstream installs [ when the test suite is built; keep it (replacement must ship it).
# Remove empty locale placeholders that carry no translation.
find %{buildroot}%{_datadir}/locales -type f -empty -delete || true

%check
export CARGO_NET_OFFLINE=true
# Upstream suite (unix + selinux/chcon/runcon + external stdbuf).
# Skips are TW/16.0 aarch64 failures only: no SELinux, no root,
# no login, tzdata/DST, big-mem, plus 2 flakes passing x86_64.
# cargo 1.100 drops the unhashed deps/libstdbuf.so the exe-dir test needs;
# stage the build output so test_stdbuf_search_order_exe_dir_first finds it.
mkdir -p target/release/deps
cp -a target/release/libstdbuf.so target/release/deps/
cargo test --offline --profile=release --no-default-features \
  --features "feat_os_unix chcon runcon selinux feat_external_libstdbuf" -- \
  --skip test_chcon::range_change \
  --skip test_chcon::recursive_follow_all_symlinks_to_ancestor \
  --skip test_chcon::recursive_follow_args_dir_symlinks_not_nested \
  --skip test_chcon::role_change \
  --skip test_chcon::type_change \
  --skip test_chcon::user_change \
  --skip test_chcon::user_change_repeated \
  --skip test_chcon::user_role_range_type \
  --skip test_chcon::valid_context \
  --skip test_chcon::valid_context_directory \
  --skip test_chcon::valid_context_directory_recursive \
  --skip test_chcon::valid_context_directory_recursive_follow_all_symlinks \
  --skip test_chcon::valid_context_directory_recursive_follow_args_dir_symlinks \
  --skip test_chcon::valid_context_on_broken_symlink \
  --skip test_chcon::valid_context_on_broken_symlink_after_deref \
  --skip test_chcon::valid_context_on_valid_symlink \
  --skip test_chcon::valid_context_on_valid_symlink_override_dereference \
  --skip test_chcon::valid_context_with_prior_xattributes \
  --skip test_chcon::valid_reference \
  --skip test_chcon::valid_reference_multi \
  --skip test_chcon::valid_reference_repeat_flags \
  --skip test_chgrp::test_big_h \
  --skip test_chgrp::test_big_p \
  --skip test_chgrp::test_error_1 \
  --skip test_chgrp::test_fail_silently \
  --skip test_chgrp::test_preserve_root \
  --skip test_chgrp::test_preserve_root_symlink \
  --skip test_chgrp::test_preserve_root_symlink_cwd_root \
  --skip test_chown::test_big_p \
  --skip test_cp::test_cp_preserve_context_with_z_fails \
  --skip test_cp::test_cp_preserve_selinux \
  --skip test_cp::test_cp_preserve_selinux_admin_context \
  --skip test_cp::test_cp_reflink_never \
  --skip test_cp::test_cp_selinux \
  --skip test_cp::test_cp_selinux_context_priority \
  --skip test_cp::test_cp_selinux_empty_context \
  --skip test_cp::test_cp_selinux_invalid \
  --skip test_cp::test_cp_selinux_recursive \
  --skip test_date::test_date_iso_numeric_timezone \
  --skip test_date::test_date_locale_default_format_timezone_position \
  --skip test_date::test_date_rejects_nonexistent_dst_inputs \
  --skip test_date::test_date_tz \
  --skip test_date::test_date_tz_various_formats \
  --skip test_date::test_date_tz_with_relative_time \
  --skip test_date::test_date_utc_time \
  --skip test_date::test_date_utc_vs_local \
  --skip test_dd::test_large_bs_does_not_fault_in_copy_buffer \
  --skip test_logname::test_normal \
  --skip test_logname::test_output_format \
  --skip test_mkdir::test_selinux \
  --skip test_mkdir::test_selinux_invalid \
  --skip test_mkfifo::test_mkfifo_selinux \
  --skip test_mkfifo::test_mkfifo_selinux_invalid \
  --skip test_mv::test_mv_selinux_context \
  --skip test_runcon::custom_context \
  --skip test_runcon::plain_context \
  --skip test_stat::test_stat_selinux \
  --skip test_tail::test_invalid_max_unchanged_stats_is_rejected \
  --skip test_touch::test_touch_changes_time_of_file_in_stdout \
  --exact

%files
%license LICENSE
%doc README.package.md
%{_bindir}/*
%{_libexecdir}/%{name}/
%{_datadir}/locales/

%files doc
%{_mandir}/man1/*.1%{?ext_man}

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/*.bash

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_*

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/*.fish

%changelog
