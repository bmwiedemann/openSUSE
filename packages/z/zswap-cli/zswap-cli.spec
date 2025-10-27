#
# spec file for package zswap-cli
#
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%bcond_without systemd
Name:           zswap-cli
Version:        1.1.1
Release:        0
Summary:        Command-line tool to control the zswap kernel module options
License:        MIT
URL:            https://github.com/xvitaly/zswap-cli
Source:         https://github.com/xvitaly/zswap-cli/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.28
BuildRequires:  libboost_program_options-devel >= 1.70.0
BuildRequires:  pandoc
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%endif

%description
Zswap-cli is a command-line tool to control the zswap kernel module options on
the fly.

Zswap is a compressed cache for swap pages. It takes pages that are in the
process of being swapped out to disk and tries to compress them into a
RAM-based memory pool with dynamic allocation.

It trades CPU cycles for a significant performance boost since reading from a
compressed cache is much faster than reading from a swap device.

%prep
%autosetup -p1

%build
%cmake \
	-DBUILD_MANPAGE:BOOL=ON \
%if %{with systemd}
	-DSYSTEMD_INTEGRATION:BOOL=ON \
%else
	-DSYSTEMD_INTEGRATION:BOOL=OFF \
%endif
	%{nil}
%make_build

%install
%cmake_install

%check
%ctest

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license LICENSE
%doc README.md docs/*
%{_bindir}/zswap-cli
%{_mandir}/man1/*.1%{?ext_man}
%if %{with systemd}
%dir %{_sysconfdir}/zswap-cli
%config(noreplace) %{_sysconfdir}/zswap-cli/zswap-cli.conf
%{_prefix}/lib/systemd/system/zswap-cli.service
%endif
%{_datadir}/bash-completion/completions/zswap-cli

%changelog
