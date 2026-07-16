#
# spec file for package libdiscid
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define libname libdiscid0

Name:           libdiscid
Version:        0.7.0
Release:        0
Summary:        Library for gathering DiscIDs and ISRCs from audio CDs
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://musicbrainz.org/doc/libdiscid
Source:         https://data.metabrainz.org/pub/musicbrainz/%{name}/%{name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE use-openssl.patch
Patch0:         use-openssl.patch

BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmusicbrainz5)
BuildRequires:  pkgconfig(libopenssl)

BuildSystem:    cmake

%description
libdiscid is a C library for creating MusicBrainz and freedb DiscIDs
from audio CDs.
It reads a CD's table of contents (TOC) and generates an identifier
which can be used to lookup the CD at MusicBrainz.
Additionally, it provides a submission URL for adding the DiscID to the
database and gathers ISRCs and the MCN from disc.

%package -n %{libname}
Summary:        Library for gathering DiscIDs and ISRCs from audio CDs
Group:          Development/Libraries/C and C++

%description -n %{libname}
libdiscid is a C library for creating MusicBrainz and freedb DiscIDs
from audio CDs.
It reads a CD's table of contents (TOC) and generates an identifier
which can be used to lookup the CD at MusicBrainz.
Additionally, it provides a submission URL for adding the DiscID to the
database and gathers ISRCs and the MCN from disc.

%package devel
Summary:        Library for gathering DiscIDs and ISRCs from audio CDs
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
libdiscid is a C library for creating MusicBrainz and freedb DiscIDs
from audio CDs.
It reads a CD's table of contents (TOC) and generates an identifier
which can be used to lookup the CD at MusicBrainz.
Additionally, it provides a submission URL for adding the DiscID to the
database and gathers ISRCs and the MCN from disc.

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%{_libdir}/libdiscid.so.*

%files devel
%{_libdir}/libdiscid.so
%{_libdir}/pkgconfig/libdiscid.pc
%dir %{_includedir}/discid
%{_includedir}/discid/discid.h

%changelog
