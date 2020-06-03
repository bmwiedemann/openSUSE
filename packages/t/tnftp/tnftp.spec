#
# spec file for package tnftp
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


Name:           tnftp
Version:        20151004
Release:        0
Summary:        Enhanced FTP Client
License:        BSD-3-Clause
Group:          Productivity/Networking/Ftp/Clients
URL:            ftp://ftp.netbsd.org/pub/NetBSD/misc/tnftp/
Source0:        ftp://ftp.netbsd.org/pub/NetBSD/misc/tnftp/%{name}-%{version}.tar.gz
Source1:        ftp://ftp.netbsd.org/pub/NetBSD/misc/tnftp/%{name}-%{version}.tar.gz.asc
Source2:        tnftp.keyring
# PATCH-FIX-UPSTREAM: do not use bundled libedit
Patch0:         tnftp-20100108-am_and_libedit.patch
Patch1:         tnftp-verify_hostname.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libedit-devel
BuildRequires:  libopenssl-devel >= 1.1
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-alternatives
Requires(post): update-alternatives
Requires(postun): update-alternatives
Conflicts:      ftp
Provides:       lukemftp = 1.6
Provides:       nkitb:%{_bindir}/ftp
Obsoletes:      lukemftp <= 1.5
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
%{name} is the FTP (File Transfer Protocol) client from NetBSD.  FTP is a widely
used protocol for transferring files over the Internet and for archiving files.
%{name} provides some advanced features beyond the Linux netkit ftp client, but
maintains a similar user interface to the traditional ftp client.  It was
formerly called lukemftp.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
#axe bundled library
rm -rf libedit
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
%if 0%{?suse_version} <= 1310
touch %{buildroot}%{_sysconfdir}/alternatives/ftp
touch %{buildroot}%{_sysconfdir}/alternatives/ftp.1.gz
%endif
ln -sf %{_sysconfdir}/alternatives/ftp %{buildroot}%{_bindir}/ftp
ln -sf %{_sysconfdir}/alternatives/ftp.1.gz %{buildroot}%{_mandir}/man1/ftp.1.gz

%post
update-alternatives --install %{_bindir}/ftp ftp %{_bindir}/%{name} 10 \
  --slave %{_mandir}/man1/ftp.1.gz ftp.1 %{_mandir}/man1/%{name}.1.gz

%postun
if [ "$1" = 0 ] ; then
  update-alternatives --remove ftp %{_bindir}/%{name}
fi

%files
%defattr(-,root,root)
%doc COPYING ChangeLog NEWS README THANKS
%ghost %{_sysconfdir}/alternatives/ftp
%ghost %{_sysconfdir}/alternatives/ftp.1.gz
%{_bindir}/ftp
%{_mandir}/man1/ftp.1.gz
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog
