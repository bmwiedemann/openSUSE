#
# spec file for package yast2-configuration-management
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


Name:           yast2-configuration-management
Version:        4.5.1
Release:        0
URL:            https://github.com/yast/yast-migration
Summary:        YaST2 - YaST Configuration Management
License:        GPL-2.0-only
Group:          System/YaST

Source0:        %{name}-%{version}.tar.bz2

# CWM DateField and TimeField widgets
BuildRequires:  update-desktop-files
BuildRequires:  yast2 >= 4.1.53
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-installation
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)

# CWM DateField and TimeField widgets
Requires:       yast2 => 4.1.53
Requires:       yast2-installation

Supplements:    autoyast(configuration-management)

BuildArch:      noarch

%description
This package contains the YaST2 component for Configuration Management Provisioning.

%prep
%setup -q

%check
%yast_check

%build

%install
%yast_install
%yast_metainfo

%files
%{yast_clientdir}
%{yast_libdir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_schemadir}
%{yast_icondir}
%doc %{yast_docdir}
%license COPYING

%changelog
