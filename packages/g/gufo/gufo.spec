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
Version:        0.37.0
Release:        0
Summary:        Local inference engine for AMD Strix Halo hardware
License:        MIT
URL:            https://github.com/gufo-org/gufo
Source:         v0.37.0.tar.gz#/gufo-%{version}.tar.gz
Source1:        gufo.service
Source2:        90-gufo.preset
Source3:        sysconfig.%{name}
Source4:        gufo-user.conf
#!CreateArchive
Source5:        vendor.tar.zst
#!CreateArchive
Source6:        configs.tar.zst
Source7:        README.SUSE

ExclusiveArch:  x86_64

BuildRequires:  cargo
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
BuildRequires:  libsndfile-devel
BuildRequires:  libswresample-devel
BuildRequires:  libuuid-devel
BuildRequires:  libwebp-devel
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
BuildRequires:  rocblas-devel
BuildRequires:  rocfft-devel
BuildRequires:  rocprim-devel
BuildRequires:  rocwmma-devel
BuildRequires:  soxr-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  xrt-devel
BuildRequires:  zstd
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

%package devel
Summary:        Development files for gufo
Requires:       %{name} = %{version}

%description devel
Development files for gufo, the local inference engine for AMD Strix Halo
hardware. This package contains the files installed under /usr/lib/gufo.

%package npu_xrt
Summary:        AMD NPU support plugin
Requires:       %{name} = %{version}

%description npu_xrt
NPU support for gufo

%prep
%autosetup -p1 -a 5
cp %{SOURCE7} README.SUSE
mv vendor/{.cargo,Cargo.lock,vendor-cargo} .

# disable loom until we have hrx working
sed -i '/gufo_loom_register_tests()/d' CMakeLists.txt
sed -i '/loom/d' extensions.lock
rm -r src/models/loom

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
install -D -m 0644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/gufo@.service
install -D -m 644 %{SOURCE2} %{buildroot}%{_presetdir}/90-gufo.preset
install -D -m 0644 %{SOURCE4} %{buildroot}%{_sysusersdir}/gufo-user.conf

# some template files matching upstream config
mkdir -p %{buildroot}/etc/gufo/
tar xfv %{SOURCE6} --strip-components=1 -C %{buildroot}/etc/gufo/

%pre
%service_add_pre gufo@.service

%post
%sysusers_create gufo-user.conf
%fillup_only -n %{name}
%service_add_post gufo@.service

%preun
%service_del_preun gufo@.service

%postun
if [ $1 -ge 1 ]; then
  %service_del_postun gufo@.service
fi

%files
%doc README.SUSE NOTICE THIRD_PARTY_NOTICES.md docs/
%license LICENSE
%{_bindir}/gufo
%{_bindir}/gufo-server
%{_datadir}/gufo
%{_datadir}/licenses/gufo
%{_unitdir}/gufo@.service
%{_presetdir}/90-gufo.preset
%{_sysusersdir}/gufo-user.conf
%{_fillupdir}/sysconfig.%{name}
%config(noreplace) /etc/gufo

%files npu_xrt
/usr/lib/gufo/libgufo_npu_xrt.so

%files devel
%exclude /usr/lib/gufo/libgufo_npu_xrt.so
/usr/lib/gufo

%changelog
