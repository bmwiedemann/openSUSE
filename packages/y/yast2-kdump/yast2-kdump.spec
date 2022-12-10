#
# spec file for package yast2-kdump
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


Name:           yast2-kdump
Version:        4.5.7
Release:        0
Summary:        Configuration of kdump
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-kdump

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)
# Replace PackageSystem with Package
BuildRequires:  yast2 >= 4.4.38
BuildRequires:  yast2-bootloader
BuildRequires:  yast2-buildtools >= 4.2.2

# Replace PackageSystem with Package
Requires:       yast2 >= 4.4.38
# Kernel parameters with multiple values and bug#945479 fixed
Requires:       yast2-bootloader >= 3.1.148
Requires:       yast2-ruby-bindings >= 1.0.0
# SpaceCalculation.GetPartitionInfo
Requires:       yast2-packager
# do not use old installation with wrong finish order
Conflicts:      yast2-installation < 3.1.198

Supplements:    (yast2 and kdump)

Supplements:    autoyast(kdump)

%description
Configuration of kdump

%prep
%setup -q

%check
%yast_check

%build

%install
%yast_install
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_libdir}
%{yast_clientdir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_schemadir}
%{yast_scrconfdir}
%doc %{yast_docdir}
%{yast_icondir}
%license COPYING

%changelog
