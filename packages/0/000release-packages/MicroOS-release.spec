#
# spec file for package openSUSE-MicroOS-release.spec
#
# Copyright (c) 2020 SUSE LLC
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


Name:           MicroOS-release
Version:        20210510
Release:        0
Summary:        openSUSE MicroOS 
License:        GPL-2.0-or-later
Group:          System/Fhs
Source100:      weakremovers.inc
BuildRequires:  skelcd-openSUSE
# Make sure we are at SLES12 SP2 level
PreReq:         glibc >= 2.19
# in rare cases, 'ln' is not found...
Requires(post): coreutils
Suggests:       branding-openSUSE
Suggests:       distribution-logos-openSUSE-MicroOS
Suggests:       openSUSE-build-key
Conflicts:      distribution-release
Conflicts:      kernel < 4.4
Provides:       distribution-release
# MicroOS is a SUSE Linux type distribution
Provides:       suse-release = %{version}-%{release}
Provides:       suse-release-oss = %{version}-%{release}
# MicroOS-release replaces Tumbleweed-Kubic-release
Provides:       openSUSE-Tumbleweed-Kubic-release
Obsoletes:      openSUSE-Tumbleweed-Kubic-release <= 20190324
Provides:       openSUSE-MicroOS-release = %{version}
Obsoletes:      openSUSE-MicroOS-release <= %{version}
# Give zypp a hint that this product must be kept up-to-date using zypper dup, not up (boo#1061384)
Provides:       product-update() = dup
# With more than one product in the FTP tree, yast needs to know which products are installable
# The name is referenced by the control file as well
Provides:       system-installation() = MicroOS
# bnc#826592
Provides:       weakremover(kernel-default) < 3.11
Provides:       weakremover(kernel-desktop) < 4.2
Provides:       weakremover(kernel-ec2) < 3.11
Provides:       weakremover(kernel-pae) < 3.11
Provides:       weakremover(kernel-vanilla) < 3.11
Provides:       weakremover(kernel-xen) < 3.11
# migrated from MANUAL_OBSOLETES/packages
Provides:       weakremover(boost-license1_56_0)
Provides:       weakremover(boost-license1_59_0)
Provides:       weakremover(gpg-pubkey-3d25d3d9-36e12d04)
Provides:       weakremover(lib++dfb-1_7-6)
Provides:       weakremover(libastro-qt5-1)
Provides:       weakremover(libboost_atomic1_59_0)
Provides:       weakremover(libboost_atomic1_60_0)
Provides:       weakremover(libboost_atomic1_62_0)
Provides:       weakremover(libboost_atomic1_63_0)
Provides:       weakremover(libboost_chrono1_59_0)
Provides:       weakremover(libboost_chrono1_60_0)
Provides:       weakremover(libboost_chrono1_62_0)
Provides:       weakremover(libboost_chrono1_63_0)
Provides:       weakremover(libboost_container1_59_0)
Provides:       weakremover(libboost_container1_60_0)
Provides:       weakremover(libboost_container1_62_0)
Provides:       weakremover(libboost_container1_63_0)
Provides:       weakremover(libboost_context1_59_0)
Provides:       weakremover(libboost_context1_60_0)
Provides:       weakremover(libboost_context1_62_0)
Provides:       weakremover(libboost_context1_63_0)
Provides:       weakremover(libboost_coroutine1_59_0)
Provides:       weakremover(libboost_coroutine1_60_0)
Provides:       weakremover(libboost_coroutine1_62_0)
Provides:       weakremover(libboost_coroutine1_63_0)
Provides:       weakremover(libboost_date_time1_59_0)
Provides:       weakremover(libboost_date_time1_60_0)
Provides:       weakremover(libboost_date_time1_62_0)
Provides:       weakremover(libboost_date_time1_63_0)
Provides:       weakremover(libboost_filesystem1_59_0)
Provides:       weakremover(libboost_filesystem1_60_0)
Provides:       weakremover(libboost_filesystem1_62_0)
Provides:       weakremover(libboost_filesystem1_63_0)
Provides:       weakremover(libboost_graph1_59_0)
Provides:       weakremover(libboost_graph1_60_0)
Provides:       weakremover(libboost_graph1_62_0)
Provides:       weakremover(libboost_graph1_63_0)
Provides:       weakremover(libboost_iostreams1_59_0)
Provides:       weakremover(libboost_locale1_59_0)
Provides:       weakremover(libboost_log1_59_0)
Provides:       weakremover(libboost_log1_60_0)
Provides:       weakremover(libboost_log1_62_0)
Provides:       weakremover(libboost_log1_63_0)
Provides:       weakremover(libboost_math1_59_0)
Provides:       weakremover(libboost_program_options1_59_0)
Provides:       weakremover(libboost_python1_59_0)
Provides:       weakremover(libboost_random1_59_0)
Provides:       weakremover(libboost_regex1_59_0)
Provides:       weakremover(libboost_regex1_60_0)
Provides:       weakremover(libboost_regex1_62_0)
Provides:       weakremover(libboost_regex1_63_0)
Provides:       weakremover(libboost_serialization1_59_0)
Provides:       weakremover(libboost_signals1_59_0)
Provides:       weakremover(libboost_system1_56_0)
Provides:       weakremover(libboost_system1_59_0)
Provides:       weakremover(libboost_test1_59_0)
Provides:       weakremover(libboost_thread1_56_0)
Provides:       weakremover(libboost_thread1_59_0)
Provides:       weakremover(libboost_timer1_59_0)
Provides:       weakremover(libboost_wave1_59_0)
Provides:       weakremover(libcamel-1_2-54)
Provides:       weakremover(libdialog12)
Provides:       weakremover(libdirectfb-1_7-6)
Provides:       weakremover(libdns146)
Provides:       weakremover(libdns160)
Provides:       weakremover(libdns161)
Provides:       weakremover(libgdict-1_0-9)
Provides:       weakremover(libgit2-23)
Provides:       weakremover(libgpaste4)
Provides:       weakremover(libhdf5-11)
Provides:       weakremover(libhdf5_hl11)
Provides:       weakremover(libicu54_1)
Provides:       weakremover(libicu54_1-ledata)
Provides:       weakremover(libicu55_1)
Provides:       weakremover(libicu55_1-ledata)
Provides:       weakremover(libicu56_1)
Provides:       weakremover(libicu56_1-ledata)
Provides:       weakremover(libimobiledevice5)
Provides:       weakremover(libisc142)
Provides:       weakremover(libisc148)
Provides:       weakremover(libisl13)
Provides:       weakremover(libixion-0_10-0)
Provides:       weakremover(liblmdb-0_9_16)
Provides:       weakremover(libmicrohttpd11)
Provides:       weakremover(libminiupnpc15)
Provides:       weakremover(libnis1)
Provides:       weakremover(libntfs-3g86)
Provides:       weakremover(liborcus-0_10-0)
Provides:       weakremover(libpoppler47)
Provides:       weakremover(libpoppler48)
Provides:       weakremover(libpoppler49)
Provides:       weakremover(libpoppler50)
Provides:       weakremover(libpoppler51)
Provides:       weakremover(libpoppler52)
Provides:       weakremover(libpoppler53)
Provides:       weakremover(libpoppler54)
Provides:       weakremover(libpoppler55)
Provides:       weakremover(libpoppler56)
Provides:       weakremover(libpoppler57)
Provides:       weakremover(libpoppler58)
Provides:       weakremover(libpoppler59)
Provides:       weakremover(libpoppler61)
Provides:       weakremover(libpoppler62)
Provides:       weakremover(libpoppler63)
Provides:       weakremover(libpoppler64)
Provides:       weakremover(libpoppler65)
Provides:       weakremover(libprocps4)
Provides:       weakremover(libprocps5)
Provides:       weakremover(libpsl0)
Provides:       weakremover(libsgutils2-1_40-2)
Provides:       weakremover(libsgutils2-1_41-2)
Provides:       weakremover(libvpx2)
Provides:       weakremover(libxtables11)
Provides:       weakremover(libzip4)
Provides:       weakremover(mt_st)
Provides:       weakremover(openssl-debuginfo)
# this package should only be available for the "basearchs" of a product
ExclusiveArch:  %ix86 x86_64 ppc64le s390x aarch64 %arm
%include %{SOURCE100}
Provides:       %name-%version
Provides:       product() = MicroOS
Provides:       product(MicroOS) = 20210510-0
Provides:       product-label() = openSUSE%20MicroOS
Provides:       product-cpeid() = cpe%3A%2Fo%3Aopensuse%3Amicroos%3A20210510
Provides:       product-url(releasenotes) = http%3A%2F%2Fdoc.opensuse.org%2Frelease%2Dnotes%2Fx86_64%2FopenSUSE%2FTumbleweed%2Frelease%2Dnotes%2DopenSUSE.rpm
Provides:       product-endoflife()
Requires:       product_flavor(MicroOS)



