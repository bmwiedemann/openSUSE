#
# spec file for package pan
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


Name:           pan
Version:        0.153
Release:        0
Summary:        A Newsreader for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Networking/News/Clients
URL:            http://pan.rebelbase.com/
Source0:        https://gitlab.gnome.org/GNOME/pan/-/archive/v%{version}/%{name}-v%{version}.tar.bz2

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext >= 0.21
BuildRequires:  itstool
BuildRequires:  libtool
BuildRequires:  libxml2-tools
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  pkgconfig(gnutls) >= 3.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkspell3-3.0) >= 2.0.16
BuildRequires:  pkgconfig(libnotify) >= 0.4.1
BuildRequires:  pkgconfig(libsecret-1)

%description
Pan is a Usenet newsreader that's good at both text and binaries.
It supports offline reading, scoring and killfiles, yEnc, NZB, PGP
handling, multiple servers, and secure connections.

%lang_package

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--with-gnutls \
	--with-dbus \
	--enable-gkr \
	--enable-manual \
	--enable-libnotify \
	%{nil}
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

%files
%license COPYING COPYING-DOCS
%doc AUTHORS NEWS README.org
%doc %{_datadir}/help/C/%{name}/
%{_mandir}/man?/pan.?%{ext_man}
%{_bindir}/%{name}
%{_datadir}/applications/*.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.%{name}.png
%{_datadir}/metainfo/*.%{name}.metainfo.xml

%files lang -f %{name}.lang

%changelog
