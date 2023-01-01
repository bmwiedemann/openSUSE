#
# spec file for package etherape
#
# Copyright (c) 2022 SUSE LLC
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


Name:           etherape
Version:        0.9.20
Release:        0
Summary:        A Graphical Network Monitor
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            https://etherape.sourceforge.io/
Source0:        https://prdownloads.sourceforge.net/etherape/%{name}-%{version}.tar.gz
Patch0:         etherape-0.9.12-desktop.patch
BuildRequires:  docbook_4
BuildRequires:  fdupes
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(goocanvas-2.0)
BuildRequires:  pkgconfig(popt)
Requires(post): update-desktop-files
Requires(postun):update-desktop-files
Requires:       xdg-utils
Recommends:     %{name}-lang
%if 0%{?is_opensuse}
BuildRequires:  autoconf-archive
%endif

%description
EtherApe is a graphical network monitor for Unix, modeled after
etherman. Featuring link layer, IP, and TCP modes, it displays network
activity graphically. Hosts and links change in size with traffic.
Various protocols are color coded in the display. It supports ethernet,
FDDI, token ring, ISDN, PPP, and SLIP devices. It can filter traffic to
show and can read traffic from a file as well as live from the network.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
%configure
%make_build

%check
%make_build check

%install
%make_install

# desktop file
# additional root desktop file
cp %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}-su.desktop
sed -i -e 's|Name=EtherApe|Name=EtherApe - Super User Mode|g' %{buildroot}%{_datadir}/applications/%{name}-su.desktop
sed -i -e 's|Exec=etherape|Exec=xdg-su -c etherape|g' %{buildroot}%{_datadir}/applications/%{name}-su.desktop
%suse_update_desktop_file %{name} System Network
%suse_update_desktop_file %{name}-su System Network

%find_lang %{name}
%fdupes -s %{buildroot}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%license COPYING
%doc TODO NEWS README* AUTHORS ABOUT-NLS
%{_bindir}/etherape
%{_datadir}/applications/etherape.desktop
%{_datadir}/applications/etherape-su.desktop
%{_datadir}/etherape
%{_mandir}/man1/etherape.1%{?ext_man}
%{_datadir}/pixmaps/etherape.png

%files lang -f %{name}.lang

%changelog
