#
# spec file for package sndio
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


%define libname libsndio7_0
Name:           sndio
Version:        1.5.0
Release:        0
Summary:        Small audio and MIDI framework
License:        ISC
Group:          Productivity/Multimedia/Sound/Midi
URL:            http://www.sndio.org/
Source:         http://www.sndio.org/sndio-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)

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

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
# not autotools configure
./configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-alsa
make %{?_smp_mflags}

%install
%make_install

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%{_bindir}/aucat
%{_bindir}/midicat
%{_bindir}/sndiod
%{_mandir}/man1/aucat.1%{?ext_man}
%{_mandir}/man1/midicat.1%{?ext_man}
%{_mandir}/man8/sndiod.8%{?ext_man}
%{_mandir}/man7/sndio.7%{?ext_man}

%files -n libsndio7_0
%{_libdir}/libsndio.so.7.0

%files -n sndio-devel
%{_includedir}/sndio.h
%{_libdir}/libsndio.so
%{_mandir}/man3/*.3%{?ext_man}

%changelog
