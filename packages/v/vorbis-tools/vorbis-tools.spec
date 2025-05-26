#
# spec file for package vorbis-tools
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           vorbis-tools
Version:        1.4.3
Release:        0
Summary:        Ogg Vorbis Tools
License:        GPL-2.0-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://www.xiph.org/
Source0:        https://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.gz
BuildRequires:  gettext-tools
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ao) >= 1.0.0
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(oggkate)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(vorbis) >= 1.3.0

%description
This package contains some tools for Ogg Vorbis:

oggenc (an encoder) and ogg123 (a playback tool). It also has vorbiscomment (to
add comments to Vorbis files), ogginfo (to give all useful information about an
Ogg file, including streams in it), oggdec (a simple command line decoder), and
vcut (which allows you to cut up Vorbis files).

%lang_package

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
rm %{buildroot}%{_datadir}/doc/vorbis-tools/ogg123rc-example
%find_lang %{name}

%check
%make_build check

%files
%license COPYING
%doc AUTHORS CHANGES README
%{_bindir}/*
%{_mandir}/man1/*.1%{?ext_man}

%files lang -f %{name}.lang
%license COPYING

%changelog
