#
# spec file for package sitecopy
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


Name:           sitecopy
BuildRequires:  fdupes
BuildRequires:  neon-devel
BuildRequires:  pkgconfig
Summary:        Local to Remote Website Synchronizer
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Utilities
Version:        0.16.6
Release:        0
Requires:       %{name}-lang = %{version}
URL:            http://www.manyfish.co.uk/sitecopy/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        http://www.lyra.org/sitecopy/sitecopy-%{version}.tar.bz2
Patch0:         sitecopy-support-neon-0.29.diff
Patch1:         06-sftpdriver.c-fix-for-new-openssh.patch
Patch2:         10-bts410703-preserve-storage-files-sigint.patch
Patch3:         30-bts320586-manpage-document-sftp.patch

%description
Sitecopy is useful for copying locally stored web sites to remote web
servers. The program will upload files which have changed locally to
the server and delete files from the server which have been removed
locally to keep the remote site synchronized with the local site, all
with a single command.	The aim is to remove the hassle of uploading
and deleting individual files using an FTP client. FTP, WebDAV, and
HTTP-based authoring servers are supported.

%lang_package
%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
# Forcibly prevent use of bundled neon/expat/gettext sources.
rm -r lib/neon/*.[ch] intl/*.[ch]

%build
%configure \
	--with-expat \
	--with-ssl
make %{?jobs:-j%jobs}

%install
OMG=`mktemp -u /tmp/$$.%{name}-install-tmp.XXXXXXXXXX`
make DESTDIR=$RPM_BUILD_ROOT docdir=$OMG pkgdatadir=$OMG install MANLANGS=
rm -rf examples
mkdir  examples
cp -avL doc/examplerc doc/update.sh examples
rm -rf "$RPM_BUILD_ROOT$OMG"
%find_lang %name
%fdupes $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/usr/bin/sitecopy
%doc BUGS NEWS COPYING README THANKS  TODO
%doc examples
%{_mandir}/man1/*

%files lang -f %{name}.lang

%changelog
