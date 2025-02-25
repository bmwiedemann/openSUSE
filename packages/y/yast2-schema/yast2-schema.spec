#
# spec file for package yast2-schema
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


%global flavor @BUILD_FLAVOR@%nil

%if "%flavor" == ""
Name:           yast2-schema
%else
Name:           yast2-schema-%{flavor}
%endif

Version:        5.0.2
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        yast2-schema-%{version}.tar.bz2

Group:          System/YaST
License:        GPL-2.0-or-later
URL:            https://github.com/yast/yast-schema

Provides:       yast2-schema = %{version}
# others cannot be used as it contains same files
Conflicts:      yast2-schema
Obsoletes:      yast2-schema < 4.4.9

# Dependencies needed to build the package
BuildRequires:  jing
BuildRequires:  libxml2-tools
BuildRequires:  trang
BuildRequires:  yast2-devtools

# All packages providing RNG files for AutoYaST
# in /usr/share/YaST2/schema/autoyast/rng/*.rng

# pervasive APQNS and key type elements in the partitioning schema
BuildRequires:  autoyast2 >= 5.0.4
BuildRequires:  yast2
# add_on_products and add_on_others types
BuildRequires:  yast2-add-on >= 4.3.3
# set 't' element in 'initrd_module' element
BuildRequires:  yast2-bootloader >= 4.3.12
BuildRequires:  yast2-configuration-management >= 4.3.0
BuildRequires:  yast2-country >= 4.3.0
# Added fcoe-client schema
BuildRequires:  yast2-fcoe-client >= 4.4.2
BuildRequires:  yast2-kdump
# add route 'extrapara' element
BuildRequires:  yast2-network >= 4.5.4

# registration is available only where suse connect is also available
%ifnarch s390 %ix86
# addons: architecture/version is optional
BuildRequires:  yast2-registration >= 4.3.12
%endif

# Add support for security policies ('security_policy')
BuildRequires:  yast2-security >= 4.5.3
BuildRequires:  yast2-services-manager
# tag home_btrfs_subvolume
BuildRequires:  yast2-users >= 4.1.11

# flavor specific dependencies
%if "%flavor" != "micro"
BuildRequires:  yast2-audit-laf >= 4.3.0
BuildRequires:  yast2-auth-client >= 4.3.0
BuildRequires:  yast2-auth-server
# YaST DNS server package and modules depending on it is dropped from TW
# (bsc#1205363)
%if 0%{?sle_version}
BuildRequires:  yast2-dhcp-server >= 4.3.0
# allow 'zone' instead of 'listentry'
BuildRequires:  yast2-dns-server >= 4.3.3
BuildRequires:  yast2-firewall >= 4.3.0
BuildRequires:  yast2-firstboot >= 4.3.0
BuildRequires:  yast2-ftp-server >= 4.3.0
BuildRequires:  yast2-geo-cluster >= 4.3.0
BuildRequires:  yast2-http-server
BuildRequires:  yast2-installation
BuildRequires:  yast2-tftp-server >= 4.1.7
# add 'iface' element
BuildRequires:  yast2-iscsi-client >= 4.3.3
BuildRequires:  yast2-mail >= 4.3.3
BuildRequires:  yast2-nfs-client
BuildRequires:  yast2-nfs-server
# YaST NIS packages are dropped from TW (bsc#1183893)
%if 0%{?sle_version}
BuildRequires:  yast2-nis-client
BuildRequires:  yast2-nis-server
%endif
BuildRequires:  yast2-ntp-client
# nested category_filter (bsc#1198848)
BuildRequires:  yast2-online-update-configuration >= 4.5.1
BuildRequires:  yast2-printer
BuildRequires:  yast2-proxy
# Package available for S390 only
%ifarch s390 s390x
BuildRequires:  yast2-s390
%endif
BuildRequires:  yast2-samba-client
BuildRequires:  yast2-samba-server
# YaST sound packages are dropped from TW (bsc#1206903)
%if 0%{?sle_version}
BuildRequires:  yast2-sound
%endif
BuildRequires:  yast2-squid
BuildRequires:  yast2-sysconfig
%endif
%endif

#!BuildIgnore: yast2-build-test

# optimization suggested by AJ:
#!BuildIgnore: tomcat5

# ignoring conflicting packages
#!BuildIgnore: yast2-branding-SLED yast2-branding-openSUSE
#!BuildIgnore: yast2-theme yast2-theme-SLED yast2-theme-openSUSE yast2-theme-SLE

# Hotfix to build a package, bnc #427684
#!BuildIgnore: xerces-j2-bootstrap libusb-0_1-4 crimson

# To speedup && to easily recover from dependency hell
#!BuildIgnore: yast2-pkg-bindings zypper libzypp yast2-gtk yast2-qt yast2-ncurses yast2-qt-pkg yast2-ncurses-pkg

# Yast packages without AutoYast support
#!BuildIgnore: yast2-country-data
#!BuildIgnore: yast2-control-center yast2-control-center-gnome yast2-control-center-qt

%if "%flavor" != ""
Summary:        YaST2 - AutoYaST Schema (%flavor variant)

%description
AutoYaST Syntax Schema (%flavor variant)
%else
Summary:        YaST2 - AutoYaST Schema

%description
AutoYaST Syntax Schema
%endif

%prep
%setup -n yast2-schema-%{version}

%build
%yast_build

%install
%yast_install

%if "%flavor" != ""
# rename the doc dir according to the current flavor
mv %{buildroot}/%{_docdir}/yast2-schema %{buildroot}/%{_docdir}/%{name}
%endif

%files
%defattr(-,root,root)
%dir %{yast_schemadir}/autoyast/rnc
%{yast_schemadir}/autoyast/rnc/profile.rnc
%{yast_schemadir}/autoyast/rnc/includes.rnc
%dir %{yast_schemadir}/autoyast/rng
%{yast_schemadir}/autoyast/rng/*.rng
%doc %{yast_docdir}
%license COPYING

%changelog
