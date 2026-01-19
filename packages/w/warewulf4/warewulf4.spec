#
# spec file for package warewulf4
#
# Copyright (c) 2026 SUSE LLC
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


%global ww4dir %{_localstatedir}/lib
%global tftpdir /srv/tftpboot
%global srvdir %{_sharedstatedir}
#%%global githash fd49254ac592d325056aa58a564933a008539607
%if 0%{?githash}
%define srcdir warewulf-%{githash}
%else
%define srcdir warewulf-%{version}
%endif

ExclusiveArch:  x86_64 aarch64

Name:           warewulf4
Version:        4.6.5
Release:        0
Summary:        A suite of tools for clustering
License:        BSD-3-Clause
Group:          Productivity/Clustering/Computing
URL:            https://warewulf.org
Source0:        https://github.com/warewulf/warewulf/releases/download/v%{version}/warewulf-%{version}.tar.gz#/warewulf4-v%{version}.tar.gz
Source1:        vendor.tar.gz
Source5:        warewulf4-rpmlintrc
Source10:       config-ww4.sh
Source11:       adjust_overlays.sh
Source20:       README.dnsmasq
Source21:       README.RKE2.md

BuildRequires:  %{python_module Sphinx-latex}
BuildRequires:  distribution-release
BuildRequires:  dracut
BuildRequires:  firewalld
BuildRequires:  go >= 1.23
BuildRequires:  golang-packaging
BuildRequires:  graphviz
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
Requires:       iproute2
Requires:       ipxe-bootimgs
Requires:       logrotate
Requires:       pigz
Requires:       ( dhcp-server or dnsmasq )
Requires:       ( tftp or dnsmasq )
Suggests:       dnsmasq
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

%package reference-doc
Supplements:    %{name} = %version
Summary:        Warewulf4 Reference book
BuildArch:      noarch

%description reference-doc
Reference documentation for warewulf4.

%package overlay-slurm
Summary:        Configuration template for slurm
Requires:       %{name} = %{version}
Recommends:     slurm
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
%autosetup -a1 -p1 -n %{srcdir}
echo %{version} > VERSION

%build
export OFFLINE_BUILD=1
export IPXESOURCE=%{_datadir}/ipxe
export GOFLAGS="-buildmode=pie"
make defaults \
    PREFIX=%{_prefix} \
    BINDIR=%{_bindir} \
    SYSCONFDIR=%{_sysconfdir} \
    DATADIR=%{ww4dir} \
    LOCALSTATEDIR=%{_localstatedir}/lib \
    SHAREDSTATEDIR=%{_localstatedir}/lib \
    MANDIR=%{_mandir} \
    INFODIR=%{_infodir} \
    DOCDIR=%{_docdir} \
    SRVDIR=%{srvdir} \
    TFTPDIR=%{tftpdir} \
    SYSTEMDDIR=%{_unitdir} \
    BASHCOMPDIR=/etc/bash_completion.d/ \
    FIREWALLDDIR=/usr/lib/firewalld/services \
    WWCLIENTDIR=/warewulf \
    WWOVERLAYDIR=%{_sysconfdir}/warewulf/overlays/ \
    %{nil}
make %{?_smp_mflags} build
make %{?_smp_mflags} latexpdf

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
# copy the LICENSE.md via %%doc
rm -f %{buildroot}/usr/share/doc/packages/warewulf/LICENSE.md
cp %{S:20} %{S:21} .

# use ipxe-bootimgs images from distribution
yq e '
  .tftp.ipxe."00:00" = "undionly.kpxe" |
  .tftp.ipxe."00:07" = "ipxe-x86_64.efi" |
  .tftp.ipxe."00:09" = "ipxe-x86_64.efi" |
  .tftp.ipxe."00:0B" = "snp-arm64.efi" |
  .["image mounts"] += {"source": "/etc/SUSEConnect", "dest": "/etc/SUSEConnect", "readonly": true} |
  .["image mounts"] += {"source": "/etc/zypp/credentials.d/SCCcredentials", "dest": "/etc/zypp/credentials.d/SCCcredentials", "readonly": true} |
  .dhcp.["systemd name"] = "dnsmasq" |
  .tftp.["systemd name"] = "dnsmasq"
  ' \
  -i %{buildroot}%{_sysconfdir}/warewulf/warewulf.conf