%description
openSUSE MicroOS combines the benefits of a rolling OS with a read-only root filesystem with transactional updates. It is a modern Linux Operating System, designed for single-service installations, such as container hosts. It is optimized for large, clustered deployments.
        It inherits the benefits of openSUSE Tumbleweed while redefining the operating system into a small, efficient and reliable distribution.

%package dvd
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(dvd)
Provides:       product_flavor(MicroOS) = 20210510-0
Summary:        openSUSE MicroOS%{?betaversion: %{betaversion}}

%description dvd
openSUSE MicroOS combines the benefits of a rolling OS with a read-only root filesystem with transactional updates. It is a modern Linux Operating System, designed for single-service installations, such as container hosts. It is optimized for large, clustered deployments.
        It inherits the benefits of openSUSE Tumbleweed while redefining the operating system into a small, efficient and reliable distribution.

%files dvd
%defattr(-,root,root)
%doc %{_defaultdocdir}/MicroOS-release-dvd

%package kubic-dvd
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(kubic-dvd)
Provides:       product_flavor(MicroOS) = 20210510-0
Summary:        openSUSE MicroOS%{?betaversion: %{betaversion}}

%description kubic-dvd
openSUSE MicroOS combines the benefits of a rolling OS with a read-only root filesystem with transactional updates. It is a modern Linux Operating System, designed for single-service installations, such as container hosts. It is optimized for large, clustered deployments.
        It inherits the benefits of openSUSE Tumbleweed while redefining the operating system into a small, efficient and reliable distribution.

