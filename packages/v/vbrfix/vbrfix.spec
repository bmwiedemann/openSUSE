#
# spec file for package vbrfix
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Packman Team <packman@links2linux.de>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           vbrfix
Version:        0.24
Release:        0
Summary:        Repair MP3 files that have incorrect VBR information
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Url:            http://www.willwap.co.uk/Programs/vbrfix.php
Source:         http://archive.ubuntu.com/ubuntu/pool/universe/v/vbrfix/vbrfix_%{version}.orig.tar.gz
Patch1:         vbrfix-exit-error-code.diff
Patch2:         vbrfix-fix-endianness.diff
Patch3:         vbrfix-fix-typos.diff
Patch4:         vbrfix-gcc-4.3.diff
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
Provides:       vbrfixc = %{version}-%{release}

%description
Many MP3 decoders estimate the time length of an MP3 file based on
the filesize divided by the first data packet's bitrate. As songs may
start with silence and hence a low bitrate packet, this length
prediction can produce quite nonsensical values, and when jumping
through a VBR file, 50%% through the file is usually not 50%% through
the song.

vbrfix places a VBR null frame at the beginning of the file to tell
the MP3 player information about the song length and indexing through
the song.

vbrfix can also fix other problems with MP3s, as all non-MP3 content
is deleted (you can keep tags that you state, though). It can also
help when merging two VBR MP3s together with a merging tool and then
needing a newly-calculated VBR null frame.

%prep
%setup -q -n "vbrfixc-%{version}"
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/vbrfixc

%changelog
