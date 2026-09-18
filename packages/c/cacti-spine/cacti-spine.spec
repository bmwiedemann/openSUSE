#
# spec file for package cacti-spine
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%{!?make_build: %define make_build make %{?_smp_mflags}}
Name:           cacti-spine
Version:        1.2.31
%global base_version %(echo %{version} | sed 's/+[^+]*//')
%global next_base_version %(echo %{base_version} | awk -F. -v OFS=. '{$NF++; print}')
Release:        0
Summary:        Threaded poller for Cacti written in C
License:        LGPL-2.1-or-later
URL:            https://www.cacti.net/spine_info.php
Source:         https://www.cacti.net/downloads/spine/%{name}-%{version}.tar.gz
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  mysql-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig(libcap)
Requires(post): permissions
Requires:       cacti >= %{base_version}
Requires:       cacti < %{next_base_version}
Requires:       rrdtool

%description
Spine is a supplemental poller for Cacti that makes use of pthreads to achieve
excellent performance.

%prep
%autosetup -p1

%build
./bootstrap
%configure \
	--enable-lcap \
	%nil
%make_build

%install
%make_install

%post
%set_permissions %{_bindir}/spine

%verifyscript
%verify_permissions -e %{_bindir}/spine

%files
%license LICENSE
%doc CHANGELOG
%config %{_sysconfdir}/spine.conf.dist
%verify(not mode caps) %{_bindir}/spine
%{_mandir}/man1/spine*

%changelog
