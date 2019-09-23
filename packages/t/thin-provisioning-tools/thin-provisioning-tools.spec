#
# spec file for package thin-provisioning-tools
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.8.5
Release:        0
Summary:        Thin Provisioning Tools
License:        GPL-3.0-only
Group:          System/Base
URL:            https://github.com/jthornber/thin-provisioning-tools/
Source0:        https://github.com/jthornber/thin-provisioning-tools/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         boost_168.patch
# PATCH-FIX-UPSTREAM https://github.com/jthornber/thin-provisioning-tools/commit/6332962ee866f5289de87ab70cd3db863298982c.patch
Patch2:         ft-lib_bcache-rename-raise-raise_.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libaio-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libexpat-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  suse-module-tools
Requires(post): coreutils
Requires(postun): coreutils
Conflicts:      device-mapper < 1.02.115

%description
A suite of tools for thin provisioning on Linux.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
  --bindir=%{_sbindir} \
  --enable-testing \
  --enable-dev-tools \
  --with-optimisation="%{optflags}" \
# In generated Makefile V=@ is used, in order to achieve verbose build ve
# must override it as V=""
make %{?_smp_mflags} V=""

%install
%make_install STRIP="/bin/true"

%post
%{?regenerate_initrd_post}

%postun
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%files
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
%{_sbindir}/thin_generate_metadata
%{_sbindir}/thin_ll_dump
%{_sbindir}/thin_ls
%{_sbindir}/thin_metadata_size
%{_sbindir}/thin_repair
%{_sbindir}/thin_restore
%{_sbindir}/thin_rmap
%{_sbindir}/thin_scan
%{_sbindir}/thin_show_duplicates
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
%{_mandir}/man8/thin_metadata_size.8%{?ext_man}
%{_mandir}/man8/thin_repair.8%{?ext_man}
%{_mandir}/man8/thin_restore.8%{?ext_man}
%{_mandir}/man8/thin_rmap.8%{?ext_man}
%{_mandir}/man8/thin_trim.8%{?ext_man}

%changelog
