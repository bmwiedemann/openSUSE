#
# spec file for package openSUSE-MicroOS-release.spec
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


Name:           openSUSE-MicroOS-release
Version:        20190930
Release:        0
Summary:        openSUSE MicroOS 
License:        GPL-2.0-or-later
Group:          System/Fhs
BuildRequires:  skelcd-openSUSE
Requires:       issue-generator
# Make sure we are at SLES12 SP2 level
PreReq:         glibc >= 2.19
# in rare cases, 'ln' is not found...
Requires(post): coreutils
Recommends:     branding-openSUSE
Recommends:     distribution-logos-openSUSE-MicroOS
Conflicts:      distribution-release
Conflicts:      kernel < 4.4
Provides:       distribution-release
# MicroOS-release replaces Tumbleweed-Kubic-release
Provides:       openSUSE-Tumbleweed-Kubic-release
Obsoletes:      openSUSE-Tumbleweed-Kubic-release <= 20190324
# With more than one product in the FTP tree, yast needs to know which products are installable
# The name is referenced by the control file as well
Provides:       system-installation() = openSUSE-MicroOS
# this package should only be available for the "basearchs" of a product
ExclusiveArch:  %ix86 x86_64 ppc64le s390x aarch64
Provides:       %name-%version
Provides:       product() = openSUSE-MicroOS
Provides:       product(openSUSE-MicroOS) = 20190930-0
Provides:       product-label() = openSUSE%20MicroOS
Provides:       product-cpeid() = cpe%3A%2Fo%3Aopensuse%3Aopensuse%2Dmicroos%3A20190930
Provides:       product-url(releasenotes) = http%3A%2F%2Fdoc.opensuse.org%2Frelease%2Dnotes%2Fx86_64%2FopenSUSE%2FTumbleweed%2Frelease%2Dnotes%2DopenSUSE.rpm
Provides:       product-endoflife()
Requires:       product_flavor(openSUSE-MicroOS)



%description
openSUSE MicroOS combines the benefits of a rolling OS with a read-only root filesystem with transactional updates. It is a modern Linux Operating System, designed for single-service installations, such as container hosts. It is optimized for large, clustered deployments.
        It inherits the benefits of openSUSE Tumbleweed while redefining the operating system into a small, efficient and reliable distribution.

%package dvd
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(dvd)
Provides:       product_flavor(openSUSE-MicroOS) = 20190930-0
Summary:        openSUSE MicroOS

%description dvd
openSUSE MicroOS combines the benefits of a rolling OS with a read-only root filesystem with transactional updates. It is a modern Linux Operating System, designed for single-service installations, such as container hosts. It is optimized for large, clustered deployments.
        It inherits the benefits of openSUSE Tumbleweed while redefining the operating system into a small, efficient and reliable distribution.

%files dvd
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-MicroOS-release-dvd

%package kubic-dvd
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(kubic-dvd)
Provides:       product_flavor(openSUSE-MicroOS) = 20190930-0
Summary:        openSUSE MicroOS

%description kubic-dvd
openSUSE MicroOS combines the benefits of a rolling OS with a read-only root filesystem with transactional updates. It is a modern Linux Operating System, designed for single-service installations, such as container hosts. It is optimized for large, clustered deployments.
        It inherits the benefits of openSUSE Tumbleweed while redefining the operating system into a small, efficient and reliable distribution.

%files kubic-dvd
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-MicroOS-release-kubic-dvd

%package appliance
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(appliance)
Provides:       product_flavor(openSUSE-MicroOS) = 20190930-0
Summary:        openSUSE MicroOS

%description appliance
openSUSE MicroOS combines the benefits of a rolling OS with a read-only root filesystem with transactional updates. It is a modern Linux Operating System, designed for single-service installations, such as container hosts. It is optimized for large, clustered deployments.
        It inherits the benefits of openSUSE Tumbleweed while redefining the operating system into a small, efficient and reliable distribution.

%files appliance
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-MicroOS-release-appliance

%package appliance-kubic
License:        BSD-3-Clause
Group:          System/Fhs
Provides:       product_flavor()
Provides:       flavor(appliance-kubic)
Provides:       product_flavor(openSUSE-MicroOS) = 20190930-0
Summary:        openSUSE MicroOS

%description appliance-kubic
openSUSE MicroOS combines the benefits of a rolling OS with a read-only root filesystem with transactional updates. It is a modern Linux Operating System, designed for single-service installations, such as container hosts. It is optimized for large, clustered deployments.
        It inherits the benefits of openSUSE Tumbleweed while redefining the operating system into a small, efficient and reliable distribution.

