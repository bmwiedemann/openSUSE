#
# spec file for package yast2-users
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


Name:           yast2-users
Version:        4.5.3
Release:        0
Summary:        YaST2 - User and Group Configuration
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-users

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  cracklib-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  perl-Digest-SHA1
BuildRequires:  update-desktop-files
# Y2Issues::WithIssues mixin
BuildRequires:  yast2 >= 4.4.18
BuildRequires:  yast2-core-devel
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-perl-bindings
BuildRequires:  yast2-security
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)

Requires:       cracklib
Requires:       perl-Digest-SHA1
Requires:       perl-X500-DN
Requires:       perl-gettext
Requires:       yast2-country

# CFA::Nsswitch
Requires:       yast2-pam >= 4.3.0

# Security::SafeRead
Requires:       yast2-security >= 4.4.1

# y2usernote, y2useritem
Requires:       yast2-perl-bindings >= 2.18.0

# this forces using yast2-ldap with correct LDAP object names (fate#303596)
Requires:       yast2-ldap >= 3.1.2

# Y2Issues::WithIssues mixin
Requires:       yast2 >= 4.4.18
# cryptsha256, cryptsha516
Requires:       yast2-core >= 2.21.0

Requires:       yast2-ruby-bindings >= 1.0.0
Obsoletes:      yast2-users-devel-doc
Conflicts:      autoyast2 < 3.1.92
# older storage uses removed deprecated method, see https://github.com/yast/yast-storage/pull/187
Conflicts:      yast2-storage < 3.1.75

Supplements:    autoyast(users:groups:user_defaults:login_settings)

%description
This package provides GUI for maintenance of linux users and groups.

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

%files
%{yast_clientdir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_moduledir}
%{yast_yncludedir}
%{yast_libdir}
%{yast_schemadir}
#agents:
%{yast_scrconfdir}
%{yast_agentdir}
%{yast_plugindir}
%{yast_icondir}
%license COPYING
%doc README.md

%changelog
