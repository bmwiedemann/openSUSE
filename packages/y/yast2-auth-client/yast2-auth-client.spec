#
# spec file for package yast2-auth-client
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


Name:           yast2-auth-client
Version:        4.6.0
Release:        0
URL:            https://github.com/yast/yast-auth-client
Summary:        YaST2 - Centralised System Authentication Configuration
License:        GPL-2.0-only
Group:          System/YaST

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  doxygen
BuildRequires:  perl-XML-Writer
BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-network
BuildRequires:  yast2-pam
BuildRequires:  yast2-testsuite
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)

PreReq:         %fillup_prereq
Requires:       net-tools
Requires:       yast2
Requires:       yast2 >= 2.21.22
Requires:       yast2-pam >= 2.20.0
Requires:       yast2-ruby-bindings >= 1.0.0

Obsoletes:      yast2-kerberos-client
Obsoletes:      yast2-ldap-client

Supplements:    autoyast(auth-client)

BuildArch:      noarch

%description
With this YaST2 module you may configure centralised system authentication, on a single or multipe network domains.

%prep
%setup -q

%build

%install
%yast_install
%yast_metainfo

%files
%doc %{yast_docdir}
%{yast_libdir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_clientdir}
%{yast_scrconfdir}
%{yast_schemadir}
%{yast_icondir}
%license COPYING

%changelog
