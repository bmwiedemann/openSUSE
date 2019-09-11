#
# spec file for package cross-rx-binutils
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cross-rx-binutils
ExcludeArch:    rx
%define cross 1
%define TARGET rx
BuildRequires:  bison
BuildRequires:  dejagnu
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
Version:        2.32
Release:        0
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
%define	make_check_handling	true
%endif
# let make check fail anyway if RUN_TESTS was requested
%if %{run_tests}
%define	make_check_handling	false
%endif
# handle all binary object formats supported by SuSE (and a few more)
%ifarch %ix86 %arm aarch64 ia64 ppc ppc64 ppc64le s390 s390x x86_64
%define build_multitarget 1
%else
%define build_multitarget 0
%endif
%define target_list aarch64 alpha armv5l armv6l armv7l armv8l hppa hppa64 i686 ia64 m68k mips powerpc powerpc64 powerpc64le riscv64 s390 s390x sh4 sparc sparc64 x86_64
#
#
#
Url:            http://www.gnu.org/software/binutils/
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
Source4:        binutils-%{version}.tar.bz2.sig
Source5:        binutils.keyring
Source1:        pre_checkin.sh
Source2:        README.First-for.SuSE.packagers
Source3:        baselibs.conf
Patch3:         binutils-skip-rpaths.patch
Patch4:         s390-biarch.diff
Patch5:         x86-64-biarch.patch
Patch6:         unit-at-a-time.patch
Patch8:         ld-relro.diff
Patch9:         testsuite.diff
Patch10:        enable-targets-gold.diff
Patch12:        s390-pic-dso.diff
Patch14:        binutils-build-as-needed.diff
Patch22:        binutils-bfd_h.patch
Patch34:        aarch64-common-pagesize.patch
Patch36:        binutils-pr22868.diff
Patch37:        binutils-revert-plt32-in-branches.diff
Patch38:        riscv-abi-check.patch
Patch39:        rx-gas-padding-pr24464.patch
Patch40:        binutils-pr24486.patch
Patch90:        cross-avr-nesc-as.patch
Patch92:        cross-avr-omit_section_dynsym.patch
Patch93:        cross-avr-size.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
PreReq:         update-alternatives

%description
C compiler utilities: ar, as, gprof, ld, nm, objcopy, objdump, ranlib,
size, strings, and strip. These utilities are needed whenever you want
to compile a program or kernel.


%package gold
Summary:        The gold linker
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
Requires:       binutils = %{version}-%{release}
PreReq:         update-alternatives
%if 0%{suse_version} > 1100
%if 0%{!?cross:1}
%define gold_archs %ix86 aarch64 %arm x86_64 ppc ppc64 ppc64le s390x %sparc
%endif
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
Provides:       binutils:/usr/include/bfd.h

%description devel
This package includes header files and static libraries necessary to
build programs which use the GNU BFD library, which is part of
binutils.


%ifarch %arm
%define HOST %{_target_cpu}-suse-linux-gnueabi
%else
%define HOST %(echo %{_target_cpu} | sed -e "s/parisc/hppa/" -e "s/i.86/i586/" -e "s/ppc/powerpc/" -e "s/sparc64v.*/sparc64/" -e "s/sparcv.*/sparc/")-suse-linux
%endif 
%define DIST %(echo '%distribution' | sed 's/ (.*)//')

%prep
echo "make check will return with %{make_check_handling} in case of testsuite failures."
%setup -q -n binutils-%{version}
# Patch is outside test_vanilla because it's supposed to be the
# patch bringing the tarball to the newest upstream version
%if !%{test_vanilla}
%patch3
%patch4
%patch5
%patch6
%patch8
%patch9
%patch10
%patch12
%patch14
%patch22
%patch34 -p1
%patch36 -p1
%if %{suse_version} < 1550
%patch37 -p1
%endif
%patch38 -p1
%patch39 -p1
%patch40 -p1
%if "%{TARGET}" == "avr"
cp gas/config/tc-avr.h gas/config/tc-avr-nesc.h
%patch90
%patch92
%patch93
%endif
#
# test_vanilla
%endif

%build
sed -i -e '/BFD_VERSION_DATE/s/$/-%(echo %release | sed 's/\.[0-9]*$//')/' bfd/version.h
RPM_OPT_FLAGS="$RPM_OPT_FLAGS -Wno-error -ffat-lto-objects"

