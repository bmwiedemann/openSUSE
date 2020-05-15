#
# spec file for package yast2-kdump
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           yast2-kdump
Version:        4.3.0
Release:        0
Summary:        Configuration of kdump
License:        GPL-2.0-only
Group:          System/YaST
Url:            https://github.com/yast/yast-kdump

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)
# Wizard::SetDesktopTitleAndIcon
BuildRequires:  yast2 >= 2.21.22
BuildRequires:  yast2-bootloader
BuildRequires:  yast2-buildtools >= 4.2.2

Requires:       yast2
# Kernel parameters with multiple values and bug#945479 fixed
Requires:       yast2-bootloader >= 3.1.148
Requires:       yast2-ruby-bindings >= 1.0.0
# SpaceCalculation.GetPartitionInfo
Requires:       yast2-packager
# do not use old installation with wrong finish order

%ifarch ppc
Recommends:     kdump
%else
Requires:       kdump
%endif
Recommends:     makedumpfile

Conflicts:      yast2-installation < 3.1.198

Supplements:    (yast2 and kdump)

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
