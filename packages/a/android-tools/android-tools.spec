#
# spec file for package android-tools
#
# Copyright (c) 2024 SUSE LLC
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


%define _pyver 3
%if 0%{?sle_version} == 150500 || 0%{?sle_version} == 150600
%define _pyver 311
%endif
%if 0%{?sle_version} == 150400
%define _pyver 310
%endif

%if 0%{?suse_version} < 1600
%define use_bundled_libfmt 1
%endif
# currently libusb with support for SuperSpeed+ is required,
# which is not yet released, so the one bundled is used.
%define use_bundled_libusb 1

Name:           android-tools
Version:        35.0.2
Release:        0
Summary:        Android platform tools
License:        Apache-2.0 AND MIT
URL:            https://developer.android.com/studio/releases/platform-tools
Source0:        https://github.com/nmeum/android-tools/releases/download/%{version}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE fix-install-completion.patch boo#1185883 munix9@googlemail.com -- Simplify completion
Patch0:         fix-install-completion.patch
BuildRequires:  cmake >= 3.12
BuildRequires:  go
BuildRequires:  llvm-gold
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python%{_pyver}
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libunwind-generic)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(zlib)
Requires:       android-udev-rules
Suggests:       %{name}-mkbootimg = %{version}
Suggests:       %{name}-partition = %{version}
Provides:       %{name}-python3 = %{version}-%{release}
Obsoletes:      %{name}-python3 < %{version}-%{release}
ExcludeArch:    s390x
%if 0%{?suse_version} < 1600
BuildRequires:  clang15
BuildRequires:  gcc11-c++
%else
BuildRequires:  clang
%endif
%if %{undefined use_bundled_libfmt}
BuildRequires:  pkgconfig(fmt) >= 10.2.0
%endif
%if %{undefined use_bundled_libusb}
BuildRequires:  pkgconfig(libusb-1.0)
%else
BuildRequires:  pkgconfig(libudev)
%endif

%description
Android SDK Platform-Tools is a component for the Android SDK.
It includes tools that interface with the Android platform.

%package mkbootimg
Summary:        Android boot.img manipulation tools
Requires:       %{name} = %{version}
BuildArch:      noarch

%description mkbootimg
This package contains the Android boot.img manipulation tools.

%package partition
Summary:        Android dynamic partition tools
Requires:       %{name} = %{version}

%description partition
This package contains the Android dynamic partition tools.

%package bash-completion
Summary:        Bash completion for android-tools
BuildRequires:  bash-completion
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for android-tools.

%prep
%autosetup -p1

%build
%define __builder ninja
export GOFLAGS="-buildmode=pie -trimpath -ldflags=-buildid="

%if 0%{?suse_version} < 1600
CMAKE_C_COMPILER=clang-15
CMAKE_CXX_COMPILER=clang++-15
%else
CMAKE_C_COMPILER=clang
CMAKE_CXX_COMPILER=clang++
%endif

%cmake \
	-DCMAKE_C_COMPILER=${CMAKE_C_COMPILER} \
	-DCMAKE_CXX_COMPILER=${CMAKE_CXX_COMPILER} \
%if %{defined use_bundled_libfmt}
	-DANDROID_TOOLS_USE_BUNDLED_FMT=ON \
%endif
%if %{defined use_bundled_libusb}
	-DANDROID_TOOLS_USE_BUNDLED_LIBUSB=ON \
	-DANDROID_TOOLS_LIBUSB_ENABLE_UDEV=ON \
%endif
%ifarch %{ix86}
	-DOPENSSL_NO_ASM=ON \
%endif
	-DBUILD_SHARED_LIBS=OFF

%cmake_build

%install
%cmake_install

# fix link
ln -sf %{_datadir}/%{name}/mkbootimg/mkbootimg.py %{buildroot}%{_bindir}/mkbootimg

# fix non-executable-script
chmod 0755 %{buildroot}%{_datadir}/%{name}/mkbootimg/gki/generate_gki_certificate.py

# fix env-script-interpreter (Leap requires special handling)
%if 0%{?suse_version} < 1600
%define python3_fix_shebang_path(+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-=) \
myargs="%{**}" \
for f in ${myargs}; do \
  [ -f $f ] && sed -i "1s@#\\!.*python.*@#\\!$(realpath %{expand:%{__python%{_pyver}}})@" $f \
done
%endif
%python3_fix_shebang_path %{buildroot}%{_bindir}/*
%python3_fix_shebang_path %{buildroot}%{_datadir}/%{name}/mkbootimg/*
%python3_fix_shebang_path %{buildroot}%{_datadir}/%{name}/mkbootimg/gki/*

%check
# call some tools, e.g. to test python3 compatibility
export PATH=%{buildroot}%{_bindir}:$PATH
export PYTHONDONTWRITEBYTECODE=1
adb --version
fastboot --version
avbtool version
mkbootimg --help

%files
%license LICENSE
%doc README.md
%{_bindir}/adb
%{_bindir}/append2simg
%{_bindir}/avbtool
%{_bindir}/e2fsdroid
%{_bindir}/ext2simg
%{_bindir}/fastboot
%{_bindir}/img2simg
%{_bindir}/make_f2fs
%{_bindir}/mke2fs.android
%{_bindir}/simg2img
%{_bindir}/sload_f2fs
%{_mandir}/man1/adb.1%{?ext_man}

%files mkbootimg
%license LICENSE
%{_bindir}/{mk,repack_,unpack_}bootimg
%{_bindir}/mkdtboimg
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/mkbootimg

%files partition
%license LICENSE
%doc vendor/extras/partition_tools/README.md
%{_bindir}/lp{add,dump,flash,make,unpack}

%files bash-completion
%{_datadir}/bash-completion/completions/adb
%{_datadir}/bash-completion/completions/fastboot

%changelog
