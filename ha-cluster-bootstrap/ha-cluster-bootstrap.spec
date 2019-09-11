#
# spec file for package ha-cluster-bootstrap
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010-2011 Novell Inc. All Rights Reserved.
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


Name:           ha-cluster-bootstrap
Version:        0.5
Release:        0
Summary:        Pacemaker HA Cluster Bootstrap Tool
License:        GPL-2.0
Group:          Productivity/Clustering/HA
Url:            https://github.com/tserong/sleha-bootstrap
Source:         sleha-bootstrap-%{version}.tar.bz2

BuildRequires:  crmsh >= 3
BuildRequires:  help2man
%if 0%{?suse_version} > 1320
BuildRequires:  python3-parallax
%else
BuildRequires:  python-parallax
%endif
Requires:       crmsh >= 3
Requires:       ha-cluster-webui
Requires:       iproute2
Requires:       pacemaker
Requires:       util-linux
Recommends:     hawk2
Recommends:     ocfs2-tools
Recommends:     sbd
Recommends:     resource-agents
Recommends:     fence-agents
# These three are required for ocfs2 setup, but not generic setup
Recommends:     parted
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Tool to bootstrap a Pacemaker High Availability cluster in a hurry.

%prep
%setup -n sleha-bootstrap-%{version}
%build

%install
install -d -m 0755 %{buildroot}%{_sbindir}
install -m 755 scripts/ha-cluster-init %{buildroot}%{_sbindir}
install -m 755 scripts/ha-cluster-join %{buildroot}%{_sbindir}
install -m 755 scripts/ha-cluster-remove %{buildroot}%{_sbindir}
install -m 755 scripts/ha-cluster-geo-init %{buildroot}%{_sbindir}
install -m 755 scripts/ha-cluster-geo-join %{buildroot}%{_sbindir}
install -m 755 scripts/ha-cluster-geo-init-arbitrator %{buildroot}%{_sbindir}
install -d -m 0755 %{buildroot}%{_prefix}/lib
install -m 644 scripts/ha-cluster-functions %{buildroot}%{_prefix}/lib
install -d %{buildroot}%{_mandir}/man8
install -p -m 644 man/ha-cluster-init.8 %{buildroot}%{_mandir}/man8
install -p -m 644 man/ha-cluster-join.8 %{buildroot}%{_mandir}/man8
install -p -m 644 man/ha-cluster-remove.8 %{buildroot}%{_mandir}/man8

%if !0%{?is_opensuse}
ln -s ha-cluster-init %{buildroot}%{_sbindir}/sleha-init
ln -s ha-cluster-join %{buildroot}%{_sbindir}/sleha-join
ln -s ha-cluster-remove %{buildroot}%{_sbindir}/sleha-remove
%endif

mkhelp() {
	help2man -s 8 -n "$1" -o %{buildroot}%{_mandir}/man8/ha-cluster-$2.8 --version-string "%{version}" --help-option "cluster $2 --help" /usr/sbin/crm
}
mkhelp "Initialize as geo cluster" geo-init
mkhelp "Join geo cluster" geo-join
mkhelp "Initialize as geo arbitrator" geo-init-arbitrator

%files
%defattr(-,root,root)
%if !0%{?is_opensuse}
%{_sbindir}/sleha-init
%{_sbindir}/sleha-join
%{_sbindir}/sleha-remove
%endif
%{_sbindir}/ha-cluster-init
%{_sbindir}/ha-cluster-join
%{_sbindir}/ha-cluster-remove
%{_sbindir}/ha-cluster-geo-init
%{_sbindir}/ha-cluster-geo-join
%{_sbindir}/ha-cluster-geo-init-arbitrator
%{_prefix}/lib/ha-cluster-functions
%doc %{_mandir}/man8/*.8*

%changelog
