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


Name:           android-tools
Version:        31.0.3p1
Release:        0
Summary:        Android platform tools
License:        Apache-2.0 AND MIT
Group:          Hardware/Mobile
URL:            https://developer.android.com/studio/releases/platform-tools
Source0:        https://github.com/nmeum/android-tools/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        vendor.tar.gz
# PATCH-FIX-OPENSUSE fix-install-completion.patch boo#1185883 munix9@googlemail.com -- Simplify completion
Patch0:         fix-install-completion.patch
# PATCH-FEATURE-OPENSUSE fix-add-e2fsprogs-contrib.patch boo#1185883 munix9@googlemail.com -- Some more e2fsprogs tools
Patch1:         fix-add-e2fsprogs-contrib.patch
# PATCH-FIX-OPENSUSE fix-add-functional-include.patch munix9@googlemail.com -- Fix gcc 12 build
Patch2:         fix-add-functional-include.patch
BuildRequires:  cmake >= 3.1
BuildRequires:  go
BuildRequires:  gtest
BuildRequires:  help2man
BuildRequires:  ninja
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libunwind-generic)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(protobuf)
Requires:       android-udev-rules
Requires:       python3
Suggests:       %{name}-mkbootimg = %{version}
Suggests:       %{name}-partition = %{version}
Provides:       %{name}-python3 = %{version}-%{release}
Obsoletes:      %{name}-python3 < %{version}-%{release}
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc10
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc-c++
%endif

%description
Android SDK Platform-Tools is a component for the Android SDK.
It includes tools that interface with the Android platform.

%package mkbootimg
Summary:        Android boot.img manipulation tools
Group:          Hardware/Mobile
Requires:       %{name} = %{version}
Requires:       python3
BuildArch:      noarch

%description mkbootimg
This package contains the Android boot.img manipulation tools.

%package partition
Summary:        Android dynamic partition tools
Group:          Hardware/Mobile
Requires:       %{name} = %{version}

%description partition
This package contains the Android dynamic partition tools.

%package bash-completion
Summary:        Bash completion for android-tools
Group:          Hardware/Mobile
BuildRequires:  bash-completion
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for android-tools.

%prep
%autosetup -p1
tar xf %{SOURCE1} -C vendor/boringssl

# fix env-script-interpreter
sed -e '1s|^#!.*|#!/usr/bin/python3|' -i vendor/avb/avbtool.py \
	vendor/mkbootimg/{mk,repack_,unpack_}bootimg.py

%build
%define __builder ninja
%if 0%{?suse_version} <= 1500
export CC=gcc-10
export CXX=g++-10
%endif
export CFLAGS="%{optflags} -fPIE -Wno-return-type"
export CXXFLAGS="$CFLAGS"
export LDFLAGS="-pie"
export GOFLAGS="-mod=vendor -buildmode=pie -trimpath"
%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build

%install
%cmake_install

# install avbtool
cp -pd vendor/avb/avbtool{,.py} %{buildroot}%{_bindir}

# generate man pages
export PATH=%{buildroot}%{_bindir}:$PATH
install -d -m 0755 %{buildroot}%{_mandir}/man1
for f in adb fastboot
do
    help2man -N %{buildroot}%{_bindir}/${f} | sed -e 's|\(/home/.*\)\(/usr/.*\)|\2|g' \
	> %{buildroot}%{_mandir}/man1/${f}.1
done
for f in lp{add,dump,flash,unpack}
do
    help2man -N --no-discard-stderr --help-option="-h" --version-string="%{version}" \
	${f} > %{buildroot}%{_mandir}/man1/${f}.1
done
for f in avbtool {mk,repack_,unpack_}bootimg
do
    help2man -N --version-string="%{version}" ${f} > %{buildroot}%{_mandir}/man1/${f}.1
done

%files
%license LICENSE
%doc README.md
%{_bindir}/adb
%{_bindir}/append2simg
%{_bindir}/avbtool{,.py}
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
%{_mandir}/man1/{mk,repack_,unpack_}bootimg.1%{?ext_man}

%files partition
%license LICENSE
%doc vendor/extras/partition_tools/README.md
%{_bindir}/lp{add,dump,flash,make,unpack}
%{_mandir}/man1/lp{add,dump,flash,unpack}.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/adb
%{_datadir}/bash-completion/completions/fastboot

%changelog
