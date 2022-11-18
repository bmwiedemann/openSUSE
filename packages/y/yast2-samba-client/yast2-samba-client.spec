#
# spec file for package yast2-samba-client
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


Name:           yast2-samba-client
Version:        4.5.2
Release:        0
Summary:        YaST2 - Samba Client Configuration
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-samba-client
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.4.0
BuildRequires:  yast2-pam
BuildRequires:  yast2-perl-bindings
Requires:       perl-XML-LibXML
# SuSEFirewall2 replaced by firewalld (fate#323460)
Requires:       yast2 >= 4.0.39
# Yast::Lan.yast_config
Requires:       yast2-network >= 4.2.0
# new Pam.ycp API
Requires:       yast2-pam >= 2.14.0
Requires:       yast2-python3-bindings >= 4.0.8
Requires:       yast2-ruby-bindings >= 1.0.0
Recommends:     samba-python3
Supplements:    autoyast(samba-client)
Conflicts:      yast2-kerberos-client < 3.1.2
BuildArch:      noarch

%description
This package contains the YaST2 component for configuration of an SMB
workgroup/domain and authentication against an SMB domain.

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
%{yast_scrconfdir}
%{yast_agentdir}
%{yast_schemadir}
%{yast_icondir}

%changelog