%if 0%{!?cross:1}
# Building native binutils
echo "Building native binutils." 
%if %build_multitarget
EXTRA_TARGETS="%(printf ,%%s-suse-linux %target_list)"
EXTRA_TARGETS="$EXTRA_TARGETS,powerpc-macos,powerpc-macos10,spu-elf,x86_64-pep"
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
%define common_flags CFLAGS="${RPM_OPT_FLAGS}" CXXFLAGS="${RPM_OPT_FLAGS}" \\\
	--prefix=%{_prefix} --libdir=%{_libdir} \\\
	--infodir=%{_infodir} --mandir=%{_mandir} \\\
	--with-bugurl=http://bugs.opensuse.org/ \\\
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
	--disable-x86-relax-relocations \
	--disable-compressed-debug-sections \
%endif
%if %{suse_version} > 1320
	--enable-compressed-debug-sections=gas \
%endif
%if %{suse_version} < 1550
	--disable-separate-code \
%endif
	--enable-new-dtags \
%if "%{TARGET}" != "mips"
	--enable-default-hash-style=both \
%endif
	--enable-shared
make %{?_smp_mflags} all-bfd TARGET-bfd=headers
# force reconfiguring (???)
rm bfd/Makefile
make %{?_smp_mflags}

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
%if "%{TARGET}" == "avr" || "%{TARGET}" == "spu"
%define TARGET_OS %{TARGET}
%else
%if "%{TARGET}" == "epiphany" || "%{TARGET}" == "riscv32" || "%{TARGET}" == "rx"
%define TARGET_OS %{TARGET}-elf
%else
%if "%{TARGET}" == "arm"
%define TARGET_OS %{TARGET}-suse-linux-gnueabi
%else
%define TARGET_OS %{TARGET}-suse-linux
%endif
%endif
%endif
../configure CFLAGS="${RPM_OPT_FLAGS}" \
  --prefix=%{_prefix} \
  --with-bugurl=http://bugs.opensuse.org/ \
  --with-pkgversion="GNU Binutils; %{DIST}" \
  --with-system-zlib \
  --disable-nls \
  --enable-new-dtags \
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
make %{?_smp_mflags} all-bfd TARGET-bfd=headers
# force reconfiguring
rm bfd/Makefile
make %{?_smp_mflags}
%if "%{TARGET}" == "avr"
# build an extra nesC version because nesC requires $'s in identifiers
cp -a gas gas-nesc
echo '#include "tc-%{TARGET}-nesc.h"' > gas-nesc/targ-cpu.h
make -C gas-nesc clean
make -C gas-nesc %{?_smp_mflags}
%endif
%endif

%check
unset SUSE_ASNEEDED
cd build-dir
%if 0%{?cross:1}
make -k check CFLAGS="-O2 -g" CXXFLAGS="-O2 -g" || %{make_check_handling}
%else
make -k check CFLAGS="$RPM_OPT_FLAGS -Wno-unused -Wno-unprototyped-calls" || :
%endif

%install
cd build-dir
%if 0%{!?cross:1}
# installing native binutils
%ifarch %gold_archs
make DESTDIR=$RPM_BUILD_ROOT install-gold
ln -sf ld.gold $RPM_BUILD_ROOT%{_bindir}/gold
%endif
make DESTDIR=$RPM_BUILD_ROOT install-info install
make -C gas/doc DESTDIR=$RPM_BUILD_ROOT install-info-am install-am
make DESTDIR=$RPM_BUILD_ROOT install-bfd install-opcodes
if [ ! -f "%buildroot/%_bindir/ld.bfd" ]; then
  mv "%buildroot/%_bindir"/{ld,ld.bfd};
else
  rm -f "%buildroot/%_bindir/ld";
