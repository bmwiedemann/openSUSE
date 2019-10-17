#
# spec file for package balsa
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


Name:           balsa
Version:        2.5.8
Release:        0
Summary:        The GNOME Mail Program
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Clients
URL:            https://pawsa.fedorapeople.org/balsa/
Source0:        %{url}/%{name}-%{version}.tar.bz2

BuildRequires:  compface-devel
BuildRequires:  fdupes
BuildRequires:  gpgme-devel
BuildRequires:  intltool
BuildRequires:  krb5-devel
BuildRequires:  libesmtp-devel
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-html2text
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gmime-2.6)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:  pkgconfig(gtksourceview-3.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

%description
An e-mail client for GNOME. It supports
* the local mailbox formats mbox, maildir and mh
* MIME support, nested mailboxes
* POP3 and IMAP mail access
* printing, spell checking
* address book with GnomeCard
* GPG/OpenPGP mail signing and encryption

%lang_package

%prep
%autosetup -p1

%build
%configure\
	--enable-more-warnings\
	--with-canberra\
	--with-ldap\
	--with-gpgme\
	--with-spell-checker=gspell\
	--with-gtksourceview\
	--with-sqlite\
	--with-rubrica\
	--with-gss\
	--with-compface\
	--with-html-widget=webkit2
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc README ChangeLog NEWS TODO AUTHORS HACKING
%doc docs/mh-mail-HOWTO docs/vconvert.awk docs/pine2vcard
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/*
%{_datadir}/applications/*.desktop
%{_datadir}/balsa/
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/balsa.appdata.xml
%{_datadir}/pixmaps/*.png
%{_datadir}/sounds/balsa
%{_mandir}/man1/balsa.1%{?ext_man}
%dir %{_sysconfdir}/sound
%dir %{_sysconfdir}/sound/events
%config %{_sysconfdir}/sound/events/*.soundlist

%files lang -f %{name}.lang

%changelog
