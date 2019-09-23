#
# spec file for package yast2-registration
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


Name:           yast2-registration
Version:        4.2.7
Release:        0
Summary:        YaST2 - Registration Module
License:        GPL-2.0-only
Group:          System/YaST
Url:            https://github.com/yast/yast-registration

Source0:        %{name}-%{version}.tar.bz2

# Y2Packager::ProductLicense
BuildRequires:  update-desktop-files
BuildRequires:  yast2 >= 4.0.63
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-slp >= 3.1.9
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:suse-connect) >= 0.3.11
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake) >= 0.2.5
# updated product renames
BuildRequires:  yast2-packager >= 4.0.40
BuildRequires:  yast2-update >= 3.1.36

# Y2Packager::ProductLicense
Requires:       yast2 >= 4.0.63
# "dupAllowVendorChange" option in Pkg.SetSolverFlags()
Requires:       yast2-pkg-bindings >= 3.1.34
# N_() method
Requires:       yast2-ruby-bindings >= 3.1.12
# SUSE::Connect::YaST.list_installer_updates
Requires:       rubygem(%{rb_default_ruby_abi}:suse-connect) >= 0.2.37
# NOTE: Workaround for bsc#947482, SUSEConnect is actually not needed by the
# YaST registration module, it is used just to install the Connect dependencies.
#
# TODO: Remove it once the SUSEConnect dependencies are properly moved to the
# suse-connect gem.
Requires:       SUSEConnect >= 0.2.37
Requires:       yast2-add-on >= 3.1.8
Requires:       yast2-slp >= 3.1.9
# Packager ProductLicense#HandleLicenseDialogRet allowing "refuse" action
Requires:       yast2-packager >= 4.2.16
Requires:       yast2-update >= 3.1.36

BuildArch:      noarch
# SUSEConnect does not build for i586 and s390 and is not supported on those architectures
# bsc#1088552
ExcludeArch:    %ix86 s390

%description
The registration module to register products and/or to fetch an update
source (mirror) automatically.

%prep
%setup -q

%build

%check
%yast_check

%install
%yast_install
%yast_metainfo

%files
%{yast_ybindir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_clientdir}
%{yast_ydatadir}
%{yast_schemadir}
%{yast_libdir}
%{yast_icondir}
%doc %{yast_docdir}
%license COPYING

%changelog
