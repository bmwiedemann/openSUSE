#
# spec file for package autossh
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define with_systemd 1

Summary:        Automatically restart SSH sessions and tunnels
License:        BSD-3-Clause
Group:          Productivity/Networking/SSH

Name:           autossh
Version:        1.4g
Release:        0
URL:            https://www.harding.motd.ca/autossh/
Source:         https://www.harding.motd.ca/autossh/%{name}-%{version}.tgz
Source1:        autossh.init
Source2:        autossh.conf
Source3:        autossh.service
Source4:        my.conf
Source5:        README.SUSE.md
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
# configure checks is the ssh client exists
BuildRequires:  openssh
Requires:       openssh
BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}

%description
Autossh is a program to start a copy of ssh and monitor it, restarting
it as necessary should it die or stop passing traffic. The idea and
the mechanism are from rstunnel (Reliable SSH Tunnel), but implemented
in C. The author's view is that it is not as fiddly as rstunnel to get
to work. Connection monitoring using a loop of port forwardings. Backs
off on rate of connection attempts when experiencing rapid failures
such as connection refused.

%prep
%setup
cp %{S:4} .
cp %{S:5} .

%build
autoreconf -fvi
%configure
make %{?_smp_mflags}

%install
%makeinstall
mkdir -p %{buildroot}/%{_sbindir}
install -D -m 444 %{S:3} %{buildroot}/%{_unitdir}/autossh@.service
ln -s /usr/sbin/service %{buildroot}/%{_sbindir}/rcautossh
rm "%buildroot/%{_datadir}/doc/autossh"/{CHANGES,README}
rm -rf "%{buildroot}/%{_datadir}/examples"

%pre
%service_add_pre %{name}.service

%preun
%service_del_preun %{name}.service

%post
%service_add_post %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr(-, root, root, 0755)
%doc CHANGES README README.SUSE.md my.conf
%doc autossh.host rscreen
%{_bindir}/autossh
%{_unitdir}/%{name}@.service
%{_sbindir}/rcautossh
%doc %{_mandir}/man1/autossh.1*

%changelog
