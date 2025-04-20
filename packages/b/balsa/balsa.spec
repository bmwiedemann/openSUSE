#
# spec file for package balsa
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


Name:           balsa
Version:        2.6.5
Release:        0
Summary:        The GNOME Mail Program
License:        GPL-2.0-or-later
URL:            https://gitlab.gnome.org/GNOME/balsa
Source0:        %{name}-%{version}.tar.zst

BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gpgme)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(webkit2gtk-4.1)

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
%meson \
	%{nil}
%meson_build

%install
%meson_install

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc README.md ChangeLog NEWS TODO AUTHORS HACKING
%doc docs/mh-mail-HOWTO docs/vconvert.awk docs/pine2vcard
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
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libhtmlfilter.so

%files lang -f %{name}.lang

%changelog
