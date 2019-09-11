#
# spec file for package weave
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


Name:           weave
Version:        2.5.2
Release:        0
Summary:        Pod Network Add-On
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/weaveworks/weave
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        weave-k8s-1.15.yaml
# This package contains the content of a container image, so yes,
# this includes the home directory and the database.
Source3:        weave-rpmlintrc
Patch0:         Makefile.diff
#BuildRequires:  golang-packaging
BuildRequires:  libpcap-devel
BuildRequires:  golang(API) >= 1.12
ExcludeArch:    s390 %{ix86}

%description
Weave Net creates a virtual network that connects containers across multiple
hosts and enables their automatic discovery. With Weave Net, portable
microservices-based applications consisting of multiple containers can run
anywhere: on one host, multiple hosts or even across cloud providers and data
centers. Applications use the network just as if the containers were all plugged
into the same network switch, without having to configure port mappings,
ambassadors or links.

%package kube
Summary:        Pod Network Add-On
Group:          System/Management
Requires:       bind-utils
Requires:       ca-certificates-mozilla
Requires:       conntrack-tools
Requires:       curl
Requires:       iproute2
Requires:       ipset
Requires:       iptables

%description kube
Weave Net creates a virtual network that connects containers across multiple
hosts and enables their automatic discovery. With Weave Net, portable
microservices-based applications consisting of multiple containers can run
anywhere: on one host, multiple hosts or even across cloud providers and data
centers. Applications use the network just as if the containers were all plugged
into the same network switch, without having to configure port mappings,
ambassadors or links.

This package contains the files to be included into the weave-kube container image

%package npc
Summary:        Pod Network Add-On
Group:          System/Management
Requires:       ipset
Requires:       iptables
Requires:       ulogd
Requires:       ulogd-pcap

%description npc
Weave Net creates a virtual network that connects containers across multiple
hosts and enables their automatic discovery. With Weave Net, portable
microservices-based applications consisting of multiple containers can run
anywhere: on one host, multiple hosts or even across cloud providers and data
centers. Applications use the network just as if the containers were all plugged
into the same network switch, without having to configure port mappings,
ambassadors or links.

This package contains the files to be included into the weave-kube container image

%package k8s-yaml
Summary:        Kubernetes yaml file to run weave container
Group:          System/Management
BuildArch:      noarch

%description k8s-yaml
This package contains the yaml file requried to download and run the
weave container in a kubernetes cluster.

weave is a virtual network that gives a subnet to each host for use with
container runtimes.

%prep
%setup -q
rm -rf vendor
tar xf %{SOURCE1}
%patch0 -p1

%build
make %{?_smp_mflags} exes WEAVE_VERSION=%{version}

%install
mkdir -p %{buildroot}/home/weave
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}/weavedb

install -m 0755 prog/weave-kube/launch.sh %{buildroot}/home/weave/
install -m 0755 prog/kube-utils/kube-utils %{buildroot}/home/weave/
install -m 0755 prog/weaver/weaver %{buildroot}/home/weave/
install -m 0755 weave %{buildroot}/home/weave/
install -m 0644 prog/weaver/weavedata.db %{buildroot}/weavedb/
install -m 0755 prog/weaveutil/weaveutil %{buildroot}%{_bindir}
install -m 0755 prog/weave-npc/weave-npc %{buildroot}%{_bindir}
# adjust the path to the ulogd plugins
sed -i -e 's|/usr/lib/ulogd|/usr/lib64/ulogd|g' prog/weave-npc/ulogd.conf
install -m 0644 prog/weave-npc/ulogd.conf %{buildroot}%{_sysconfdir}/ulogd.conf.weave

mkdir -p %{buildroot}%{_datadir}/k8s-yaml/weave
install -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/k8s-yaml/weave/weave.yaml

%files kube
%license LICENSE
/home/weave
%{_bindir}/weaveutil
/weavedb

%files npc
%license LICENSE
%{_bindir}/weave-npc
%config %{_sysconfdir}/ulogd.conf.weave

%files k8s-yaml
%dir %{_datarootdir}/k8s-yaml
%dir %{_datarootdir}/k8s-yaml/weave
%{_datarootdir}/k8s-yaml/weave/weave.yaml

%changelog
