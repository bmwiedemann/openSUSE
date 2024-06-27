#
# spec file for package binutils
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


%define flavor @BUILD_FLAVOR@%{nil}

%if "%{flavor}" != ""
%define cross 1
%define targetarch %(echo %flavor | sed -e 's/i.86/i586/;s/ppc/powerpc/')
%define TARGET %targetarch

# Spec parsing does not support execution of external command,
# that's why we use the if-else chain.
%if "%{flavor}" == "i386"
ExcludeArch:    %ix86
%else
%if "%{flavor}" == "arm"
ExcludeArch:    %arm
%else
ExcludeArch:    %{flavor}
%endif
%endif

%endif

%if "%{flavor}" == ""
Name:           binutils
%else
Name:           cross-%{flavor}-binutils
%endif

BuildRequires:  bc
BuildRequires:  bison
BuildRequires:  dejagnu
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
# for the testsuite
%if 0%{suse_version} >= 1210
BuildRequires:  glibc-devel-static
%endif
%if 0%{suse_version} > 1220
BuildRequires:  makeinfo
%endif
%if 0%{suse_version} > 1110
BuildRequires:  zlib-devel-static
%else
BuildRequires:  zlib-devel
%endif
%if %{suse_version} > 1500
BuildRequires:  libzstd-devel
%endif
Version:        2.42
Release:        0

# disable libalternatives for now until it's changed to not
# introduce cmake/cunit-tests into the bootstrap cycle
%if 0 && 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%bcond_without bootstrap

#
# RUN_TESTS
%define run_tests %(test ! -f %_sourcedir/RUN_TESTS ; echo $?)
# check the vanilla binutils, with no patches applied
# TEST_VANILLA
%define test_vanilla %(test ! -f %_sourcedir/TEST_VANILLA ; echo $?)
#
# handle test suite failures
#
%ifarch alpha %arm aarch64 hppa mips sh4 %sparc
%define	make_check_handling	true
%else
# XXX check again
# XXX disabled because gold is seriously broken for now
# Note that some gold tests fail due to gcc-PIE which leads PIE executables
%define	make_check_handling	true
%endif
# let make check fail anyway if RUN_TESTS was requested
%if %{run_tests}
%define	make_check_handling	false
%endif
# handle all binary object formats supported by SUSE (and a few more)
%ifarch %ix86 %arm aarch64 ia64 ppc ppc64 ppc64le riscv64 s390 s390x x86_64 %x86_64
%define build_multitarget 1
%else
%define build_multitarget 0
%endif
%define target_list aarch64 alpha armv5l armv6l armv7l armv8l avr pru epiphany hppa hppa64 i686 ia64 m68k mips powerpc powerpc64 powerpc64le riscv64 rx s390 s390x sh4 sparc sparc64 x86_64 xtensa

%define build_gprofng 0

%if %{suse_version} > 1500
%ifarch aarch64 %ix86 x86_64 %x86_64
%define build_gprofng 1
%endif
%endif

#
#
#
URL:            https://www.gnu.org/software/binutils/
PreReq:         %{install_info_prereq}
# bug437293
%ifarch ppc64
Obsoletes:      binutils-64bit
%endif
#
Summary:        GNU Binutils
License:        GFDL-1.3-only AND GPL-3.0-or-later
Group:          Development/Tools/Building
Source:         binutils-%{version}.tar.bz2
Source2:        binutils-%{version}.tar.bz2.sig
Source3:        binutils.keyring
Source4:        baselibs.conf
Patch1:         binutils-2.42-branch.diff.gz
Patch3:         binutils-skip-rpaths.patch
Patch4:         s390-biarch.diff
Patch5:         x86-64-biarch.patch
Patch6:         unit-at-a-time.patch
Patch8:         ld-relro.diff
Patch9:         testsuite.diff
Patch10:        enable-targets-gold.diff
Patch12:        s390-pic-dso.diff
Patch14:        binutils-build-as-needed.diff
Patch15:        binutils-znow.patch
Patch22:        binutils-bfd_h.patch
Patch34:        aarch64-common-pagesize.patch
Patch37:        binutils-revert-plt32-in-branches.diff
Patch38:        binutils-fix-invalid-op-errata.diff
Patch39:        binutils-revert-nm-symversion.diff
Patch40:        binutils-fix-abierrormsg.diff
Patch41:        binutils-fix-relax.diff
Patch42:        binutils-compat-old-behaviour.diff
Patch43:        binutils-revert-hlasm-insns.diff
Patch44:        binutils-revert-rela.diff
Patch60:        binutils-disable-code-arch-error.diff
Patch61:        riscv-no-relax.patch
Patch90:        cross-avr-nesc-as.patch
Patch92:        cross-avr-omit_section_dynsym.patch
Patch93:        cross-avr-size.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{with libalternatives}
Requires:       alts
%else
PreReq:         update-alternatives
%endif

