#
# spec file for package yast2-mail
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


Name:           yast2-mail
Version:        4.3.3
Release:        0
Summary:        YaST2 - Mail Configuration
License:        GPL-2.0-or-later
Group:          System/YaST
URL:            https://github.com/yast/yast-mail

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-testsuite

PreReq:         %fillup_prereq

# SuSEFirewall2 replaced by firewalld (fate#323460)
Requires:       yast2 >= 4.0.39
Requires:       yast2-ldap
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       yast2-users

Supplements:    autoyast(mail)

BuildArch:      noarch

%description
The YaST2 component for mail configuration. It handles Postfix, Cyrus,
Amavis and Fetchmail.

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

%post
%{fillup_only -n mail}

%files
%{yast_yncludedir}
%{yast_clientdir}
%{yast_moduledir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_schemadir}
%{yast_scrconfdir}
%{yast_agentdir}
%attr(0755,root,root) %{yast_agentdir}/setup_dkim_verifying.pl
%{_sysconfdir}/openldap/
%doc %{yast_docdir}
%license COPYING
%{yast_icondir}
%{_fillupdir}/sysconfig.mail

%changelog
