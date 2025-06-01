#
# spec file for package tnftp
#
# Copyright (c) 2025 SUSE LLC
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


Name:           tnftp
Version:        20230507
Release:        0
Summary:        Enhanced FTP Client
License:        BSD-3-Clause
Group:          Productivity/Networking/Ftp/Clients
URL:            https://ftp.netbsd.org/pub/NetBSD/misc/tnftp/
Source0:        https://ftp.netbsd.org/pub/NetBSD/misc/tnftp/%{name}-%{version}.tar.gz
Source1:        https://ftp.netbsd.org/pub/NetBSD/misc/tnftp/%{name}-%{version}.tar.gz.asc
Source2:        tnftp.keyring
BuildRequires:  libopenssl-devel >= 1.1
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(ncurses)
Requires(post): update-alternatives
Conflicts:      ftp
Provides:       lukemftp = 1.6
Provides:       nkitb:%{_bindir}/ftp
Obsoletes:      lukemftp <= 1.5

%description
%{name} is the FTP (File Transfer Protocol) client from NetBSD.  FTP is a widely
used protocol for transferring files over the Internet and for archiving files.
%{name} provides some advanced features beyond the Linux netkit ftp client, but
maintains a similar user interface to the traditional ftp client.  It was
formerly called lukemftp.

%prep
%setup -q

%build
%configure \
  --enable-editcomplete \
  --without-local-libedit
#axe bundled library
rm -rf libedit
%make_build

%install
%make_install
ln -sf %{_bindir}/%{name} %{buildroot}%{_bindir}/ftp
ln -sf %{_mandir}/man1/ftp.1%{?ext_man} %{buildroot}%{_mandir}/man1/ftp.1%{?ext_man}

%post
if [ "$1" = 0 ] ; then
  update-alternatives --remove ftp %{_bindir}/%{name}
fi

%files
%license COPYING
%doc ChangeLog NEWS README THANKS
%{_bindir}/ftp
%{_mandir}/man1/ftp.1%{?ext_man}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
