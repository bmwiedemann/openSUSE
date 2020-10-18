#
# spec file for package patterns-yast
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


%bcond_with betatest

Name:           patterns-yast

Version:        20191229
Release:        0
Summary:        Patterns for Installation (YaST)
License:        MIT
Group:          Metapackages
URL:            https://github.com/yast/patterns-yast
Source0:        %{name}-rpmlintrc
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the YaST patterns.

################################################################################

%package yast2_basis
%pattern_basetechnologies
Summary:        YaST Base Utilities
Group:          Metapackages
Provides:       pattern() = yast2_basis
Provides:       pattern-icon() = yast
Provides:       pattern-order() = 1220
Provides:       pattern-visible()

Requires:       libyui-ncurses-pkg
Requires:       yast2
Requires:       yast2-firewall
Requires:       yast2-packager
Requires:       yast2-theme

Recommends:     yast2-metapackage-handler

Suggests:       yast2-firstboot
Suggests:       yast2-snapper

# SLE only
%if !0%{?is_opensuse}
Requires:       yast2-registration
Recommends:     yast2-support
# yast2 clone_system is expected to be installed by default (sle-beta)
Recommends:     autoyast2-installation
%endif

%if 0%{?is_opensuse}
Requires:       yast2-alternatives
# bsc#1083398
Recommends:     yast2-vm
%endif

# Don't install update facilities on Tumbleweed
%if 0%{?sle_version}
Requires:       yast2-online-update
Requires:       yast2-online-update-frontend
Requires:       yast2-update
Suggests:       yast2-online-update-configuration
%endif

%description yast2_basis
YaST tools for basic system administration.

%files yast2_basis
%dir %{_docdir}/patterns
%{_docdir}/patterns/yast2_basis.txt

################################################################################

%package yast2_desktop
%pattern_basetechnologies
Summary:        YaST Desktop Utilities
Group:          Metapackages
Provides:       pattern() = yast2_desktop
Provides:       pattern-icon() = yast
Provides:       pattern-order() = 1222
Provides:       pattern-visible()

Requires:       yast2-country
# Included for the release notes client
Requires:       yast2-installation
Requires:       yast2-services-manager
Requires:       yast2-sysconfig
Requires:       yast2-users

Recommends:     yast2-fonts
Recommends:     yast2-journal
Recommends:     yast2-printer
Recommends:     yast2-scanner

%description yast2_desktop
YaST tools for desktop system administration.

%files yast2_desktop
%dir %{_docdir}/patterns
%{_docdir}/patterns/yast2_desktop.txt

################################################################################

%package yast2_server
%pattern_basetechnologies
Summary:        YaST Server Utilities
Group:          Metapackages
Provides:       pattern() = yast2_server
Provides:       pattern-icon() = yast
Provides:       pattern-order() = 1224
Provides:       pattern-visible()

# Included for the release notes client
Requires:       yast2-installation
Requires:       yast2-ldap
Requires:       yast2-mail
# Useless on desktop, since NM is the default there
Requires:       yast2-network
Requires:       yast2-security
Requires:       yast2-services-manager
Requires:       yast2-sysconfig
Requires:       yast2-transfer
Requires:       yast2-tune
Requires:       yast2-users

Recommends:     yast2-auth-client
Recommends:     yast2-auth-server
Recommends:     yast2-iscsi-client
Recommends:     yast2-journal
Recommends:     yast2-ldap-client
Recommends:     yast2-nfs-client
Recommends:     yast2-nis-client
Recommends:     yast2-ntp-client
# see the discussion in #386473
Recommends:     yast2-samba-client
Recommends:     yast2-samba-server
Recommends:     yast2-slp
Recommends:     yast2-sudo
Recommends:     yast2-tftp-server
# #542936
Recommends:     yast2-vpn

Suggests:       autoyast2
Suggests:       yast2-drbd
Suggests:       yast2-multipath
# #381365
Suggests:       yast2-squid

%description yast2_server
YaST tools for server system administration.

%files yast2_server
%dir %{_docdir}/patterns
%{_docdir}/patterns/yast2_server.txt

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
%dir %{_docdir}/patterns
%{_docdir}/patterns/yast2_install_wf.txt

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

%description x11_yast
Graphical YaST user interfaces for minimal X desktop.

%files x11_yast
%dir %{_docdir}/patterns
%{_docdir}/patterns/x11_yast.txt

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
%dir %{_docdir}/patterns
%{_docdir}/patterns/devel_yast.txt

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}%{_docdir}/patterns/
echo 'This file marks the pattern yast2_basis to be installed.' > %{buildroot}%{_docdir}/patterns/yast2_basis.txt
echo 'This file marks the pattern yast2_desktop to be installed.' > %{buildroot}%{_docdir}/patterns/yast2_desktop.txt
echo 'This file marks the pattern yast2_server to be installed.' > %{buildroot}%{_docdir}/patterns/yast2_server.txt
echo 'This file marks the pattern yast2_install_wf to be installed.' > %{buildroot}%{_docdir}/patterns/yast2_install_wf.txt
echo 'This file marks the pattern x11_yast to be installed.' > %{buildroot}%{_docdir}/patterns/x11_yast.txt
echo 'This file marks the pattern devel_yast to be installed.' > %{buildroot}%{_docdir}/patterns/devel_yast.txt

%changelog
