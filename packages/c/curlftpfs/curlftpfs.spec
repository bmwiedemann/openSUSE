#
# spec file for package curlftpfs
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           curlftpfs
Version:        0.9.2
Release:        0
Summary:        Filesystem for mounting FTP hosts using FUSE and libcurl
License:        GPL-2.0+
Group:          System/Filesystems
Url:            http://curlftpfs.sourceforge.net/
Source:         %{name}-%{version}.tar.bz2
Patch:          bug-580609.patch
Patch1:         curlftpfs-needs-pthread
Patch2:         bug-955687.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  curl-devel
BuildRequires:  fuse-devel
BuildRequires:  glib2-devel
BuildRequires:  libtool
Requires:       fuse

%description
CurlFtpFS is a filesystem for mount yast2-ftp-server (FTP hosts) based
on fuse (FUSE) and libcurl. Important features are:

- openssl (SSL support),

- connecting through squid (tunneling HTTP proxies)

- automatic reconnect on server timeout.



Authors:
--------
    Robson Braga Araujo <robsonbraga@gmail.com>

%prep
%setup -q
%patch
%patch1 -p1
%patch2

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%{makeinstall}

%files
%defattr (-, root, root)
%{_bindir}/curlftpfs
%{_mandir}/*/%{name}.*

%changelog
