#
# spec file for package bees
#
# Copyright (c) 2022 SUSE LLC
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


Name:           bees
Version:        0.8
Release:        0
Summary:        Best-Effort Extent-Same, a btrfs deduplication agent
License:        GPL-3.0-only
Group:          System/Filesystems
URL:            https://github.com/Zygo/bees
Source:         https://github.com/Zygo/bees/archive/refs/tags/v%{version}.tar.gz
Patch1:         fix-Makefile-version.diff
BuildRequires:  gcc-c++
BuildRequires:  libbtrfs-devel
BuildRequires:  libuuid-devel
BuildRequires:  make

%description
bees is a block-oriented userspace deduplication agent designed for large btrfs
filesystems. It is an offline dedupe combined with an incremental data scan
capability to minimize time data spends on disk from write to dedupe.

Hilights:

* Space-efficient hash table and matching algorithms - can use as little as 1
  GB hash table per 10 TB unique data (0.1GB/TB)
* Daemon incrementally dedupes new data using btrfs tree search
* Works with btrfs compression - dedupe any combination of compressed and uncompressed files
* Persistent hash table for rapid restart after shutdown
* Whole-filesystem dedupe - including snapshots
* Constant hash table size - no increased RAM usage if data set becomes larger
* Works on live data - no scheduled downtime required
* Automatic self-throttling based on system load

%prep
%setup -q
%patch1 -p1

%build
cat >localconf <<-EOF
	SYSTEMD_SYSTEM_UNIT_DIR=%{_unitdir}
	LIBEXEC_PREFIX=%{_bindir}
	LIB_PREFIX=%{_libdir}
	PREFIX=%{_prefix}
	LIBDIR=%{_libdir}
	DEFAULT_MAKE_TARGET=all
EOF

%make_build

%install
%make_install

%files
%license COPYING
%doc README.md
%{_bindir}/bees
%{_sbindir}/beesd
%{_unitdir}/beesd@.service
%dir %{_sysconfdir}/bees
%{_sysconfdir}/bees/beesd.conf.sample

%changelog
