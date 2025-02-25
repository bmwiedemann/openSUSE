#
# spec file for package kmod
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

Name:           kmod
%define lname	libkmod2
Version:        34
Release:        0
Summary:        Utilities to load modules into the kernel
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Kernel
URL:            https://www.kernel.org/pub/linux/utils/kernel/kmod/

#Git-Web:	http://git.kernel.org/?p=utils/kernel/kmod/kmod.git;a=summary
#Git-Clone:	git://git.kernel.org/pub/scm/utils/kernel/kmod/kmod
Source:         https://www.kernel.org/pub/linux/utils/kernel/kmod/kmod-%version.tar.xz
Source2:        https://www.kernel.org/pub/linux/utils/kernel/kmod/kmod-%version.tar.sign
Source3:        %name.keyring
Source4:        README.usrmerge
Patch1:         0002-modprobe-Recognize-allow-unsupported-modules-on-comm.patch
Patch2:         0003-libkmod-config-Recognize-allow_unsupported_modules-i.patch
Patch3:         0009-libkmod-Implement-filtering-of-unsupported-modules-o.patch
Patch4:         0010-modprobe-Implement-allow-unsupported-modules.patch
Patch5:         0011-Do-not-filter-unsupported-modules-when-running-a-van.patch
Patch6:         0012-modprobe-print-unsupported-status.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libopenssl-devel >= 1.1.0
BuildRequires:  libtool
BuildRequires:  pkg-config >= 0.21
BuildRequires:  scdoc
BuildRequires:  xz
BuildRequires:  pkgconfig(liblzma) >= 4.99
%if 0%{?use_zstd}
BuildRequires:  pkgconfig(libzstd)
Provides:       kmod-zstd
%endif
BuildRequires:  pkgconfig(zlib)
Requires(post): coreutils
Obsoletes:      kmod-compat < %version-%release
Provides:       kmod-compat = %version-%release
# kmod and libkmod have no dependency but we want to provide
# same features across kmod provided tools and tools linking to libkmod
Conflicts:      %lname < %version-%release
Conflicts:      %lname > %version-%release
Requires:       suse-module-tools
Obsoletes:      module-init-tools < 3.16
Provides:       module-init-tools = 3.16
Provides:       modutils
Obsoletes:      %name-bash-completion < %version-%release
Provides:       %name-bash-completion = %version-%release

%description
kmod is a set of tools to handle common tasks with Linux kernel
modules like insert, remove, list, check properties, resolve
dependencies and aliases.

These tools are designed on top of libkmod, a library that is shipped
with kmod. The aim is to be compatible with tools, configurations and
indexes from module-init-tools project.

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
cp %{SOURCE4} .

%build
rm -f m4/gtk-doc.m4 libkmod/docs/gtk-doc.make # dangling symlinks
touch m4/gtk-doc.m4 libkmod/docs/gtk-doc.make
GTKDOCIZE=/bin/true autoreconf -fi
export LDFLAGS="-Wl,-z,relro,-z,now"
# The extra --includedir gives us the possibility to detect dependent
# packages which fail to properly use pkgconfig, cf. bugzilla.opensuse.org/795968
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
%make_build

%install
b="%buildroot"
%make_install
rm -f "$b/%_libdir"/*.la
mkdir -p "$b/%_bindir" "$b/bin"
for i in lsmod; do
	ln -s "%_bindir/kmod" "$b/%_bindir/$i"
%if 0%{?suse_version} < 1550
	ln -s "%_bindir/kmod" "$b/bin/$i"
%endif
done

%post
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%ldconfig_scriptlets -n %lname

%files
%if 0%{?suse_version} > 1500
%doc README.usrmerge
%endif
%_bindir/kmod
%_bindir/lsmod
%_sbindir/depmod
%_sbindir/insmod
%_sbindir/lsmod
%_sbindir/modinfo
%_sbindir/modprobe
%_sbindir/rmmod
%_mandir/man[58]/*.[58]*
%_datadir/pkgconfig/kmod.pc
%if 0%{?suse_version} < 1550
/bin/lsmod
/sbin/depmod
/sbin/insmod
/sbin/lsmod
/sbin/modinfo
/sbin/modprobe
/sbin/rmmod
%endif
%_datadir/bash-completion/
%_datadir/fish/
%_datadir/zsh/

%files -n %lname
%_libdir/libkmod.so.2*

%files -n libkmod-devel
%_includedir/*
%_libdir/pkgconfig/libkmod.pc
%_libdir/libkmod.so

%changelog
