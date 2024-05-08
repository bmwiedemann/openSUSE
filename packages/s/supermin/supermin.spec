#
# spec file for package supermin
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


Name:           supermin
Version:        5.3.3
Release:        0
Summary:        Bootstrapping tool for creating supermin appliances
License:        GPL-3.0-or-later
Group:          System/Filesystems
URL:            https://libguestfs.org/
Source0:        https://download.libguestfs.org/supermin/5.3-development/supermin-5.3.3.tar.gz
Source1:        https://download.libguestfs.org/supermin/5.3-development/supermin-5.3.3.tar.gz.sig
Source9:        supermin.keyring
Patch1:         001-Improved-debugging-of-the-supermin-if-newer-calculation.patch
Patch2:         002-Fix-if-newer-copy-kernel.patch
Patch3:         003-Fix-kernel-filtering-for-aarch64-architecture.patch
Patch4:         004-Use-output-complete-exe-instead-of-custom.patch
Patch5:         005-Only-supply-output-complete-exe-to-final-link.patch
Patch6:         006-Rename-function-file-kernel.patch
Patch7:         007-Uncompress-kernel-on-RISC-V.patch
Patch8:         008-Fix-link-to-renamed-kernel-documentation.patch
Patch9:         009-New-mailing-list-email-address.patch
Patch30:        suse_release.patch
Patch31:        supermin-kernel_version_compressed.patch
Patch32:        disable-test-if-newer-ext2.patch
Patch33:        detect-aarch64-kernel.patch
BuildRequires:  augeas
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  distribution-release
BuildRequires:  e2fsprogs
BuildRequires:  glibc-devel-static
BuildRequires:  gzip
BuildRequires:  hivex
BuildRequires:  kernel-default
BuildRequires:  ncurses-devel
BuildRequires:  ocaml
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml-rpm-macros >= 4.02.1
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  zstd
BuildRequires:  zypper
BuildRequires:  pkgconfig(com_err)
BuildRequires:  pkgconfig(ext2fs)
BuildRequires:  pkgconfig(rpm)
Requires:       distribution-release
Requires:       e2fsprogs
%if 0%{?suse_version} < 1599
Requires:       sysconfig-netconfig
%endif
Requires:       tar
Requires:       xmlstarlet
Requires:       zypper
Provides:       febootstrap
%{?ocaml_preserve_bytecode}
# this must follow libguestfs, which is the only consumer of this pkg
ExclusiveArch:  x86_64 ppc64 ppc64le s390x aarch64 riscv64

%description
supermin is a tool for building supermin appliances. These are tiny
appliances (similar to virtual machines), usually around 100KB in size,
which get fully instantiated on-the-fly in a fraction of a second when
you need to boot one of them.

%prep
%autosetup -p1

%build
export ZYPPER=zypper
export ZYPPER=%{_bindir}/zypper
touch INSTALL NEWS AUTHORS ChangeLog
#.gnulib/gnulib-tool --update
autoreconf -fi
%configure --help
%configure --disable-network-tests
%make_build \
	%{?_smp_mflags}

%install
%make_install
find %{buildroot} -ls

%check
ls -alt /boot /lib/modules || :
ls -altd /lib/modules/*/* || :

for i in /boot/image* /boot/Image* /boot/vmlinu* /boot/zImage*
do
  test -f "$i" || continue
  if get_kernel_version "${i}" > $$
  then
    if test -s $$
    then
      read SUPERMIN_KERNEL_VERSION < $$
      export "SUPERMIN_KERNEL=$i"
      export "SUPERMIN_KERNEL_VERSION=$SUPERMIN_KERNEL_VERSION"
      export "SUPERMIN_MODULES=/lib/modules/${SUPERMIN_KERNEL_VERSION}"
      break
    fi
  fi
done
rm -fv $$
test -n "${SUPERMIN_KERNEL}"
test -n "${SUPERMIN_KERNEL_VERSION}"
test -d "${SUPERMIN_MODULES}"
%ifnarch s390x
if make check
then
  rc=0
else
  : rc $?
  rc=1
fi
cat tests/test-suite.log
exit ${rc}
%endif

%files
%doc README
%doc TODO
%{_bindir}/*
%{_mandir}/*/*

%changelog
