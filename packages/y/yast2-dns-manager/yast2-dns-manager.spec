#
# spec file for package yast2-dns-manager
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           yast2-dns-manager
Version:        0.1
Release:        0
Summary:        Samba Internal DNS Manager
License:        GPL-3.0-only
Group:          Productivity/Networking/Samba
Url:            http://www.github.com/yast/yast2-dns-manager
Source:         %{name}-%{version}.tar.bz2
BuildArch:      noarch
Requires:       krb5-client
Requires:       samba-client
Requires:       samba-python3
Requires:       yast2
Requires:       yast2-adcommon-python
Requires:       yast2-python3-bindings >= 4.0.0
BuildRequires:  perl-XML-Writer
BuildRequires:  python3
BuildRequires:  update-desktop-files
BuildRequires:  yast2
BuildRequires:  yast2-devtools
BuildRequires:  yast2-testsuite
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)

%description
DNS Manager for the Internal Samba Active Directory Domain Controller DNS server.

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
%{yast_moduledir}
%doc %{yast_docdir}
%license COPYING

%changelog
