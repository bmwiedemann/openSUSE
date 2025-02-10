#
# spec file for package warewulf
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


%global flavor @BUILD_FLAVOR@%{nil}

%if "%{?flavor}" == ""
ExclusiveArch:  do_not_build
%else
 %if 0%{?suse_version} > 1500
ExclusiveArch:  x86_64 aarch64
 %else
ExclusiveArch:  x86_64 aarch64 i586
 %endif
 %ifarch x86_64 # on arch != x86_64 only build warewulf-provision-%%arch-initramfs
  %define full_build 1
 %endif
%endif

Name:           warewulf
Version:        3.8.1
Release:        0
Summary:        A suite of tools for clustering
License:        BSD-3-Clause-LBNL
Group:          Productivity/Clustering/Computing
URL:            http://warewulf.lbl.gov/
Source0:        https://github.com/warewulf/warewulf3/archive/%{version}.tar.gz#/%{name}3-%{version}.tar.gz
Source100:      install-recipe.md
Source101:      install-recipe-vm.md
Patch0:         wwinit-Check-if-service-is-enabled-before-enabling-it.patch
Patch1:         Perl-Escape-left-curly-brace-properly-in-regexps-for-perl-5.26.patch
Patch2:         wwinit-If-no-ntp-key-file-is-present-comment-it-out-in-new-config-143.patch
Patch3:         wwinit-If-original-ntpd.conf-file-has-this-has-keys-set-up-copy-them-128.patch
Patch4:         Check-for-SUSE-system-and-set-Apache2-config-path-accordingly.patch
Patch5:         Add-Leap-42.3-15.0-Tumbleweed-remove-support-for-openSUSE-13.1-133.patch
Patch6:         common-functions-When-checking-for-RPM-package-check-whatprovides-134.patch
Patch7:         wwinit-Check-for-tftp-server-capability-as-well-135.patch
Patch8:         Provisioning-httpd-Make-plugin-directory-configurable-at-build-time-138.patch
Patch9:         common-Allow-bash-completion-directory-to-be-configurable-139.patch
Patch10:        wwmkchroot-Fix-SUSE-specific-installation-functions-to-work-with-openSUSE-and-SLES-132.patch
Patch11:        wwinit-Add-check-for-properly-configured-network-136.patch
Patch12:        vnfs-Add-auto-agree-with-licenses-to-include-suse-PKGR_CMD-142.patch
Patch13:        Suse-prov-config-local-binary-copy-140.patch
Patch14:        busybox-Newer-versions-of-glibc-do-not-ship-rpc-functions-any-more-130.patch
Patch15:        common-Correctly-detect-SUSE-system-for-system-services.patch
Patch16:        common-Consolidate-system-service-module-for-SUSE.patch
#Patch17:        provision-Update-ipxe-to-Github-commitid-133f4c4.patch
Patch18:        Remove-shebang-from-scripts-only-intended-to-be-sourced.patch
Patch19:        vnfs-SUSE-copy-repo-files-to-correct-location.patch
Patch20:        vnfs-SUSE-make-sure-zypper-auto-accepts-licenses.patch
Patch21:        vnfs-SUSE-Make-sure-no-repos-are-left-over-when-adding-a-list-of-repositories.patch
Patch22:        common-Really-install-network-check-script.patch
Patch23:        provision-Check-for-presence-of-busybox_links_path-replacement.patch
Patch24:        provision-Add-build-configuration-to-allow-for-use-of-local-arm-ipxe-images.patch
Patch25:        ipmi-allow-build-to-use-locally-installed-ipmitools.patch
# SUSE specific
Patch26:        common-LSB-Move-common-functions-script-library-to-libexec.patch
Patch27:        provision-If-available-us-haveged-in-warewulf-initrd.patch
Patch28:        cluster-remove-firstboot-stuff.patch
Patch29:        LSB-Use-sharedstatedir-instead-of-localstatedir-for-WW_STATEDIR.patch
Patch30:        common-Check-for-package-mariadb-as-well.patch
Patch31:        vnfs-SUSE-Templates-Leap-15.1-Leap-15.3-added-SLE-15.patch
Patch32:        common-Check-for-non-empty-string-before-chomp.patch
Patch33:        common-Create-database-user-separately-to-allow-empty-password.patch
Patch34:        common-Fix-help-text.patch
Patch35:        cluster-Don-t-attempt-ntp-configuration-when-chrony-is-found.patch
Patch36:        cluster-If-hostname-doesn-t-contain-the-domain-try-to-derive-this-from-FQDN.patch
Patch37:        provision-Unify-handling-of-initramfs-location.patch
Patch38:        initramfs-Going-forward-bin-or-sbin-are-mere-links-to-usr-cater-for-this.patch
Patch39:        initramfs-Add-network-handling-support-for-SUSE.patch
Patch40:        initramfs-Handle-NTP-client-configuration-for-SUSE.patch
Patch41:        Add-lib-modules-opt_kversion-sysctl.conf-to-initfs-if-present.patch
Patch42:        vnfs-Do-not-pull-in-recommended-packages-on-SUSE.patch
Patch43:        Add-suse-to-overlay-template.patch
Patch44:        vnfs-On-SUSE-don-t-copy-repository-information-into-chroot.patch
Patch45:        provision-For-reproducible-builds-equalize-time-stamps-in-CPIO-archives.patch
Patch46:        ipmi-For-reproducible-builds-equalize-time-stamps-in-CPIO-archives.patch