%files kubic-dvd
%defattr(-,root,root)
%doc %{_defaultdocdir}/MicroOS-release-kubic-dvd

%package appliance
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(appliance)
Provides:       product_flavor(MicroOS) = 20210510-0
Summary:        openSUSE MicroOS%{?betaversion: %{betaversion}}

%description appliance
openSUSE MicroOS combines the benefits of a rolling OS with a read-only root filesystem with transactional updates. It is a modern Linux Operating System, designed for single-service installations, such as container hosts. It is optimized for large, clustered deployments.
        It inherits the benefits of openSUSE Tumbleweed while redefining the operating system into a small, efficient and reliable distribution.

%files appliance
%defattr(-,root,root)
%doc %{_defaultdocdir}/MicroOS-release-appliance

%package appliance-kubic
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(appliance-kubic)
Provides:       product_flavor(MicroOS) = 20210510-0
Summary:        openSUSE MicroOS%{?betaversion: %{betaversion}}

%description appliance-kubic
openSUSE MicroOS combines the benefits of a rolling OS with a read-only root filesystem with transactional updates. It is a modern Linux Operating System, designed for single-service installations, such as container hosts. It is optimized for large, clustered deployments.
        It inherits the benefits of openSUSE Tumbleweed while redefining the operating system into a small, efficient and reliable distribution.

%files appliance-kubic
%defattr(-,root,root)
%doc %{_defaultdocdir}/MicroOS-release-appliance-kubic



%prep

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_prefix}/lib/issue.d
echo -e "\nWelcome to openSUSE MicroOS (%{_target_cpu}) - Kernel \\\r (\\\l).\n" > %{buildroot}%{_prefix}/lib/issue.d/10-OS
echo -e "\n" > %{buildroot}%{_prefix}/lib/issue.d/90-OS

touch %{buildroot}%{_sysconfdir}/motd

# Put EULA into correct place
mkdir -p %{buildroot}/%{_sysconfdir}/YaST2/licenses/base
cd %{buildroot}/%{_sysconfdir}/YaST2/licenses/base
if [ -f /CD1/license.tar.gz ]; then
  tar -xzf /CD1/license.tar.gz
elif [ -f %{_prefix}/lib/skelcd/CD1/license.tar.gz ]; then
  tar -xzf %{_prefix}/lib/skelcd/CD1/license.tar.gz
fi

VERSION_ID=`echo %{version}|tr '[:upper:]' '[:lower:]'|sed -e 's/ //g;'`
# note: VERSION is an optional field and has no meaning other than informative on a rolling distro
# We do thus not add it to the os-release file
cat > %{buildroot}%{_prefix}/lib/os-release <<EOF
NAME="openSUSE MicroOS"
# VERSION="%{version}%{?betaversion: %{betaversion}}"
ID="opensuse-microos"
ID_LIKE="suse opensuse opensuse-tumbleweed"
VERSION_ID="$VERSION_ID"
PRETTY_NAME="openSUSE MicroOS"
ANSI_COLOR="0;32"
CPE_NAME="cpe:/o:opensuse:microos:%{version}"
BUG_REPORT_URL="https://bugs.opensuse.org"
HOME_URL="https://www.opensuse.org/"
DOCUMENTATION_URL="https://en.opensuse.org/Portal:MicroOS"
LOGO="distributor-logo"
EOF
ln -s ..%{_prefix}/lib/os-release %{buildroot}%{_sysconfdir}/os-release

