#
# spec file for package samplicator
#
# Copyright (c) 2017, Martin Hauke <mardnh@gmx.de>
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

Name:           samplicator
Version:        1.3.8rc1+git.20171112
Release:        0
Summary:        Tool to send copies of (UDP) datagrams to multiple receivers
License:        GPL-2.0-only
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/sleinen/samplicator
#Git-Clone:     https://github.com/sleinen/samplicator.git
Source:         %{name}-%{version}.tar.xz
Source1:        %{name}.service
Source2:        %{name}.sysconfig
Source3:        samplicator.8
Source4:        samplicator.conf.example
BuildRequires:  autoconf
BuildRequires:  automake

%description
This program receives UDP datagrams on a given port, and resends
those datagrams to a specified set of receivers.
In addition, a sampling divisor N may be specified individually for each
receiver, which will then only receive one in N of the received packets.
Optional spoofing is also supported.

%prep
%setup -q

%build
autoreconf -fiv
export CFLAGS="%{optflags} -std=gnu11"
%configure
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}/%{_sbindir}
mv %{buildroot}/%{_bindir}/samplicate %{buildroot}/%{_sbindir}/samplicate
install -Dpm 0644 %{_sourcedir}/samplicator.8 %{buildroot}%{_mandir}/man8/samplicate.8
install -Dpm 0644 %{_sourcedir}/%{name}.service %{buildroot}%{_unitdir}/%{name}.service
install -Dpm 0644 %{_sourcedir}/%{name}.sysconfig %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -Dpm 0644 %{_sourcedir}/%{name}.conf.example %{buildroot}%{_sysconfdir}/%{name}.conf
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

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
%doc AUTHORS ChangeLog NEWS README.md
%{_sbindir}/samplicate
%{_sbindir}/rc%{name}
%config %{_sysconfdir}/%{name}.conf
%{_mandir}/man8/samplicate.8%{?ext_man}
%{_unitdir}/%{name}.service
%{_fillupdir}/sysconfig.%{name}

%changelog
