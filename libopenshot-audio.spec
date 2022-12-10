#
# spec file for package libopenshot-audio
#
# Copyright (c) 2022 SUSE LLC
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


%define sover 9

Name:           libopenshot-audio
Version:        0.3.0
Release:        0
Summary:        Audio library for the OpenShot video editor
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://openshot.org/
Source0:        %{name}-%{version}.tar.xz
Source99:       %{name}.changes

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)

%description
The OpenShot Audio Library allows editing and playback of audio.
It was derived from the JUCE library.

%package -n     %{name}%{sover}
Summary:        Audio library for the OpenShot video editor
Group:          System/Libraries

%description -n %{name}%{sover}
The OpenShot Audio Library allows editing and playback of audio.
It was derived from the JUCE library.

This package contains the shared library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}

%description    devel
The OpenShot Audio Library.

This package contains header files and libraries needed to develop
application that use %{name}.

%prep
%autosetup -p1

%build
export SOURCE_DATE_EPOCH=$(date +%s -r %{S:99})
%cmake \
	-DCMAKE_SHARED_LINKER_FLAGS="-Wl,--as-needed" \
	%{nil}
%cmake_build

%install
%cmake_install

%post   -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%doc AUTHORS
%license COPYING
%{_libdir}/%{name}.so.*

%files devel
%{_bindir}/openshot*
%{_libdir}/%{name}.so
%{_includedir}/%{name}
%{_mandir}/man?/openshot*
%dir %{_libdir}/cmake/OpenShotAudio
%{_libdir}/cmake/OpenShotAudio/FindASIO.cmake
%{_libdir}/cmake/OpenShotAudio/OpenShotAudio*.cmake

%changelog