%if "%{?flavor}" != "common"
BuildRequires:  bsdtar
%if 0%{suse_version} > 1500
BuildRequires:  busybox-warewulf3
%else
BuildRequires:  busybox
BuildRequires:  busybox-static
%endif
BuildRequires:  device-mapper-devel
BuildRequires:  e2fsprogs
%if 0%{?sle_version:1} && 0%{?sle_version} < 150400
BuildRequires:  haveged
%endif
BuildRequires:  ipmitool
%if 0%{?full_build}
BuildRequires:  ipxe-bootimgs
%endif
BuildRequires:  libselinux-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libuuid-devel
BuildRequires:  parted
BuildRequires:  warewulf-common
BuildRequires:  xz-devel
BuildRequires:  perl(Apache)
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  distribution-release
BuildRequires:  fdupes
BuildRequires:  sysuser-tools
# NOTYET
#BuildRequires: xfsprogs
#BuildRequires: curl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Warewulf is a set of utilities designed to better enable utilization
and maintenance of clusters or groups of computers.

%package common
Summary:        Main Warewulf daemon and utilities
Group:          Productivity/Clustering/Computing
Requires(pre):  shadow
Requires(post): mysql
Requires:       mysql
Requires:       perl-warewulf-common
Requires:       warewulf-doc
BuildArch:      noarch

%description common
Warewulf is a scalable systems management suite originally developed to
manage large high-performance Linux clusters. Focused on general
scalable system management, it includes a framework for system
configuration, management, provisioning/installation, monitoring, event
notification, and more via a modular plugin architecture.

This is the main package which includes the command line interface,
initialization script, and configuration definition. All other warewulf
modules depend on this module for configuration information.

%package -n perl-warewulf-common
Summary:        Perl support scripts for the Warewulf3 system
Group:          Productivity/Clustering/Computing
%{perl_requires}
%{sysusers_requires}
Requires:       perl-DBD-mysql
BuildArch:      noarch

%description -n perl-warewulf-common
Warewulf is a scalable systems management suite originally developed to
manage large high-performance Linux clusters. Focused on general
scalable system management, it includes a framework for system
configuration, management, provisioning/installation, monitoring, event
notification, and more via a modular plugin architecture.

This package includes the supporting libs for the Warewulf daemon.

%package doc
Summary:        Warewulf documentation and install recipes
Group:          Productivity/Clustering/Computing
BuildArch:      noarch

%description doc
Warewulf is a scalable systems management suite originally developed to
manage large high-performance Linux clusters. Focused on general
scalable system management, it includes a framework for system
configuration, management, provisioning/installation, monitoring, event
notification, and more via a modular plugin architecture.

This package contains documentation for Warewulf, and installation
recipes to assist in the deployment of a Warewulf cluster.

%package provision
Summary:        Warewulf Cluster Provisioning Module
Group:          Productivity/Clustering/Computing
Requires:       perl-warewulf-provision
Requires:       warewulf-common
BuildArch:      noarch

%description provision
Warewulf is a scalable systems management suite originally developed to
manage large high-performance Linux clusters. Focused on general
scalable system management, it includes a framework for system
configuration, management, provisioning/installation, monitoring, event
notification, and more via a modular plugin architecture.  The
provision module provides functionality for provisioning, configuring,
and booting systems.