%description
C compiler utilities: ar, as, gprof, ld, nm, objcopy, objdump, ranlib,
size, strings, and strip. These utilities are needed whenever you want
to compile a program or kernel.

%package gold
Summary:        The gold linker
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
Requires:       binutils = %{version}-%{release}
%if %{with libalternatives}
Requires:       alts
%else
PreReq:         update-alternatives
%endif
%if 0%{!?cross:1} && 0%{?suse_version} >= 1310
%define gold_archs %ix86 aarch64 %arm x86_64 %x86_64 ppc ppc64 ppc64le s390x %sparc
%endif

%description gold
gold is an ELF linker.	It is intended to have complete support for ELF
and to run as fast as possible on modern systems.  For normal use it is
a drop-in replacement for the older GNU linker.

%package devel
Summary:        GNU binutils (BFD development files)
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       binutils = %{version}-%{release}
Requires:       zlib-devel
%if %{suse_version} > 1500
Requires:       libzstd-devel
%endif
Provides:       binutils:/usr/include/bfd.h

%description devel
This package includes header files and static libraries necessary to
build programs which use the GNU BFD library, which is part of
binutils.

%package -n libctf0
Summary:        Compact C Type Format library (runtime, BFD dependency)
License:        GFDL-1.3-only AND GPL-3.0-or-later
Group:          Development/Tools/Building

%description -n libctf0
This package includes the libctf shared library.
The Compact C Type Format (CTF) is a way of representing information about a binary program

%package -n libctf-nobfd0
Summary:        Compact C Type Format library (runtime, no BFD dependency)
License:        GFDL-1.3-only AND GPL-3.0-or-later
Group:          Development/Tools/Building

%description -n libctf-nobfd0
This package includes the libctf-nobfd shared library.
The Compact C Type Format (CTF) is a way of representing information about a binary program

%package -n gprofng
Summary:        The next generation profiling tool for Linux
License:        GFDL-1.3-only AND GPL-3.0-or-later
Group:          Development/Tools/Building

%description -n gprofng
The next generation profiling tool for Linux

%ifarch %arm
%define HOST %{_target_cpu}-suse-linux-gnueabi
%else
%define HOST %(echo %{_target_cpu} | sed -s -e "s/x86_64_v./x86_64/" -e "s/parisc/hppa/" -e "s/i.86/i586/" -e "s/ppc/powerpc/" -e "s/sparc64v.*/sparc64/" -e "s/sparcv.*/sparc/")-suse-linux
%endif
%define DIST %(echo '%distribution' | sed 's/ (.*)//')

%if 0%{suse_version} >= 1500
# Synchronize output by lines, useful for configure output
%define make_output_sync -Oline
%endif

%prep
echo "make check will return with %{make_check_handling} in case of testsuite failures."
%setup -q -n binutils-%{version}

# Backup flex and biscon files for later verification.
cp ld/ldlex.l ld/ldlex.l.orig
cp ld/ldgram.y ld/ldgram.y.orig

