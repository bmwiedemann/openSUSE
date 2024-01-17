#
# spec file for package ncftp
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


Name:           ncftp
Version:        3.2.6
Release:        0
Summary:        A Comfortable FTP Program
License:        ClArtistic
Group:          Productivity/Networking/Ftp/Clients
URL:            https://www.ncftp.com/
Source:         ftp://ftp.ncftp.com/ncftp/%{name}-%{version}-src.tar.xz
Patch0:         ncftp-3.1.8-locale.diff
Patch2:         ncftp-3.1.8-implicit_decl.diff
Patch3:         ncftp-3.2.5-no-date.patch
# PATCH-FIX-OPENSUSE make build reproducible (boo#1084909)
Patch4:         ncftp-3.2.6-no-uname.patch
Patch5:         ncftp-gcc10-gBm.patch
BuildRequires:  dos2unix
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This program has been in service on UNIX systems since 1991 and is a
popular alternative to the standard FTP program, %{_bindir}/ftp. NcFTP
offers many ease-of-use and performance enhancements over the stock FTP
client and runs on a wide variety of UNIX platforms as well as
operating systems like Microsoft Windows and Apple Mac OS X.

%prep
%setup -q
%patch0 -p1
%patch2
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
export CFLAGS="%{optflags} -D_LARGEFILE64_SOURCE"
%configure \
  --enable-ssp
make %{?_smp_mflags} STRIP=/bin/touch

%install
dos2unix doc/*.txt
make DESTDIR=%{buildroot} install %{?_smp_mflags} STRIP=/bin/touch

%files
%defattr(-,root,root)
%doc *.txt
%doc doc/*.txt
%doc doc/html
%{_bindir}/ncftp
%{_bindir}/ncftpbatch
%{_bindir}/ncftpbookmarks
%{_bindir}/ncftpget
%{_bindir}/ncftpls
%{_bindir}/ncftpput
%{_bindir}/ncftpspooler
%{_mandir}/man1/ncftp.1*
%{_mandir}/man1/ncftpbatch.1*
%{_mandir}/man1/ncftpget.1*
%{_mandir}/man1/ncftpls.1*
%{_mandir}/man1/ncftpput.1*
%{_mandir}/man1/ncftpspooler.1*

%changelog