This package contains the core provisioning components and
administrative tools.  To actually provision systems, the
warewulf-provision-server package is also required.

%package -n perl-warewulf-provision
Summary:        Perl support scripts for the Warewulf3 provisioning system
Group:          Productivity/Clustering/Computing
%{?perl_requires}
Requires:       perl-warewulf-common
BuildArch:      noarch

%description -n perl-warewulf-provision
Warewulf is a scalable systems management suite originally developed to
manage large high-performance Linux clusters. Focused on general
scalable system management, it includes a framework for system
configuration, management, provisioning/installation, monitoring, event
notification, and more via a modular plugin architecture.  The
provision module provides functionality for provisioning, configuring,
and booting systems.

This package includes the supporting libs for the Warewulf
provisioning module.

%package provision-server
Summary:        Warewulf Cluster Provisioning Module Server
Group:          Productivity/Clustering/Computing
Requires:       perl-warewulf-provision-server
Requires:       warewulf-common
BuildArch:      noarch

%description provision-server
Warewulf is a scalable systems management suite originally developed to
manage large high-performance Linux clusters. Focused on general
scalable system management, it includes a framework for system
configuration, management, provisioning/installation, monitoring, event
notification, and more via a modular plugin architecture.  The
provision module provides functionality for provisioning, configuring,
and booting systems.

This package contains the CGI scripts and event components to actually
provision systems.  Systems used solely for administration of Warewulf
do not require this package.

%package -n perl-warewulf-provision-server
Summary:        Perl support scripts for the Warewulf3 provisioning system
Group:          Productivity/Clustering/Computing
%{?perl_requires}
Requires:       apache2
Requires:       dhcp-server
Requires:       nfs-kernel-server
Requires:       perl-CGI
Requires:       perl-warewulf-common
Requires:       tftp
Requires:       perl(Apache)
BuildArch:      noarch

%description -n perl-warewulf-provision-server
Warewulf is a scalable systems management suite originally developed to
manage large high-performance Linux clusters. Focused on general
scalable system management, it includes a framework for system
configuration, management, provisioning/installation, monitoring, event
notification, and more via a modular plugin architecture.  The
provision module provides functionality for provisioning, configuring,
and booting systems.

This package includes the supporting libs for the Warewulf
provisioning server module.

%package provision-%{_arch}-initramfs
Summary:        Warewulf Cluster Provisioning Module initramfs for %{_arch} systems
Group:          Productivity/Clustering/Computing
Requires:       warewulf-provision
BuildArch:      noarch

%description provision-%{_arch}-initramfs
Warewulf is a scalable systems management suite originally developed to
manage large high-performance Linux clusters. Focused on general
scalable system management, it includes a framework for system
configuration, management, provisioning/installation, monitoring, event
notification, and more via a modular plugin architecture.  The
provision module provides functionality for provisioning, configuring,
and booting systems.

This package contains the %{_arch}-specific initramfs used to build the
bootstrap for %{_arch} systems.

%package provision-ipxe-images
Summary:        Warewulf Cluster Provisioning Module iPXE Images
Group:          Productivity/Clustering/Computing
Requires:       warewulf-provision-server
BuildArch:      noarch

%description provision-ipxe-images
Warewulf is a scalable systems management suite originally developed to
manage large high-performance Linux clusters. Focused on general
scalable system management, it includes a framework for system
configuration, management, provisioning/installation, monitoring, event
notification, and more via a modular plugin architecture.  The
provision module provides functionality for provisioning, configuring,
and booting systems.

This package contains the iPXE images used to boot warewulf on i586,
x86_64, and arm64 systems.

%package vnfs
Summary:        Warewulf VNFS Module
Group:          Productivity/Clustering/Computing
Requires:       warewulf-common
BuildArch:      noarch

%description vnfs
Warewulf is a scalable systems management suite originally developed to
manage large high-performance Linux clusters. Focused on general
scalable system management, it includes a framework for system
configuration, management, provisioning/installation, monitoring, event
notification, and more via a modular plugin architecture.

This is the VNFS module which supports the creation and management of
Virtual Node FileSystem objects.

%package cluster
Summary:        Tools used for clustering with Warewulf
Group:          Productivity/Clustering/Computing
%{?perl_requires}
Requires:       dhcp-server
Requires:       warewulf-common
Requires:       warewulf-provision
BuildArch:      noarch

