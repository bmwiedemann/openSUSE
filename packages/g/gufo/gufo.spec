#
# spec file for package gufo
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           gufo
Version:        0.7.1
Release:        0
Summary:        Local inference engine for AMD Strix Halo hardware
License:        MIT
URL:            https://github.com/gufo-org/gufo
Source:         %name-%{version}.tar.gz
Source1:        gufo-server.service
Source2:        90-gufo-server.preset
Source3:        sysconfig.%{name}-server
Source4:        gufo-user.conf

ExclusiveArch:  x86_64

# gcc 16 is incompatible atm
%define gcc_version 15
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  gcc%{gcc_version}-c++
BuildRequires:  hipblas-devel
BuildRequires:  hipblaslt-devel
BuildRequires:  hipcub-devel
BuildRequires:  libavcodec-devel
BuildRequires:  libavformat-devel
BuildRequires:  libavutil-devel
BuildRequires:  libicu-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libswresample-devel
BuildRequires:  libwebp-devel
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  rocblas-devel
BuildRequires:  rocfft-devel
BuildRequires:  rocprim-devel
BuildRequires:  rocwmma-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  group(render)
BuildRequires:  group(video)
Requires:       group(render)
Requires:       group(video)
%sysusers_requires
Requires(pre):  %fillup_prereq
%systemd_ordering

%description
Gufo is a vertical local inference engine specifically built and optimized
for AMD Strix Halo hardware (Ryzen AI MAX+ 395 systems with Radeon 8060S).
It provides high-performance model serving with support for Qwen3.8, DeepSeek
V4 Flash, MiniMax H3, Qwen3-TTS, and other models.

%prep
%autosetup -p1

%build
export CXX="g++-%gcc_version"
export CXXFLAGS="$CXXFLAGS -fPIC"
%cmake \
    -DCMAKE_HIP_FLAGS="--gcc-install-dir=%_libdir/gcc/%{_target_cpu}-suse-linux/%gcc_version" \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DBUILD_TESTING=OFF \
    -DGUFO_BUILD_TOOLS=OFF \
    -DROCM_PATH=%{_libdir}/rocm \
    -DENGINE_ENABLE_HIP=ON
%cmake_build

%install
%cmake_install
install -D -m 0644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.%{name}-server
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/gufo-server.service
install -D -m 644 %{SOURCE2} %{buildroot}%{_presetdir}/90-gufo-server.preset
install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/gufo-user.conf

%post
%service_add_post gufo-server.service
%fillup_only -n %{name}-server
%sysusers_create gufo-user.conf

%preun
%service_del_preun gufo-server.service

%postun
if [ $1 -ge 1 ]; then
  %service_del_postun gufo-server.service
fi

%files
%doc LICENSE NOTICE THIRD_PARTY_NOTICES.md docs/
%license LICENSE
%{_bindir}/gufo
%{_bindir}/gufo-server
%{_datadir}/gufo
%{_datadir}/licenses/gufo
%{_unitdir}/gufo-server.service
%{_presetdir}/90-gufo-server.preset
%{_sysusersdir}/gufo-user.conf
%{_fillupdir}/sysconfig.%{name}-server

%changelog
