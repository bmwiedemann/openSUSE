#
# spec file for package patterns-yast
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%bcond_with betatest

Name:           patterns-yast

Version:        20190411
Release:        0
Summary:        Patterns for Installation (Yast)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the Yast patterns.

################################################################################

%package yast2_basis
%pattern_basetechnologies
Summary:        YaST System Administration
Group:          Metapackages
Provides:       pattern() = yast2_basis
Provides:       pattern-icon() = yast
Provides:       pattern-order() = 1220
Provides:       pattern-visible()

Requires:       libyui-ncurses-pkg
Requires:       yast2
%if 0%{?is_opensuse}
# opensuse only, see bsc#1125040
Requires:       yast2-alternatives
%endif
Requires:       yast2-country
Requires:       yast2-firewall
Requires:       yast2-hardware-detection
Requires:       yast2-installation
Requires:       yast2-ldap
Requires:       yast2-mail
Requires:       yast2-network
Requires:       yast2-online-update
Requires:       yast2-online-update-frontend
Requires:       yast2-packager
Requires:       yast2-pam
Requires:       yast2-perl-bindings
Requires:       yast2-pkg-bindings
%if !0%{?is_opensuse}
# SLE only
Requires:       yast2-registration
%endif
Requires:       yast2-security
Requires:       yast2-services-manager
Requires:       yast2-storage-ng
Requires:       yast2-sysconfig
Requires:       yast2-transfer
Requires:       yast2-tune
Requires:       yast2-update
Requires:       yast2-users
Requires:       yast2-xml
Recommends:     yast2-auth-client
Recommends:     yast2-auth-server
Recommends:     yast2-iscsi-client
Recommends:     yast2-journal
Recommends:     yast2-ldap-client
Recommends:     yast2-metapackage-handler
Recommends:     yast2-nfs-client
Recommends:     yast2-nis-client
Recommends:     yast2-ntp-client
Recommends:     yast2-printer
Recommends:     yast2-slp
Recommends:     yast2-sudo
Recommends:     yast2-support
# see the discussion in #386473
Recommends:     yast2-samba-client
Recommends:     yast2-samba-server
Recommends:     yast2-tftp-server
# #542936
Recommends:     yast2-vpn
# Recommend Chrony at least until boo#936378 is fixed and YaST is not trying to configure a service that's not there
Recommends:     chrony
Suggests:       yast2-online-update-configuration
Suggests:       autoyast2
# yast2 clone_system is expected to be installed by default (sle-beta)
Recommends:     autoyast2-installation
Suggests:       libyui-qt-pkg
Suggests:       libyui-gtk-pkg
Suggests:       yast2-drbd
Suggests:       yast2-firstboot
Suggests:       yast2-multipath
Suggests:       yast2-snapper
# #381365
Suggests:       yast2-squid
# themeing for hardcore KDE lovers
Suggests:       yast2-theme-oxygen
# see extra-packages for reasons
Suggests:       sbl
Suggests:       Mesa
Suggests:       i4l-isdnlog
Suggests:       ypserv
Suggests:       install-initrd
# for yast2-scanner
# mandatory
Suggests:       sane-backends
# optionally
Suggests:       hplip
# optionally, open source, derived from iscan
Suggests:       iscan-free
# yast2-sound
Suggests:       alsa-firmware
Suggests:       alsa-tools
# yast2-printer - printing via novell ipx
Suggests:       ncpfs
Suggests:       kernel-kdump
Suggests:       sssd
Suggests:       snapper
# FATE 304350
Suggests:       sblim-sfcb
Suggests:       cim-schema
Requires:       yast2-theme
# bsc#1083398
%if 0%{?is_opensuse}
Recommends:     yast2-vm
%endif

%description yast2_basis
YaST tools for basic system administration.

%files yast2_basis
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/yast2_basis.txt

################################################################################

