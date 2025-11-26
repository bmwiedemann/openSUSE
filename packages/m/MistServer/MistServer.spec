#
# spec file for package MistServer
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


Name:           MistServer
Version:        3.9.1
Release:        0
Summary:        Internet streaming media toolkit
License:        Unlicense
URL:            https://github.com/DDVTECH/mistserver
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        mistserver.sysuser
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  group(video)
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(librist)
BuildRequires:  pkgconfig(libsrtp2)
BuildRequires:  pkgconfig(mbedtls)
BuildRequires:  pkgconfig(srt)
BuildRequires:  pkgconfig(usrsctp)
Requires:       group(video)
Recommends:     ffmpeg
%sysusers_requires
%{?systemd_ordering}

%description
%{name} is a streaming media toolkit for over-the-top media
services (internet streaming) ideal for developers and system integrators.

%package devel
Summary:        Development files for %{name}
BuildArch:      noarch

%description devel
Development files for %{name}.

%prep
%autosetup -n mistserver-%{version}

%build

# Libraries are not versioned, version on RPM side
echo "V_%{version} { global: *; };" > /tmp/z.sym
export LDFLAGS="$LDFLAGS -Wl,--version-script=/tmp/z.sym"

# Disable warnings caused by certain upstream coding practices
# to make it possible to focus on other and future warnings
export CXXFLAGS="$CXXFLAGS -Wno-strict-aliasing"

# Default char to unsigned according to uppstream
export CXXFLAGS="$CXXFLAGS -funsigned-char"

%meson \
  -DDEBUG=3 \
  -DLOCAL_GENERATORS=false \
  -DNOGA=true \
  -DNOUPDATE=true \
  -DRELEASE=%{version}
%meson_build

%sysusers_generate_pre %{SOURCE2} %{name} %{name}.conf

%install
%meson_install

# service
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/mistserver.conf

%pre -f %{name}.pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%license UNLICENSE
%doc README.md
%ghost %config(noreplace) %attr(0644, root, mistserver) %{_sysconfdir}/%{name}.json
%{_bindir}/MistAnalyserAV1
%{_bindir}/MistAnalyserDTSC
%{_bindir}/MistAnalyserEBML
%{_bindir}/MistAnalyserFLAC
%{_bindir}/MistAnalyserFLV
%{_bindir}/MistAnalyserH264
%{_bindir}/MistAnalyserHLS
%{_bindir}/MistAnalyserMP4
%{_bindir}/MistAnalyserOGG
%{_bindir}/MistAnalyserRIFF
%{_bindir}/MistAnalyserRTMP
%{_bindir}/MistAnalyserRTSP
%{_bindir}/MistAnalyserTS
%{_bindir}/MistController
%{_bindir}/MistInAAC
%{_bindir}/MistInBalancer
%{_bindir}/MistInBuffer
%{_bindir}/MistInDTSC
%{_bindir}/MistInEBML
%{_bindir}/MistInFLAC
%{_bindir}/MistInFLV
%{_bindir}/MistInFolder
%{_bindir}/MistInH264
%{_bindir}/MistInHLS
%{_bindir}/MistInISMV
%{_bindir}/MistInMP3
%{_bindir}/MistInMP4
%{_bindir}/MistInOGG
%{_bindir}/MistInPlaylist
%{_bindir}/MistInRTSP
%{_bindir}/MistInSDP
%{_bindir}/MistInSubRip
%{_bindir}/MistInTS
%{_bindir}/MistInTSRIST
%{_bindir}/MistInTSSRT
%{_bindir}/MistInV4L2
%{_bindir}/MistOutAAC
%{_bindir}/MistOutCMAF
%{_bindir}/MistOutDTSC
%{_bindir}/MistOutEBML
%{_bindir}/MistOutFLAC
%{_bindir}/MistOutFLV
%{_bindir}/MistOutH264
%{_bindir}/MistOutHDS
%{_bindir}/MistOutHLS
%{_bindir}/MistOutHTTP
%{_bindir}/MistOutHTTPMinimalServer
%{_bindir}/MistOutHTTPS
%{_bindir}/MistOutHTTPTS
%{_bindir}/MistOutJPG
%{_bindir}/MistOutJSON
%{_bindir}/MistOutJSONLine
%{_bindir}/MistOutMP3
%{_bindir}/MistOutMP4
%{_bindir}/MistOutOGG
%{_bindir}/MistOutRTMP
%{_bindir}/MistOutRTSP
%{_bindir}/MistOutSDP
%{_bindir}/MistOutSubRip
%{_bindir}/MistOutTS
%{_bindir}/MistOutTSRIST
%{_bindir}/MistOutTSSRT
%{_bindir}/MistOutWAV
%{_bindir}/MistOutWebRTC
%{_bindir}/MistProcFFMPEG
%{_bindir}/MistProcLivepeer
%{_bindir}/MistProcMKVExec
%{_bindir}/MistSession
%{_bindir}/MistTranslateH264
%{_bindir}/MistUtilAMF
%{_bindir}/MistUtilCertbot
%{_bindir}/MistUtilHealth
%{_bindir}/MistUtilLog
%{_bindir}/MistUtilMETA
%{_bindir}/MistUtilNuke
%{_bindir}/MistUtilRAX
%{_bindir}/MistUtilWriter
%{_libdir}/libmist.so
%{_libdir}/libmist_srt.so
%{_sysusersdir}/mistserver.conf
%{_unitdir}/%{name}.service

%files devel
%{_includedir}/mist

%changelog
