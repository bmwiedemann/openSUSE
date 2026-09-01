#
# spec file for package soapy-audio
#
# Copyright (c) 2026 SUSE LLC
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


# SoapySDR module ABI directory; must track soapy-sdr.
%define soapy_modver 0.8-3
%define soapy_modname soapysdr%{soapy_modver}-module-audio
Name:           soapy-audio
# Upstream last tagged 0.1.1 in 2019. Master is that tag plus the two hamlib
# patches we used to carry, so the snapshot ships patch-free. '+git' keeps it
# sorting above the tag.
Version:        0.1.1+git20251009.63b22ec
Release:        0
Summary:        SoapySDR module for audio devices
# Legal-Review-Notice: cmake/Modules/FindRtAudio.cmake is BSD-3-Clause (Idiap
# Research Institute); LibFindMacros.cmake and Findhamlib.cmake carry no notice
# at all. All three are build-system helpers, never compiled into a shipped
# artifact. The in-tree RtAudio (see %%build) IS linked in and is MIT - its
# extra "please send modifications upstream" sentence is explicitly non-binding
# - and its notice ships as LICENSE.RtAudio.txt.
License:        MIT
URL:            https://github.com/pothosware/SoapyAudio
Source:         %{name}-%{version}.tar.zst
# NB: nothing here may pull in rtaudio-devel - upstream's FindRtAudio.cmake
# would then prefer the system rtaudio 6 and fail to compile (see %%build).
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
# for SoapySDRUtil in %%check
BuildRequires:  soapy-sdr
BuildRequires:  pkgconfig(SoapySDR)
BuildRequires:  pkgconfig(hamlib)
BuildRequires:  pkgconfig(libpulse-simple)

%description
Soapy Audio - audio device support for Soapy SDR.
A Soapy module that supports audio devices within the Soapy API.

%package -n %{soapy_modname}
Summary:        SoapySDR module for audio devices
# soname dep pulls only libSoapySDR, which is what dlopens the module;
# require the package too so SoapySDRUtil is there to probe and use it
Requires:       soapy-sdr
Provides:       bundled(rtaudio) = 5.1.0

%description -n %{soapy_modname}
Soapy Audio - audio device support for Soapy SDR.
A Soapy module that supports audio devices within the Soapy API.

This lets any soundcard-class receiver (Softrock, SDR transceivers on a
line-in, FUNcube dongles) appear as a SoapySDR device, with optional hamlib
rig control for frequency tuning.

%prep
%autosetup
# MIT requires the notice to travel with the binary, and the bundled RtAudio
# carries its own only inside the header.
sed -n '/RtAudio: realtime audio/,/OTHER DEALINGS IN THE SOFTWARE/p' \
    RtAudio/RtAudio.h > LICENSE.RtAudio.txt

%build
# rtaudio 6 dropped the RtAudioError API upstream still uses, and moved device
# enumeration from a 0..count-1 index to opaque ids, which upstream does not
# do - so the in-tree RtAudio 5.1.0 is built instead of linking system rtaudio.
# PulseAudio only: RtAudio picks the first compiled API whose getDeviceCount()
# is non-zero, and RtApiPulse always claims one device, so any other backend
# compiled in beside it is unreachable dead code.
%cmake \
    -DUSE_HAMLIB=ON \
    -DUSE_AUDIO_PULSE=ON \
    -DUSE_AUDIO_ALSA=OFF \
    -DUSE_AUDIO_JACK=OFF \
    -DUSE_AUDIO_OSS=OFF
%cmake_build

%install
%cmake_install

%check
# No upstream test suite; verify the module is loadable by SoapySDR.
SOAPY_SDR_PLUGIN_PATH=%{buildroot}%{_libdir}/SoapySDR/modules%{soapy_modver} \
    SoapySDRUtil --check=audio

%files -n %{soapy_modname}
%license LICENSE.txt LICENSE.RtAudio.txt
%doc Changelog.txt README.md
%dir %{_libdir}/SoapySDR
%dir %{_libdir}/SoapySDR/modules%{soapy_modver}
%{_libdir}/SoapySDR/modules%{soapy_modver}/libaudioSupport.so

%changelog