# Patch is outside test_vanilla because it's supposed to be the
# patch bringing the tarball to the newest upstream version
%patch -P 1 -p1
%if !%{test_vanilla}
%patch -P 3 -p1
%patch -P 4
%patch -P 5
%patch -P 6
%patch -P 8
%patch -P 9
%patch -P 10
%patch -P 12
%patch -P 14
%patch -P 15
%patch -P 22
%patch -P 34 -p1
%if %{suse_version} < 1550
%patch -P 37 -p1
%endif
%patch -P 38
%patch -P 39 -p1
%patch -P 40 -p1
%patch -P 41 -p1
%if %{suse_version} < 1550
%patch -P 42 -p1
%patch -P 43 -p1
%patch -P 44 -p1
%endif
%patch -P 60 -p1
%patch -P 61 -p1
%if "%{TARGET}" == "avr"
cp gas/config/tc-avr.h gas/config/tc-avr-nesc.h
%patch -P 90
%patch -P 92
%patch -P 93 -p1
%endif
#
# test_vanilla
%endif

# Due to legacy flex version present in SLE-12 (and older), we cannot
# re-generate flex and bison files and so we verify that any patch modify these files.
diff -u ld/ldlex.l ld/ldlex.l.orig
diff -u ld/ldgram.y ld/ldgram.y.orig

%build
%define _lto_cflags %{nil}
sed -i -e '/BFD_VERSION_DATE/s/$/-%(echo %release | sed 's/\.[0-9]*$//')/' bfd/version.h
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wno-error"

%if 0%{!?cross:1}
# Building native binutils
echo "Building native binutils."
%if %build_multitarget
EXTRA_TARGETS="%(printf ,%%s-suse-linux %target_list)"
EXTRA_TARGETS="$EXTRA_TARGETS,powerpc-macos,powerpc-macos10,spu-elf,x86_64-pep,bpf-none"
%else
EXTRA_TARGETS=
%ifarch sparc
EXTRA_TARGETS="$EXTRA_TARGETS,sparc64-suse-linux"
%endif
%ifarch ppc
EXTRA_TARGETS="$EXTRA_TARGETS,powerpc64-suse-linux"
%endif
%ifarch s390
EXTRA_TARGETS="$EXTRA_TARGETS,s390x-suse-linux"
%endif
%ifarch s390x
EXTRA_TARGETS="$EXTRA_TARGETS,s390-suse-linux"
%endif
%ifarch %ix86
EXTRA_TARGETS="$EXTRA_TARGETS,x86_64-suse-linux"
%endif
%ifarch ppc ppc64 ppc64le
EXTRA_TARGETS="$EXTRA_TARGETS,spu-elf"
%endif
%ifarch %arm
EXTRA_TARGETS="$EXTRA_TARGETS,arm-suse-linux-gnueabi"
%endif
%ifarch aarch64
EXTRA_TARGETS="$EXTRA_TARGETS,aarch64-suse-linux"
%endif
%endif
# Normally we'd like to add --enable-deterministic-archives
# here (which by default makes uid/mtime be zero for archive
# members), to increase chances of getting a reproducable build
# But this breaks Makefile rules when directly accessing archives:
# rebuilding the same archive from unchanged .o files recreates
# it, because timestamps in the .a are 0, unequal to the actual timestamp
# of the .o files :-/
#
# Enable the following 2 configure options explicitly
# (--enable-warn-execstack=yes, --enable-warn-rwx-segments=yes)
# as they are not enabled by default for some targets (and we use --enable-targets=[many]).
%define common_flags CFLAGS="${RPM_OPT_FLAGS}" CXXFLAGS="${RPM_OPT_FLAGS}" \\\
	--prefix=%{_prefix} --libdir=%{_libdir} \\\
	--infodir=%{_infodir} --mandir=%{_mandir} \\\
	--with-bugurl=https://bugs.opensuse.org/ \\\
	--with-pkgversion="GNU Binutils; %{DIST}" \\\
	--with-separate-debug-dir=%{_prefix}/lib/debug \\\
	--with-pic --with-system-zlib --build=%{HOST}
mkdir build-dir
cd build-dir
../configure %common_flags \
	${EXTRA_TARGETS:+--enable-targets="${EXTRA_TARGETS#,}"} \
	--enable-plugins \
%ifarch %gold_archs
	--enable-gold \
	--enable-threads \
