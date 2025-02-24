#
# spec file for the Linux Kernel Library
#
# Copyright (c) 2023 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#
# Please submit bugfixes or comments via https://bugs.opensuse.org/
#

Name:           lkl
# Downstream made-up version number, reflects corrseponding kernel version.
Version:        0.6.4+git.d156fd7786d
Release:        0
Summary:        EXPERIMENTAL: Linux Kernel Library (LKL) utilities
License:        GPL-2.0-only
Group:          System/Kernel
Url:            https://lkl.github.io
Source:         %{name}-%{version}.tar.zst
Source1:        61-lklfuse.rules
Source2:        lklfuse-mount@.service
Patch1:		0001-tools-build-Fix-s-detection-code-in-tools-build-Make.patch
# regular Linux kernel build dependencies
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150300
BuildRequires:  bash-sh
%endif
BuildRequires:  bc
BuildRequires:  bison
BuildRequires:  coreutils
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  hmaccalc
BuildRequires:  libopenssl-devel
BuildRequires:  libelf-devel
BuildRequires:  elfutils
# install target invokes arch/lkl/scripts/headers_install.py
BuildRequires:  python3
# lkl binary dependencies
BuildRequires:  fuse3-devel
BuildRequires:  libarchive-devel
BuildRequires:  zstd

%description
LKL (Linux Kernel Library) is aiming to allow reusing the Linux kernel code as
extensively as possible with minimal effort and reduced maintenance overhead.

Examples of how LKL can be used are: creating userspace applications (running on
Linux and other operating systems) that can read or write Linux filesystems or
can use the Linux networking stack, creating kernel drivers for other operating
systems that can read Linux filesystems, bootloaders support for reading/writing
Linux filesystems, etc.

With LKL, the kernel code is compiled into an object file that can be directly
linked by applications. The API offered by LKL is based on the Linux system call
interface.

WARNING: LKL is EXPERIMENTAL; using it could cause data corruption!

%package -n lklfuse
Summary:	EXPERIMENTAL: Access storage via an unprivileged user process
Requires:	shadow
BuildRequires:	shadow
Provides:	group(lklfuse)
Provides:	user(lklfuse)

%description -n lklfuse
WARNING: lklfuse is EXPERIMENTAL; using it could cause data corruption!

lklfuse builds upon the Linux Kernel Library (LKL) to reuse kernel filesystem
drivers as part of an unprivileged user-space application.

A udev rule and corresponding systemd user service are provided to
automatically mount connected USB block devices.

%package -n liblkl0
Summary:	EXPERIMENTAL: Library package for the Linux Kernel Library

%description -n liblkl0
Shared-object dependencies for the Linux Kernel Library (LKL).

WARNING: LKL is EXPERIMENTAL; using it could cause data corruption!

%package devel
Summary:	EXPERIMENTAL: Development package for the Linux Kernel Library
Requires:	liblkl0 = %{version}-%{release}

%description devel
Development package for the Linux Kernel Library (LKL). With LKL, the kernel
code is compiled into an object file that can be directly linked by
applications. The API offered by LKL is based on the Linux system call
interface.

WARNING: LKL is EXPERIMENTAL; using it could cause data corruption!

%package test
Summary:	Various test binaries for the Linux Kernel Library (LKL)

%description test
Boot, network and disk I/O test binaries for the Linux Kernel Library (LKL).

WARNING: LKL is EXPERIMENTAL; using it could cause data corruption!

%prep
%autosetup -p1

%build
# for reproducible builds results (boo#1237474)
export KBUILD_BUILD_TIMESTAMP=$(date -d @${SOURCE_DATE_EPOCH:-$(stat --format=%%Y COPYING)})
export KBUILD_BUILD_USER=geeko
export KBUILD_BUILD_HOST=buildhost

# TODO: binaries are statically linked against liblkl.a
#       there should be an option link against liblkl.so
%make_build -C tools/lkl KCONFIG=opensuse_defconfig

%install
%make_install -C tools/lkl \
        BINDIR=%{_bindir} \
        INCDIR=%{_includedir} \
        LIBDIR=%{_libdir}

# TODO: so versioning should be done upstream
mv %{buildroot}/%{_libdir}/liblkl.so %{buildroot}/%{_libdir}/liblkl.so.0
mv %{buildroot}/%{_libdir}/liblkl-hijack.so %{buildroot}/%{_libdir}/liblkl-hijack.so.0
mv %{buildroot}/%{_libdir}/liblkl-zpoline.so %{buildroot}/%{_libdir}/liblkl-zpoline.so.0

ln -s liblkl.so.0 %{buildroot}/%{_libdir}/liblkl.so
ln -s liblkl-hijack.so.0 %{buildroot}/%{_libdir}/liblkl-hijack.so
ln -s liblkl-zpoline.so.0 %{buildroot}/%{_libdir}/liblkl-zpoline.so

# TODO: cpfromfs link should be done upstream
ln -s cptofs %{buildroot}/%{_bindir}/cpfromfs

rm %{buildroot}/%{_libdir}/liblkl.a

install -m 0644 -D %{SOURCE1} %{buildroot}/%{_udevrulesdir}/61-lklfuse.rules
install -m 0644 -D %{SOURCE2} %{buildroot}/%{_unitdir}/lklfuse-mount@.service

%check
# tests aren't installed so we need to be in the correct _builddir path
tools/lkl/tests/boot

%pre -n lklfuse
getent group lklfuse >/dev/null || groupadd -r lklfuse
getent passwd lklfuse >/dev/null || \
  useradd -g lklfuse --no-create-home -r -s /sbin/nologin lklfuse

%post -n lklfuse
cat >> %{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}-something << EOF

WARNING: lklfuse is EXPERIMENTAL; using it could cause data corruption!

EOF

%post -n liblkl0 -p /sbin/ldconfig
%postun -n liblkl0 -p /sbin/ldconfig

%files -n lklfuse
# TODO: manpage
%{_bindir}/lklfuse
%{_udevrulesdir}/61-lklfuse.rules
%{_unitdir}/lklfuse-mount@.service

%files -n liblkl0
%attr(0755, root, root) %{_libdir}/*.so.0

%files devel
%license COPYING
%license LICENSES/preferred/GPL-2.0
%license LICENSES/exceptions/Linux-syscall-note
%license Documentation/process/license-rules.rst
%doc Documentation/lkl.txt
%{_libdir}/*.so
%{_includedir}/*

%files test
# could put following in with lklfuse, but don't want to cause confusion...
%{_bindir}/cptofs
%{_bindir}/cpfromfs
%{_bindir}/fs2tar

%changelog
