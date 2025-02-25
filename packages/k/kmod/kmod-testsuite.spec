#
# spec file for package kmod-testsuite
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


%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
%define use_zstd 1
%endif

Name:           kmod-testsuite
%define lname	libkmod2
Version:        34
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
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  kernel-default-devel
BuildRequires:  libopenssl-devel >= 1.1.0
BuildRequires:  libtool
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
%setup -q -n kmod-%version
%autopatch -p1

%build
rm -f m4/gtk-doc.m4 libkmod/docs/gtk-doc.make # dangling symlinks
touch m4/gtk-doc.m4 libkmod/docs/gtk-doc.make
GTKDOCIZE=/bin/true autoreconf -fi
export LDFLAGS="-Wl,-z,relro,-z,now"
# The extra --includedir gives us the possibility to detect dependent
# packages which fail to properly use pkgconfig.
%configure \
	--with-xz \
	--with-zlib \
	--with-openssl \
%if 0%{?use_zstd}
	--with-zstd \
%endif
	--includedir="%_includedir/kmod" \
	--with-rootlibdir="%_libdir" \
%if 0%{?suse_version} > 1500
	--with-module-directory="%_prefix/lib/modules" \
%endif
	--bindir="%_bindir"
%make_build KDIR="%kdir"

%install
# empty

%check
%ifarch ppc64
make check V=1 KDIR="%kdir" || echo "Warning: bypass boo#897845"
%else
make check V=1 KDIR="%kdir"
%endif

%changelog