%endif
%if %{suse_version} <= 1320
	CXX="g++ -std=gnu++11" \
	--disable-x86-relax-relocations \
	--disable-compressed-debug-sections \
%endif
%if %{suse_version} > 1320
	--enable-compressed-debug-sections=gas \
%endif
%if %{suse_version} < 1550
	--disable-x86-used-note \
	--disable-separate-code \
%endif
	--enable-new-dtags \
%if "%{TARGET}" != "mips"
	--enable-default-hash-style=both \
%endif
	--enable-shared \
%if %{suse_version} > 1500
%if %{with bootstrap} && 0%{?do_profiling}
	--enable-pgo-build=lto \
%endif
	--enable-colored-disassembly \
%endif
%if ! %build_gprofng
	--disable-gprofng \
%endif
	--enable-obsolete \
	--enable-warn-execstack=yes \
	--enable-warn-rwx-segments=yes

#FIXME: enable in the future
#%if %{suse_version} > 1550
#  --enable-default-compressed-debug-sections-algorithm=zstd \
#%endif

# we patch headers (bfd-in.h) that are input to other headers
# which are generated only with --enable-maintainer-mode (which we
# don't do) or explicitely by make headers, so do this:
make %{?make_output_sync} %{?_smp_mflags} all-bfd TARGET-bfd=headers V=1
# the above interacts with --enable-pgo-build=lto because all-bfd doesn't
# have the PGO handling, hence it's config.cache files are wrong
# remove all of those for reconfigure
rm */config.cache
# force reconfiguring
rm bfd/Makefile
make %{?make_output_sync} %{?_smp_mflags} V=1

%else
# building cross-TARGET-binutils
echo "Building cross binutils."
mkdir build-dir
cd build-dir
EXTRA_TARGETS=
%if "%{TARGET}" == "sparc"
EXTRA_TARGETS="$EXTRA_TARGETS,sparc64-suse-linux"
%endif
%if "%{TARGET}" == "powerpc"
EXTRA_TARGETS="$EXTRA_TARGETS,powerpc64-suse-linux"
%endif
%if "%{TARGET}" == "s390"
EXTRA_TARGETS="$EXTRA_TARGETS,s390x-suse-linux"
%endif
%if "%{TARGET}" == "s390x"
EXTRA_TARGETS="$EXTRA_TARGETS,s390-suse-linux"
%endif
%if "%{TARGET}" == "i586"
EXTRA_TARGETS="$EXTRA_TARGETS,x86_64-suse-linux"
%endif
%if "%{TARGET}" == "hppa"
EXTRA_TARGETS="$EXTRA_TARGETS,hppa64-suse-linux"
%endif
%if "%{TARGET}" == "arm"
EXTRA_TARGETS="$EXTRA_TARGETS,arm-suse-linux-gnueabi"
%endif
%if "%{TARGET}" == "aarch64"
EXTRA_TARGETS="$EXTRA_TARGETS,aarch64-suse-linux"
%endif
%if "%{TARGET}" == "avr" || "%{TARGET}" == "spu" || "%{TARGET}" == "pru"
%define TARGET_OS %{TARGET}
%else
%if "%{TARGET}" == "epiphany" || "%{TARGET}" == "riscv32" || "%{TARGET}" == "rx"
%define TARGET_OS %{TARGET}-elf
%else
%if "%{TARGET}" == "arm"
%define TARGET_OS %{TARGET}-suse-linux-gnueabi
%else
%if "%{TARGET}" == "bpf"
%define TARGET_OS %{TARGET}-none
%else
%define TARGET_OS %{TARGET}-suse-linux
%endif
%endif
%endif
%endif
../configure CFLAGS="${RPM_OPT_FLAGS}" \
  --prefix=%{_prefix} \
  --with-bugurl=https://bugs.opensuse.org/ \
  --with-pkgversion="GNU Binutils; %{DIST}" \
  --with-system-zlib \
  --disable-nls \
  --enable-new-dtags \
	--enable-obsolete \
	--disable-gprofng \
%if %{suse_version} <= 1320
  --disable-x86-relax-relocations \
