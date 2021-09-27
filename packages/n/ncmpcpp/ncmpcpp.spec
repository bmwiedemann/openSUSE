#
# spec file for package ncmpcpp
#
# Copyright (c) 2021 SUSE LLC
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


Name:           ncmpcpp
Version:        0.9.2
Release:        0
Summary:        Music Player Daemon Client
License:        GPL-2.0-only
Group:          Productivity/Multimedia/Sound/Players
URL:            https://rybczak.net/ncmpcpp
Source:         https://github.com/ncmpcpp/ncmpcpp/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  curl-devel
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libboost_locale-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libtag-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmpdclient)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(readline)
Requires:       mpd > 0.16

%description
ncmpcpp is an ncurses client for MPD (Music Player Daemon), inspired
by ncmpc. It features a tag editor, playlist editor, search engine,
media library, music visualizer, a last.fm artist database
information fetcher and an alternative user interface.

%prep
%autosetup

%build
autoreconf -fiv
%configure \
  --enable-clock \
  --enable-outputs \
  --enable-visualizer
%make_build

%install
%make_install
rm -rf "%{buildroot}%{_datadir}/doc"

%files
%license COPYING
%doc AUTHORS CHANGELOG.md doc/config doc/bindings
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