%files appliance-kubic
%defattr(-,root,root)
%doc %{_defaultdocdir}/openSUSE-MicroOS-release-appliance-kubic



%prep

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_libexecdir}/issue.d
echo -e "\nWelcome to openSUSE MicroOS (%{_target_cpu}) - Kernel \\\r (\\\l).\n" > %{buildroot}%{_libexecdir}/issue.d/10-OS
echo -e "\n" > %{buildroot}%{_libexecdir}/issue.d/90-OS

touch %{buildroot}%{_sysconfdir}/motd

# Put EULA into correct place
mkdir -p %{buildroot}/%{_sysconfdir}/YaST2/licenses/base
cd %{buildroot}/%{_sysconfdir}/YaST2/licenses/base
if [ -f /CD1/license.tar.gz ]; then
  tar -xzf /CD1/license.tar.gz
elif [ -f %{_libexecdir}/skelcd/CD1/license.tar.gz ]; then
  tar -xzf %{_libexecdir}/skelcd/CD1/license.tar.gz
fi

VERSION_ID=`echo %{version}|tr '[:upper:]' '[:lower:]'|sed -e 's/ //g;'`
# note: VERSION is an optional field and has no meaning other than informative on a rolling distro
# We do thus not add it to the os-release file
cat > %{buildroot}%{_libexecdir}/os-release <<EOF
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
LOGO="distributor-logo"
EOF
ln -s ..%{_libexecdir}/os-release %{buildroot}%{_sysconfdir}/os-release

mkdir -p $RPM_BUILD_ROOT/etc/products.d
cat >$RPM_BUILD_ROOT/etc/products.d/openSUSE-MicroOS.prod << EOF
<?xml version="1.0" encoding="UTF-8"?>
<product schemeversion="0">
  <vendor>openSUSE</vendor>
  <name>openSUSE-MicroOS</name>
  <version>20190930</version>
  <release>0</release>
  <endoflife></endoflife>
  <arch>%{_target_cpu}</arch>
  <cpeid>cpe:/o:opensuse:opensuse-microos:20190930</cpeid>
  <productline>openSUSE-MicroOS</productline>
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

mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/openSUSE-MicroOS-release-dvd
cat >$RPM_BUILD_ROOT/%{_defaultdocdir}/openSUSE-MicroOS-release-dvd/README << EOF
This package only exists for providing the product flavor 'dvd'.

EOF

mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/openSUSE-MicroOS-release-kubic-dvd
cat >$RPM_BUILD_ROOT/%{_defaultdocdir}/openSUSE-MicroOS-release-kubic-dvd/README << EOF
This package only exists for providing the product flavor 'kubic-dvd'.

EOF

mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/openSUSE-MicroOS-release-appliance
cat >$RPM_BUILD_ROOT/%{_defaultdocdir}/openSUSE-MicroOS-release-appliance/README << EOF
This package only exists for providing the product flavor 'appliance'.

EOF

mkdir -p $RPM_BUILD_ROOT/%{_defaultdocdir}/openSUSE-MicroOS-release-appliance-kubic
cat >$RPM_BUILD_ROOT/%{_defaultdocdir}/openSUSE-MicroOS-release-appliance-kubic/README << EOF
This package only exists for providing the product flavor 'appliance-kubic'.

EOF



%post
# Update from openSUSE-Tumbleweed-Kubic to openSUSE-MicroOS
# Fix the baseproduct symlink and make sure, it exists
if [ -L %{_sysconfdir}/products.d/baseproduct ] ; then
    PRODLINK=$(basename $(readlink -f %{_sysconfdir}/products.d/baseproduct))
    if [ "$PRODLINK"  == "openSUSE-Tumbleweed-Kubic.prod" ]; then
      rm -f %{_sysconfdir}/products.d/baseproduct
    fi
fi
if [ ! -e %{_sysconfdir}/products.d/baseproduct ]; then
    ln -sf openSUSE-MicroOS.prod %{_sysconfdir}/products.d/baseproduct
fi

%files
%defattr(644,root,root,755)
%{_sysconfdir}/os-release
%{_libexecdir}/os-release
%dir %{_sysconfdir}/products.d
%{_sysconfdir}/products.d/*
%dir %{_sysconfdir}/YaST2/
%config(noreplace) %{_sysconfdir}/motd
%dir %{_sysconfdir}/YaST2/licenses/
%dir %{_sysconfdir}/YaST2/licenses/base/
# no %doc here, or we will not install them
%{_sysconfdir}/YaST2/licenses/base/license*txt
%{_sysconfdir}/YaST2/licenses/base/no-acceptance-needed
%dir %{_libexecdir}/issue.d
%{_libexecdir}/issue.d/*-OS

%changelog
