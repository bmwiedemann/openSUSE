#
# spec file for package yast2-printer
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


Name:           yast2-printer
Version:        4.6.0
Release:        0
Summary:        YaST2 - Printer Configuration
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-printer
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-libX11-devel
BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.4.0
Requires:       %{_bindir}/sed
Requires:       /bin/mktemp
Requires:       yast2 >= 3.1.183
Requires:       yast2-ruby-bindings >= 1.0.0
Recommends:     cups-client
Recommends:     iptables
Recommends:     netcat
Recommends:     samba-client
Supplements:    autoyast(printer)
Obsoletes:      yast2-printer-devel-doc

# Exclude libX11 from the requires list which is pulled in by Autoreqprov
# because of the basicadd_displaytest tool
%global __requires_exclude_from basicadd_displaytest

%description
This package contains the YaST2 component for printer configuration.

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

%files
%license COPYING
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_moduledir}
%{yast_clientdir}
%{yast_yncludedir}
%{yast_schemadir}
%{yast_ydatadir}
%{yast_ybindir}
%{yast_icondir}

%changelog