%description cluster
Warewulf is a scalable systems management suite originally developed to
manage large high-performance Linux clusters. Focused on general
scalable system management, it includes a framework for system
configuration, management, provisioning/installation, monitoring, event
notification, and more via a modular plugin architecture.

This package contains tools to facilitate management of a Cluster
with Warewulf.

%package -n perl-warewulf-cluster
Summary:        Perl support scripts for the Warewulf3 cluster module
Group:          Productivity/Clustering/Computing
%{?perl_requires}
Requires:       perl-warewulf-common
BuildArch:      noarch

%description -n perl-warewulf-cluster
Warewulf is a scalable systems management suite originally developed to
manage large high-performance Linux clusters. Focused on general
scalable system management, it includes a framework for system
configuration, management, provisioning/installation, monitoring, event
notification, and more via a modular plugin architecture.

This package includes the supporting libs for the Warewulf cluster
server module.

%package -n perl-warewulf-ipmi
Summary:        Perl support scripts for the Warewulf3 IPMI module
Group:          Productivity/Clustering/Computing
Requires:       ipmitool
Requires:       perl-warewulf-common
%{?perl_requires}
BuildArch:      noarch

%description -n perl-warewulf-ipmi
Warewulf is a scalable systems management suite originally developed to
manage large high-performance Linux clusters. Focused on general
scalable system management, it includes a framework for system
configuration, management, provisioning/installation, monitoring, event
notification, and more via a modular plugin architecture.

This package includes the supporting libs for the Warewulf ipmi module.

%prep
%setup -q -n %{name}3-%{version}
cp %{SOURCE100} ./common/README.SUSE-INSTALL-RECIPE
cp %{SOURCE101} ./common/README.SUSE-VM-CONFIG-RECIPE
# common
%patch -P 0 -p1
%patch -P 6 -p1
%patch -P 9 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%patch -P 26 -p1
%patch -P 29 -p1
%patch -P 30 -p1
# provision
%patch -P 1 -p1
%patch -P 4 -p1
%patch -P 8 -p1
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 37 -p1
# IPXE sources not needed
%patch -P 23 -p1
%patch -P 24 -p1
%patch -P 27 -p1
%patch -P 38 -p1
%patch -P 39 -p1
%patch -P 40 -p1
%patch -P 45 -p1
# vnfs
%patch -P 5 -p1
%patch -P 10 -p1
%patch -P 12 -p1
%patch -P 19 -p1
%patch -P 20 -p1
%patch -P 21 -p1
%patch -P 31 -p1
%patch -P 41 -p1
%patch -P 42 -p1
%patch -P 43 -p1
%patch -P 44 -p1
# cluster
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 7 -p1
%patch -P 11 -p1
%patch -P 22 -p1
%patch -P 28 -p1
%patch -P 35 -p1
%patch -P 36 -p1
# ipmi
%patch -P 25 -p1
%patch -P 46 -p1
# common
%patch -P 18 -p1
%patch -P 32 -p1
%patch -P 33 -p1
%patch -P 34 -p1

%build
%if "%{?flavor}" == "common"
 cd common
 autoreconf -f -i
 %configure \
%if 0%{?sle_version} >= 150000 || 0%{?sle_version} == 0
    --with-bashcompletionconfdir=%{_datadir}/bash-completion/
%endif
 make
 cd ..

%else

%if 0%{?full_build}

modules="vnfs cluster"
for pkg in ${modules}; do
cd ${pkg}
autoreconf -f -i
%configure
make
cd ..
done

cd ipmi
autoreconf -f -i
%configure --with-local-ipmitool=%_bindir/ipmitool
make
cd ..

%endif

cd provision
autoreconf -f -i
busybox_links=%_datadir/busybox/busybox-warewulf3.links
test -e $busybox_links || busybox_links=%_datadir/busybox/busybox.links
busybox_bin=%_bindir/busybox-warewulf3
test -e $busybox_bin || busybox_bin=%_bindir/busybox-static
%if 0%{?full_build}
%configure \
    --enable-cross-compile \
    --with-local-busybox=$busybox_bin \
    --with-busybox-links-file=$busybox_links \
    --with-local-e2fsprogs=%_prefix/sbin/mkfs.ext4 \
    --with-local-ipxe_undionly=%_datadir/ipxe/undionly.kpxe \
    --with-local-ipxe_snp_i386=%_datadir/ipxe/snp-i386.efi \
    --with-local-ipxe_snp_x86_64=%_datadir/ipxe/snp-i386.efi \
    --with-local-ipxe_snp_arm64=%_datadir/ipxe/snp-arm64.efi \
    --with-local-libarchive=%_bindir/bsdtar \
    --with-local-parted=%_prefix/sbin/parted \
    --with-local-partprobe=%_prefix/sbin/partprobe \
    --with-apache2moddir=%_libdir/apache2