%endif
  --build=%{HOST} --target=%{TARGET_OS} \
%if "%{TARGET}" == "spu"
  --with-sysroot=/usr/spu \
%else
  --with-sysroot=%{_prefix}/%{TARGET_OS}/sys-root \
%endif
%if "%{TARGET}" != "mips"
  --enable-default-hash-style=both \
%endif
  ${EXTRA_TARGETS:+--enable-targets="${EXTRA_TARGETS#,}"}
make %{?make_output_sync} %{?_smp_mflags} all-bfd TARGET-bfd=headers V=1
rm */config.cache
# force reconfiguring
rm bfd/Makefile
make %{?make_output_sync} %{?_smp_mflags} V=1
%if "%{TARGET}" == "avr"
# build an extra nesC version because nesC requires $'s in identifiers
cp -a gas gas-nesc
echo '#include "tc-%{TARGET}-nesc.h"' > gas-nesc/targ-cpu.h
make -C gas-nesc clean
make -C gas-nesc %{?make_output_sync} %{?_smp_mflags}
%endif
%endif

%check
unset SUSE_ASNEEDED
# newer distros set this envvar (e.g. to get deterministic archives by default)
# but of course that breaks tests that precisely are
# designed for checking file replacement in archives based on mtime.
# just get rid of it for the binutils testsuite
unset SOURCE_DATE_EPOCH
cd build-dir
%if 0%{?cross:1}
make -k check CFLAGS="-O2 -g" CXXFLAGS="-O2 -g" CFLAGS_FOR_TARGET="-O2 -g" CXXFLAGS_FOR_TARGET="-O2 -g" || %{make_check_handling}
%else
# _FORTIFY_SOURCE does not work with -O0
make -k check CFLAGS="-g $RPM_OPT_FLAGS -U_FORTIFY_SOURCE" CXXFLAGS="-g $RPM_OPT_FLAGS -U_FORTIFY_SOURCE" CFLAGS_FOR_TARGET="-g $RPM_OPT_FLAGS -U_FORTIFY_SOURCE" CXXFLAGS_FOR_TARGET="-g $RPM_OPT_FLAGS -U_FORTIFY_SOURCE" || %{make_check_handling}
%endif

%install
cd build-dir
%if 0%{!?cross:1}
# installing native binutils
%ifarch %gold_archs
make DESTDIR=%{buildroot} install-gold
ln -sf ld.gold %{buildroot}%{_bindir}/gold
%endif
make DESTDIR=%{buildroot} install-info install
make DESTDIR=%{buildroot} install-bfd install-opcodes
if [ ! -f "%{buildroot}/%_bindir/ld.bfd" ]; then
  mv "%{buildroot}/%_bindir"/{ld,ld.bfd};
else
  rm -f "%{buildroot}/%_bindir/ld";
fi
%if ! 0%{with libalternatives}
mkdir -p "%{buildroot}/%_sysconfdir/alternatives";
# Keep older versions of brp-symlink happy
%if %{suse_version} < 1310
ln -s "%_bindir/ld" "%{buildroot}/%_sysconfdir/alternatives/ld"
%endif
ln -s "%_sysconfdir/alternatives/ld" "%{buildroot}/%_bindir/ld";
%else
ln -s %{_bindir}/alts "%{buildroot}/%_bindir/ld";
mkdir -p %{buildroot}%{_datadir}/libalternatives/ld;
cat > %{buildroot}%{_datadir}/libalternatives/ld/1.conf <<EOF
binary=%{_bindir}/ld.gold
EOF
cat > %{buildroot}%{_datadir}/libalternatives/ld/2.conf <<EOF
binary=%{_bindir}/ld.bfd
EOF
%endif

