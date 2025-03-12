#
# spec file for package sndio
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define libname libsndio7
Name:           sndio
Version:        1.10.0
Release:        0
Summary:        Small audio and MIDI framework
License:        ISC
Group:          Productivity/Multimedia/Sound/Midi
URL:            https://www.sndio.org/
Source:         https://sndio.org/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libbsd)

%description
It provides an lightweight audio & MIDI server and a fully documented
user-space API to access either the server or directly the hardware in
a uniform way. Sndio is designed to work for desktop applications, but
pays special attention to synchronization mechanisms and reliability
required by music applications. Reliability through simplicity are part
of the project goals.

%package -n %{libname}
Summary:        Small audio and MIDI framework
Group:          System/Libraries

%description -n %{libname}
It provides an lightweight audio & MIDI server and a fully documented
user-space API to access either the server or directly the hardware in
a uniform way. Sndio is designed to work for desktop applications, but
pays special attention to synchronization mechanisms and reliability
required by music applications. Reliability through simplicity are part
of the project goals.

%package -n sndio-devel
Summary:        Library Developer Files for sndio
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n sndio-devel
This package contains files needed for development with the sndio
library.

%package -n sndioctl
Summary:        Small audio and MIDI framework
Group:          Productivity/Multimedia/Sound/Midi

%description -n sndioctl
This package contains the controller binary for sndio.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}"
# not autotools configure
./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-alsa --with-libbsd
%make_build

%install
%make_install

%ldconfig_scriptlets -n %{libname}

%files
%license LICENSE
%{_bindir}/aucat
%{_bindir}/midicat
%{_bindir}/sndiod
%{_mandir}/man1/aucat.1%{?ext_man}
%{_mandir}/man1/midicat.1%{?ext_man}
%{_mandir}/man8/sndiod.8%{?ext_man}
%{_mandir}/man7/sndio.7%{?ext_man}

%files -n %{libname}
%license LICENSE
%{_libdir}/libsndio.so.*

%files -n sndio-devel
%license LICENSE
%{_includedir}/sndio.h
%{_libdir}/pkgconfig/sndio.pc
%{_libdir}/libsndio.so
%{_mandir}/man3/*.3%{?ext_man}

%files -n sndioctl
%license LICENSE
%{_bindir}/sndioctl
%{_mandir}/man1/sndioctl.1%{?ext_man}

%changelog
