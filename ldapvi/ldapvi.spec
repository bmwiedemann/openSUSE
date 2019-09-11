#
# spec file for package ldapvi
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


Name:           ldapvi
Version:        1.7
Release:        0.0
Summary:        An interactive LDAP editor for Unix terminals
License:        GPL-2.0-only
Group:          Productivity/Networking/LDAP/Utilities
Url:            http://www.lichteblau.com/ldapvi
Source:         http://www.lichteblau.com/download/ldapvi-%{version}.tar.gz
# PATCH-FIX-UPSTREAM GNUMakefile.in.patch
Patch0:         GNUMakefile.in.patch
# PATCH-FIX-UPSTREAM 0001-renamed-getline.patch
Patch1:         0001-renamed-getline.patch
# PATCH-FIX-UPSTREAM 0001-declare-some-void-functions-to-be-really-void.patch
Patch2:         0001-declare-some-void-functions-to-be-really-void.patch
# PATCH-FIX-UPSTREAM 0001-return-0-instead-of-nothing.patch
Patch3:         0001-return-0-instead-of-nothing.patch
# PATCH-FIX-UPSTREAM 0001-Improved-subprocess.patch
Patch4:         0001-Improved-subprocess.patch
# PATCH-FIX-UPSTREAM 0002-improved-subprocess-2.patch
Patch5:         0002-improved-subprocess-2.patch
Patch6:         0006-correct-gpl2-text.patch
# PATCH-FIX-UPSTREAM 0007-crypth.patch
Patch7:         0007-crypth.patch
BuildRequires:  cyrus-sasl-devel
BuildRequires:  libxslt
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(glib-2.0)
%if 0%{?suse_version}
BuildRequires:  openldap2-devel
%endif
%if 0%{?centos_version} || 0%{?fedora_version} || 0%{?rhel_version} || 0%{?mandriva_version}
BuildRequires:  openldap-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ldapvi is an interactive LDAP client for Unix terminals.
Using it, you can update LDAP entries with a text editor.
Think of it as vipw(1) for LDAP.

%prep
%setup -q
%patch0 -p0
%patch1 -p2
%patch2 -p2
%patch3 -p2
%patch4 -p2
%patch5 -p2
%patch6 -p1
%patch7 -p1

%build
%configure
make
cd manual
make manual.html

%install
%make_install

%files
%defattr(-, root, root, 0755)
%doc NEWS COPYING manual/manual.html manual/manual.css manual/bg.png
%{_bindir}/ldapvi
%{_mandir}/man1/ldapvi.1.gz

%changelog
