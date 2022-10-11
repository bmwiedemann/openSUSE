#
# spec file for package librubberband
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


%define sover   2
Name:           librubberband
Version:        3.1.0
Release:        0
Summary:        Audio time-stretching and pitch-shifting library
License:        GPL-2.0-or-later
Group:          System/Libraries
URL:            https://www.breakfastquay.com/rubberband/
Source:         https://breakfastquay.com/files/releases/rubberband-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ladspa-devel
BuildRequires:  meson >= 0.53.0
BuildRequires:  pkgconfig
BuildRequires:  vamp-plugin-sdk-devel
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(vamp-sdk)
Requires:       ladspa
Requires:       lv2

%description
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another.

%package -n     %{name}%{sover}
Summary:        Audio time-stretching and pitch-shifting library
Group:          System/Libraries
URL:            https://www.breakfastquay.com/rubberband/

%description -n %{name}%{sover}
Rubber Band is a library and utility program that permits you to change the
tempo and pitch of an audio recording independently of one another.

%package -n     rubberband-cli
Summary:        Command line interface for %{name}
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Requires:       %{name}%{sover} = %{version}

%description -n rubberband-cli
Package rubberband-cli contains a command-line utility that can be used to exploit
Rubber Band's capabilities.

%package -n     rubberband-ladspa
Summary:        LADSPA plugin for %{name}
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Requires:       %{name}%{sover} = %{version}

%description -n rubberband-ladspa
Package rubberband-ladspa is LADSPA plugin that can change the pitch of a sound in real-time.

%package -n     rubberband-lv2
Summary:        LV2 plugins for %{name}
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       %{name}%{sover} = %{version}

%description -n rubberband-lv2
Package rubberband-lv2 contains the rubberband LV2 plugin.

%package -n     rubberband-vamp
Summary:        Vamp plugins for %{name}
Group:          Productivity/Multimedia/Sound/Editors and Convertors
Requires:       %{name}%{sover} = %{version}

%description -n rubberband-vamp
This package contains the following Vamp plugins:
 * increments (Output Increments): Output time increment for each
   input step
 * aggregate_increments (Accumulated Output Increments): Accumulated
   output time increments
 * divergence (Divergence from Linear): Difference between actual
   output time and the output time for a theoretical linear stretch
 * phaseresetdf (Phase Reset Detection Function): Curve whose peaks
   are used to identify transients for phase reset points
 * smoothedphaseresetdf (Smoothed Phase Reset Detection Function):
   Phase reset curve smoothed for peak picking
 * phaseresetpoints (Phase Reset Points): Points estimated as
   transients at which phase reset occurs
 * timesyncpoints (Time Sync Points): Salient points which stretcher
   aims to place with strictly correct timing

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n rubberband-%{version}

%build
%meson -Dfft=fftw
%meson_build

%install
%meson_install

rm %{buildroot}%{_libdir}/*.a

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license COPYING
%doc README.md
%{_libdir}/%{name}.so.%{sover}*

%files devel
%dir %{_includedir}/rubberband
%{_includedir}/rubberband/*.h
%{_libdir}/librubberband.so
%{_libdir}/pkgconfig/rubberband.pc

%files -n rubberband-cli
%{_bindir}/rubberband
%{_bindir}/rubberband-r3

%files -n rubberband-ladspa
%dir %{_libdir}/ladspa
%dir %{_datadir}/ladspa
%dir %{_datadir}/ladspa/rdf
%{_libdir}/ladspa/ladspa-rubberband.cat
%{_libdir}/ladspa/ladspa-rubberband.so
%{_datadir}/ladspa/rdf/ladspa-rubberband.rdf

%files -n rubberband-lv2
%dir %{_libdir}/lv2
%dir %{_libdir}/lv2/rubberband.lv2
%{_libdir}/lv2/rubberband.lv2/lv2-rubberband.so
%{_libdir}/lv2/rubberband.lv2/lv2-rubberband.ttl
%{_libdir}/lv2/rubberband.lv2/manifest.ttl

%files -n rubberband-vamp
%dir %{_libdir}/vamp
%{_libdir}/vamp/vamp-rubberband.cat
%{_libdir}/vamp/vamp-rubberband.so

%changelog