%package yast2_install_wf
%pattern_basetechnologies
Summary:        YaST Installation Packages
Group:          Metapackages
Provides:       pattern() = yast2_install_wf
Provides:       pattern-icon() = yast
Provides:       pattern-order() = 1240

Requires:       libyui-ncurses-pkg
Requires:       yast2-installation
Requires:       yast2-network
Requires:       yast2-users
# bnc#535101
Requires:       yast2-bootloader
# required to write ntp.conf (bnc#723018)
Requires:       yast2-ntp-client
Suggests:       autoyast2-installation
Suggests:       yast2-firewall
Suggests:       yast2-ldap
Suggests:       yast2-ldap-client
Suggests:       yast2-nfs-client
Suggests:       yast2-nis-client
Suggests:       yast2-printer
Suggests:       yast2-samba-client
Suggests:       yast2-slp
Suggests:       yast2-update
Suggests:       autoyast2
%ifarch x86_64
Suggests:       samba-client-32bit
Suggests:       samba-winbind-32bit
%endif
%ifarch ppc64
Suggests:       pam_fp-64bit
Suggests:       pam_krb5-64bit
Suggests:       nss_ldap-64bit
Suggests:       pam_ldap-64bit
Suggests:       samba-client-64bit
Suggests:       samba-winbind-64bit
%endif
Suggests:       tgt

%description yast2_install_wf
YaST tools for installing your system.

%files yast2_install_wf
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/yast2_install_wf.txt

################################################################################

%package x11_yast
%pattern_basetechnologies
Summary:        YaST User Interfaces
Group:          Metapackages
Provides:       pattern() = x11_yast
Provides:       pattern-extends() = yast2_basis
Provides:       pattern-icon() = pattern-generic
Provides:       pattern-order() = 1320
# from data/X11-YaST
Recommends:     libyui-qt-pkg
Recommends:     yast2-control-center-qt
# yast modules for the desktop
Recommends:     yast2-scanner
Recommends:     yast2-fonts

%description x11_yast
Graphical YaST user interfaces for minimal X desktop.

%files x11_yast
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/x11_yast.txt

################################################################################

%package devel_yast
%pattern_development
Summary:        YaST Development
Group:          Metapackages
Provides:       pattern() = devel_yast
Provides:       pattern-icon() = pattern-yast-devel
Provides:       pattern-order() = 3460
Provides:       pattern-visible()

Recommends:     yast2-devtools
Recommends:     yast2-testsuite
Recommends:     osc
Recommends:     rubygem(%{rb_default_ruby_abi}:yast-rake)
Recommends:     rubygem(%{rb_default_ruby_abi}:byebug)
Recommends:     rubygem(%{rb_default_ruby_abi}:parallel_tests)
Recommends:     rubygem(%{rb_default_ruby_abi}:rspec)
Recommends:     rubygem(%{rb_default_ruby_abi}:simplecov)
Recommends:     rubygem(%{rb_default_ruby_abi}:yard)
# only in OBS YaST:Head, but install it when available
# YaST currently requires version 0.41.2
Recommends:     rubygem(%{rb_default_ruby_abi}:rubocop) = 0.41.2
Suggests:       yast2-ycp-ui-bindings-devel
# Bug 304645 gives the list below:
Recommends:     yast2-core-devel
Recommends:     yast2-perl-bindings
Recommends:     yast2-ruby-bindings
Recommends:     git
Recommends:     libzypp-devel
Recommends:     yast2-libyui-devel
Recommends:     libyui-qt-devel
Recommends:     libyui-ncurses-devel

%description devel_yast
Tools and libraries for developing YaST modules, the setup and configuration tool for openSUSE.

%files devel_yast
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/devel_yast.txt

################################################################################

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/
echo 'This file marks the pattern yast2_basis to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/yast2_basis.txt
echo 'This file marks the pattern yast2_install_wf to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/yast2_install_wf.txt
echo 'This file marks the pattern x11_yast to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/x11_yast.txt
echo 'This file marks the pattern devel_yast to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/devel_yast.txt

%changelog
