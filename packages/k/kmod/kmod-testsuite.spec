#
# spec file for package kmod-testsuite
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


%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
%define use_zstd 1
%endif

Name:           kmod-testsuite
%define lname	libkmod2
Version:        34.3
Release:        0
Summary:        Testsuite of the kmod package
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Kernel
URL:            https://www.kernel.org/pub/linux/utils/kernel/kmod/
#Git-Web:	http://git.kernel.org/?p=utils/kernel/kmod/kmod.git;a=summary
#Git-Clone:	git://git.kernel.org/pub/scm/utils/kernel/kmod/kmod
Source:         https://www.kernel.org/pub/linux/utils/kernel/kmod/kmod-%version.tar.xz
Source2:        https://www.kernel.org/pub/linux/utils/kernel/kmod/kmod-%version.tar.sign
Source3:        kmod.keyring
Patch1:         0002-modprobe-Recognize-allow-unsupported-modules-on-comm.patch
Patch2:         0003-libkmod-config-Recognize-allow_unsupported_modules-i.patch
Patch3:         0009-libkmod-Implement-filtering-of-unsupported-modules-o.patch
Patch4:         0010-modprobe-Implement-allow-unsupported-modules.patch
Patch5:         0011-Do-not-filter-unsupported-modules-when-running-a-van.patch
Patch6:         0012-modprobe-print-unsupported-status.patch
Patch7:         Revert-build-check-for-__xstat-declarations.patch
Patch8:         riscv-hwprobe.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  kernel-default-devel
BuildRequires:  libopenssl-devel >= 1.1.0
BuildRequires:  meson
BuildRequires:  pkg-config >= 0.21
BuildRequires:  scdoc
BuildRequires:  xz
BuildRequires:  pkgconfig(liblzma) >= 4.99
%if 0%{?use_zstd}
BuildRequires:  zstd
BuildRequires:  pkgconfig(libzstd)
%endif
BuildRequires:  pkgconfig(zlib)
Requires:       suse-module-tools
%if !0%{?is_opensuse}
ExcludeArch:    %ix86 s390
%endif
%define kdir /usr/src/linux-obj/%_target_cpu/default

%description
This spec file does not produce any binary RPMs. It just builds kmod and
runs its testsuite. It has been split off the kmod package to avoid a
buildloop with the kernel.

%prep
%autosetup -p1 -n kmod-%version

%build
rm -f m4/gtk-doc.m4 libkmod/docs/gtk-doc.make # dangling symlinks
touch m4/gtk-doc.m4 libkmod/docs/gtk-doc.make
%set_build_flags
export LDFLAGS="$LDFLAGS -Wl,-z,relro,-z,now"
%meson \
%if !0%{?use_zstd}
	-Dzstd=disabled \
%endif
	-Dmoduledir="%_prefix/lib/modules" -Dbuild-tests=true

export KDIR="%kdir"
%meson_build

%install

%check
result=0
export KDIR="%kdir"
%meson_test || result=$?
find . -name test-suite.log -exec cat "{}" "+"
exit $result

%changelog
