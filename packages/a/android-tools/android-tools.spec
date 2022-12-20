#
# spec file for package android-tools
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


%if 0%{?suse_version} <= 1500
%if 0%{?sle_version} >= 150400
%define _pyn 310
%define _pyd 3.10
%else
%define _pyn 39
%define _pyd 3.9
%endif
%else
%define _pyn 3
%define _pyd 3
%endif

Name:           android-tools
Version:        33.0.3p2
Release:        0
Summary:        Android platform tools
License:        Apache-2.0 AND MIT
URL:            https://developer.android.com/studio/releases/platform-tools
Source0:        https://github.com/nmeum/android-tools/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        vendor.tar.gz
Source2:        man-pages.tar.gz
# PATCH-FIX-OPENSUSE fix-install-completion.patch boo#1185883 munix9@googlemail.com -- Simplify completion
Patch0:         fix-install-completion.patch
BuildRequires:  clang
BuildRequires:  cmake >= 3.12
BuildRequires:  go
BuildRequires:  gtest
BuildRequires:  llvm-gold
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python%{_pyn}
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libunwind-generic)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(protobuf)
Requires:       android-udev-rules
Requires:       python%{_pyn}
Suggests:       %{name}-mkbootimg = %{version}
Suggests:       %{name}-partition = %{version}
Provides:       %{name}-python3 = %{version}-%{release}
Obsoletes:      %{name}-python3 < %{version}-%{release}
ExcludeArch:    s390x
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc11-c++
%endif

%description
Android SDK Platform-Tools is a component for the Android SDK.
It includes tools that interface with the Android platform.

%package mkbootimg
Summary:        Android boot.img manipulation tools
Requires:       %{name} = %{version}
Requires:       python%{_pyn}
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
%autosetup -a2 -p1
tar xf %{SOURCE1} -C vendor/boringssl

# fix env-script-interpreter
sed -e '1s|^#!.*|#!/usr/bin/python%{_pyd}|' -i vendor/avb/avbtool.py \
	vendor/mkbootimg/{mk,repack_,unpack_}bootimg.py \
	vendor/mkbootimg/gki/generate_gki_certificate.py \
	vendor/libufdt/utils/src/mkdtboimg.py

%build
%define __builder ninja
export GOFLAGS="-mod=vendor -buildmode=pie -trimpath"

%cmake \
	-DBUILD_SHARED_LIBS=OFF		\
	-DCMAKE_C_COMPILER=clang	\
	-DCMAKE_CXX_COMPILER=clang++
%cmake_build

%install
%cmake_install

# fix non-executable-script
chmod 0755 %{buildroot}%{_datadir}/%{name}/mkbootimg/gki/generate_gki_certificate.py

# man pages
install -d -m 0755 %{buildroot}%{_mandir}
cp -a man/man1 %{buildroot}%{_mandir}

%check
# call some tools to test python3 compatibility
export PATH=%{buildroot}%{_bindir}:$PATH
export PYTHONDONTWRITEBYTECODE=1
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
%{_bindir}/mke2fs.android
%{_bindir}/simg2img
%{_mandir}/man1/adb.1%{?ext_man}
%{_mandir}/man1/avbtool.1%{?ext_man}
%{_mandir}/man1/fastboot.1%{?ext_man}

%files mkbootimg
%license LICENSE
%{_bindir}/{mk,repack_,unpack_}bootimg
%{_bindir}/mkdtboimg
%{_mandir}/man1/{mk,repack_,unpack_}bootimg.1%{?ext_man}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/mkbootimg

%files partition
%license LICENSE
%doc vendor/extras/partition_tools/README.md
%{_bindir}/lp{add,dump,flash,make,unpack}
%{_mandir}/man1/lp{add,dump,flash,make,unpack}.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/adb
%{_datadir}/bash-completion/completions/fastboot

%changelog
