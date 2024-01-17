#
# spec file for package actkbd
#
# Copyright (c) 2023 SUSE LLC
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
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           actkbd
Version:        0.2.8
Release:        0
Summary:        A keyboard shortcut daemon
License:        GPL-2.0-only
Group:          System/Console
URL:            http://users.softlab.ece.ntua.gr/~thkala/projects/actkbd/
Source0:        http://users.softlab.ece.ntua.gr/~thkala/projects/actkbd/files/actkbd-%{version}.tar.bz2
Source1:        actkbd.service
Source2:        actkbd.conf
Source3:        actkbd.sysconfig
Patch0:         actkbd-0.2.7-amd64.patch
BuildRequires:  systemd-rpm-macros
Requires(post): %fillup_prereq
%{?systemd_ordering}

%description
actkbd is a daemon that reacts to user defined keys and launches specific
commands. It can be used to utilize multimedia keys on simple setups, or
assigned custom actions to rarely used keys.

%prep
%autosetup -p1

%build
%make_build CFLAGS="%{optflags}"

%install
install -d -m 0755 %{buildroot}%{_unitdir} \
                   %{buildroot}%{_sbindir} \
                   %{buildroot}%{_sysconfdir} \
                   %{buildroot}%{_fillupdir} \
                   %{buildroot}%{_docdir}/%{name}/samples

install -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/actkbd.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcactkbd

install -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/actkbd.conf
install -m 0644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.actkbd
install -m 0755 actkbd %{buildroot}%{_sbindir}/actkbd
install -m 0644 samples/* %{buildroot}%{_docdir}/%{name}/samples/

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
%doc README NEWS FAQ AUTHORS
%config %{_sysconfdir}/actkbd.conf
%{_fillupdir}/*
%{_sbindir}/actkbd
%{_unitdir}/actkbd.service
%{_sbindir}/rcactkbd
%{_docdir}/%{name}/samples

%changelog
