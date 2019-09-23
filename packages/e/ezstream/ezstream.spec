#
# spec file for package ezstream
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ezstream
Version:        0.6.0
Release:        0
Summary:        Icecast media streaming client
License:        GPL-2.0
Group:          Productivity/Multimedia/Sound/Players
URL:            http://www.icecast.org/ezstream.php
Source:         https://downloads.xiph.org/releases/ezstream/ezstream-%{version}.tar.gz
Source1:        ezstream.changes
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(shout)
BuildRequires:  pkgconfig(taglib_c)

%description
Ezstream is a command line source client for Icecast media streaming servers.

The basic mode of operation streams media files or data from standard
input without reencoding and thus requires little resources. It can
use various external transcoders and stream the result. Additional
features include scriptable playlist and metadata handling.

Supported media formats for streaming are MP3, Ogg Vorbis and Ogg
Theora. Native metadata support includes MP3 (ID3v1 only) and Ogg,
plus all those known to TagLib.

%prep
%setup -q
FAKE_BUILDDATE=$(LC_ALL=C date -u -r  %{SOURCE1} '+%%B %%d, %%Y')
sed -i "s/BUILD_DATE=\$(date '+%%B %%d, %%Y')/BUILD_DATE=\"$FAKE_BUILDDATE\"/" configure.ac

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install

rm examples/Makefile*

rm -rf "%{buildroot}%{_datadir}/examples"
rm -rf "%{buildroot}%{_datadir}/doc"

%files
%doc COPYING NEWS README
%doc examples
%{_bindir}/ezstream
%{_bindir}/ezstream-file.sh
%{_mandir}/man1/ezstream.1*
%{_mandir}/man1/ezstream-file.sh.1*

%changelog