# SUSE starts user UIDs at 1000
#sed -i -e 's@\(.* \$_UID \(>\|-ge\) \)500\(.*\)@\11000\3@' %{buildroot}%{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/profile.d/ssh_setup.*sh.ww
# fix dhcp for SUSE
mv %{buildroot}%{ww4dir}/warewulf/overlays/host/rootfs/etc/dhcp/dhcpd.conf.ww %{buildroot}%{ww4dir}/warewulf/overlays/host/rootfs/etc/dhcpd.conf.ww
rmdir %{buildroot}%{ww4dir}/warewulf/overlays/host/rootfs/etc/dhcp

# create systemuser
echo "u warewulf -" > system-user-%{name}.conf
echo "g warewulf -" >> system-user-%{name}.conf
%sysusers_generate_pre system-user-%{name}.conf %{name} system-user-%{name}.conf
install -D -m 644 system-user-%{name}.conf %{buildroot}%{_sysusersdir}/system-user-%{name}.conf
install -D -m 755 %{S:10} %{buildroot}%{ww4dir}/warewulf/scripts/config-warewulf.sh
install -D -m 755 %{S:11} %{buildroot}%{ww4dir}/warewulf/scripts/adjust_overlays.sh

# get the slurm package ready
mkdir -p %{buildroot}%{ww4dir}/warewulf/overlays/host/rootfs/etc/slurm
mv %{buildroot}%{_sysconfdir}/warewulf/examples/slurm.conf.ww %{buildroot}%{ww4dir}/warewulf/overlays/host/rootfs/etc/slurm
mkdir -p %{buildroot}%{ww4dir}/warewulf/overlays/slurm/rootfs/etc/munge
cat >  %{buildroot}%{ww4dir}/warewulf/overlays/slurm/rootfs/etc/munge/munge.key.ww <<EOF
{{ Include "/etc/munge/munge.key" -}}
EOF
chmod 600 %{buildroot}%{ww4dir}/warewulf/overlays/slurm/rootfs/etc/munge/munge.key.ww
mkdir -p %{buildroot}%{ww4dir}/warewulf/overlays/slurm/rootfs/etc/slurm
cat >  %{buildroot}%{ww4dir}/warewulf/overlays/slurm/rootfs/etc/slurm/slurm.conf.ww <<EOF
{{ Include "/etc/slurm/slurm.conf" }}
EOF
# prepare RKE2 configuration template
mkdir -p %{buildroot}%{ww4dir}/warewulf/overlays/rke2-config/etc/rancher/rke2
cat > %{buildroot}%{ww4dir}/warewulf/overlays/rke2-config/etc/rancher/rke2/config.yaml.ww <<EOF
{{ if ne (index .Tags "server") "" -}}
server: https://{{ index .Tags "server" }}:9345
{{ end -}}
{{ if ne (index .Tags "clienttoken") "" -}}
token: {{ index .Tags "connectiontoken" }}
{{ end -}}
EOF
chmod 600 %{buildroot}%{ww4dir}/warewulf/overlays/rke2-config/etc/rancher/rke2/config.yaml.ww
# move the other example templates for client overlays to package documentation
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}
mv %{buildroot}/%{_sysconfdir}/warewulf/examples %{buildroot}%{_defaultdocdir}/%{name}/example-templates
# fix logrotate name
mv %{buildroot}/%{_sysconfdir}/logrotate.d/warewulfd.conf %{buildroot}/%{_sysconfdir}/logrotate.d/warewulf4
# add version tag to documentation
mv ./userdocs/_build/latex/warewulfuserguide.pdf ./userdocs/_build/latex/warewulfuserguide-%{version}.pdf

%pre -f %{name}.pre
%service_add_pre warewulfd.service

