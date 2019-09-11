#
# spec file for package seahorse-sharing
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           seahorse-sharing
Version:        3.8.0
Release:        0
Summary:        Sharing of PGP public keys via DNS-SD and HKP
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            http://projects.gnome.org/seahorse/
Source:         http://download.gnome.org/sources/seahorse-sharing/3.8/%{name}-%{version}.tar.xz
BuildRequires:  gpg2
BuildRequires:  gpgme-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(avahi-glib) >= 0.6
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(sm)
Recommends:     %{name}-lang
Enhances:       seahorse

%description
This package adds sharing of PGP public keys via DNS-SD and HKP.

%lang_package

%prep
%setup -q
sed -i "s:1.2 1.4 2.0:1.2 1.4 2.0 2.1 2.2:" configure

%build
%configure
make %{?_smp_mflags} V=1

%install
%make_install
%suse_update_desktop_file %{name}
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS MAINTAINERS NEWS README
%{_sysconfdir}/xdg/autostart/seahorse-sharing.desktop
%{_bindir}/seahorse-sharing
%{_mandir}/man1/seahorse-sharing.1%{?ext_man}
%dir %{_datadir}/pixmaps/seahorse/
%dir %{_datadir}/pixmaps/seahorse/*/
%{_datadir}/pixmaps/seahorse/*/seahorse-share-keys.*

%files lang -f %{name}.lang

%changelog
