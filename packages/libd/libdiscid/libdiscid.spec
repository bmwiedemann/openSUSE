#
# spec file for package libdiscid
#
# Copyright (c) 2023 SUSE LLC
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
Version:        0.6.4
Release:        0
Summary:        Library for gathering DiscIDs and ISRCs from audio CDs
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://musicbrainz.org/doc/libdiscid
Source:         http://ftp.musicbrainz.org/pub/musicbrainz/libdiscid/%{name}-%{version}.tar.gz
Source1000:     baselibs.conf
# PATCH-FEATURE-OPENSUSE libdiscid-no-crypto.patch
Patch0:         libdiscid-no-crypto.patch
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmusicbrainz5)

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

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fiv
%configure \
    --disable-silent-rules \
    --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%{_libdir}/libdiscid.so.0*

%files devel
%dir %{_includedir}/discid
%{_includedir}/discid/*.h
%{_libdir}/libdiscid.so
%{_libdir}/pkgconfig/libdiscid.pc

%changelog
