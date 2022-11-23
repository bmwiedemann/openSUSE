#
# spec file for package openSUSE-release.spec
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


%define product openSUSE
#define betaversion %{nil}
%define codename Tumbleweed
Name:           openSUSE-release
Version:        20221123
Release:        0
# 0 is the product release, not the build release of this package
Summary:        openSUSE Tumbleweed
License:        BSD-3-Clause
Group:          System/Fhs
Source100:      weakremovers.inc
BuildRequires:  skelcd-control-openSUSE
BuildRequires:  skelcd-openSUSE
Suggests:       branding-openSUSE
Suggests:       distribution-logos-openSUSE-Tumbleweed
Suggests:       java-11-openjdk
Suggests:       mariadb
Suggests:       mariadb-client
Suggests:       openSUSE-build-key
Suggests:       openssl-1_1
Conflicts:      core-release <= 10
Conflicts:      distribution-release
Conflicts:      sled-release <= 10
Conflicts:      sles-release <= 10
Provides:       aaa_version
Provides:       distribution-release
Provides:       suse-release = %{version}-%{release}
Provides:       suse-release-oss = %{version}-%{release}
# Give zypp a hint that this product must be kept up-to-date using zypper dup, not up (boo#1061384)
Provides:       product-update() = dup
# Since we have more than one product in the FTP tree, we need to give yast a hint
Provides:       system-installation() = openSUSE
Obsoletes:      aaa_version
Obsoletes:      openSUSE-Promo-release <= 11.1
Obsoletes:      openSUSE-release-live <= 11.0
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
%include %{SOURCE100}
Provides:       %name-%version
Provides:       product() = openSUSE
Provides:       product(openSUSE) = 20221123-0
%ifarch x86_64
Provides:       product-register-target() = openSUSE%2DTumbleweed%2Dx86_64
%endif
%ifarch s390x
Provides:       product-register-target() = openSUSE%2DTumbleweed%2Ds390x
%endif
%ifarch ppc64le
Provides:       product-register-target() = openSUSE%2DTumbleweed%2Dppc64le
%endif
%ifarch aarch64
Provides:       product-register-target() = openSUSE%2DTumbleweed%2Daarch64
%endif
Provides:       product-label() = openSUSE
Provides:       product-cpeid() = cpe%3A%2Fo%3Aopensuse%3Aopensuse%3A20221123
Provides:       product-url(releasenotes) = http%3A%2F%2Fdoc.opensuse.org%2Frelease%2Dnotes%2Fx86_64%2FopenSUSE%2FTumbleweed%2Frelease%2Dnotes%2DopenSUSE.rpm
Provides:       product-url(repository) = http%3A%2F%2Fdownload.opensuse.org%2Ftumbleweed%2Frepo%2Foss%2F
Requires:       product_flavor(openSUSE)


%description
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%package -n openSUSE-release-ftp
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(ftp)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description ftp
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files ftp
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-ftp

%package -n openSUSE-release-mini
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(mini)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description mini
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files mini
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-mini

%package -n openSUSE-release-dvd
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(dvd)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description dvd
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files dvd
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-dvd

%package -n openSUSE-release-livecd-kde
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(livecd-kde)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description livecd-kde
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files livecd-kde
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-livecd-kde

%package -n openSUSE-release-livecd-x11
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(livecd-x11)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description livecd-x11
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files livecd-x11
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-livecd-x11

%package -n openSUSE-release-livecd-gnome
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(livecd-gnome)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description livecd-gnome
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files livecd-gnome
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-livecd-gnome

%package -n openSUSE-release-livecd-xfce
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(livecd-xfce)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description livecd-xfce
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files livecd-xfce
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-livecd-xfce

%package -n openSUSE-release-usb-kde
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(usb-kde)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description usb-kde
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files usb-kde
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-usb-kde

%package -n openSUSE-release-usb-gnome
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(usb-gnome)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description usb-gnome
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files usb-gnome
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-usb-gnome

