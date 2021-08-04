#
# spec file for package android-tools
#
# Copyright (c) 2021 SUSE LLC
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
Version:        31.0.2
Release:        0
Summary:        Android platform tools
License:        Apache-2.0 AND MIT
Group:          Hardware/Mobile
URL:            https://developer.android.com/studio/releases/platform-tools
Source0:        https://github.com/nmeum/android-tools/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        vendor.tar.gz
# PATCH-FIX-OPENSUSE fix-pie-build.patch boo#1185883 munix9@googlemail.com -- Build with -fPIE/-pie
Patch0:         fix-pie-build.patch
# PATCH-FIX-OPENSUSE fix-install-completion.patch boo#1185883 munix9@googlemail.com -- Simplify completion
Patch1:         fix-install-completion.patch
# PATCH-FEATURE-OPENSUSE fix-add-e2fsprogs-contrib.patch boo#1185883 munix9@googlemail.com -- Some more e2fsprogs tools
Patch2:         fix-add-e2fsprogs-contrib.patch
# PATCH-FEATURE-OPENSUSE fix-install-python-tools.patch boo#1185883 munix9@googlemail.com -- Some python3 tools
Patch3:         fix-install-python-tools.patch
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
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc10
BuildRequires:  gcc10-c++
%else
BuildRequires:  gcc >= 10
BuildRequires:  gcc-c++ >= 10
%endif

%description
Android SDK Platform-Tools is a component for the Android SDK.
It includes tools that interface with the Android platform.

%package python3
Summary:        Python3 Android platform tools
Group:          Hardware/Mobile
BuildRequires:  python3-protobuf
Requires:       %{name} = %{version}
Requires:       python3
Requires:       python3-protobuf
Supplements:    (%{name} and python3)
BuildArch:      noarch

%description python3
Additional Android platform tools that require python3.

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

install -d -m 0755 %{buildroot}%{_mandir}/man1
for f in adb fastboot
do
    help2man -N %{buildroot}%{_bindir}/${f} | sed -e 's|\(/home/.*\)\(/usr/.*\)|\2|g' \
	> %{buildroot}%{_mandir}/man1/${f}.1
done
for f in aftltool avbtool mkbootimg
do
    help2man -N %{buildroot}%{_bindir}/${f} --version-string="%{version}" \
	> %{buildroot}%{_mandir}/man1/${f}.1
done
rm -r %{buildroot}%{_bindir}/__pycache__

%files
%license LICENSE
%doc README.md
%{_bindir}/adb
%{_bindir}/append2simg
%{_bindir}/e2fsdroid
%{_bindir}/ext2simg
%{_bindir}/fastboot
%{_bindir}/img2simg
%{_bindir}/mke2fs.android
%{_bindir}/simg2img
%{_mandir}/man1/adb.1%{?ext_man}
%{_mandir}/man1/fastboot.1%{?ext_man}

%files python3
%{_bindir}/aftltool{,.py}
%{_bindir}/avbtool{,.py}
%{_bindir}/mkbootimg
%{_mandir}/man1/aftltool.1%{?ext_man}
%{_mandir}/man1/avbtool.1%{?ext_man}
%{_mandir}/man1/mkbootimg.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/adb
%{_datadir}/bash-completion/completions/fastboot

%changelog
