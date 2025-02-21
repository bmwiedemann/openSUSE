#
# spec file for package warewulf4
#
# Copyright (c) 2025 SUSE LLC
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


%global tftpdir /srv/tftpboot
%global srvdir %{_sharedstatedir}
#%%global githash 5b0de8ea5397ca42584335517fd4959d7ffe3da5

ExclusiveArch:  x86_64 aarch64

Name:           warewulf4
Version:        4.5.8
Release:        0
Summary:        A suite of tools for clustering
License:        BSD-3-Clause
Group:          Productivity/Clustering/Computing
URL:            https://warewulf.org
Source0:        warewulf-%{version}.tar
Source1:        vendor.tar.xz
Source5:        warewulf4-rpmlintrc
Source10:       config-ww4.sh
Source11:       adjust_overlays.sh
Source20:       README.dnsmasq
Source21:       README.RKE2.md

BuildRequires:  distribution-release
BuildRequires:  dracut
BuildRequires:  firewalld
BuildRequires:  go >= 1.20
BuildRequires:  golang-packaging
BuildRequires:  iproute2
BuildRequires:  libgpg-error-devel
BuildRequires:  logrotate
BuildRequires:  make
BuildRequires:  munge
BuildRequires:  sysuser-tools
BuildRequires:  tftp
BuildRequires:  yq
BuildRequires:  pkgconfig(gpgme)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%sysusers_requires
Requires:       %{name}-overlay = %{version}
Requires:       firewalld
Requires:       iproute2
Requires:       ipxe-bootimgs
Requires:       logrotate
Requires:       pigz
Requires:       tftp
Requires:       ( dhcp-server or dnsmasq )
Suggests:       dhcp-server
Recommends:     bash-completion
Recommends:     ipmitool
Recommends:     nfs-kernel-server

%{?go_nostrip}

%description
Warewulf v4 combines ultra scalability, flexibility, and simplicity with being
light weight, non-intrusive, and a great tool for scientists and seasoned
system administrators alike. Warewulf empowers you to scalably and easily
manage thousands of compute resources.

%package overlay
# Smells like a circular dependcy, but needed in this case as the
# files belong to the warewulf user
Requires(pre):  %{name} = %version
Summary:        Default overlay for warewulf
Group:          Productivity/Clustering/Computing

%description overlay
Includes the default overlays so that they can be updated seprately.

%package man
Supplements:    %{name} = %version
Summary:        Warewulf4 Man Pages
BuildArch:      noarch

%description man
Man pages for warewulf4.

%package overlay-slurm
Summary:        Configuration template for slurm
Requires:       %{name} = %{version}
Requires:       slurm
BuildArch:      noarch
Obsoletes:      warewulf4-slurm <= 4.4.0
Provides:       warewulf4-slurm = %version

%description overlay-slurm
This package installs the necessary configuration files in order to run a slurm
cluster on the configured warewulf nodes.

%package overlay-rke2
Summary:        Configuration template for RKE2
Requires:       %{name} = %{version}
Requires:       slurm
BuildArch:      noarch

%description overlay-rke2
This package provides a template that is used to share a connection token
and server endpoint information across an RKE2 cluster.

%package dracut
Summary:        Dracut module for loading a Warewulf container image
BuildArch:      noarch

Requires:       dracut

%description dracut
This subpackage contains a dracut module that can be used to generate
an initramfs that can fetch and boot a Warewulf container image from a
Warewulf server.

%prep
%autosetup -a1 -p1 -n warewulf-%{version}
echo %{version} > VERSION

%build
export OFFLINE_BUILD=1
export IPXESOURCE=%{_datadir}/ipxe
export GOFLAGS="-buildmode=pie"
make defaults \
    PREFIX=%{_prefix} \
    BINDIR=%{_bindir} \
    SYSCONFDIR=%{_sysconfdir} \
    DATADIR=%{_datadir} \
    LOCALSTATEDIR=%{_sharedstatedir} \
    SHAREDSTATEDIR=%{_sharedstatedir} \
    MANDIR=%{_mandir} \
    INFODIR=%{_infodir} \
    DOCDIR=%{_docdir} \
    SRVDIR=%{srvdir} \
    TFTPDIR=%{tftpdir} \
    SYSTEMDDIR=%{_unitdir} \
    BASHCOMPDIR=/etc/bash_completion.d/ \
    FIREWALLDDIR=/usr/lib/firewalld/services \
    WWCLIENTDIR=/warewulf
