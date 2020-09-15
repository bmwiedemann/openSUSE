#
# spec file for package yast2-installation
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


Name:           yast2-installation
Version:        4.3.17
Release:        0
Summary:        YaST2 - Installation Parts
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-installation

Source0:        %{name}-%{version}.tar.bz2
Source1:        YaST2-Second-Stage.service
Source2:        YaST2-Firstboot.service

BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 3.1.10
# for AbortException and handle direct abort
BuildRequires:  yast2-ruby-bindings >= 4.0.6
# needed for xml agent reading about products
BuildRequires:  yast2-xml
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)
# Yast::OSRelease.ReleaseVersionHumanReadable
BuildRequires:  yast2 >= 4.2.56
# Y2Packager::MediumType
BuildRequires:  yast2-packager >= 4.2.27
# CIOIgnore
BuildRequires:  yast2-bootloader
# using /usr/bin/udevadm
BuildRequires:  yast2-storage-ng >= 4.2.71
# Y2Network::NtpServer
BuildRequires:  yast2-network >= 4.2.55
# new root password cwm widget
BuildRequires:  yast2-users >= 3.2.8
# storage-ng based version
BuildRequires:  yast2-bootloader
BuildRequires:  yast2-country >= 3.3.1

PreReq:         %fillup_prereq
Requires:       yast2-country >= 3.3.1
Requires:       yast2-users >= 3.2.8
# tar-gzip some system files and untar-ungzip them after the installation (FATE #300421, #120103)
Requires:       coreutils
Requires:       gzip
Requires:       tar
# Augeas lenses
Requires:       augeas-lenses
# Only in inst-sys
Requires:       yast2-storage-ng >= 4.0.175
# Language::GetLanguageItems and other API
# Language::Set (handles downloading the translation extensions)
Requires:       yast2-country-data >= 2.16.11
# Pkg::ProvidePackage
Requires:       yast2-pkg-bindings >= 3.1.33
# Y2Packager::MediumType
Requires:       yast2-packager >= 4.2.22
# CIOIgnore
Requires:       yast2-bootloader
# use in startup scripts
Requires:       initviocons
# Proxy settings for 2nd stage (bnc#764951)
Requires:       yast2-proxy
# Systemd default target and services. This version supports
# writing settings in the first installation stage.
Requires:       yast2-services-manager >= 3.2.1
# UI::Wizards::Layout
Requires:       yast2 >= 4.3.16
# Y2Network::NtpServer
Requires:       yast2-network >= 4.2.55
# for AbortException and handle direct abort
Requires:       yast2-ruby-bindings >= 4.0.6
# for the first/second stage of installation
# currently not used
# bugzilla #208307
#Requires:      /usr/bin/jpegtopnm
#Requires:      /usr/bin/pnmtopng
# BNC 446533, /sbin/lspci called but not installed
Requires:       pciutils
# Needed call /sbin/ip in vnc.sh/network.sh
Requires:       iproute2
%if 0%{?suse_version} >= 1210
%{systemd_requires}
%endif

# SingleItemSelector not enforcing an initial selection
Conflicts:      libyui < 3.8.2
# Pkg::SourceProvideSignedFile Pkg::SourceProvideDigestedFile
# pkg-bindings are not directly required
Conflicts:      yast2-pkg-bindings < 2.17.25
# InstError
Conflicts:      yast2 < 2.18.6
# storage-ng based version
Conflicts:      yast2-bootloader < 3.3.1
# Added new function WFM::ClientExists
Conflicts:      yast2-core < 2.17.10
# Top bar with logo
Conflicts:      yast2-ycp-ui-bindings < 3.1.7
# Registration#get_updates_list does not handle exceptions
Conflicts:      yast2-registration < 3.2.3
# Mouse-related scripts moved to yast2-mouse
Conflicts:      yast2-mouse < 2.18.0
# new autoinst_files_finish call
Conflicts:      autoyast2 < 4.3.26

Obsoletes:      yast2-installation-devel-doc

Recommends:     yast2-online-update
Recommends:     yast2-firewall
Recommends:     yast2-add-on

Supplements:    autoyast(deploy_image:ssh_import)

BuildArch:      noarch

%description
System installation code as present on installation media.

%prep
%setup -q

%check
%yast_check

%build

%install
%yast_install
%yast_metainfo

for f in `find %{buildroot}%{_datadir}/autoinstall/modules -name "*.desktop"`; do
    %suse_update_desktop_file $f
done

mkdir -p %{buildroot}%{yast_vardir}/hooks/installation
mkdir -p %{buildroot}%{yast_ystartupdir}/startup/hooks/preFirstCall
mkdir -p %{buildroot}%{yast_ystartupdir}/startup/hooks/preSecondCall
mkdir -p %{buildroot}%{yast_ystartupdir}/startup/hooks/postFirstCall
mkdir -p %{buildroot}%{yast_ystartupdir}/startup/hooks/postSecondCall
mkdir -p %{buildroot}%{yast_ystartupdir}/startup/hooks/preFirstStage
mkdir -p %{buildroot}%{yast_ystartupdir}/startup/hooks/preSecondStage
mkdir -p %{buildroot}%{yast_ystartupdir}/startup/hooks/postFirstStage
mkdir -p %{buildroot}%{yast_ystartupdir}/startup/hooks/postSecondStage

mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}

%post
%{fillup_only -ns security checksig}

%if 0%{suse_version} > 1140

%service_add_post YaST2-Second-Stage.service YaST2-Firstboot.service

# bsc#924278 Always enable these services by default, they are already listed
# in systemd-presets-branding package, but that works for new installations
# only, it does not work for upgrades from SLE 11 where scripts had different
# name and were not handled by systemd.
# When we upgrade/update from systemd-based system, scripts are always enabled
# by the service_add_post macro.
systemctl enable YaST2-Second-Stage.service
systemctl enable YaST2-Firstboot.service

%pre
%service_add_pre YaST2-Second-Stage.service YaST2-Firstboot.service

%preun
%service_del_preun YaST2-Second-Stage.service YaST2-Firstboot.service

%postun
%service_del_postun YaST2-Second-Stage.service YaST2-Firstboot.service

#suse_version
%endif

%files

# systemd service files
%{_unitdir}
# yupdate script
%{_bindir}/
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{_datadir}/autoinstall/
%{yast_schemadir}
%{yast_yncludedir}
%{yast_libdir}
# agents
%{yast_scrconfdir}
# fillup
%{_fillupdir}/sysconfig.security-checksig
# programs and scripts
%{yast_ystartupdir}/startup
# installation hooks
%{yast_vardir}
%doc %{yast_docdir}
%license COPYING
%{yast_icondir}

%changelog
