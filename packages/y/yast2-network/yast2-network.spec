#
# spec file for package yast2-network
#
# Copyright (c) 2020 SUSE LLC
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


Name:           yast2-network
Version:        4.3.26
Release:        0
Summary:        YaST2 - Network Configuration
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-network

Source0:        %{name}-%{version}.tar.bz2

# testsuite
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 3.1.15
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
#for install task
BuildRequires:  yast2-storage-ng
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)
# AutoYaST ElementPath class
BuildRequires:  yast2 >= 4.3.20

BuildRequires:  yast2-packager >= 4.0.18
# Product control need xml agent
BuildRequires:  yast2-xml
# cfa for parsing hosts
BuildRequires:  rubygem(%rb_default_ruby_abi:cfa) >= 0.6.4
# lenses are needed to use cfa
BuildRequires:  augeas-lenses

PreReq:         /bin/rm
#netconfig (FaTE #303618)
Requires:       sysconfig >= 0.80.0
Requires:       yast2-proxy
Requires:       yast2-storage-ng
# AutoYaST ElementPath class
Requires:       yast2 >= 4.3.20
# Packages::vnc_packages
Requires:       augeas-lenses
Requires:       yast2-packager >= 4.0.18
Requires:       rubygem(%rb_default_ruby_abi:cfa) >= 0.6.4
# BusID of all the cards with the same one (bsc#1007172)
Requires:       hostname
Requires:       hwinfo         >= 21.35
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       yast2-xml

# testsuite
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)

# carrier detection
Conflicts:      yast2-core < 2.10.6

# new calls in AutoinstGeneral
Conflicts:      autoyast2 < 4.3.23

Obsoletes:      yast2-network-devel-doc <= 3.1.154
Provides:       yast2-network-devel-doc = %{version}

Supplements:    autoyast(host:networking:remote)

BuildArch:      noarch

%build

%description
This package contains the YaST2 component for network configuration.

%prep
%setup -q

%check
%yast_check

%install
%yast_install
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_scrconfdir}
%{yast_agentdir}
%{yast_schemadir}
%{yast_libdir}
%{yast_ydatadir}
%{yast_icondir}
%{yast_metainfodir}
%license COPYING
%doc %{yast_docdir}

%changelog
