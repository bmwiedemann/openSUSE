#
# spec file for package ufw
#
# Copyright (c) 2024 SUSE LLC
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


%define major_ver 0.36
Name:           ufw
Version:        %{major_ver}.2
Release:        0
Summary:        Uncomplicated Firewall
License:        GPL-3.0-only
Group:          Productivity/Networking/Security
URL:            https://launchpad.net/ufw
Source0:        https://launchpad.net/ufw/%{major_ver}/%{version}/+download/%{name}-%{version}.tar.gz
BuildRequires:  bash-completion
BuildRequires:  iptables
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
Requires:       bash-completion
Recommends:     %{name}-lang
BuildArch:      noarch
%systemd_requires

%description
The Uncomplicated Firewall(ufw) is a front-end for netfilter, which
aims to make it easier for people unfamiliar with firewall concepts.
Ufw provides a framework for managing netfilter as well as
manipulating the firewall.

%lang_package

%prep
%setup -q

%build
%python3_build

%install
%python3_install
sed -i "1{s|/usr/bin/env||}" %{buildroot}%{_sbindir}/ufw
mkdir -p %{buildroot}/%{_bindir}
install -Dm0644 shell-completion/bash %{buildroot}%{_datadir}/bash-completion/completions/ufw.sh
install -Dm0644 doc/systemd.example %{buildroot}%{_unitdir}/%{name}.service
ln -s %{_mandir}/man8/ufw.8.gz %{buildroot}%{_mandir}/man8/rcufw.8.gz
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
ln -s %{_sbindir}/ufw %{buildroot}/%{_bindir}/ufw

%pre
%service_add_pre ufw.service

%post
%service_add_post ufw.service

%preun
%service_del_preun ufw.service

%postun
%service_del_postun ufw.service

%files
/lib/ufw/ufw-init
/lib/ufw/ufw-init-functions
%{python3_sitelib}/ufw-%{version}-py%{python3_version}.egg-info
%{_sbindir}/ufw
%{_sbindir}/rcufw
%{_bindir}/ufw
%{_mandir}/man8/ufw-framework.8%{?ext_man}
%{_mandir}/man8/ufw.8%{?ext_man}
%{_mandir}/man8/rcufw.8%{?ext_man}
%config %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/applications.d
%config %{_sysconfdir}/default/ufw
%{_datadir}/bash-completion/completions/ufw.sh
%{_unitdir}/%{name}.service
/lib/ufw
%{python3_sitelib}/ufw
%{_datadir}/%{name}
%{_datadir}/%{name}/iptables
%exclude %{_datadir}/%{name}/messages

%files lang
%dir %{_datadir}/%{name}/messages
%lang(zh_TW) %{_datadir}/%{name}/messages/zh_TW.mo
%lang(ar) %{_datadir}/%{name}/messages/ar.mo
%lang(bg) %{_datadir}/%{name}/messages/bg.mo
%lang(ca) %{_datadir}/%{name}/messages/ca.mo
%lang(cs) %{_datadir}/%{name}/messages/cs.mo
%lang(da) %{_datadir}/%{name}/messages/da.mo
%lang(de) %{_datadir}/%{name}/messages/de.mo
%lang(el) %{_datadir}/%{name}/messages/el.mo
%lang(en_AU) %{_datadir}/%{name}/messages/en_AU.mo
%lang(en_GB) %{_datadir}/%{name}/messages/en_GB.mo
%lang(es) %{_datadir}/%{name}/messages/es.mo
%lang(fi) %{_datadir}/%{name}/messages/fi.mo
%lang(fr) %{_datadir}/%{name}/messages/fr.mo
%lang(he) %{_datadir}/%{name}/messages/he.mo
%lang(hu) %{_datadir}/%{name}/messages/hu.mo
%lang(id) %{_datadir}/%{name}/messages/id.mo
%lang(it) %{_datadir}/%{name}/messages/it.mo
%lang(nb) %{_datadir}/%{name}/messages/nb.mo
%lang(nl) %{_datadir}/%{name}/messages/nl.mo
%lang(pl) %{_datadir}/%{name}/messages/pl.mo
%lang(pt) %{_datadir}/%{name}/messages/pt.mo
%lang(pt_BR) %{_datadir}/%{name}/messages/pt_BR.mo
%lang(ru) %{_datadir}/%{name}/messages/ru.mo
%lang(sk) %{_datadir}/%{name}/messages/sk.mo
%lang(dl) %{_datadir}/%{name}/messages/sl.mo
%lang(sr) %{_datadir}/%{name}/messages/sr.mo
%lang(sv) %{_datadir}/%{name}/messages/sv.mo
%lang(tl) %{_datadir}/%{name}/messages/tl.mo
%lang(zh_CN) %{_datadir}/%{name}/messages/zh_CN.mo
%lang(ast) %{_datadir}/%{name}/messages/ast.mo
%lang(bs) %{_datadir}/%{name}/messages/bs.mo
%lang(ja) %{_datadir}/%{name}/messages/ja.mo
%lang(ur) %{_datadir}/%{name}/messages/ur.mo

%changelog