%package -n openSUSE-release-usb-x11
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(usb-x11)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description usb-x11
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files usb-x11
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-usb-x11

%package -n openSUSE-release-appliance
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(appliance)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description appliance
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files appliance
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-appliance

%package -n openSUSE-release-appliance-docker
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(appliance-docker)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description appliance-docker
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files appliance-docker
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-appliance-docker

%package -n openSUSE-release-appliance-kvm
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(appliance-kvm)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description appliance-kvm
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files appliance-kvm
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-appliance-kvm

%package -n openSUSE-release-appliance-vmware
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(appliance-vmware)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description appliance-vmware
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files appliance-vmware
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-appliance-vmware

%package -n openSUSE-release-appliance-openstack
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(appliance-openstack)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description appliance-openstack
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files appliance-openstack
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-appliance-openstack

%package -n openSUSE-release-appliance-hyperv
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(appliance-hyperv)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description appliance-hyperv
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files appliance-hyperv
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-appliance-hyperv

%package -n openSUSE-release-appliance-vagrant
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(appliance-vagrant)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description appliance-vagrant
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files appliance-vagrant
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-appliance-vagrant

%package -n openSUSE-release-appliance-wsl
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(appliance-wsl)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description appliance-wsl
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files appliance-wsl
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-appliance-wsl

%package -n openSUSE-release-appliance-custom
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(appliance-custom)
Provides:       product_flavor(openSUSE) = 20221123-0
Summary:        openSUSE Tumbleweed%{?betaversion: %{betaversion}}

%description appliance-custom
openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.

%files appliance-custom
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-release-appliance-custom



%prep
%setup -qcT
mkdir license
if [ -f /CD1/license.tar.gz ]; then
  tar -C license -xzf /CD1/license.tar.gz
elif [ -f %{_prefix}/lib/skelcd/CD1/license.tar.gz ]; then
  tar -C license -xzf %{_prefix}/lib/skelcd/CD1/license.tar.gz
fi

%build

%install
mkdir -p %{buildroot}%{_sysconfdir} %{buildroot}%{_prefix}/lib/issue.d %{buildroot}/run

echo -e 'Welcome to %{product} %{codename} %{version}%{?betaversion: %{betaversion}} - Kernel \\r (\\l).\n' > %{buildroot}%{_prefix}/lib/issue.d/10-openSUSE.conf
echo -e "\n" > %{buildroot}%{_prefix}/lib/issue.d/90-openSUSE.conf
echo    'Welcome to %{product} %{codename} %{version}%{?betaversion: %{betaversion}} - Kernel %%r (%%t).' > %{buildroot}%{_sysconfdir}/issue.net

VERSION_ID=`echo %{version}|tr '[:upper:]' '[:lower:]'|sed -e 's/ //g;'`
# note: VERSION is an optional field and has no meaning other than informative on a rolling distro
# We do thus not add it to the os-release file
cat > %{buildroot}%{_prefix}/lib/os-release <<EOF
NAME="openSUSE Tumbleweed"
# VERSION="%{version}%{?betaversion: %{betaversion}}"
ID="opensuse-tumbleweed"
ID_LIKE="opensuse suse"
VERSION_ID="$VERSION_ID"
PRETTY_NAME="openSUSE Tumbleweed"
ANSI_COLOR="0;32"
CPE_NAME="cpe:/o:opensuse:tumbleweed:%{version}"
BUG_REPORT_URL="https://bugs.opensuse.org"
HOME_URL="https://www.opensuse.org/"
DOCUMENTATION_URL="https://en.opensuse.org/Portal:Tumbleweed"
LOGO="distributor-logo-Tumbleweed"
EOF
ln -s ..%{_prefix}/lib/os-release %{buildroot}%{_sysconfdir}/os-release