mkdir -p $RPM_BUILD_ROOT/etc/products.d
cat >$RPM_BUILD_ROOT/etc/products.d/MicroOS.prod << EOF
<?xml version="1.0" encoding="UTF-8"?>
<product schemeversion="0">
  <vendor>openSUSE</vendor>
  <name>MicroOS</name>
  <version>20210510</version>
  <release>0</release>
  <endoflife></endoflife>
  <arch>%{_target_cpu}</arch>
  <cpeid>cpe:/o:opensuse:microos:20210510</cpeid>
  <productline>MicroOS</productline>
  <register>
    <pool>
    </pool>
    <updates>
    </updates>
  </register>
  <repositories>
  </repositories>
  <summary>openSUSE MicroOS</summary>
  <shortsummary>openSUSE MicroOS</shortsummary>
  <description>openSUSE MicroOS combines the benefits of a rolling OS with a read-only root filesystem with transactional updates. It is a modern Linux Operating System, designed for single-service installations, such as container hosts. It is optimized for large, clustered deployments.
        It inherits the benefits of openSUSE Tumbleweed while redefining the operating system into a small, efficient and reliable distribution.</description>
  <linguas>
    <language>en_US</language>
  </linguas>
  <urls>
    <url name="releasenotes">http://doc.opensuse.org/release-notes/x86_64/openSUSE/Tumbleweed/release-notes-openSUSE.rpm</url>
  </urls>
  <buildconfig>
    <producttheme>MicroOS</producttheme>
    <create_flavors>true</create_flavors>
  </buildconfig>
  <installconfig>
    <defaultlang>en_US</defaultlang>
    <datadir>suse</datadir>
    <descriptiondir>suse/setup/descr</descriptiondir>
    <releasepackage name="%{name}" flag="EQ" version="%{version}" release="%{release}"/>
    <distribution>openSUSE</distribution>
  </installconfig>
  <runtimeconfig/>
</product>

EOF

mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/MicroOS-release-dvd
cat >$RPM_BUILD_ROOT/%{_defaultdocdir}/MicroOS-release-dvd/README << EOF
This package only exists for providing the product flavor 'dvd'.

EOF

mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/MicroOS-release-kubic-dvd
cat >$RPM_BUILD_ROOT/%{_defaultdocdir}/MicroOS-release-kubic-dvd/README << EOF
This package only exists for providing the product flavor 'kubic-dvd'.

EOF

mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/MicroOS-release-appliance
cat >$RPM_BUILD_ROOT/%{_defaultdocdir}/MicroOS-release-appliance/README << EOF
This package only exists for providing the product flavor 'appliance'.

EOF

mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/MicroOS-release-appliance-kubic
cat >$RPM_BUILD_ROOT/%{_defaultdocdir}/MicroOS-release-appliance-kubic/README << EOF
This package only exists for providing the product flavor 'appliance-kubic'.

EOF



%post
# Update from openSUSE-Tumbleweed-Kubic to openSUSE-MicroOS
# Fix the baseproduct symlink and make sure, it exists
if [ -L %{_sysconfdir}/products.d/baseproduct ] ; then
    PRODLINK=$(basename $(readlink -f %{_sysconfdir}/products.d/baseproduct))
    if [ "$PRODLINK"  = "openSUSE-Tumbleweed-Kubic.prod" -o "$PRODLINK"  = "openSUSE-MicroOS.prod" ]; then
      rm -f %{_sysconfdir}/products.d/baseproduct
    fi
fi
if [ ! -e %{_sysconfdir}/products.d/baseproduct ]; then
    ln -sf MicroOS.prod %{_sysconfdir}/products.d/baseproduct
fi

%files
%defattr(644,root,root,755)
%{_sysconfdir}/os-release
%{_prefix}/lib/os-release
%dir %{_sysconfdir}/products.d
%{_sysconfdir}/products.d/*
%dir %{_sysconfdir}/YaST2/
%config(noreplace) %{_sysconfdir}/motd
%dir %{_sysconfdir}/YaST2/licenses/
%dir %{_sysconfdir}/YaST2/licenses/base/
# no %doc here, or we will not install them
%{_sysconfdir}/YaST2/licenses/base/license*txt
%{_sysconfdir}/YaST2/licenses/base/no-acceptance-needed
%dir %{_prefix}/lib/issue.d
%{_prefix}/lib/issue.d/*-OS

%changelog
