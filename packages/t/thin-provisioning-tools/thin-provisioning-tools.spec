#
# spec file for package thin-provisioning-tools
#
# Copyright (c) 2025 SUSE LLC
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


Name:           thin-provisioning-tools
Version:        1.1.0
Release:        0
Summary:        Thin Provisioning Tools
License:        GPL-3.0-only
URL:            https://github.com/jthornber/thin-provisioning-tools/
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  clang-devel
BuildRequires:  device-mapper-devel
BuildRequires:  pkgconfig
BuildRequires:  suse-module-tools
BuildRequires:  pkgconfig(libudev)
Requires(post): coreutils
Requires(postun): coreutils
Conflicts:      device-mapper < 1.02.115

%description
A suite of tools for thin provisioning on Linux.

%prep
%autosetup -a1

%build
%{cargo_build}

%install
make install STRIP="/bin/true" MANPATH=%{buildroot}%{_mandir} BINDIR=%{buildroot}%{_sbindir}

%check
%{cargo_test}

%post
%{?regenerate_initrd_post}

%postun
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%files
%doc README.md
%license COPYING
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

%changelog
