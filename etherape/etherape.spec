#
# spec file for package etherape
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


Name:           etherape
Version:        0.9.18
Release:        0
Summary:        A Graphical Network Monitor
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
Url:            http://etherape.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/etherape/%{name}-%{version}.tar.gz
Patch0:         etherape-0.9.12-desktop.patch
BuildRequires:  docbook_4
BuildRequires:  fdupes
BuildRequires:  goocanvas-devel
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(popt)
%if 0%{?is_opensuse}
BuildRequires:  autoconf-archive
%endif
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
Recommends:     %{name}-lang

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
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check

%install
%make_install
%suse_update_desktop_file %{name} System Network
%find_lang %{name}
%fdupes -s %{buildroot}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%defattr(-, root, root)
%doc COPYING TODO NEWS README* AUTHORS ABOUT-NLS
%{_bindir}/etherape
%{_datadir}/applications/etherape.desktop
%{_datadir}/etherape
%{_mandir}/man1/etherape.1%{ext_man}
%{_datadir}/pixmaps/etherape.png

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
