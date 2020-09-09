#
# spec file for package yast2-schema
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


Name:           yast2-schema
Version:        4.3.6
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

URL:            https://github.com/yast/yast-schema

# Dependencies needed to build the package
BuildRequires:  jing
BuildRequires:  libxml2-tools
BuildRequires:  trang
BuildRequires:  yast2-devtools

# All packages providing RNG files for AutoYaST
# in /usr/share/YaST2/schema/autoyast/rng/*.rng

# proper validation of installed{,_version} elements in rules.xml
BuildRequires:  autoyast2 >= 4.3.43
BuildRequires:  yast2
# add_on_products and add_on_others types
BuildRequires:  yast2-add-on >= 4.3.3
BuildRequires:  yast2-audit-laf >= 4.3.0
BuildRequires:  yast2-auth-client >= 4.3.0
BuildRequires:  yast2-auth-server
# tag secure_boot
BuildRequires:  yast2-bootloader >= 4.3.0
BuildRequires:  yast2-configuration-management >= 4.3.0
BuildRequires:  yast2-country >= 4.3.0
BuildRequires:  yast2-dhcp-server >= 4.3.0
BuildRequires:  yast2-dns-server >= 4.3.0
BuildRequires:  yast2-firewall >= 4.3.0
BuildRequires:  yast2-firstboot >= 4.3.0
BuildRequires:  yast2-ftp-server >= 4.3.0
BuildRequires:  yast2-geo-cluster >= 4.3.0
BuildRequires:  yast2-http-server
BuildRequires:  yast2-installation
BuildRequires:  yast2-iscsi-client
BuildRequires:  yast2-kdump
BuildRequires:  yast2-mail
BuildRequires:  yast2-tftp-server >= 4.1.7
# setup_before_proposal element
BuildRequires:  yast2-network >= 4.3.10
BuildRequires:  yast2-nfs-client
BuildRequires:  yast2-nfs-server
BuildRequires:  yast2-nis-client
BuildRequires:  yast2-nis-server
BuildRequires:  yast2-ntp-client
BuildRequires:  yast2-online-update-configuration
BuildRequires:  yast2-printer
BuildRequires:  yast2-proxy
# registration is available only where suse connect is also available
%ifnarch s390 %ix86
# release_type element is not mandatory
BuildRequires:  yast2-registration >= 4.3.8
%endif
# Package available for S390 only
%ifarch s390 s390x
BuildRequires:  yast2-s390
%endif
BuildRequires:  yast2-samba-client
BuildRequires:  yast2-samba-server
# sys_gid_max, sys_gid_min, sys_uid_max,... in security.rnc
BuildRequires:  yast2-security >= 4.2.8
BuildRequires:  yast2-services-manager
BuildRequires:  yast2-sound
BuildRequires:  yast2-squid
BuildRequires:  yast2-sysconfig
# tag home_btrfs_subvolume
BuildRequires:  yast2-users >= 4.1.11

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

Summary:        YaST2 - AutoYaST Schema
License:        GPL-2.0-or-later
Group:          System/YaST

%description
AutoYaST Syntax Schema

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install

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