mkdir -p %{buildroot}%{_prefix}/lib/motd.d/
echo "Have a lot of fun..." > %{buildroot}%{_prefix}/lib/motd.d/welcome
# Bug 404141 - /etc/YaST/control.xml should be owned by some package
mkdir -p %{buildroot}%{_sysconfdir}/YaST2/
echo %{buildroot}
if [ -f /CD1/control.xml ]; then
  install -m 644 /CD1/control.xml %{buildroot}%{_sysconfdir}/YaST2/
elif [ -f %{_prefix}/lib/skelcd/CD1/control.xml ]; then
  install -m 644 %{_prefix}/lib/skelcd/CD1/control.xml %{buildroot}%{_sysconfdir}/YaST2/
fi

# enable vendor change openSUSE,SUSE for DUP from 15.3 to TW (boo#1198332)
mkdir -p %{buildroot}%{_sysconfdir}/zypp/vendors.d
echo -e "[main]\nvendors=openSUSE,SUSE,SUSE LLC <https://www.suse.com/>\n" > %{buildroot}%{_sysconfdir}/zypp/vendors.d/00-openSUSE.conf


# fate#319341, make openSUSE-release own YaST license files. TODO:
# get rid of /etc/YaST2/licenses
install -D -d -m 755 "%{buildroot}%_defaultlicensedir/product/base"
install -D -d -m 755 "%{buildroot}%_defaultlicensedir"
cp -a license "%{buildroot}%_defaultlicensedir/%name"
pushd license
for i in *; do
	ln -s "%_defaultlicensedir/%name/$i" %{buildroot}%_defaultlicensedir/product/base/$i
done

mkdir -p %{buildroot}%{_sysconfdir}/products.d
cat >%{buildroot}%{_sysconfdir}/products.d/openSUSE.prod << EOF
<?xml version="1.0" encoding="UTF-8"?>
<product schemeversion="0">
  <vendor>openSUSE</vendor>
  <name>openSUSE</name>
  <version>20221123</version>
  <release>0</release>
  <arch>%{_target_cpu}</arch>
  <cpeid>cpe:/o:opensuse:opensuse:20221123</cpeid>
  <productline>openSUSE</productline>
  <register>
    <pool>
    </pool>
    <updates>
      <distrotarget arch="x86_64">openSUSE-Tumbleweed-x86_64</distrotarget>
      <distrotarget arch="s390x">openSUSE-Tumbleweed-s390x</distrotarget>
      <distrotarget arch="ppc64le">openSUSE-Tumbleweed-ppc64le</distrotarget>
      <distrotarget arch="aarch64">openSUSE-Tumbleweed-aarch64</distrotarget>
    </updates>
  </register>
  <repositories>
  </repositories>
  <updaterepokey>000000000</updaterepokey>
  <summary>openSUSE Tumbleweed</summary>
  <shortsummary>openSUSE</shortsummary>
  <description>openSUSE Tumbleweed is the rolling distribution by the openSUSE.org project.</description>
  <linguas>
    <language>cs</language>
    <language>da</language>
    <language>de</language>
    <language>el</language>
    <language>en</language>
    <language>en_GB</language>
    <language>en_US</language>
    <language>es</language>
    <language>fr</language>
    <language>hu</language>
    <language>it</language>
    <language>ja</language>
    <language>pl</language>
    <language>pt</language>
    <language>pt_BR</language>
    <language>ru</language>
    <language>zh</language>
    <language>zh_CN</language>
    <language>zh_TW</language>
  </linguas>
  <urls>
    <url name="releasenotes">http://doc.opensuse.org/release-notes/x86_64/openSUSE/Tumbleweed/release-notes-openSUSE.rpm</url>
    <url name="repository">http://download.opensuse.org/tumbleweed/repo/oss/</url>
  </urls>
  <buildconfig>
    <producttheme>openSUSE</producttheme>
    <create_flavors>true</create_flavors>
  </buildconfig>
  <installconfig>
    <defaultlang>en_US</defaultlang>
    <default_obs_repository_name>openSUSE_Tumbleweed</default_obs_repository_name>
    <default_obs_download_url>%{_download_url}</default_obs_download_url>
    <releasepackage name="openSUSE-release" flag="EQ" version="%{version}" release="%{release}"/>
    <distribution>openSUSE</distribution>
  </installconfig>
  <runtimeconfig/>