fi
mkdir -p "%buildroot/%_sysconfdir/alternatives";
# Keep older versions of brp-symlink happy
%if %{suse_version} < 1310
ln -s "%_bindir/ld" "%buildroot/%_sysconfdir/alternatives/ld"
%endif
ln -s "%_sysconfdir/alternatives/ld" "%buildroot/%_bindir/ld";
rm -rf $RPM_BUILD_ROOT%{_prefix}/%{HOST}/bin
mkdir -p $RPM_BUILD_ROOT%{_prefix}/%{HOST}/bin
ln -sf ../../bin/{ar,as,ld,nm,ranlib,strip} $RPM_BUILD_ROOT%{_prefix}/%{HOST}/bin
mv $RPM_BUILD_ROOT%{_prefix}/%{HOST}/lib/ldscripts $RPM_BUILD_ROOT%{_libdir}
ln -sf ../../%{_lib}/ldscripts $RPM_BUILD_ROOT%{_prefix}/%{HOST}/lib/ldscripts
# Install header files
make -C libiberty install_to_libdir target_header_dir=/usr/include DESTDIR=$RPM_BUILD_ROOT
# We want the PIC libiberty.a
install -m 644 libiberty/pic/libiberty.a $RPM_BUILD_ROOT%{_libdir}
#
chmod a+x $RPM_BUILD_ROOT%{_libdir}/libbfd-*
chmod a+x $RPM_BUILD_ROOT%{_libdir}/libopcodes-*
# No shared linking outside binutils
rm $RPM_BUILD_ROOT%{_libdir}/lib{bfd,opcodes}.so
rm $RPM_BUILD_ROOT%{_libdir}/lib{bfd,opcodes}.la
# Remove unwanted files to shut up rpm
rm -f $RPM_BUILD_ROOT%{_infodir}/configure* $RPM_BUILD_ROOT%{_infodir}/standards.info*
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/dlltool.1 $RPM_BUILD_ROOT%{_mandir}/man1/windres.1 $RPM_BUILD_ROOT%{_mandir}/man1/windmc.1
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
mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}
install -m 644 binutils/NEWS $RPM_BUILD_ROOT%{_docdir}/%{name}/NEWS-binutils
install -m 644 gas/NEWS $RPM_BUILD_ROOT%{_docdir}/%{name}/NEWS-gas
install -m 644 ld/NEWS $RPM_BUILD_ROOT%{_docdir}/%{name}/NEWS-ld
%else
# installing cross-TARGET-binutils and TARGET-binutils
make DESTDIR=$RPM_BUILD_ROOT install
# Replace hard links by symlinks, so that rpmlint doesn't complain
T=$(basename %buildroot/usr/%{TARGET_OS})
for f in %buildroot/usr/$T/bin/* ; do
   ln -sf /usr/bin/$T-$(basename $f) $f
done
%if "%{TARGET}" == "arm"
# Instead of building duplicate binutils, add symlinks
for f in %buildroot/usr/$T/bin/* ; do
  for p in arm-none-eabi; do
    ln -sf %{_bindir}/$T-$(basename $f) %buildroot%{_bindir}/$p-$(basename $f)
  done
done
%endif
%if "%{TARGET}" == "riscv64"
# Instead of building duplicate binutils, add symlinks
for f in %buildroot/usr/$T/bin/* ; do
  for p in riscv64-elf; do
    ln -sf %{_bindir}/$T-$(basename $f) %buildroot%{_bindir}/$p-$(basename $f)
  done
done
%endif
%if "%{TARGET}" == "avr"
install -c gas-nesc/as-new $RPM_BUILD_ROOT%{_prefix}/bin/%{TARGET_OS}-nesc-as
ln -sf ../../bin/%{TARGET_OS}-nesc-as $RPM_BUILD_ROOT%{_prefix}/%{TARGET_OS}/bin/nesc-as
%endif
rm -rf $RPM_BUILD_ROOT%{_mandir}
rm -rf $RPM_BUILD_ROOT%{_infodir}
rm -rf $RPM_BUILD_ROOT%{_prefix}/lib*
rm -rf $RPM_BUILD_ROOT%{_prefix}/include
rm -f $RPM_BUILD_ROOT%{_prefix}/bin/*-c++filt
> ../binutils.lang
%endif

%if 0%{!?cross:1}
%post
/sbin/ldconfig
"%_sbindir/update-alternatives" --install \
	"%_bindir/ld" ld "%_bindir/ld.bfd" 2
%install_info --info-dir=%{_infodir} %{_infodir}/as.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/bfd.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/binutils.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/gprof.info.gz
%install_info --info-dir=%{_infodir} %{_infodir}/ld.info.gz

%post gold
"%_sbindir/update-alternatives" --install \
	"%_bindir/ld" ld "%_bindir/ld.gold" 1

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/as.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/bfd.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/binutils.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/gprof.info.gz
%install_info_delete --info-dir=%{_infodir} %{_infodir}/ld.info.gz
if [ "$1" = 0 ]; then
	"%_sbindir/update-alternatives" --remove ld "%_bindir/ld.bfd";
fi;

%preun gold
if [ "$1" = 0 ]; then
	"%_sbindir/update-alternatives" --remove ld "%_bindir/ld.gold";
fi;

%postun
/sbin/ldconfig
%endif

%files -f binutils.lang
%defattr(-,root,root)
%if 0%{!?cross:1}
%{_docdir}/%{name}
%{_prefix}/%{HOST}/bin/*
%{_prefix}/%{HOST}/lib/ldscripts
%{_libdir}/ldscripts
%{_bindir}/*
%ghost %_sysconfdir/alternatives/ld
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
%endif

%if 0%{!?cross:1}
%files devel
%defattr(-,root,root)
%{_prefix}/include/*.h
%{_libdir}/lib*.*a
%endif

%changelog
