#
# spec file for package cardpeek
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cardpeek
Version:        0.8.4
Release:        0
Summary:        Tool To Read Contents of ISO7816 Smart Cards (Credit Cards, GSM SIM etc
License:        GPL-3.0
Group:          Productivity/Security
Url:            http://pannetrat.com/Cardpeek/
Source:         http://downloads.pannetrat.com/install/%{name}-%{version}.tar.gz
Patch0:         cardpeek-lua5.3.patch
# PATCH-FIX-UPSTREAM https://github.com/L1L1/cardpeek/pull/97
Patch1:         reproducible.patch
BuildRequires:  desktop-file-utils
BuildRequires:  hicolor-icon-theme
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpcsclite)
BuildRequires:  pkgconfig(lua)

%description
Cardpeek is a Linux tool to read the contents of ISO7816 smart cards.
It features a GTK GUI to represent card data is a tree view, and is
extendable with a scripting language (LUA).

The goal of this project is to allow smart card owners to be better
informed about what type of personal information is stored in these
devices.

The tool currently reads the contents of:
    * EMV cards
    * Calypso public transport cards (such as Navigo)
    * Moneo ePurse cards
    * Vitale 2 French health cards.
    * GSM cards (beta)

See %{_docdir}/cardpeek/cardpeek_ref.en.pdf for more details.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
  --docdir=%{_docdir}/%{name} \
  --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
# NEWS is empty
%doc AUTHORS COPYING ChangeLog README
%doc %{_defaultdocdir}/%{name}/cardpeek_ref.en.pdf
%{_mandir}/man1/cardpeek.1%{?ext_man}
%{_bindir}/cardpeek
%dir %{_datadir}/appdata
%{_datadir}/appdata/cardpeek.appdata.xml
%{_datadir}/applications/cardpeek.desktop
%{_datadir}/icons/hicolor/*/*/*.*

%changelog
