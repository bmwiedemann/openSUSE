#
# spec file for package yast2-samba-server
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


Name:           yast2-samba-server
Version:        4.6.0
Release:        0
URL:            https://github.com/yast/yast-samba-server
Summary:        YaST2 - Samba Server Configuration
Group:          System/YaST
License:        GPL-2.0-only

Source0:        %{name}-%{version}.tar.bz2

# Service.Active
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  perl-Crypt-SmbHash
BuildRequires:  perl-X500-DN
BuildRequires:  update-desktop-files
# Yast2::ServiceWidget
BuildRequires:  yast2 >= 4.1.0
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-ldap
BuildRequires:  yast2-perl-bindings
BuildRequires:  yast2-users

# Test suite
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)
BuildRequires:  rubygem(%{rb_default_ruby_abi}:rspec)

Requires:       perl-Crypt-SmbHash
# Yast2::ServiceWidget
Requires:       yast2 >= 4.1.0
Requires:       yast2-ldap >= 3.1.2
Requires:       yast2-network
Requires:       yast2-perl-bindings
# samba-client/routines.rb
Requires:       yast2-samba-client >= 3.1.15
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       yast2-users

# bnc #386473, recommend yast2-samba-server when installaing these packages
Supplements:    samba

Supplements:    autoyast(samba-server)

BuildArch:      noarch

%description
This package contains the YaST2 component for Samba server
configuration.

%prep
%setup -q

%check
rake test:unit

%build
%yast_build

%install
%yast_install
%yast_metainfo

%files
%{yast_yncludedir}
%{yast_ydatadir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_schemadir}
%{yast_icondir}
%doc %{yast_docdir}
%license COPYING

%changelog
