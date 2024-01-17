#
# spec file for package libofa
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libofa
Version:        0.9.3
Release:        0
Summary:        Open Fingerprint Architecture Library
License:        GPL-2.0-or-later OR APL-1.0
Group:          Development/Libraries/C and C++
URL:            https://code.google.com/p/musicip-libofa/
Source0:        %{name}-%{version}.tar.bz2
Source1:        baselibs.conf
Patch0:         libofa-incl.patch
Patch1:         libofa-0.9.3-gcc43.patch
Patch2:         libofa-0.9.3-pkgconfigbloat.patch
Patch3:         libofa-0.9.3-gcc44.patch
Patch4:         libofa-curl-types.patch
Patch5:         libofa-0.9.3-gcc47.patch
BuildRequires:  curl-devel
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fftw3)

%description
MusicDNS and the Open Fingerprint Architecture provide a system for
identifying a piece of music with nothing more than the sound of the
piece itself.
This library is by design compatible with the MusicDNS web service.
Non-commercial access to the service is available at
http://www.musicdns.org.

%package -n libofa0
Summary:        Open Fingerprint Architecture Library
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n libofa0
MusicDNS and the Open Fingerprint Architecture provide a system for
identifying a piece of music with nothing more than the sound of the
piece itself.
This library is by design compatible with the MusicDNS web service.
Non-commercial access to the service is available at
http://www.musicdns.org.

%package devel
Summary:        Open Fingerprint Architecture Library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libofa0 = %{version}
Requires:       pkgconfig(expat)
Requires:       pkgconfig(fftw3)

%description devel
MusicDNS and the Open Fingerprint Architecture provide a system for
identifying a piece of music with nothing more than the sound of the
piece itself.
This library is by design compatible with the MusicDNS web service.
Non-commercial access to the service is available at
http://www.musicdns.org.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3 -p1
%patch4
%patch5 -p1
dos2unix README

%build
autoreconf -fvi
%configure  --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files -n libofa0
%{_libdir}/lib*.so.0*

%files devel
%license COPYING
%doc AUTHORS README
%doc examples/*.cpp examples/*.h
%dir %{_includedir}/ofa1
%{_includedir}/ofa1/*.h
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%post -n libofa0 -p /sbin/ldconfig
%postun -n libofa0 -p /sbin/ldconfig

%changelog
