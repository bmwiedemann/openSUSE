#
# spec file for package pcaudiolib
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


%define sover   0
Name:           pcaudiolib
Version:        1.3
Release:        0
Summary:        Portable C Audio Library
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://reecedunn.co.uk/espeak-for-android
Source:         https://github.com/espeak-ng/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse)

%description
The Portable C Audio Library (pcaudiolib) provides a C API to different audio devices.

%package     -n libpcaudio%{sover}
Summary:        Cross platform audio library
Group:          System/Libraries

%description -n libpcaudio%{sover}
The Portable C Audio Library (pcaudiolib) provides a C API to different audio devices.

%package        devel
Summary:        Development files for libpcaudio0
Group:          Development/Languages/C and C++
Requires:       libpcaudio%{sover} = %{version}

%description    devel
The Portable C Audio Library (pcaudiolib) provides a C API to different audio devices.

%prep
%autosetup

%build
./autogen.sh
%configure --disable-static --disable-silent-rules
%make_build

%install
%make_install
rm -vf %{buildroot}%{_libdir}/*.{a,la}

%post -n libpcaudio%{sover} -p /sbin/ldconfig
%postun -n libpcaudio%{sover} -p /sbin/ldconfig

%files -n libpcaudio%{sover}
%license COPYING
%{_libdir}/libpcaudio.so.*

%files devel
%doc README.md
%license COPYING
%{_libdir}/libpcaudio.so
%dir %{_includedir}/pcaudiolib
%{_includedir}/pcaudiolib/audio.h

%changelog
