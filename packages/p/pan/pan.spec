#
# spec file for package pan
#
# Copyright (c) 2024 SUSE LLC
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


%define __builder ninja
Name:           pan
Version:        0.161
Release:        0
Summary:        A Newsreader for GNOME
License:        GPL-2.0-or-later
Group:          Productivity/Networking/News/Clients
URL:            http://pan.rebelbase.com/
Source0:        https://gitlab.gnome.org/GNOME/pan/-/archive/v%{version}/%{name}-v%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext >= 0.21
BuildRequires:  itstool
BuildRequires:  libxml2-tools
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(enchant-2)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  pkgconfig(gnutls) >= 3.0.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gspell-1)
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
# Build with static libs: https://gitlab.gnome.org/GNOME/pan/-/issues/190
%cmake \
  -DBUILD_SHARED_LIBS=OFF \
  -DBUILD_STATIC_LIBS=ON \
  -DENABLE_MANUAL=ON \
  -DWANT_GNUTLS=ON \
  -DWANT_DBUS=ON \
  -DWANT_GKR=ON \
  -DWANT_NOTIFY=ON \
	%{nil}
%cmake_build

%install
%cmake_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_prefix}

%check

%files
%license COPYING COPYING-DOCS
%doc AUTHORS NEWS README.org
%doc %{_datadir}/help/C/%{name}/
%{_mandir}/man?/pan.?%{ext_man}
%{_bindir}/%{name}
%{_datadir}/applications/*.%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/*.%{name}.png
%{_datadir}/metainfo/*.%{name}.metainfo.xml
%{_datadir}/dbus-1/services/org.gnome.pan.service
%{_datadir}/pan/

%files lang -f %{name}.lang

%changelog
