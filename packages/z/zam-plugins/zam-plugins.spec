#
# spec file for package zam-plugins
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018 Edgar Aichinger <edogawa@aon.at>
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


Name:           zam-plugins
Version:        3.12
Release:        0
Summary:        A collection of audio plugins for high quality processing
License:        GPL-2.0-or-later
URL:            http://www.zamaudio.com/?p=976
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE zam-plugins-verbose_build.patch aloisio@gmx.com -- prints compilation flags
Patch0:         zam-plugins-verbose_build.patch
BuildRequires:  gcc-c++
BuildRequires:  ladspa
BuildRequires:  ladspa-devel
BuildRequires:  lv2
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(liblo)
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
ExclusiveArch:  %ix86 x86_64

%description
These plugins provide DSP. Of these, ZamValve has two different
models, one of which uses very large proportion of CPU, but has been
reported to produce more realistic sound than the tanh model.

There currently is no documentation on how to use these plugins, but
anyone who is familiar with outboard gear should be able to work it out.
The default settings and almost every slider is calibrated to
standard ranges.

The suite so far consists of:

ZamAutoSat - Automatic saturation plugin
ZamComp - Mono Compressor plugin
ZamCompX2 - Stereo Compressor plugin
ZamCompExp - Stereo Compressor/Expander plugin
ZamEQ2 - 2x parametric EQ (with high/lowshelf and HP/LP) plugin
ZamValve - Valve distortion (WDF physical model or tanh) plugin
ZamGEQ31 - Mono 31 band graphic equalizer plugin
ZamGEQ31X2 - Stereo 31 band graphic equalizer plugin

%package -n ladspa-%{name}
Summary:        A collection of audio plugins for high quality processing
Requires:       ladspa
Conflicts:      %{name}

%description -n ladspa-%{name}
These plugins provide DSP. Of these, ZamValve has two different
models, one of which uses very large proportion of CPU, but has been
reported to produce more realistic sound than the tanh model.

There currently is no documentation on how to use these plugins, but
anyone who is familiar with outboard gear should be able to work it out.
The default settings and almost every slider is calibrated to
standard ranges.

The suite so far consists of:

ZamAutoSat - Automatic saturation plugin
ZamComp - Mono Compressor plugin
ZamCompX2 - Stereo Compressor plugin
ZamCompExp - Stereo Compressor/Expander plugin
ZamEQ2 - 2x parametric EQ (with high/lowshelf and HP/LP) plugin
ZamValve - Valve distortion (WDF physical model or tanh) plugin
ZamGEQ31 - Mono 31 band graphic equalizer plugin
ZamGEQ31X2 - Stereo 31 band graphic equalizer plugin

%package -n lv2-%{name}
Summary:        A collection of audio plugins for high quality processing
Requires:       lv2
Conflicts:      %{name}

%description -n lv2-%{name}
These plugins provide DSP. Of these, ZamValve has two different
models, one of which uses very large proportion of CPU, but has been
reported to produce more realistic sound than the tanh model.

There currently is no documentation on how to use these plugins, but
anyone who is familiar with outboard gear should be able to work it out.
The default settings and almost every slider is calibrated to
standard ranges.

The suite so far consists of:

ZamAutoSat - Automatic saturation plugin
ZamComp - Mono Compressor plugin
ZamCompX2 - Stereo Compressor plugin
ZamCompExp - Stereo Compressor/Expander plugin
ZamEQ2 - 2x parametric EQ (with high/lowshelf and HP/LP) plugin
ZamValve - Valve distortion (WDF physical model or tanh) plugin
ZamGEQ31 - Mono 31 band graphic equalizer plugin
ZamGEQ31X2 - Stereo 31 band graphic equalizer plugin

%package vst
Summary:        A collection of audio plugins for high quality processing
Conflicts:      %{name}

%description vst
These plugins provide DSP. Of these, ZamValve has two different
models, one of which uses very large proportion of CPU, but has been
reported to produce more realistic sound than the tanh model.

There currently is no documentation on how to use these plugins, but
anyone who is familiar with outboard gear should be able to work it out.
The default settings and almost every slider is calibrated to
standard ranges.

The suite so far consists of:

ZamAutoSat - Automatic saturation plugin
ZamComp - Mono Compressor plugin
ZamCompX2 - Stereo Compressor plugin
ZamCompExp - Stereo Compressor/Expander plugin
ZamEQ2 - 2x parametric EQ (with high/lowshelf and HP/LP) plugin
ZamValve - Valve distortion (WDF physical model or tanh) plugin
ZamGEQ31 - Mono 31 band graphic equalizer plugin
ZamGEQ31X2 - Stereo 31 band graphic equalizer plugin

%package jack
Summary:        A collection of audio plugins for high quality processing
Conflicts:      %{name}

%description jack
These plugins provide DSP. Of these, ZamValve has two different
models, one of which uses very large proportion of CPU, but has been
reported to produce more realistic sound than the tanh model.

There currently is no documentation on how to use these plugins, but
anyone who is familiar with outboard gear should be able to work it out.
The default settings and almost every slider is calibrated to
standard ranges.

The suite so far consists of:

ZamAutoSat - Automatic saturation plugin
ZamComp - Mono Compressor plugin
ZamCompX2 - Stereo Compressor plugin
ZamCompExp - Stereo Compressor/Expander plugin
ZamEQ2 - 2x parametric EQ (with high/lowshelf and HP/LP) plugin
ZamValve - Valve distortion (WDF physical model or tanh) plugin
ZamGEQ31 - Mono 31 band graphic equalizer plugin
ZamGEQ31X2 - Stereo 31 band graphic equalizer plugin

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"
%make_build SKIP_STRIPPING=true

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_lib}
# remove executable flag where not needed
find %{buildroot}%{_libdir}/lv2 -name \*.ttl -exec chmod -x {} +

%files jack
%{_bindir}/Za*

%files -n ladspa-%{name}
%{_libdir}/ladspa/Za*-ladspa.so

%files -n lv2-%{name}
%{_libdir}/lv2/Za*.lv2

%files vst
%dir %{_libdir}/vst
%{_libdir}/vst/Za*-vst.so

%changelog
