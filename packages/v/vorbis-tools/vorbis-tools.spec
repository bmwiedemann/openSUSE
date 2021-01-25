#
# spec file for package vorbis-tools
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


Name:           vorbis-tools
Version:        1.4.2
Release:        0
Summary:        Ogg Vorbis Tools
License:        GPL-2.0-only
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://www.xiph.org/
Source0:        https://downloads.xiph.org/releases/vorbis/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE vorbis-tools-cflags.diff bnc#93888 -- Remove -fsigned-char option
Patch1:         vorbis-tools-cflags.diff
BuildRequires:  flac-devel
BuildRequires:  gettext-tools
BuildRequires:  libao-devel
BuildRequires:  libcurl-devel
BuildRequires:  libkate-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  pkgconfig
BuildRequires:  speex-devel

%description
This package contains some tools for Ogg Vorbis:

oggenc (an encoder) and ogg123 (a playback tool). It also has vorbiscomment (to
add comments to Vorbis files), ogginfo (to give all useful information about an
Ogg file, including streams in it), oggdec (a simple command line decoder), and
vcut (which allows you to cut up Vorbis files).

%lang_package

%prep
%setup -q
%patch1

%build
# Because of patch vorbis-tools-cflags.diff regenerate build system
cp %{_datadir}/gettext/config.rpath .
autoreconf --force --install
export CFLAGS="%{optflags} -fPIE"
export LDFLAGS="-pie"
%configure --disable-rpath
%make_build

%install
%make_install

# Remove unneeded files (they will be included in /usr/share/doc/packages/vorbis-tools/)
rm -rf %{buildroot}%{_datadir}/doc/%{name}-%{version}/
%find_lang %{name}

%files
%license COPYING
%doc AUTHORS CHANGES README
%doc ogg123/ogg123rc-example
%{_bindir}/ogg123
%{_bindir}/oggdec
%{_bindir}/oggenc
%{_bindir}/ogginfo
%{_bindir}/vcut
%{_bindir}/vorbiscomment
%{_mandir}/man1/ogg123.1%{?ext_man}
%{_mandir}/man1/oggdec.1%{?ext_man}
%{_mandir}/man1/oggenc.1%{?ext_man}
%{_mandir}/man1/ogginfo.1%{?ext_man}
%{_mandir}/man1/vcut.1%{?ext_man}
%{_mandir}/man1/vorbiscomment.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
