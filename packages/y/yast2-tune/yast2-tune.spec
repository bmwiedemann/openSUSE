#
# spec file for package yast2-tune
#
# Copyright (c) 2023 SUSE LLC
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


Name:           yast2-tune
Version:        4.6.0
Release:        0
Summary:        YaST2 - Hardware Tuning
License:        GPL-2.0-or-later
Group:          System/YaST
URL:            https://github.com/yast/yast-tune
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  update-desktop-files
# CFA::SysctlConfig
BuildRequires:  yast2 >= 4.2.67
BuildRequires:  yast2-devtools >= 4.4.0
# # CFA::SysctlConfig
Requires:       yast2 >= 4.2.67
Requires:       yast2-bootloader
Requires:       yast2-ruby-bindings >= 1.0.0

%description
This package contains the YaST2 component for hardware configuration.

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

%post
# rename the config file to the new modprobe schema
if test -e %{_sysconfdir}/modprobe.d/newid; then
    mv -f %{_sysconfdir}/modprobe.d/newid %{_sysconfdir}/modprobe.d/50-newid.conf
fi

%files
%license COPYING
%{yast_yncludedir}
%{yast_clientdir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_moduledir}
%{yast_libdir}
%{yast_scrconfdir}
%{yast_icondir}

%changelog
