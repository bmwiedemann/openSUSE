#
# spec file for package rtaudio
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


%define sover 6
Name:           rtaudio
Version:        5.0.0
Release:        0
Summary:        Real-time Audio I/O Library
License:        MIT
Group:          Development/Libraries/C and C++
URL:            http://www.music.mcgill.ca/~gary/rtaudio/
Source0:        http://www.music.mcgill.ca/~gary/rtaudio/release/rtaudio-5.0.0.tar.gz
BuildRequires:  alsa-lib-devel
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libpulse-devel

%description
RtAudio is a set of C++ classes that provide a common API for
realtime audio input/output across different operating systems.

%package -n librtaudio%{sover}
Summary:        Real-time audio I/O library
Group:          System/Libraries

%description  -n librtaudio%{sover}
RtAudio is a set of C++ classes that provide a common API for
realtime audio input/output across different operating systems.
RtAudio allows simultaneous multi API support, supports dynamic
connection of devices, provides extensive audio device parameter
control, allows audio device capability probing, and has automatic
internal conversion for data format, channel number compensation,
(de)interleaving, and byte-swapping.

%package devel
Summary:        Development files for rtaudio
Group:          Development/Libraries/C and C++
Requires:       librtaudio%{sover} = %{version}-%{release}

%description devel
RtAudio is a set of C++ classes that provide a common API for
realtime audio input/output across different operating systems.

This subpackage contains the headers for rtaudio.

%prep
%setup -q
# remove proprietary content
rm -r include/ tests/Windows
# remove all hidden files
find . -name ".*" -delete
# extract livense from readme
sed -n '/license/,$p' readme > COPYING

%build
%configure --with-jack --with-alsa --with-pulse --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
rm %{buildroot}%{_libdir}/lib%{name}.la

%post   -n librtaudio%{sover} -p /sbin/ldconfig
%postun -n librtaudio%{sover} -p /sbin/ldconfig

%files -n librtaudio%{sover}
%doc readme doc/release.txt
%{_libdir}/lib%{name}.so.*
%license COPYING

%files devel
%doc doc/html
%license COPYING
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib%{name}.so

%changelog
