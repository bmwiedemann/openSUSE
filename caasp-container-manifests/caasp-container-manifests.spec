#
# spec file for package caasp-container-manifests
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if 0%{?suse_version} == 1315 && !0%{?is_opensuse}
  %define _base_image sles12
%endif

%if 0%{?suse_version} == 1500 && !0%{?is_opensuse}
  # Use the sles12 images from the registry
  %define _base_image registry.suse.de/devel/casp/3.0/controllernode/images_container_base/sles12
%endif

%if 0%{?is_opensuse} && 0%{?suse_version} > 1500
  %define _base_image kubic
%endif

Name:           caasp-container-manifests
Version:        4.0.0+git_r324_f124eb9
Release:        0
Summary:        Manifest file templates for containers on controller node
License:        Apache-2.0
Group:          System/Management
Url:            https://github.com/kubic-project/caasp-container-manifests
Source:         master.tar.gz

# If it is not SLE15, require container-feeder
# Otherwise, we are using the SUSE Registry
%if 0%{?sle_version} < 150000
Requires:       container-feeder

# Require all the docker images
Requires:       %{_base_image}-caasp-dex-image >= 2.0.0
Requires:       %{_base_image}-dnsmasq-nanny-image >= 2.0.0
Requires:       %{_base_image}-flannel-image >= 2.0.0
Requires:       %{_base_image}-haproxy-image >= 2.0.0
Requires:       %{_base_image}-kubedns-image >= 2.0.0
Requires:       %{_base_image}-mariadb-image >= 2.0.0
Requires:       %{_base_image}-openldap-image >= 2.0.0
Requires:       %{_base_image}-pause-image >= 2.0.0
Requires:       %{_base_image}-pv-recycler-node-image >= 2.0.0
Requires:       %{_base_image}-salt-api-image >= 2.0.0
Requires:       %{_base_image}-salt-master-image >= 2.0.0
Requires:       %{_base_image}-salt-minion-image >= 2.0.0
Requires:       %{_base_image}-sidecar-image >= 2.0.0
Requires:       %{_base_image}-tiller-image >= 2.0.0
Requires:       %{_base_image}-velum-image >= 2.0.0
%endif
# Require all  the things we mount from the host from the kubernetes-salt package
Requires:       kubernetes-salt
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Manifest file templates will instruct kubelet service to bring up salt
and velum containers on a controller node.

%prep
%setup -q -n caasp-container-manifests-master

%build

%install
for file in manifests/*.yaml; do
  install -D -m 0644 $file %{buildroot}/%{_datadir}/%{name}/$file
  # fix image name
  sed -e "s|image:[ ]*sles12/\(.*\):|image: %{_base_image}/\1:|g" -i %{buildroot}/%{_datadir}/%{name}/$file
done
install -D -m 0644 config/haproxy/haproxy.cfg %{buildroot}/etc/caasp/haproxy/haproxy.cfg
install -D -m 0755 activate.sh %{buildroot}/%{_datadir}/%{name}/activate.sh
# fix image name in activate
sed -e "s|sles12/pause|%{_base_image}/pause|g" -i %{buildroot}/%{_datadir}/%{name}/activate.sh
%if 0%{?suse_version} >= 1500
# Adjust pause image version in activate
sed -e "s|pause:1.0.0|pause:0.1|g" -i %{buildroot}/%{_datadir}/%{name}/activate.sh
%endif
install -D -m 0755 gen-certs.sh %{buildroot}/%{_datadir}/%{name}/gen-certs.sh
for dir in salt/grains salt/minion.d-ca; do
  install -d %{buildroot}/%{_datadir}/%{name}/config/$dir
  install -D -m 0644 config/$dir/* %{buildroot}/%{_datadir}/%{name}/config/$dir
done
cp -R setup %{buildroot}/%{_datadir}/%{name}

# Install service
install -D -m 0755 admin-node-setup.sh %{buildroot}/%{_datadir}/%{name}/admin-node-setup.sh
mkdir -p %{buildroot}/%{_unitdir}
install -D -m 0644 admin-node-setup.service %{buildroot}/%{_unitdir}/
sed -e "s#__ADMIN_NODE_SETUP_PATH__#%{_datadir}/%{name}#" -i %{buildroot}/%{_unitdir}/admin-node-setup.service
install -D -m 0644 admin-node-init.service %{buildroot}/%{_unitdir}/
sed -e "s#__ADMIN_NODE_SETUP_PATH__#%{_datadir}/%{name}#" -i %{buildroot}/%{_unitdir}/admin-node-init.service
mkdir -p %{buildroot}/%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}/%{_sbindir}/rcadmin-node-setup

%pre
%service_add_pre admin-node-setup.service admin-node-init.service

%post
%service_add_post admin-node-setup.service admin-node-init.service

%preun
%service_del_preun admin-node-setup.service admin-node-init.service

%postun
%service_del_postun admin-node-setup.service admin-node-init.service

%files
%defattr(-,root,root)
%doc README.md
%if 0%{?suse_version} < 1500
%doc LICENSE
%else
%license LICENSE
%endif
%dir %{_datadir}/%{name}
%dir /etc/caasp
%dir /etc/caasp/haproxy
%config(noreplace) /etc/caasp/haproxy/haproxy.cfg
%{_sbindir}/rcadmin-node-setup
%{_unitdir}/admin-node-init.service
%{_unitdir}/admin-node-setup.service
%{_datadir}/%{name}/*

%changelog
