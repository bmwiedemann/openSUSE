#
# spec file for package yast2-aduc
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


Name:           yast2-aduc
Version:        2.2
Release:        0
Summary:        Active Directory Users and Computers for YaST
License:        GPL-3.0-only
Group:          Productivity/Networking/Samba
URL:            https://github.com/yast/yast2-aduc

Source:         %{name}-%{version}.tar.bz2

BuildRequires:  perl-XML-Writer
BuildRequires:  python3
BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools
BuildRequires:  yast2-testsuite
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)

Requires:       krb5-client
Requires:       samba-client
Requires:       samba-python3
Requires:       yast2
Requires:       yast2-adcommon-python >= 0.7
Requires:       yast2-python3-bindings >= 4.0.0

Provides:       yast-aduc = %{version}
Obsoletes:      yast-aduc < %{version}

BuildArch:      noarch

%description
The Active Directory Users and Computers for YaST module provides tools for
creating and modifying Users, Groups, and Computer objects in Active Directory.

%prep
%setup -q

%build

%install
%yast_install

%files
%{yast_clientdir}
%{yast_yncludedir}
%{yast_desktopdir}
%doc %{yast_docdir}
%license COPYING

%changelog