rm -rf %{buildroot}%{_prefix}/%{HOST}/bin
mkdir -p %{buildroot}%{_prefix}/%{HOST}/bin
ln -sf ../../bin/{ar,as,ld,nm,ranlib,strip} %{buildroot}%{_prefix}/%{HOST}/bin
mv %{buildroot}%{_prefix}/%{HOST}/lib/ldscripts $RPM_BUILD_ROOT%{_libdir}
rm -f $RPM_BUILD_ROOT%{_libdir}/ldscripts/stamp
ln -sf ../../%{_lib}/ldscripts %{buildroot}%{_prefix}/%{HOST}/lib/ldscripts
# Install header files
make -C libiberty install_to_libdir target_header_dir=/usr/include DESTDIR=%{buildroot}
# We want the PIC libiberty.a
install -m 644 libiberty/pic/libiberty.a %{buildroot}%{_libdir}
#
chmod a+x %{buildroot}%{_libdir}/libbfd-*
chmod a+x %{buildroot}%{_libdir}/libopcodes-*
# No shared linking outside binutils
rm %{buildroot}%{_libdir}/lib{bfd,opcodes}.so
rm %{buildroot}%{_libdir}/lib{bfd,opcodes,ctf,ctf-nobfd}.la
rm -f %{buildroot}%{_libdir}/gprofng/lib*.{l,}a
# Remove unwanted files to shut up rpm
rm -f %{buildroot}%{_infodir}/configure* $RPM_BUILD_ROOT%{_infodir}/standards.info*
rm -f %{buildroot}%{_mandir}/man1/dlltool.1 $RPM_BUILD_ROOT%{_mandir}/man1/windres.1 $RPM_BUILD_ROOT%{_mandir}/man1/windmc.1
cd ..
%find_lang binutils
%find_lang bfd binutils.lang
%find_lang gas binutils.lang
%find_lang ld binutils.lang
%find_lang opcodes binutils.lang
%find_lang gprof binutils.lang
%ifarch %gold_archs
%find_lang gold binutils-gold.lang
%endif
mkdir -p %{buildroot}%{_docdir}/%{name}
install -m 644 binutils/NEWS %{buildroot}%{_docdir}/%{name}/NEWS-binutils
install -m 644 gas/NEWS %{buildroot}%{_docdir}/%{name}/NEWS-gas
install -m 644 ld/NEWS %{buildroot}%{_docdir}/%{name}/NEWS-ld
%else
# installing cross-TARGET-binutils and TARGET-binutils
make DESTDIR=%{buildroot} install
# Replace hard links by symlinks, so that rpmlint doesn't complain
T=$(basename %{buildroot}/usr/%{TARGET_OS})
for f in %{buildroot}/usr/$T/bin/* ; do
   ln -sf /usr/bin/$T-$(basename $f) $f
done
%if "%{TARGET}" == "arm"
# Instead of building duplicate binutils, add symlinks
for f in %{buildroot}%{_bindir}/${T}-* ; do
  _toolname=${f##$(dirname $f)/${T}-}
  for p in arm-none-eabi; do
    ln -sf %{_bindir}/$T-${_toolname} %{buildroot}%{_bindir}/$p-${_toolname}
  done
done
%endif
%if "%{TARGET}" == "riscv64"
# Instead of building duplicate binutils, add symlinks
for f in %{buildroot}/usr/$T/bin/* ; do
  for p in riscv64-elf; do
    ln -sf %{_bindir}/$T-$(basename $f) %{buildroot}%{_bindir}/$p-$(basename $f)
  done
done
%endif
%if "%{TARGET}" == "avr"
install -c gas-nesc/as-new %{buildroot}%{_prefix}/bin/%{TARGET_OS}-nesc-as
ln -sf ../../bin/%{TARGET_OS}-nesc-as %{buildroot}%{_prefix}/%{TARGET_OS}/bin/nesc-as
%endif
rm -rf %{buildroot}%{_mandir}
rm -rf %{buildroot}%{_infodir}
rm -rf %{buildroot}%{_prefix}/lib*
rm -rf %{buildroot}%{_prefix}/include
rm -f %{buildroot}%{_prefix}/bin/*-c++filt
> ../binutils.lang
%endif
%fdupes %{buildroot}%{_prefix}

%if 0%{!?cross:1}
%post
/sbin/ldconfig
%if ! %{with libalternatives}
"%_sbindir/update-alternatives" --install \
	"%_bindir/ld" ld "%_bindir/ld.bfd" 2
%endif
%install_info --info-dir=%{_infodir} %{_infodir}/as.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/bfd.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/binutils.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/gprof.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/ld.info.gz

%if ! %{with libalternatives}
%post gold
"%_sbindir/update-alternatives" --install \
	"%_bindir/ld" ld "%_bindir/ld.gold" 1
%endif

%post -n libctf0 -p /sbin/ldconfig
%post -n libctf-nobfd0 -p /sbin/ldconfig

%if %{with libalternatives}
%pre
# removing old update-alternatives entries
if [ "$1" -gt 0 ] && [ -f %{_sbindir}/update-alternatives ] ; then
	"%_sbindir/update-alternatives" --remove ld "%_bindir/ld.bfd";
fi;

%pre gold
# removing old update-alternatives entries
if [ "$1" -gt 0 ] && [ -f %{_sbindir}/update-alternatives ] ; then
	"%_sbindir/update-alternatives" --remove ld "%_bindir/ld.gold";
fi;
%endif

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/as.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/bfd.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/binutils.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gprof.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/ld.info.gz
%if ! %{with libalternatives}
if [ "$1" = 0 ]; then
	"%_sbindir/update-alternatives" --remove ld "%_bindir/ld.bfd";
fi;
%endif

%if ! %{with libalternatives}
%preun gold
if [ "$1" = 0 ]; then
	"%_sbindir/update-alternatives" --remove ld "%_bindir/ld.gold";
fi;
%endif

%postun -n libctf0 -p /sbin/ldconfig
%postun -n libctf-nobfd0 -p /sbin/ldconfig

%postun -p /sbin/ldconfig
%endif

%files -f binutils.lang
%defattr(-,root,root)
%if 0%{!?cross:1}
%{_docdir}/%{name}
%{_prefix}/%{HOST}/bin/*
%{_prefix}/%{HOST}/lib/ldscripts
%{_libdir}/ldscripts
%{_libdir}/libsframe.so.*
%if %build_gprofng
%{_libdir}/libgprofng.so.*
%endif
%dir %{_libdir}/bfd-plugins
%{_libdir}/bfd-plugins/libdep.so
%{_bindir}/*
%if ! 0%{with libalternatives}
%ghost %_sysconfdir/alternatives/ld
%else
%dir %{_datadir}/libalternatives
%dir %{_datadir}/libalternatives/ld
%{_datadir}/libalternatives/ld/2.conf
%endif
%ifarch %gold_archs
%exclude %{_bindir}/gold
%exclude %{_bindir}/ld.gold
%endif
%doc %{_infodir}/*.gz
%{_libdir}/lib*-%{version}*.so
%doc %{_mandir}/man1/*.1.gz
%else
%{_prefix}/%{TARGET_OS}
%{_prefix}/bin/*
%endif

%ifarch %gold_archs
%files gold -f binutils-gold.lang
%defattr(-,root,root)
%doc gold/NEWS gold/README
%{_bindir}/gold
%{_bindir}/ld.gold
%if %{with libalternatives}
%dir %{_datadir}/libalternatives
%dir %{_datadir}/libalternatives/ld
%{_datadir}/libalternatives/ld/1.conf
%endif
%endif

%if 0%{!?cross:1}
%files devel
%defattr(-,root,root)
%{_prefix}/include/*.h
%{_libdir}/lib*.*a
%{_libdir}/libctf.so
%{_libdir}/libctf-nobfd.so
%{_libdir}/libsframe.so
%if %build_gprofng
%{_libdir}/libgprofng.so
%endif

%files -n libctf0
%defattr(-,root,root)
%{_libdir}/libctf.so.*

%files -n libctf-nobfd0
%defattr(-,root,root)
%{_libdir}/libctf-nobfd.so.*

%if %{suse_version} > 1500
%ifarch %ix86 x86_64 %x86_64 aarch64
%files -n gprofng
%defattr(-,root,root)
%dir %{_libdir}/gprofng/
%{_libdir}/gprofng/lib*.so
%{_distconfdir}/gprofng.rc
%endif
%endif

%endif

%changelog
