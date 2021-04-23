#
# spec file for package yast2-nis-client
#
# Copyright (c) 2021 SUSE LLC
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


Name:           yast2-nis-client
Version:        4.4.1
Release:        0
Summary:        YaST2 - Network Information Services (NIS, YP) Configuration
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-nis-client
Source0:        %{name}-%{version}.tar.bz2
# SuSEfirewall2_* services merged into one service yast2-2.23.17
BuildRequires:  doxygen
BuildRequires:  gcc-c++
# Nsswitch#Write
BuildRequires:  libnsl-devel
BuildRequires:  libtirpc-devel
BuildRequires:  libtool
BuildRequires:  update-desktop-files
BuildRequires:  yast2 >= 2.23.17
BuildRequires:  yast2-core-devel
BuildRequires:  yast2-devtools >= 4.4.0
BuildRequires:  yast2-pam >= 4.3.0
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
# Wizard::SetDesktopTitleAndIcon
Requires:       yast2 >= 2.21.22
Requires:       yast2-network
# Fixed Nsswitch#WriteDb
Requires:       yast2-pam >= 4.3.2
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       yp-tools
Supplements:    autoyast(nis)
# .net.hostnames.rpc
Conflicts:      yast2-core < 2.8.0
Provides:       yast2-config-network:%{_prefix}/lib/YaST2/clients/lan_ypclient.ycp
Provides:       yast2-config-nis
Provides:       yast2-config-nis-devel
Provides:       yast2-trans-nis
Obsoletes:      yast2-config-nis
Obsoletes:      yast2-config-nis-devel
Obsoletes:      yast2-nis-client-devel-doc
Obsoletes:      yast2-trans-nis

%description
The YaST2 component for NIS configuration. NIS is a service similar to
yellow pages.

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

%files
%license COPYING
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_agentdir}
%{yast_plugindir}
%{yast_scrconfdir}
%{yast_schemadir}
%{yast_icondir}

%changelog
