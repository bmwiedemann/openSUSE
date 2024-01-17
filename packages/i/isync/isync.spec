#
# spec file for package isync
#
# Copyright (c) 2023 SUSE LLC
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


Name:           isync
Version:        1.4.4
Release:        0
Summary:        Utility to synchronize IMAP mailboxes with local maildir folders
License:        GPL-2.0-only
URL:            https://isync.sourceforge.io/
Source:         https://prdownloads.sourceforge.net/isync/%{name}-%{version}.tar.gz
Source1:        https://prdownloads.sourceforge.net/isync/%{name}-%{version}.tar.gz.asc
# gpg2 --recv-keys 106457B8735659A4D40F56456F5447F95D001D85
# gpg2 --export --armour oswald.buddenhagen@gmx.de > isync.keyring
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM  work-around-unexpected-EOF-error-messages-at-end-of-SSL-connections.patch boo#1208166 yfjiang@suse.com -- handle the unexpected EOF error message at the end of ssl connection
Patch0:         work-around-unexpected-EOF-error-messages-at-end-of-SSL-connections.patch
BuildRequires:  db-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libsasl2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
isync is a command line application which synchronizes mailboxes; currently
Maildir and IMAP4 mailboxes are supported. New messages, message deletions
and flag changes can be propagated both ways. isync is suitable for use in
IMAP-disconnected mode.

Synchronization is based on unique message identifiers (UIDs), so no
identification conflicts can occur (as opposed to some other mail
synchronizers). Synchronization state is kept in one local text file per
mailbox pair; multiple replicas of a mailbox can be maintained.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install docdir=%{_docdir}/%{name}

%files
%license COPYING
%doc README AUTHORS ChangeLog NEWS
%{_bindir}/mbsync-get-cert
%{_bindir}/mbsync
%{_bindir}/mdconvert
%exclude %{_docdir}/%{name}/TODO
%{_docdir}/%{name}/examples/*
%dir %{_docdir}/%{name}/examples
%{_mandir}/man1/mbsync.1%{?ext_man}
%{_mandir}/man1/mdconvert.1%{?ext_man}

%changelog
