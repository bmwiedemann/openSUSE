#
# spec file for package yast2-vpn
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


Name:           yast2-vpn
Version:        4.6.0
Release:        0
URL:            https://github.com/yast/yast-vpn
Source0:        %{name}-%{version}.tar.bz2
Summary:        A YaST module for configuring VPN gateway and clients
License:        GPL-2.0-only
Group:          System/YaST

# CFA::SysctlConfig
BuildRequires:  yast2 >= 4.2.67
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-ruby-bindings
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)

PreReq:         %fillup_prereq

# CFA::SysctlConfig
Requires:       yast2 >= 4.2.67
Requires:       yast2-ruby-bindings

Supplements:    autoyast(vpn)

BuildArch:      noarch

%description
A YaST module for managing VPN gateway and client connections to secure site-to-site communication via IPSec VPN.

%prep
%setup -q

%check
%yast_check

%build

%install
%yast_install
%yast_metainfo

%files
%doc %{yast_docdir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_moduledir}
%{yast_clientdir}
%{yast_schemadir}
%{yast_libdir}
%{yast_scrconfdir}
%{yast_icondir}

%changelog
