#
# spec file for package nfacct
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


Name:           nfacct
Version:        1.0.2
Release:        0
Summary:        Netfilter Extended Accounting utility
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://netfilter.org/projects/nfacct/

#Git-Web:	http://git.netfilter.org/
#Git-Clone:	git://git.netfilter.org/nfacct
Source:         ftp://ftp.netfilter.org/pub/nfacct/%name-%version.tar.bz2
Source2:        ftp://ftp.netfilter.org/pub/nfacct/%name-%version.tar.bz2.sig
Source3:        %name.keyring
BuildRequires:  pkgconfig(libmnl) >= 1.0.0
BuildRequires:  pkgconfig(libnetfilter_acct) >= 1.0.3

%description
This utility allows you to manipulate the extended accounting
infrastructure.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%_sbindir/nfacct
%_mandir/man*/nfacct*

%changelog
