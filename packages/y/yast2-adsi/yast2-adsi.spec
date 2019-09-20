#
# spec file for package yast2-adsi
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-adsi
Version:        1.5
Release:        0
Summary:        Active Directory Compatible Service Interfaces Editor
License:        GPL-3.0-only
Group:          Productivity/Networking/Samba
Url:            https://github.com/yast/yast-adsi
Source:         %{name}-%{version}.tar.bz2

BuildRequires:  perl-XML-Writer
BuildRequires:  python3
BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools
BuildRequires:  yast2-testsuite
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)

Requires:       krb5-client
Requires:       python3-ldap
Requires:       samba-client
Requires:       samba-python3
Requires:       yast2
Requires:       yast2-adcommon-python >= 0.6
Requires:       yast2-python3-bindings >= 4.0.0

BuildArch:      noarch

%description
The ADSI Edit for YaST module provides tools for viewing and modifying
an LDAP tree.

%prep
%setup -q

%build

%install
%yast_install
%yast_metainfo

%files
%{yast_clientdir}
%{yast_yncludedir}
%{yast_desktopdir}
%{yast_metainfodir}
%license COPYING

%changelog
