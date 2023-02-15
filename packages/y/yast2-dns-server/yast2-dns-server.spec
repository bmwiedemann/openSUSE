#
# spec file for package yast2-dns-server
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


Name:           yast2-dns-server
Version:        4.5.0
Release:        0
URL:            https://github.com/yast/yast-dns-server
Summary:        YaST2 - DNS Server Configuration
License:        GPL-2.0-only
Group:          System/YaST

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  perl-XML-Writer
BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-ldap >= 3.1.4
BuildRequires:  yast2-perl-bindings
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)
# Yast2::ServiceWidget
BuildRequires:  yast2 >= 4.2.11

Requires:       /usr/bin/host
Requires:       perl-gettext
# Exporter Data::Dumper
Requires:       perl-base
# Time
Requires:       bind-utils
Requires:       perl
Requires:       yast2-perl-bindings
# Ldap module and agents
Requires:       yast2-ldap >= 3.1.4
# /sbin/ip
Requires:       iproute2
# DnsServerUI::CurrentlyUsedIPs
Requires:       grep
Requires:       sed
# Script /sbin/netconfig 0.71.2+?
# FATE #303386: Network setup tools
Requires:       yast2-sysconfig
# Yast2::ServiceWidget
Requires:       yast2 >= 4.1.0
Requires:       yast2-ruby-bindings >= 1.0.0

Supplements:    autoyast(dns-server)

BuildArch:      noarch

%description
This package contains the YaST2 component for DNS server configuration.

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_libdir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_scrconfdir}
%{yast_agentdir}
%{yast_schemadir}
%doc %{yast_docdir}
%{yast_icondir}
%license COPYING

%changelog
