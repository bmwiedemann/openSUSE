#
# spec file for package skelcd-control-MicroOS
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
#   https://github.com/yast/skelcd-control-MicroOS repository
#
#   See https://github.com/yast/.github/blob/master/CONTRIBUTING.md
#   for more details.
#
######################################################################

Name:           skelcd-control-MicroOS
# xmllint (for validation)
BuildRequires:  libxml2-tools
# RNG validation schema
BuildRequires:  yast2-installation-control >= 4.4.3

# xsltproc - for building control.TWMicroOS.xml from control.MicroOS.xml
BuildRequires:  libxslt-tools
BuildRequires:  diffutils
# we need to copy some parts from the openSUSE control.xml to MicroOS
BuildRequires:  skelcd-control-openSUSE

######################################################################
#
# Here is the list of Yast packages which are needed in the
# installation system (inst-sys) for the Yast installer
#

# branding
Requires:       yast2-theme
Requires:       yast2-qt-branding-openSUSE

# Generic Yast packages needed for the installer
Requires:       autoyast2
Requires:       yast2-add-on
Requires:       yast2-buildtools
Requires:       yast2-caasp >= 4.2.1
Requires:       yast2-devtools
Requires:       yast2-fcoe-client
# For creating the AutoYast profile at the end of installation (bnc#887406)
Requires:       yast2-firewall
# instsys_cleanup
Requires:       yast2-installation >= 3.1.217.9
Requires:       yast2-iscsi-client
%ifnarch %{arm}
Requires:       yast2-kdump
# yast2-kdump has only runtime dependency but the package is also needed in the inst-sys
Requires:       kdump
%endif
Requires:       yast2-multipath
Requires:       yast2-network >= 3.1.42
Requires:       yast2-nfs-client
Requires:       yast2-ntp-client
Requires:       yast2-proxy
Requires:       yast2-services-manager
Requires:       yast2-slp
Requires:       yast2-trans-stats
Requires:       yast2-tune
Requires:       yast2-update
Requires:       yast2-users
Requires:       yast2-x11
# Ruby debugger in the inst-sys (FATE#318421)
Requires:       rubygem(%{rb_default_ruby_abi}:byebug)
# Install and enable xrdp by default (FATE#320363)
Requires:       yast2-rdp

# Ensure no two skelcd-control-* packages can be installed in the same time,
# an OBS check reports a file conflict for the /CD1/control.xml file from
# the other packages.
Conflicts:      product_control
Provides:       product_control

# we really do not need the YaST packages for building, ignore the dependencies
# to have faster builds and less rebuilds triggered by dependencies
# these are pulled in by the skelcd-control-openSUSE dependencies
#!BuildIgnore: yast2-caasp yast2-branding-openSUSE yast2-qt-branding-openSUSE
#!BuildIgnore: autoyast2 yast2-add-on yast2-buildtools yast2-devtools
#!BuildIgnore: yast2-fcoe-client yast2-firewall
#!BuildIgnore: yast2-installation yast2-iscsi-client yast2-kdump yast2-multipath
#!BuildIgnore: yast2-network yast2-nfs-client yast2-ntp-client yast2-proxy
#!BuildIgnore: yast2-services-manager yast2-slp yast2-trans-stats yast2-tune
#!BuildIgnore: yast2-update yast2-users yast2-x11 yast2-rdp
#!BuildIgnore: yast2-reipl yast2-s390 yast2-vm
#!BuildIgnore: rubygem(%{rb_default_ruby_abi}:byebug)
#!BuildIgnore: yast2-branding-openSUSE-Oxygen yast2-configuration-management
#!BuildIgnore: yast2-core yast2-hardware-detection yast2-installation-control
#!BuildIgnore: yast2-logs yast2-perl-bindings yast2-pkg-bindings yast2-ruby-bindings
#!BuildIgnore: yast2 yast2-ycp-ui-bindings

# Architecture specific packages
#
%ifarch s390 s390x
Requires:       yast2-reipl >= 3.1.4
Requires:       yast2-s390
%endif

%ifarch %ix86 x86_64
Requires:       yast2-vm
%endif

#
######################################################################

URL:            https://github.com/yast/skelcd-control-MicroOS
AutoReqProv:    off
Version:        20221205
Release:        0
Summary:        The MicroOS control file needed for installation
License:        MIT
Group:          Metapackages
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         %{name}-%{version}.tar.bz2

%if 0%{?suse_version} >= 1500 && !0%{?skelcd_compat}
%define skelcdpath /usr/lib/skelcd
%endif

%description
The package contains the MicroOS control file needed for installation.

%prep

%setup -n %{name}-%{version}

%build
# build control.TWMicroOS.xml from control.MicroOS.xml
make -C control control.TWMicroOS.xml
# display the changes (just for easier debugging)
# don't fail, a difference is expected
diff -u control/control.MicroOS.xml control/control.TWMicroOS.xml || :

%check
#
# Verify syntax
#
make -C control check

%install
#
# Add control file
#
mkdir -p %{buildroot}/%{?skelcdpath}/CD1
install -m 644 control/control.TWMicroOS.xml %{buildroot}/%{?skelcdpath}/CD1/control.xml

# install LICENSE (required by build service check)
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}
install -m 644 LICENSE %{buildroot}/%{_defaultdocdir}/%{name}

%files
%defattr(644,root,root,755)
%if %{defined skelcdpath}
%dir %{skelcdpath}
%endif
%dir %{?skelcdpath}/CD1
%{?skelcdpath}/CD1/control.xml
%doc %dir %{_defaultdocdir}/%{name}
%license %{_defaultdocdir}/%{name}/LICENSE

%changelog
