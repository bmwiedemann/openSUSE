#
# spec file for package pianobar
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Packman team: http://packman.links2linux.org/
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


Name:           pianobar
Version:        2019.02.14
Release:        0
Summary:        Pandora Player
License:        MIT
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://6xq.net/pianobar
Source0:        https://github.com/PromyLOPh/pianobar/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ao)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(json)
BuildRequires:  pkgconfig(libavcodec) >= 58.7.100
BuildRequires:  pkgconfig(libavfilter) >= 7.0.101
BuildRequires:  pkgconfig(libavformat) >= 58.0.102
BuildRequires:  pkgconfig(libavutil) >= 56.6.100
BuildRequires:  pkgconfig(libcurl)

%description
pianobar is a console client for the personalized web radio pandora

- play and manage (create, add more music, delete, rename, ...) your stations
- rate played songs and let pandora explain why they have been selected
- show upcoming songs/song history
- configure keybindings
- last.fm scrobbling support (external application)
- proxy support for listeners outside the USA

%prep
%setup -q

%build
export CC="gcc"
export CFLAGS="-std=c99 %{optflags}"
make %{?_smp_mflags} V=1

%install
make install PREFIX=%{_prefix} DESTDIR=%{buildroot}

%files
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
