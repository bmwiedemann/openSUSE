#
# spec file for package skelcd-control-openSUSE-promo
#
# Copyright (c) 2022 SUSE LLC
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


######################################################################
#
# IMPORTANT: Please do not change the control file or this spec file
#   in build service directly, use
#   https://github.com/yast/skelcd-control-openSUSE repository
#
#   See https://github.com/yast/.github/blob/master/CONTRIBUTING.md
#   for more details.
#
######################################################################
Name:           skelcd-control-openSUSE-promo
Version:        20221212
Release:        0
Summary:        The openSUSE Installation Control file
License:        MIT
Group:          Metapackages
URL:            https://github.com/yast/skelcd-control-openSUSE
Source:         skelcd-control-openSUSE-%{version}.tar.bz2
# we do not distribute it, but need to have it here, otherwise build service checks complain
Source99:       README.md
# xmllint
BuildRequires:  libxml2-tools
# xsltproc
BuildRequires:  libxslt-tools
# Added 'lsm' section (jsc#SLE-22069)
BuildRequires:  yast2-installation-control >= 4.4.7
######################################################################
#
# Here is the list of Yast packages which are needed in the
# installation system (inst-sys) for the Yast installer
#
# Generic Yast packages needed for the installer
#
######################################################################
Requires:       autoyast2
Requires:       yast2-add-on
Requires:       yast2-fcoe-client
# For creating the AutoYast profile at the end of installation (bnc#887406)
Requires:       yast2-firewall
# instsys_cleanup
Requires:       yast2-installation >= 3.1.201
Requires:       yast2-iscsi-client
%ifnarch %{arm}
Requires:       yast2-kdump
# yast2-kdump has only runtime dependency but the package is also needed in the inst-sys
Requires:       kdump
%endif
Requires:       yast2-multipath
Requires:       yast2-network >= 3.1.24
Requires:       yast2-nfs-client
Requires:       yast2-ntp-client
Requires:       yast2-proxy
# this is the default theme
Requires:       yast2-qt-branding-openSUSE
Requires:       yast2-configuration-management
Requires:       yast2-services-manager
Requires:       yast2-slp
Requires:       yast2-theme
Requires:       yast2-trans-stats
Requires:       yast2-tune
Requires:       yast2-update
Requires:       yast2-users
Requires:       yast2-x11
# Ruby debugger in the inst-sys (FATE#318421)
Requires:       rubygem(%{rb_default_ruby_abi}:byebug)

Conflicts:      product_control
Provides:       product_control
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Architecture specific packages
%ifarch s390 s390x
Requires:       yast2-reipl >= 3.1.4
Requires:       yast2-s390
%endif

%ifarch %ix86 x86_64
Requires:       yast2-vm
%endif

# Release notes should be part of the installation media (bsc#1167866)
Requires:       release-notes

%if 0%{?suse_version} >= 1500 && !0%{?skelcd_compat}
%define skelcdpath /usr/lib/skelcd
%endif

%description
This package contains the control file used for openSUSE installation.

%prep

%setup -q -n skelcd-control-openSUSE-%{version}

%build
make %{?_smp_mflags} -C control

%check
make %{?_smp_mflags} -C control check

%install
#
# Add control file
#
%if "%{name}" == "skelcd-control-openSUSE-promo"
    CONTROL_FILE=control.openSUSE-promo.xml
%else
    CONTROL_FILE=control.openSUSE.xml
%endif

mkdir -p $RPM_BUILD_ROOT%{?skelcdpath}/CD1
install -m 644 control/${CONTROL_FILE} $RPM_BUILD_ROOT%{?skelcdpath}/CD1/control.xml

%define update_repo 0
%if 0%{?sle_version} <= 150200
# With Tumbleweed and Leap 15.2 and before, aarch64 arm ppc ppc64 ppc64le riscv64 s390x are separated from regular Leap repo.
%ifarch aarch64 %arm %ix86 ppc ppc64 ppc64le riscv64 s390x
%define update_repo 1
%endif
%endif
%if 0%{?sle_version} >= 150300
# With Leap 15.3 and later, armv7 is the only archs separated, others (aarch64, etc.) are in the same repo.
%ifarch %arm
%define update_repo 1
%endif
%endif

%if "%{update_repo}" == "1"
    ports_arch="%{_arch}"
    %ifarch %ix86
        ports_arch="i586"
    %endif
    %ifarch ppc ppc64 ppc64le
        ports_arch="ppc"
    %endif
    %ifarch armv6l armv6hl
        ports_arch="armv6hl"
    %endif
    %ifarch armv7l armv7hl
        ports_arch="armv7hl"
    %endif
    %ifarch riscv64
        ports_arch="riscv"
    %endif
    %ifarch s390x
        ports_arch="zsystems"
    %endif
    sed -i -e "s,http://download.opensuse.org/distribution/,http://download.opensuse.org/ports/$ports_arch/distribution/," %{buildroot}%{?skelcdpath}/CD1/control.xml
    sed -i -e "s,http://download.opensuse.org/tumbleweed/,http://download.opensuse.org/ports/$ports_arch/tumbleweed/," %{buildroot}%{?skelcdpath}/CD1/control.xml
    # Leap debug repo (from :Update) has a different path since all 'ports' (ARM and PPC) are in the same repo
    sed -i -e "s,http://download.opensuse.org/debug/update,http://download.opensuse.org/ports/debug/update," %{buildroot}%{?skelcdpath}/CD1/control.xml
    sed -i -e "s,http://download.opensuse.org/debug/,http://download.opensuse.org/ports/$ports_arch/debug/," %{buildroot}%{?skelcdpath}/CD1/control.xml
    sed -i -e "s,http://download.opensuse.org/source/,http://download.opensuse.org/ports/$ports_arch/source/," %{buildroot}%{?skelcdpath}/CD1/control.xml
    sed -i -e "s,http://download.opensuse.org/update/leap/,http://download.opensuse.org/ports/update/leap/," %{buildroot}%{?skelcdpath}/CD1/control.xml
    sed -i -e "s,http://download.opensuse.org/update/tumbleweed/,http://download.opensuse.org/ports/$ports_arch/update/tumbleweed/," %{buildroot}%{?skelcdpath}/CD1/control.xml
    # Update external link
    sed -i -e "s,https://download.opensuse.org/YaST/Repos/openSUSE_Factory_Servers.xml,https://download.opensuse.org/YaST/Repos/openSUSE_$ports_arch\_Factory_Servers.xml," %{buildroot}%{?skelcdpath}/CD1/control.xml
    sed -i -e "s,https://download.opensuse.org/YaST/Repos/openSUSE_Leap_,https://download.opensuse.org/YaST/Repos/openSUSE_$ports_arch\_Leap_," %{buildroot}%{?skelcdpath}/CD1/control.xml
    #we parse out non existing non-oss repo for ports
    xsltproc -o %{buildroot}%{?skelcdpath}/CD1/control_ports.xml control/nonoss.xsl %{buildroot}%{?skelcdpath}/CD1/control.xml
    mv %{buildroot}%{?skelcdpath}/CD1/control{_ports,}.xml
    xmllint --noout --relaxng %{_datadir}/YaST2/control/control.rng %{buildroot}%{?skelcdpath}/CD1/control.xml
%endif

%files
%defattr(644,root,root,755)
%if %{defined skelcdpath}
%dir %{skelcdpath}
%endif
%dir %{?skelcdpath}/CD1
%{?skelcdpath}/CD1/control.xml

%changelog
