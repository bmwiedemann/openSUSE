#
# spec file for package fapg
#
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           fapg
Version:        0.45
Release:        0
Summary:        Fast Audio Playlist Generator
License:        GPL-2.0-or-later
URL:            http://royale.zerezo.com/fapg/
Source:         http://royale.zerezo.com/fapg/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(liburiparser)

%description
FAPG (Fast Audio Playlist Generator) is a tool to generate list of audio files
(Wav, MP3, Ogg, etc) in various formats (M3U, PLS, HTML, etc). It is designed
for speed even for large lists, and automation use.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/fapg
%{_mandir}/man1/fapg.1%{?ext_man}

%changelog