</product>

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-ftp
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-ftp/README << EOF
This package only exists for providing the product flavor 'ftp'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-mini
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-mini/README << EOF
This package only exists for providing the product flavor 'mini'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-dvd
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-dvd/README << EOF
This package only exists for providing the product flavor 'dvd'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-livecd-kde
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-livecd-kde/README << EOF
This package only exists for providing the product flavor 'livecd-kde'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-livecd-x11
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-livecd-x11/README << EOF
This package only exists for providing the product flavor 'livecd-x11'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-livecd-gnome
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-livecd-gnome/README << EOF
This package only exists for providing the product flavor 'livecd-gnome'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-livecd-xfce
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-livecd-xfce/README << EOF
This package only exists for providing the product flavor 'livecd-xfce'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-usb-kde
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-usb-kde/README << EOF
This package only exists for providing the product flavor 'usb-kde'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-usb-gnome
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-usb-gnome/README << EOF
This package only exists for providing the product flavor 'usb-gnome'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-usb-x11
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-usb-x11/README << EOF
This package only exists for providing the product flavor 'usb-x11'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-appliance
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-appliance/README << EOF
This package only exists for providing the product flavor 'appliance'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-docker
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-docker/README << EOF
This package only exists for providing the product flavor 'appliance-docker'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-kvm
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-kvm/README << EOF
This package only exists for providing the product flavor 'appliance-kvm'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-vmware
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-vmware/README << EOF
This package only exists for providing the product flavor 'appliance-vmware'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-openstack
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-openstack/README << EOF
This package only exists for providing the product flavor 'appliance-openstack'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-hyperv
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-hyperv/README << EOF
This package only exists for providing the product flavor 'appliance-hyperv'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-vagrant
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-vagrant/README << EOF
This package only exists for providing the product flavor 'appliance-vagrant'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-wsl
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-wsl/README << EOF
This package only exists for providing the product flavor 'appliance-wsl'.

EOF

mkdir -p %{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-custom
cat >%{buildroot}%{_defaultdocdir}/openSUSE-release-appliance-custom/README << EOF
This package only exists for providing the product flavor 'appliance-custom'.

EOF


# this is a base product, create symlink
ln -s openSUSE.prod %{buildroot}%{_sysconfdir}/products.d/baseproduct

%posttrans
# Launch the issue-generator: we have a new config file in /usr/lib/issue.d that needs to be represented
if [ -x %{_sbindir}/issue-generator ]; then
    if [ -x %{_bindir}/systemd-tmpfiles ]; then
      %{_bindir}/systemd-tmpfiles --create issue-generator.conf || :
    fi
    %{_sbindir}/issue-generator || :
fi

%files
%defattr(644,root,root,755)
%dir %_defaultlicensedir/product
%_defaultlicensedir/product/base
%license license/*
%{_sysconfdir}/os-release
%{_prefix}/lib/os-release
# Bug 404141 - /etc/YaST/control.xml should be owned by some package
%dir %{_sysconfdir}/YaST2/
%config %{_sysconfdir}/YaST2/control.xml
%config %{_sysconfdir}/zypp/vendors.d/00-openSUSE.conf
%{_prefix}/lib/motd.d/welcome
%dir %{_prefix}/lib/issue.d/
%{_prefix}/lib/issue.d/10-openSUSE.conf
%{_prefix}/lib/issue.d/90-openSUSE.conf
%config(noreplace) %{_sysconfdir}/issue.net
%{_sysconfdir}/products.d

%changelog
