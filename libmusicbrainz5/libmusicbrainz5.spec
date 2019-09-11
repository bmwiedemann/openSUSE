#
# spec file for package libmusicbrainz5
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define _name   libmusicbrainz
Name:           libmusicbrainz5
Version:        5.1.0
Release:        0
Summary:        Library That Provides Access to the MusicBrainz Server
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://musicbrainz.org/doc/libmusicbrainz
Source0:        https://github.com/metabrainz/libmusicbrainz/releases/download/release-%{version}/%{_name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  neon-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0)

%description
MusicBrainz is the second generation incarnation of the CD Index. This
server is designed to enable audio CD, MP3 and Vorbis players to
download metadata about the music they are playing.

%package -n libmusicbrainz5-1
Summary:        Library That Provides Access to the MusicBrainz Server
Group:          System/Libraries

%description -n libmusicbrainz5-1
MusicBrainz is the second generation incarnation of the CD Index. This
server is designed to enable audio CD, MP3 and Vorbis players to
download metadata about the music they are playing.

%package devel
Summary:        Library That Provides Access to the MusicBrainz Server
Group:          Development/Libraries/C and C++
Requires:       libmusicbrainz5-1 = %{version}
Requires:       libstdc++-devel

%description devel
MusicBrainz is the second generation incarnation of the CD Index. This
server is designed to enable audio CD, MP3 and Vorbis players to
download metadata about the music they are playing.

%prep
%setup -q -n %{_name}-%{version}

%build
CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64"
CXXFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -fvisibility-inlines-hidden"
%cmake
make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install

%post -n libmusicbrainz5-1 -p /sbin/ldconfig
%postun -n libmusicbrainz5-1 -p /sbin/ldconfig

%files -n libmusicbrainz5-1
%license COPYING.txt
%doc AUTHORS.txt NEWS.txt README.md
%{_libdir}/libmusicbrainz5.so.[0-9]*

%files devel
%doc examples/*.cc examples/*.c
%{_includedir}/musicbrainz5/
%{_libdir}/libmusicbrainz5.so
%{_libdir}/pkgconfig/libmusicbrainz5.pc

%changelog
