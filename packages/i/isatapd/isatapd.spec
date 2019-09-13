#
# spec file for package isatapd
#
# Copyright (c) 2018, Martin Hauke <mardnh@gmx.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           isatapd
Version:        0.9.7+git.20141015
Release:        0
Summary:        Daemon for creating and maintaining an ISATAP client tunnel (RFC 5214)
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            http://saschahlusiak.de/linux/isatap.htm
#Git-Clone:     https://github.com/shlusiak/isatapd.git
Source:         %{name}-%{version}.tar.xz
Source1:        %{name}.service
Source2:        %{name}.sysconfig
Patch0:         isatapd-fix-ftbfs-linux-4.8.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  systemd-rpm-macros
Requires(post): %fillup_prereq

%description
The daemon uses the in-kernel ISATAP support first introduced in Linux 2.6.25.
It does NOT operate the tunnel or handle any IPv6 traffic, it only sets
up the tunnel parameters, the Potential Router List, sends periodic
router solicitations and tries to detect link changes.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
install -Dpm0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -Dpm0644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcisatapd

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%fillup_only

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_sbindir}/isatapd
%{_sbindir}/rcisatapd
%{_mandir}/man8/isatapd.8%{?ext_man}
%{_unitdir}/%{name}.service
%{_fillupdir}/sysconfig.%{name}

%changelog