%else
%configure \
    --with-local-busybox=$busybox_bin \
    --with-busybox-links-file=$busybox_links \
    --with-local-e2fsprogs=%_prefix/sbin/mkfs.ext4 \
    --with-local-libarchive=%_bindir/bsdtar \
    --with-local-parted=%_prefix/sbin/parted \
    --with-local-partprobe=%_prefix/sbin/partprobe
#NOTYET   --with-local-xfsprogs=/sbin/mkfs.xfs, --with-local-curl=%{bindir}/curl
cd initramfs
%endif
make
cd ..

%endif

%install
%if "%{?flavor}" == "common"
cd common
%make_install

mkdir -p %{buildroot}/%{_docdir}

cd ..
echo "g %{name} -" > system-group-%{name}.conf
%sysusers_generate_pre system-group-%{name}.conf %{name} system-group-%{name}.conf
install -D -m 644 system-group-%{name}.conf %{buildroot}%{_sysusersdir}/system-group-%{name}.conf

%else

%if 0%{?full_build}
for pkg in vnfs cluster ipmi; do
cd ${pkg}
%make_install
cd ..
done

# vnfs
# Don't exclude these
for i in /var/log/ /usr/lib/locale /usr/share/locale ; do
    sed -i -e "/${i//\//\\\/}/s@\(.*\)@#\1@g"  %{buildroot}/%{_sysconfdir}/warewulf/vnfs.conf
done

%endif # x86_64

# provision
%if 0%{?full_build}

cd provision
%make_install
cd ..
mv %{buildroot}/%{_sysconfdir}/warewulf/filesystem %{buildroot}/%{_datadir}/warewulf/filesystem
echo "tftpdir = /srv/tftpboot" >> %{buildroot}/%{_sysconfdir}/warewulf/provision.conf
install -d %{buildroot}/%{_datadir}/warewulf/ipxe
rm -rf %{buildroot}/%{_usrsrc}/warewulf

%else

cd provision/initramfs
%make_install
cd ../..

%endif

%endif # common

%if 0%{?full_build}
find %{buildroot}/%{perl_vendorlib}/Warewulf -type f -exec chmod a-x '{}' '+'
%endif
%fdupes -s %{buildroot}

%post common
if [ $1 -eq 2 ] ; then
    %{_bindir}/wwsh object canonicalize -t node >/dev/null 2>&1 || :
    %{_bindir}/wwsh object canonicalize -t file >/dev/null 2>&1 || :
fi

%pre -n perl-warewulf-common -f %{name}.pre

%pre common
systemctl enable --now mariadb >/dev/null 2>&1 || :