make %{?_smp_mflags} build \
    PREFIX=%{_prefix} \
    BINDIR=%{_bindir} \
    SYSCONFDIR=%{_sysconfdir} \
    DATADIR=%{_datadir} \
    LOCALSTATEDIR=%{_sharedstatedir} \
    SHAREDSTATEDIR=%{_sharedstatedir} \
    MANDIR=%{_mandir} \
    INFODIR=%{_infodir} \
    DOCDIR=%{_docdir} \
    SRVDIR=%{srvdir} \
    TFTPDIR=%{tftpdir} \
    SYSTEMDDIR=%{_unitdir} \
    BASHCOMPDIR=/etc/bash_completion.d/ \
    FIREWALLDDIR=/usr/lib/firewalld/services \
    WWCLIENTDIR=/warewulf

%install
# we have a broken symlink for wwclient
export NO_BRP_STALE_LINK_ERROR=yes
export IPXESOURCE=%{_datadir}/ipxe
# overlays will end up here
export OFFLINE_BUILD=1
export LOCALSTATEDIR=%{_localstatedir}/lib
%{makeinstall}

# cleanup
mkdir -p %{buildroot}%{_sbindir}/
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcwarewulfd

mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv -v %{buildroot}%{_sysconfdir}/bash_completion.d/wwctl \
  %{buildroot}%{_datadir}/bash-completion/completions/wwctl
# copy the LICESNSE.md via %%doc
rm -f %{buildroot}/usr/share/doc/packages/warewulf/LICENSE.md
cp %{S:20} %{S:21} .

# use ipxe-bootimgs images from distribution
yq e '
  .tftp.["systemd name"] = "tftp.socket" |
  .tftp.ipxe."00:00" = "undionly.kpxe" |
  .tftp.ipxe."00:07" = "ipxe-x86_64.efi" |
  .tftp.ipxe."00:09" = "ipxe-x86_64.efi" |
  .tftp.ipxe."00:0B" = "snp-arm64.efi" |
  .["container mounts"] += {"source": "/etc/SUSEConnect", "dest": "/etc/SUSEConnect", "readonly": true} |
  .["container mounts"] += {"source": "/etc/zypp/credentials.d/SCCcredentials", "dest": "/etc/zypp/credentials.d/SCCcredentials", "readonly": true}' \
  -i %{buildroot}%{_sysconfdir}/warewulf/warewulf.conf
