#
# spec file for package ldapfuse
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ldapfuse
Version:        1.0
Release:        0
Summary:        Browse LDAP trees via filesystem
License:        GPL-3.0
Group:          System/Filesystems
Url:            http://ldapfuse.sf.net/

#Git-Clone:	git://ldapfuse.git.sf.net/gitroot/ldapfuse/ldapfuse
Source:         http://downloads.sf.net/ldapfuse/%name-%version.tar.xz
Source2:        http://downloads.sf.net/ldapfuse/%name-%version.tar.xz.asc
Source3:        %name.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  openldap2-devel >= 2.3
BuildRequires:  pkgconfig >= 0.19
BuildRequires:  xz
BuildRequires:  pkgconfig(fuse) >= 2.7
BuildRequires:  pkgconfig(libHX) >= 3.12

%description
A virtual filesystem for FUSE that allows to navigate an LDAP tree.

Author:
-------
	Jan Engelhardt

%prep
%setup -q

%build
if [ ! -e configure ]; then
	./autogen.sh;
fi;
%configure
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot";

%files
%defattr(-,root,root)
%_bindir/*
%doc %_mandir/*/*

%changelog