%if "%{?flavor}" == "common"
%files common
%defattr(-, root, root)
%if 0%{?sle_version} >= 150000 || 0%{?sle_version} == 0
%{_datadir}/bash-completion/warewulf_completion
%else
%{_sysconfdir}/bash_completion.d/*
%endif
%attr(0755, root, warewulf) %dir %{_sysconfdir}/warewulf/
%attr(0755, root, warewulf) %dir %{_sysconfdir}/warewulf/defaults/
%dir %{_libexecdir}/warewulf
%dir %{_libexecdir}/warewulf/wwinit
%dir %{_datadir}/warewulf
%{_bindir}/wwconfig
%{_bindir}/wwinit
%{_bindir}/wwsh
%{_libexecdir}/warewulf/wwinit/10-database.init
%{_libexecdir}/warewulf/wwinit/25-wwsh.init
%{_libexecdir}/warewulf/wwinit/functions
%{_mandir}/man1/wwsh.1.gz
%{_datadir}/warewulf/import-nodes.perceus

%files -n perl-warewulf-common
%defattr(-, root, root)
%attr(0644, root, warewulf) %config(noreplace) %{_sysconfdir}/warewulf/database.conf
%attr(0640, root, warewulf) %config(noreplace) %{_sysconfdir}/warewulf/database-root.conf
%attr(0644, root, warewulf) %config(noreplace) %{_sysconfdir}/warewulf/defaults/node.conf
%{perl_vendorlib}/*
%{_sysusersdir}/system-group-%{name}.conf

%files doc
%defattr(-, root, root)
%doc common/COPYING common/ChangeLog common/README common/LICENSE common/README.SUSE-INSTALL-RECIPE common/README.SUSE-VM-CONFIG-RECIPE

%else

%files provision-%{_arch}-initramfs
%defattr(-, root, root)
%dir %{_localstatedir}/lib/warewulf
%dir %{_localstatedir}/lib/warewulf/initramfs
%{_localstatedir}/lib/warewulf/initramfs/*

%ifarch x86_64
%files provision
%defattr(-, root, root)
%attr(0640, root, warewulf) %config(noreplace) %{_sysconfdir}/warewulf/defaults/provision.conf
%attr(0644, root, warewulf) %config(noreplace) %{_sysconfdir}/warewulf/livesync.conf
%attr(0644, root, warewulf) %config(noreplace) %{_sysconfdir}/warewulf/provision.conf
%dir %{_datadir}/warewulf/filesystem
%dir %{_datadir}/warewulf/filesystem/examples
%{_datadir}/warewulf/filesystem/examples/efi_example.cmds
%{_datadir}/warewulf/filesystem/examples/gpt_example.cmds
%{_datadir}/warewulf/filesystem/examples/gpt_label_example.cmds
%{_datadir}/warewulf/filesystem/examples/gpt_uuid_example.cmds
%{_datadir}/warewulf/filesystem/examples/hybrid_example.cmds
%{_datadir}/warewulf/filesystem/examples/mbr_example.cmds
%{_datadir}/warewulf/filesystem/examples/tmpfs_example.cmds

%files -n perl-warewulf-provision
%defattr(-, root, root)
%{perl_vendorlib}/Warewulf/Bootstrap.pm
%{perl_vendorlib}/Warewulf/Provision.pm
%{perl_vendorlib}/Warewulf/Vnfs.pm
%{perl_vendorlib}/Warewulf/DSO/*
%{perl_vendorlib}/Warewulf/Provision
%{perl_vendorlib}/Warewulf/Event/DynamicHosts.pm
%{perl_vendorlib}/Warewulf/Event/DefaultProvisionNode.pm
%{perl_vendorlib}/Warewulf/Event/ProvisionFileDelete.pm
%{perl_vendorlib}/Warewulf/Module/Cli/Bootstrap.pm
%{perl_vendorlib}/Warewulf/Module/Cli/Provision.pm
%{perl_vendorlib}/Warewulf/Module/Cli/Vnfs.pm
%dir %{perl_vendorlib}/Warewulf

%files provision-server
%config(noreplace) %{_sysconfdir}/apache2/conf.d/warewulf-httpd.conf
%attr(0640, root, warewulf) %config %{_sysconfdir}/warewulf/dhcpd-template.conf
%{_bindir}/wwlivesync
%{_bindir}/wwnodescan
%{_mandir}/man1/wwlivesync.1.gz
%{_mandir}/man1/wwnodescan.1.gz
%dir %{_libexecdir}/warewulf/cgi-bin
%{_libexecdir}/warewulf/cgi-bin/file.pl
%{_libexecdir}/warewulf/cgi-bin/nodeconfig.pl
%{_libexecdir}/warewulf/cgi-bin/script.pl
%{_libexecdir}/warewulf/cgi-bin/vnfs.pl
%dir %{_datadir}/warewulf/ipxe

%files provision-ipxe-images
%defattr(-, root, root)
%dir %{_datadir}/warewulf/ipxe/bin-i386-efi
%dir %{_datadir}/warewulf/ipxe/bin-i386-pcbios
%dir %{_datadir}/warewulf/ipxe/bin-x86_64-efi
%dir %{_datadir}/warewulf/ipxe/bin-arm64-efi
%{_datadir}/warewulf/ipxe/bin-i386-efi/snp.efi
%{_datadir}/warewulf/ipxe/bin-i386-pcbios/undionly.kpxe
%{_datadir}/warewulf/ipxe/bin-x86_64-efi/snp.efi
%{_datadir}/warewulf/ipxe/bin-arm64-efi/snp.efi

%files -n perl-warewulf-provision-server
%defattr(-, root, root)
%{perl_vendorlib}/Warewulf/Event/Bootstrap.pm
%{perl_vendorlib}/Warewulf/Event/Dhcp.pm
%{perl_vendorlib}/Warewulf/Event/Pxe.pm
%{perl_vendorlib}/Warewulf/Module/Cli/Pxe.pm
%{perl_vendorlib}/Warewulf/Module/Cli/Dhcp.pm
%dir %{perl_vendorlib}/Warewulf

%files vnfs
%defattr(644, root, root)
%config(noreplace) %{_sysconfdir}/warewulf/vnfs.conf
%config(noreplace) %{_sysconfdir}/warewulf/bootstrap.conf
%attr(755, root, root) %{_bindir}/wwbootstrap
%attr(755, root, root) %{_bindir}/wwmkchroot
%attr(755, root, root) %{_bindir}/wwvnfs
%dir %{_libexecdir}/warewulf/wwmkchroot
%{_libexecdir}/warewulf/wwmkchroot/centos-5.tmpl
%{_libexecdir}/warewulf/wwmkchroot/centos-6.tmpl
%{_libexecdir}/warewulf/wwmkchroot/centos-7.tmpl
%{_libexecdir}/warewulf/wwmkchroot/debian-8.tmpl
%{_libexecdir}/warewulf/wwmkchroot/debian7-32.tmpl
%{_libexecdir}/warewulf/wwmkchroot/debian7-64.tmpl
%{_libexecdir}/warewulf/wwmkchroot/functions
%{_libexecdir}/warewulf/wwmkchroot/golden-system.tmpl
%{_libexecdir}/warewulf/wwmkchroot/include-deb
%{_libexecdir}/warewulf/wwmkchroot/include-rhel
%{_libexecdir}/warewulf/wwmkchroot/include-suse
%{_libexecdir}/warewulf/wwmkchroot/include-ubuntu
%{_libexecdir}/warewulf/wwmkchroot/opensuse-15.3.tmpl
%{_libexecdir}/warewulf/wwmkchroot/opensuse-42.3.tmpl
%{_libexecdir}/warewulf/wwmkchroot/opensuse-tumbleweed.tmpl
%{_libexecdir}/warewulf/wwmkchroot/rhel-generic.tmpl
%{_libexecdir}/warewulf/wwmkchroot/sl-5.tmpl
%{_libexecdir}/warewulf/wwmkchroot/sl-6.tmpl
%{_libexecdir}/warewulf/wwmkchroot/sl-7.tmpl
%{_libexecdir}/warewulf/wwmkchroot/sles-11.tmpl
%{_libexecdir}/warewulf/wwmkchroot/sles-12.tmpl
%{_libexecdir}/warewulf/wwmkchroot/sle-15.tmpl
%{_libexecdir}/warewulf/wwmkchroot/ubuntu-16.04.tmpl
%{_mandir}/man1/wwbootstrap.1.gz
%{_mandir}/man1/wwvnfs.1.gz

%files cluster
%defattr(-, root, root)
%config %{_sysconfdir}/profile.d/cluster-env.csh
%config %{_sysconfdir}/profile.d/cluster-env.sh
%{_bindir}/cluster-env
%{_bindir}/wwuseradd
%{_libexecdir}/warewulf/wwinit/30-domain.init
%{_libexecdir}/warewulf/wwinit/40-authfiles.init
%{_libexecdir}/warewulf/wwinit/50-dhcp.init
%{_libexecdir}/warewulf/wwinit/50-nfsd.init
%{_libexecdir}/warewulf/wwinit/50-network.init
%{_libexecdir}/warewulf/wwinit/50-ntpd.init
%{_libexecdir}/warewulf/wwinit/50-ssh_keys.init
%{_libexecdir}/warewulf/wwinit/50-tftp.init
%{_libexecdir}/warewulf/wwinit/60-hostfile.init
%{_libexecdir}/warewulf/wwinit/90-bootstrap.init
%{_libexecdir}/warewulf/wwinit/91-vnfs.init

%files -n perl-warewulf-cluster
%defattr(-, root, root)
%{perl_vendorlib}/Warewulf/Module/Cli/Ssh.pm
%dir %{perl_vendorlib}/Warewulf

%files -n perl-warewulf-ipmi
%defattr(-, root, root)
%{perl_vendorlib}/Warewulf/Ipmi.pm
%{perl_vendorlib}/Warewulf/Module/Cli/Ipmi.pm
%dir %{perl_vendorlib}/Warewulf
%endif # ifarch x86_64
%endif # common

%changelog