# SUSE starts user UIDs at 1000
sed -i -e 's@\(.* \$_UID \(>\|-ge\) \)500\(.*\)@\11000\3@' %{buildroot}%{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/profile.d/ssh_setup.*sh.ww
# fix dhcp for SUSE
mv %{buildroot}%{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/dhcp/dhcpd.conf.ww %{buildroot}%{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/dhcpd.conf.ww
rmdir %{buildroot}%{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/dhcp

# create systemuser
echo "u warewulf -" > system-user-%{name}.conf
echo "g warewulf -" >> system-user-%{name}.conf
%sysusers_generate_pre system-user-%{name}.conf %{name} system-user-%{name}.conf
install -D -m 644 system-user-%{name}.conf %{buildroot}%{_sysusersdir}/system-user-%{name}.conf
install -D -m 755 %{S:10} %{buildroot}%{_datadir}/warewulf/scripts/config-warewulf.sh
install -D -m 755 %{S:11} %{buildroot}%{_datadir}/warewulf/scripts/%{basename:S:11}

# get the slurm package ready
mkdir -p %{buildroot}%{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/slurm
mv %{buildroot}%{_sysconfdir}/warewulf/examples/slurm.conf.ww %{buildroot}%{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/slurm
mkdir -p %{buildroot}%{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/munge
cat >  %{buildroot}%{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/munge/munge.key.ww <<EOF
{{ Include "/etc/munge/munge.key" -}}
EOF
chmod 600 %{buildroot}%{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/munge/munge.key.ww
mkdir -p %{buildroot}%{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/slurm
cat >  %{buildroot}%{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/slurm/slurm.conf.ww <<EOF
{{ Include "/etc/slurm/slurm.conf" }}
EOF
# prepare RKE2 configuration template
mkdir -p %{buildroot}%{_localstatedir}/lib/warewulf/overlays/rke2-config/etc/rancher/rke2
cat > %{buildroot}%{_localstatedir}/lib/warewulf/overlays/rke2-config/etc/rancher/rke2/config.yaml.ww <<EOF
{{ if ne (index .Tags "server") "" -}}
server: https://{{ index .Tags "server" }}:9345
{{ end -}}
{{ if ne (index .Tags "clienttoken") "" -}}
token: {{ index .Tags "connectiontoken" }}
{{ end -}}
EOF
chmod 600 %{buildroot}%{_localstatedir}/lib/warewulf/overlays/rke2-config/etc/rancher/rke2/config.yaml.ww
# move the other example templates for client overlays to package documentation
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}
mv %{buildroot}/%{_sysconfdir}/warewulf/examples %{buildroot}%{_defaultdocdir}/%{name}/example-templates
# fix logrotate name
mv %{buildroot}/%{_sysconfdir}/logrotate.d/warewulfd.conf %{buildroot}/%{_sysconfdir}/logrotate.d/warewulf4

%pre -f %{name}.pre
%service_add_pre warewulfd.service

%post
%service_add_post warewulfd.service
%{_datadir}/warewulf/scripts/config-warewulf.sh

%preun
%service_del_preun warewulfd.service

%postun
%service_del_postun warewulfd.service

%posttrans overlay
%{_datadir}/warewulf/scripts/%{basename:S:11}

%files
%defattr(-,root,root)
%doc README.md
%doc README.dnsmasq
%license LICENSE.md
%{_datadir}/bash-completion/completions/wwctl
%attr(0755, root, warewulf) %dir %{_sysconfdir}/warewulf
%attr(0755, root, warewulf) %dir %{_defaultdocdir}/%{name}/example-templates
%config(noreplace) %{_sysconfdir}/warewulf/nodes.conf
%config(noreplace) %{_sysconfdir}/warewulf/warewulf.conf
%config(noreplace) %{_sysconfdir}/warewulf/grub
%config(noreplace) %{_sysconfdir}/warewulf/ipxe
%config %{_sysconfdir}/logrotate.d/warewulf4
%{_defaultdocdir}/%{name}/example-templates
%{_prefix}/lib/firewalld/services/warewulf.xml
%exclude %{_datadir}/warewulf/overlays
%exclude %{_datadir}/warewulf/scripts/%{basename:S:11}
%{_bindir}/wwctl
%{_sbindir}/rcwarewulfd
%{_unitdir}/warewulfd.service
%{_sysusersdir}/system-user-%{name}.conf
%{_datadir}/warewulf
%ghost %{_sysconfdir}/profile.d/ssh_setup.sh
%ghost %{_sysconfdir}/profile.d/ssh_setup.csh

%files man
%{_mandir}/man1/wwctl*1.gz
%{_mandir}/man5/*conf*gz

%files overlay
# The configuration files in this location are for the compute
# nodes, so when modified we do not replace them as sensible
# admin will read the changelog
%{_localstatedir}/lib/warewulf/overlays
%dir %{_localstatedir}/lib/warewulf
%config(noreplace) %{_localstatedir}/lib/warewulf/overlays
%{_datadir}/warewulf/scripts/%{basename:S:11}
%exclude %{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/slurm
%exclude %{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/slurm
%exclude %{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/munge
%exclude %{_localstatedir}/lib/warewulf/overlays/rke2-config

%files overlay-slurm
%dir %{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/slurm
%{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/slurm/slurm.conf.ww
%dir %{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/slurm
%{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/slurm/slurm.conf.ww
%dir %{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/munge
%{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/munge/munge.key.ww
%dir %attr(0700,munge,munge) %{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/munge
%attr(0600,munge,munge) %config(noreplace) %{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/munge/munge.key.ww

%files overlay-rke2
%doc README.RKE2.md
%dir %{_localstatedir}/lib/warewulf/overlays/rke2-config
%dir %{_localstatedir}/lib/warewulf/overlays/rke2-config/etc
%dir %{_localstatedir}/lib/warewulf/overlays/rke2-config/etc/rancher
%dir %{_localstatedir}/lib/warewulf/overlays/rke2-config/etc/rancher/rke2
%attr(0600,root,root) %{_localstatedir}/lib/warewulf/overlays/rke2-config/etc/rancher/rke2/config.yaml.ww

%files dracut
%defattr(-, root, root)
%dir %{_prefix}/lib/dracut/modules.d/90wwinit
%{_prefix}/lib/dracut/modules.d/90wwinit/*.sh

%changelog
