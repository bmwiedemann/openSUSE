#
# spec file for package actkbd
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

Name:           actkbd
Version:        0.2.8
Release:        0
Summary:        A keyboard shortcut daemon
License:        GPL-2.0-only
Group:          System/Console
Url:            http://users.softlab.ece.ntua.gr/~thkala/projects/actkbd/
Source0:        http://users.softlab.ece.ntua.gr/~thkala/projects/actkbd/files/actkbd-%{version}.tar.bz2
Source1:        actkbd.service
Source2:        actkbd.conf
Source3:        actkbd.sysconfig
Patch0:         actkbd-0.2.7-amd64.patch
BuildRequires:  systemd-rpm-macros
Requires(post): %fillup_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_ordering}

%description
actkbd is a daemon that reacts to user defined keys and launches specific
commands. It can be used to utilize multimedia keys on simple setups, or
assigned custom actions to rarely used keys.

%prep
%setup -q
%patch0 -p1

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
install -Dm 644 %{SOURCE1} %{buildroot}%{_unitdir}/actkbd.service
mkdir -p %{buildroot}%{_sbindir}/
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcactkbd

install -Dm 644 %{SOURCE2} %{buildroot}%{_sysconfdir}/actkbd.conf
install -Dm 644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.actkbd

install -Dm 755 actkbd %{buildroot}%{_sbindir}/actkbd

install -d %{buildroot}%{_docdir}/%{name}/samples
install -dm 644 samples %{buildroot}%{_docdir}/%{name}/samples

%pre
%service_add_pre actkbd.service

%post
%fillup_only -n actkbd
%service_add_post actkbd.service

%preun
%service_del_preun actkbd.service

%postun
%service_del_postun actkbd.service

%files
%defattr(-,root,root)
%doc README NEWS FAQ AUTHORS
%config %{_sysconfdir}/actkbd.conf
%{_fillupdir}/*
%{_sbindir}/actkbd
%{_unitdir}/actkbd.service
%{_sbindir}/rcactkbd
%{_docdir}/%{name}/samples

%changelog
