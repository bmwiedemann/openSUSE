#
# spec file for package android-tools
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


%if 0%{?suse_version} < 1600
%bcond_without  bundled_libfmt
%bcond_without  bundled_libusb
%else
%bcond_with     bundled_libfmt
%bcond_with     bundled_libusb
%endif

Name:           android-tools
Version:        36.0.1
Release:        0
Summary:        Android platform tools
License:        Apache-2.0 AND MIT
# https://developer.android.com/tools/releases/platform-tools
URL:            https://github.com/nmeum/android-tools
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE fix-install-completion.patch boo#1185883 munix9@googlemail.com -- Simplify completion
Patch0:         fix-install-completion.patch
# PATCH-FIX-OPENSUSE fix-mdns-references.patch munix9@googlemail.com -- Remove all references to mDNS from the man page
Patch1:         fix-mdns-references.patch
BuildRequires:  cmake >= 3.12
BuildRequires:  llvm-gold
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libunwind-generic)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(protobuf) >= 21
BuildRequires:  pkgconfig(zlib)
Suggests:       %{name}-mkbootimg
Suggests:       %{name}-partition
Suggests:       android-udev-rules
Provides:       %{name}-bash-completion = %{version}
Obsoletes:      %{name}-bash-completion < %{version}
Provides:       %{name}-python3 = %{version}
Obsoletes:      %{name}-python3 < %{version}
Provides:       adb = 1.0.41
Provides:       avbtool = 1.3.0
Provides:       sload_f2fs = 1.16.0
Provides:       bundled(boringssl)
ExcludeArch:    ppc ppc64 ppc64le s390x
%if 0%{?suse_version} < 1600
BuildRequires:  clang15
BuildRequires:  gcc11-c++
BuildRequires:  python311-base
Requires:       python311-base
%else
BuildRequires:  clang
BuildRequires:  python3-base
Requires:       python3-base
%endif
%if %{with bundled_libfmt}
Provides:       bundled(fmt) = 11.0.2
%else
BuildRequires:  pkgconfig(fmt) >= 11.0.2
%endif
%if %{with bundled_libusb}
BuildRequires:  pkgconfig(libudev)
Provides:       bundled(libusb-1_0) = 1.0.29
%else
BuildRequires:  pkgconfig(libusb-1.0) >= 1.0.29
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

%prep
%autosetup -p1

# fix empty adb man page title
%define man_date %(LC_ALL=C date -u -d@$SOURCE_DATE_EPOCH '+%%B %%Y')
sed -e 's/^\.TH .*/.TH ADB "1" "%{man_date}" "%{name} %{version}" "User Commands"/' \
    -i vendor/adb/docs/user/adb.1

%build
%define __builder ninja
%cmake \
%if 0%{?suse_version} < 1600
	-DCMAKE_C_COMPILER=clang-15 \
	-DCMAKE_CXX_COMPILER=clang++-15 \
%else
	-DCMAKE_C_COMPILER=clang \
	-DCMAKE_CXX_COMPILER=clang++ \
%endif
%ifarch %{ix86}
	-DOPENSSL_NO_ASM=ON \
%endif
%if %{with bundled_libfmt}
	-DANDROID_TOOLS_USE_BUNDLED_FMT=ON \
%endif
%if %{with bundled_libusb}
	-DANDROID_TOOLS_USE_BUNDLED_LIBUSB=ON \
	-DANDROID_TOOLS_LIBUSB_ENABLE_UDEV=ON \
%endif
	-DBUILD_SHARED_LIBS=OFF
%cmake_build

%install
%cmake_install

# fix link
ln -sf %{_datadir}/%{name}/mkbootimg/mkbootimg.py %{buildroot}%{_bindir}/mkbootimg

# fix non-executable-script
chmod 0755 %{buildroot}%{_datadir}/%{name}/mkbootimg/gki/generate_gki_certificate.py

# fix env-script-interpreter (Leap < 16.0 requires special handling)
%if 0%{?suse_version} < 1600
%define python3_fix_shebang_path(+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-=) \
myargs="%{**}" \
for f in ${myargs}; do \
  [ -f $f ] && sed -i "1s@#\\!.*python.*@#\\!$(realpath %{__python311})@" $f \
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
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%if 0%{?suse_version} < 1600
%exclude %{_datadir}/bash-completion/completions/adb
%else
%{_datadir}/bash-completion/completions/adb
%endif
%{_datadir}/bash-completion/completions/fastboot
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

%changelog
