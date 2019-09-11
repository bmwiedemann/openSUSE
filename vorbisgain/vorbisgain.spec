#
# spec file for package vorbisgain
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 B1 Systems GmbH, Vohburg, Germany.
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


Name:           vorbisgain
Version:        0.37
Release:        0
Summary:        Calculate the Replay Gain for Ogg Vorbis files
License:        LGPL-2.1
Group:          Productivity/Multimedia/Sound/Utilities
Url:            https://sjeng.org/vorbisgain.html
Source0:        https://www.sjeng.org/ftp/vorbis/%{name}-%{version}.tar.gz
BuildRequires:  dos2unix
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel

%description
Calculate the Replay Gain for Ogg Vorbis files

VorbisGain is a utility that uses a psychoacoustic method to correct
the volume of an Ogg Vorbis file to a predefined standardized
loudness.

It is meant as a replacement for the normalization that is commonly
used before encoding. Although normalization will ensure that each
song has the same peak volume, this unfortunately does not say
anything about the apparent loudness of the music, with the end result
being that many normalized files still don't sound equally
loud. VorbisGain uses psychoacoustics to address this
deficiency. Moreover, unlike normalization, it's a lossless procedure
which works by adding tags to the file. Additionally, it will add
hints that can be used to prevent clipping on playback. It is based
upon the ReplayGain technology.

The end result is that playback is both more convenient and of higher
quality compared to a non-VorbisGain'ed file.

%prep
%setup -q
# workaround wrong end-of-line encoding
dos2unix -f COPYING NEWS

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc README COPYING NEWS
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
