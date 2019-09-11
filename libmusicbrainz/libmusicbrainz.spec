#
# spec file for package libmusicbrainz
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libmusicbrainz
BuildRequires:  gcc-c++
BuildRequires:  libexpat-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
Summary:        Library That Provides Access to the MusicBrainz Server
License:        LGPL-2.1+
Group:          System/Libraries
Version:        2.1.5
Release:        0
Url:            http://www.musicbrainz.org/
Source:         %{name}-%{version}.tar.bz2
Source1000:     baselibs.conf
Patch0:         libmusicbrainz-2.1.5-gcc43.patch
# PATCH-FIX-OPENSUSE gcc6-fix-errors.patch -- Fix errors spotted by GCC6.
Patch1:         gcc6-fix-errors.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
MusicBrainz is the second generation incarnation of the CD Index. This
server is designed to enable audio CD, MP3 and Vorbis players to
download metadata about the music they are playing.

%package -n libmusicbrainz4
Summary:        Library That Provides Access to the MusicBrainz Server
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libmusicbrainz4
MusicBrainz is the second generation incarnation of the CD Index. This
server is designed to enable audio CD, MP3 and Vorbis players to
download metadata about the music they are playing.

%package devel
Requires:       libmusicbrainz4 = %{version} libstdc++-devel
Summary:        Include Files and Libraries Mandatory for Development
Group:          Development/Libraries/C and C++

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoreconf -fiv
%configure --disable-static --with-pic
%{__make} %{?jobs:-j%jobs}

%install
%makeinstall
rm -f %{buildroot}%{_libdir}/libmusicbrainz.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -n libmusicbrainz4 -p /sbin/ldconfig

%postun -n libmusicbrainz4 -p /sbin/ldconfig

%files -n libmusicbrainz4
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README TODO
%{_libdir}/libmusicbrainz.so.4*

%files devel
%defattr(-, root, root)
%doc examples/*cpp examples/*c
%{_includedir}/musicbrainz
%{_libdir}/libmusicbrainz.so
%{_libdir}/pkgconfig/*.pc

%changelog
