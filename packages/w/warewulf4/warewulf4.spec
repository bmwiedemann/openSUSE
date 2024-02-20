#
# spec file for package warewulf4
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


%global vers 4.5.0
%global rls_cndt rc1
%if "0%{?rls_cndt}" != "0"
%global rls_char ~
%endif
%global tftpdir /srv/tftpboot
%global srvdir %{_sharedstatedir}
#%%global githash 5b0de8ea5397ca42584335517fd4959d7ffe3da5

ExclusiveArch:  x86_64 aarch64

Name:           warewulf4
Version:        %{vers}%{?rls_char}%{?rls_cndt}
Release:        0
Summary:        A suite of tools for clustering
License:        BSD-3-Clause
Group:          Productivity/Clustering/Computing
URL:            https://warewulf.org
Source0:        https://github.com/warewulf/warewulf/releases/download/v%{vers}%{?rls_cndt}/warewulf-%{vers}%{rls_cndt}.tar.gz#/warewulf4-v%{version}.tar.gz
#Source1:        vendor.tar.gz
Source5:        warewulf4-rpmlintrc
Source10:       config-ww4.sh
Source20:       README.dnsmasq
#Patch12:        clean-warewulf-conf.patch
#Patch15:        dnsmasq-template-move.patch
#Conflicts:      warewulf4-slurm < %version

# no firewalld in sle12
%if 0%{?sle_version} >= 150000 || 0%{?suse_version} > 1500
BuildRequires:  firewalld
%endif
BuildRequires:  distribution-release
BuildRequires:  dracut
BuildRequires:  go >= 1.20
BuildRequires:  golang-packaging
BuildRequires:  libgpg-error-devel
BuildRequires:  make
BuildRequires:  munge
BuildRequires:  sysuser-tools
BuildRequires:  tftp
BuildRequires:  yq
BuildRequires:  pkgconfig(gpgme)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%sysusers_requires
Requires:       %{name}-overlay = %{version}
Requires:       dhcp-server
Requires:       ipxe-bootimgs
Requires:       pigz
Requires:       tftp
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
Requires(pre):  %{name}
Summary:        Default overlay for warewulf
Group:          Productivity/Clustering/Computing

%description overlay
Includes the default overlays so that they can be updated seprately.

%package api
Requires:       %{name}
Summary:        Contains the services for the warewulf rest API
Conflicts:      warewulf-provision-x86_64-initramfs

%description api
Contains the binaries for the access of warewulf through a rest API and from
the commandline from an external host.

%package man
Supplements:    %{name}
Provides:       warewulf4-doc = %version
Obsoletes:      warewulf4-doc < %version
Summary:        Warewulf4 Man Pages
BuildArch:      noarch

%description man
Man pages for warewulf4.

%package overlay-slurm
Summary:        Configuration template for slurm
Requires:       %{name} = %{version}
Requires:       slurm
BuildArch:      noarch
Obsoletes:      warewulf4-slurm < 4.4.0
Provides:       warewulf4-slurm = %version

%description overlay-slurm
This package install the necessary configuration files in order to run a slurm
cluster on the configured warewulf nodes.

%prep
%setup -q -n warewulf-%{vers}%{rls_cndt}
%autopatch -p1
# tar xzf %{S:1}

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
cp %{S:20} .

# use ipxe-bootimgs images from distribution
yq e '
  .tftp.ipxe."00:00" = "undionly.kpxe" |
  .tftp.ipxe."00:07" = "ipxe-x86_64.efi" |
  .tftp.ipxe."00:09" = "ipxe-x86_64.efi" |
  .tftp.ipxe."00:0B" = "snp-arm64.efi" |
  .["container mounts"] += {"source": "/etc/SUSEConnect", "dest": "/etc/SUSEConnect", "readonly": true} |
  .["container mounts"] += {"source": "/etc/zypp/credentials.d/SCCcredentials", "dest": "/etc/zypp/credentials.d/SCCcredentials", "readonly": true}' \
  -i %{buildroot}%{_sysconfdir}/warewulf/warewulf.conf
#sed -i -e 's@\(^\s*\)\(.*:.*\):@\1"\2":@' %%{buildroot}%%{_sysconfdir}/warewulf/warewulf.conf
# fix dhcp for SUSE
mv %{buildroot}%{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/dhcp/dhcpd.conf.ww %{buildroot}%{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/dhcpd.conf.ww
rmdir %{buildroot}%{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/dhcp

# create systemuser
echo "u warewulf -" > system-user-%{name}.conf
echo "g warewulf -" >> system-user-%{name}.conf
%sysusers_generate_pre system-user-%{name}.conf %{name} system-user-%{name}.conf
install -D -m 644 system-user-%{name}.conf %{buildroot}%{_sysusersdir}/system-user-%{name}.conf
install -D -m 755 %{S:10} %{buildroot}%{_datadir}/warewulf/scripts/config-warewulf.sh

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
# move the other example templates for client overlays to package documentation
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}
mv %{buildroot}/%{_sysconfdir}/warewulf/examples %{buildroot}%{_defaultdocdir}/%{name}/example-templates

%pre -f %{name}.pre
%service_add_pre warewulfd.service

%post
%service_add_post warewulfd.service
%{_datadir}/warewulf/scripts/config-warewulf.sh

%preun
%service_del_preun warewulfd.service

%postun
%service_del_postun warewulfd.service

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
%{_defaultdocdir}/%{name}/example-templates
%{_prefix}/lib/firewalld/services/warewulf.xml
%exclude %{_datadir}/warewulf/overlays
%{_bindir}/wwctl
%{_sbindir}/rcwarewulfd
%{_unitdir}/warewulfd.service
%{_sysusersdir}/system-user-%{name}.conf
%{_datadir}/warewulf

%files man
%{_mandir}/man1/wwctl*1.gz
%{_mandir}/man5/*conf*gz

%files api
%{_bindir}/wwapic
%{_bindir}/wwapid
%{_bindir}/wwapird
%config(noreplace) %{_sysconfdir}/warewulf/wwapic.conf
%config(noreplace) %{_sysconfdir}/warewulf/wwapid.conf
%config(noreplace) %{_sysconfdir}/warewulf/wwapird.conf

%files overlay
# The configuration files in this location are for the compute
# nodes, so when modified we do not replace them as sensible
# admin will read the changelog
%{_localstatedir}/lib/warewulf/overlays
%dir %{_localstatedir}/lib/warewulf
%config(noreplace) %{_localstatedir}/lib/warewulf/overlays
%exclude %{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/slurm
%exclude %{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/slurm
%exclude %{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/munge

%files overlay-slurm
%dir %{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/slurm
%{_localstatedir}/lib/warewulf/overlays/host/rootfs/etc/slurm/slurm.conf.ww
%dir %{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/slurm
%{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/slurm/slurm.conf.ww
%dir %{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/munge
%{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/munge/munge.key.ww
%dir %attr(0700,munge,munge) %{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/munge
%attr(0600,munge,munge) %config(noreplace) %{_localstatedir}/lib/warewulf/overlays/generic/rootfs/etc/munge/munge.key.ww

%changelog