%post
%service_add_post warewulfd.service
if [ $1 -eq 1 ] ; then
    cp %{_sysconfdir}/warewulf/nodes.conf %{_sysconfdir}/warewulf/nodes.conf.4.5.x
    cp %{_sysconfdir}/warewulf/warewulf.conf %{_sysconfdir}/warewulf/warewulf.conf.4.5.x
    %{_bindir}/wwctl upgrade nodes --replace-overlay --add-defaults
    %{_bindir}/wwctl upgrade config
else
    %{ww4dir}/warewulf/scripts/config-warewulf.sh
fi

%preun
%service_del_preun warewulfd.service

%postun
%service_del_postun warewulfd.service

#%%posttrans overlay
#%{ww4dir}/warewulf/scripts/adjust_overlays.sh

%files
%defattr(-,root,root)
%doc README.md README.dnsmasq
%license LICENSE.md
%{_datadir}/bash-completion/completions/wwctl
%attr(0755, root, warewulf) %dir %{_sysconfdir}/warewulf
%attr(0755, root, warewulf) %dir %{_defaultdocdir}/%{name}/example-templates
%config %{_sysconfdir}/warewulf/warewulf.conf
%config(noreplace) %{_sysconfdir}/warewulf/nodes.conf
%config(noreplace) %{_sysconfdir}/warewulf/grub
%config(noreplace) %{_sysconfdir}/warewulf/ipxe
%config(noreplace) %{_sysconfdir}/warewulf/auth.conf
%config %{_sysconfdir}/logrotate.d/warewulf4
%{_defaultdocdir}/%{name}/example-templates
%{_prefix}/lib/firewalld/services/warewulf.xml
%{_bindir}/wwctl
%{_sbindir}/rcwarewulfd
%{_unitdir}/warewulfd.service
%{_sysusersdir}/system-user-%{name}.conf
%{ww4dir}/warewulf/bmc
%{ww4dir}/warewulf/scripts
%ghost %{_sysconfdir}/profile.d/ssh_setup.sh
%ghost %{_sysconfdir}/profile.d/ssh_setup.csh
%dir %{ww4dir}/warewulf

%files man
%{_mandir}/man1/wwctl*1.gz
%{_mandir}/man5/*conf*gz

%files overlay
# The configuration files in this location are for the compute
# nodes, so when modified we do not replace them as sensible
# admin will read the changelog
%{ww4dir}/warewulf/overlays
%exclude %{ww4dir}/warewulf/overlays/host/rootfs/etc/slurm
%exclude %{ww4dir}/warewulf/overlays/slurm/rootfs/etc/slurm
%exclude %{ww4dir}/warewulf/overlays/slurm/rootfs/etc/munge
%exclude %{ww4dir}/warewulf/overlays/rke2-config

%files overlay-slurm
%dir %{ww4dir}/warewulf/overlays/host/rootfs/etc/slurm
%{ww4dir}/warewulf/overlays/host/rootfs/etc/slurm/slurm.conf.ww
%{ww4dir}/warewulf/overlays/slurm
%dir %attr(0700,munge,munge) %{ww4dir}/warewulf/overlays/slurm/rootfs/etc/munge
%attr(0600,munge,munge) %config(noreplace) %{ww4dir}/warewulf/overlays/slurm/rootfs/etc/munge/munge.key.ww

%files overlay-rke2
%doc README.RKE2.md
%dir %{ww4dir}/warewulf/overlays/rke2-config
%dir %{ww4dir}/warewulf/overlays/rke2-config/etc
%dir %{ww4dir}/warewulf/overlays/rke2-config/etc/rancher
%dir %{ww4dir}/warewulf/overlays/rke2-config/etc/rancher/rke2
%attr(0600,root,root) %{ww4dir}/warewulf/overlays/rke2-config/etc/rancher/rke2/config.yaml.ww

%files dracut
%defattr(-, root, root)
%{_prefix}/lib/dracut/modules.d/90wwinit

%files reference-doc
%doc ./userdocs/_build/latex/warewulfuserguide-%{version}.pdf

%changelog
