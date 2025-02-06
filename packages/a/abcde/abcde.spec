#
# spec file for package abcde
#
# Copyright (c) 2025 SUSE LLC
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


# Enable if your system provides perl(MusicBrainz::DiscID) and perl(WebService::MusicBrainz)
%bcond_without musicbrainz
Name:           abcde
Version:        2.9.3
Release:        0
Summary:        Front-end program to a number of utilities for encoding a CD to files
License:        GPL-2.0-or-later
URL:            https://abcde.einval.com/
Source0:        https://abcde.einval.com/download/%{name}-%{version}.tar.gz
Source1:        https://abcde.einval.com/download/%{name}-%{version}.tar.gz.sign
# Steve McIntyre is the current maintainer
# gpg2 --recv-key 0x587979573442684E
# gpg2 --export --export-options export-minimal 0x587979573442684E > abcde.keyring
Source99:       %{name}.keyring
# PATCH-FEATURE-OPENSUSE use-cddbmethod.patch -- Use cddb instead of musicbrainz in perl module is not available
Patch0:         use-cddbmethod.patch
# PATCH-FIX-OPENSUSE abcde.bug.204.patch -- https://abcde.einval.com/bugzilla/show_bug.cgi?id=204
Patch1:         abcde.bug.204.patch
Patch2:         abcde-use-gnudb.patch
Requires:       cd-discid
Requires:       cdparanoia
Requires:       wget
# eyeD3 and vorbis are default config
Recommends:     eyeD3
# lame is often used for mp3 encoding
Recommends:     lame
Recommends:     vorbis-tools
BuildArch:      noarch
%if %{with musicbrainz}
Requires:       perl(MusicBrainz::DiscID)
Requires:       perl(WebService::MusicBrainz) >= 1.0.4
%endif

%description
A front-end program to cdparanoia, wget, cd-discid, id3, and a
custom Ogg or MP3 encoder, defaulting to oggenc. It grabs an entire CD
and converts each track to Ogg or MP3, and then comments or adds ID3
tags to each file.

%prep
%setup -q
%if !%{with musicbrainz}
%patch -P 0 -p1
%endif
%patch -P 1 -p0
%patch -P 2 -p3

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 abcde %{buildroot}%{_bindir}
install -m 755 cddb-tool %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
cp *.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_sysconfdir}
cp abcde.conf %{buildroot}%{_sysconfdir}
%if %{with musicbrainz}
install -m 755 abcde-musicbrainz-tool %{buildroot}%{_bindir}
%endif

%files
%license COPYING
%doc README FAQ
%{_mandir}/man1/*
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/abcde.conf

%changelog
