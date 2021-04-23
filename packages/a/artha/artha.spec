#
# spec file for package artha
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


Name:           artha
Version:        1.0.5
Release:        0
Summary:        Offline English thesaurus based on WordNet
License:        GPL-2.0-only
Group:          Productivity/Office/Dictionary
URL:            http://artha.sourceforge.net
Source:         https://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  wordnet-devel
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.22
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.24
Requires:       enchant
Requires:       hunspell
Requires:       wordnet

%description
Artha is a free cross-platform English thesaurus that works
completely off-line and is based on WordNet.

%prep
%setup -q
chmod -x TODO

%build
autoreconf -f
%configure
%make_build

%install
%make_install DESTDIR=%{buildroot} INSTALL="install -p"
%if 0%{?suse_version}
%suse_update_desktop_file -r artha Office Dictionary
%endif

%files
%license COPYING
%doc ChangeLog README NEWS TODO AUTHORS
%dir %{_datadir}/artha
%{_bindir}/artha
%{_datadir}/applications/artha.desktop
%{_datadir}/artha/gui.glade
%{_datadir}/pixmaps/artha.png
%{_mandir}/man1/artha.1%{?ext_man}

%changelog
