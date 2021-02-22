#
# spec file for package kmod
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


Name:           kmod
%define lname	libkmod2
Version:        28
Release:        0
Summary:        Utilities to load modules into the kernel
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          System/Kernel
URL:            https://www.kernel.org/pub/linux/utils/kernel/kmod/

#Git-Web:	http://git.kernel.org/?p=utils/kernel/kmod/kmod.git;a=summary
#Git-Clone:	git://git.kernel.org/pub/scm/utils/kernel/kmod/kmod
Source:         https://www.kernel.org/pub/linux/utils/kernel/kmod/kmod-%version.tar.xz
Source2:        https://www.kernel.org/pub/linux/utils/kernel/kmod/kmod-%version.tar.sign
Patch1:         0002-modprobe-Recognize-allow-unsupported-modules-on-comm.patch
Patch2:         0003-libkmod-config-Recognize-allow_unsupported_modules-i.patch
Patch3:         0009-libkmod-Implement-filtering-of-unsupported-modules-o.patch
Patch4:         0010-modprobe-Implement-allow-unsupported-modules.patch
Patch5:         0011-Do-not-filter-unsupported-modules-when-running-a-van.patch
Patch6:         0012-modprobe-print-unsupported-status.patch
Patch7:         usr-lib-modprobe.patch
Patch8:         no-stylesheet-download.patch
Patch9:         0001-Fix-modinfo-F-always-shows-name-for-built-ins.patch
Patch10:        0001-libkmod-config-revamp-kcmdline-parsing-into-a-state-.patch
Patch11:        0002-libkmod-config-re-quote-option-from-kernel-cmdline.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  libopenssl-devel >= 1.1.0
BuildRequires:  libtool
BuildRequires:  libxslt-tools
BuildRequires:  pkgconfig >= 0.21
BuildRequires:  xz
BuildRequires:  pkgconfig(liblzma) >= 4.99
BuildRequires:  pkgconfig(zlib)
Requires(post): coreutils
Obsoletes:      kmod-compat < %version-%release
Provides:       kmod-compat = %version-%release
Requires:       suse-module-tools
Obsoletes:      module-init-tools < 3.16
Provides:       module-init-tools = 3.16
Provides:       modutils

%description
kmod is a set of tools to handle common tasks with Linux kernel
modules like insert, remove, list, check properties, resolve
dependencies and aliases.

These tools are designed on top of libkmod, a library that is shipped
with kmod. The aim is to be compatible with tools, configurations and
indexes from module-init-tools project.

%package bash-completion
Summary:        Bash completion routines for the kmod utilities
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          System/Shells
BuildArch:      noarch
Requires:       %{name}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
Contains bash completion support for kmod utilities.

%package -n %lname
Summary:        Library to interact with Linux kernel modules
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n %lname
libkmod was created to allow programs to easily insert, remove and
list modules, also checking its properties, dependencies and aliases.

%package -n libkmod-devel
Summary:        Development files for libkmod
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description -n libkmod-devel
libkmod was created to allow programs to easily insert, remove and
list modules, also checking its properties, dependencies and aliases.

This package contains the development headers for the library found
in %lname.

%prep
%autosetup -p1

%build
autoreconf -fi
export LDFLAGS="-Wl,-z,relro,-z,now"
# The extra --includedir gives us the possibility to detect dependent
# packages which fail to properly use pkgconfig, cf. bugzilla.opensuse.org/795968
%configure \
	--with-xz \
	--with-zlib \
	--with-openssl \
	--includedir="%_includedir/kmod" \
	--with-rootlibdir="%_libdir" \
	--bindir="%_bindir"
make %{?_smp_mflags} V=1

%install
b="%buildroot"
%make_install
rm -f "$b/%_libdir"/*.la

mkdir -p "$b/%_sbindir" "$b/sbin"
for i in depmod insmod lsmod modinfo modprobe rmmod; do
	ln -s "%_bindir/kmod" "$b/%_sbindir/$i"
%if !0%{?usrmerged}
	ln -s "%_bindir/kmod" "$b/sbin/$i"
%endif
done
mkdir -p "$b/%_bindir" "$b/bin"
for i in lsmod; do
	ln -s "%_bindir/kmod" "$b/%_bindir/$i"
%if !0%{?usrmerged}
	ln -s "%_bindir/kmod" "$b/bin/$i"
%endif
done

%post
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_bindir/kmod
%_bindir/lsmod
%_sbindir/depmod
%_sbindir/insmod
%_sbindir/lsmod
%_sbindir/modinfo
%_sbindir/modprobe
%_sbindir/rmmod
%_mandir/man[58]/*.[58]*
%if !0%{?usrmerged}
/bin/lsmod
/sbin/depmod
/sbin/insmod
/sbin/lsmod
/sbin/modinfo
/sbin/modprobe
/sbin/rmmod
%endif

%files bash-completion
%_datadir/bash-completion/

%files -n %lname
%_libdir/libkmod.so.2*

%files -n libkmod-devel
%_includedir/*
%_libdir/pkgconfig/libkmod.pc
%_libdir/libkmod.so

%changelog
