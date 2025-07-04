#
# spec file for package rpm
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%{?!_fillupdir:%define _fillupdir /var/adm/fillup-templates}

%global librpmsover 10

Name:           rpm
BuildRequires:  binutils
BuildRequires:  bzip2
BuildRequires:  cmake
BuildRequires:  file-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel
BuildRequires:  gzip
BuildRequires:  libacl-devel
BuildRequires:  libarchive-devel
BuildRequires:  libbz2-devel
BuildRequires:  libcap-devel
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libselinux-devel
BuildRequires:  libsemanage-devel
BuildRequires:  libtool
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  patch
BuildRequires:  perl-base
BuildRequires:  popt-devel
BuildRequires:  rpm-build
BuildRequires:  xz-devel
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
#!BuildIgnore:  rpmlint-Factory
Provides:       rpminst
Requires(post): %fillup_prereq
Requires:       rpm-config-SUSE
Summary:        The RPM Package Manager
License:        GPL-2.0-or-later
Group:          System/Packages
Version:        4.20.1
Release:        0
URL:            https://rpm.org/
#Git-Clone:     https://github.com/rpm-software-management/rpm
Source:         https://ftp.osuosl.org/pub/rpm/releases/rpm-4.20.x/rpm-%{version}.tar.bz2
#Git-Clone:     https://github.com/rpm-software-management/rpmpgp_legacy
Source1:        rpmpgp_legacy-1.1.tar.gz
Source5:        rpmsort
Source8:        rpmconfigcheck
Source9:        sysconfig.services-rpm
Source12:       baselibs.conf
Source13:       rpmconfigcheck.service
Source14:       build-aux.tar.bz2
# quilt patches start here
Patch5:         usr-lib-sysimage-rpm.patch
Patch13:        ignore-auxv.diff
Patch12:        localetag.diff
Patch18:        refreshtestarch.diff
Patch24:        brp.diff
Patch25:        brpcompress.diff
Patch26:        checkfilesnoinfodir.diff
Patch29:        findlang.diff
Patch30:        macrosin.diff
Patch32:        platformin.diff
Patch33:        rpmpopt.diff
Patch34:        rpmrc.diff
Patch36:        rpmqpack.diff
Patch38:        build.diff
Patch43:        rpm-shorten-changelog.diff
Patch46:        remove-brp-strips.diff
Patch51:        specfilemacro.diff
Patch60:        safeugid.diff
Patch61:        noprereqdeprec.diff
Patch66:        remove-translations.diff
Patch67:        headeradddb.diff
Patch69:        nobuildcolor.diff
Patch70:        fileattrs.diff
Patch71:        nomagiccheck.diff
Patch73:        assumeexec.diff
Patch77:        langnoc.diff
Patch78:        headerchk2.diff
Patch85:        brp-compress-no-img.patch
Patch93:        weakdepscompat.diff
Patch94:        checksepwarn.diff
Patch99:        enable-postin-scripts-error.diff
Patch100:       rpm-findlang-inject-metainfo.patch
Patch102:       emptymanifest.diff
Patch103:       find-lang-qt-qm.patch
Patch117:       findsupplements.diff
Patch122:       db_conversion.diff
Patch123:       nextiteratorheaderblob.diff
Patch131:       posttrans.diff
Patch133:       zstdpool.diff
Patch134:       zstdthreaded.diff
Patch135:       selinux_transactional_update.patch
Patch136:       rpmsort_reverse.diff
Patch138:       canongnu.diff
Patch139:       cmake_python_version.diff
Patch141:       0002-log-build-time-if-it-is-set-from-SOURCE_DATE_EPOCH.patch
Patch142:       0003-Error-out-on-a-missing-changelog-date.patch
Patch150:       unshare.diff
Patch151:       buildroot-symlink.diff
Patch154:       undefbuildroot.diff
Patch155:       rpm2archive.diff
Patch156:       mtime_policy_set.diff
Patch157:       cmake_fhardened.diff
Patch158:       archcheck.diff
Patch159:       emptypw.diff
Patch160:       buildsysprep.diff
Patch161:       pgpreleasemtime.diff
Patch6464:      auto-config-update-aarch64-ppc64le.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#
# avoid bootstrapping problem
%define _binary_payload w9.bzdio

%description
RPM Package Manager is the main tool for managing the software packages
of the SUSE Linux distribution.

RPM can be used to install and remove software packages. With rpm, it
is easy to update packages.  RPM keeps track of all these manipulations
in a central database.	This way it is possible to get an overview of
all installed packages.  RPM also supports database queries.

%package -n librpmbuild%{librpmsover}
Summary:        Library for building RPM packages
# Was part of rpm before
Group:          System/Libraries
Conflicts:      rpm < %{version}

%description -n librpmbuild%{librpmsover}
Thie package contains a library with functions for building RPM packages.

%package devel
Summary:        Development files for librpm
Group:          Development/Libraries/C and C++
Requires:       rpm = %{version}
# for people confusing the one with the other
Recommends:     rpm-build = %{version}
Requires:       popt-devel

%description devel
This package contains the RPM C library and header files.  These
development files will simplify the process of writing programs which
manipulate RPM packages and databases and are intended to make it
easier to create graphical package managers or any other tools that
need an intimate knowledge of RPM packages in order to function.

%package build
Summary:        Tools and Scripts to create rpm packages
Group:          System/Packages
Requires:       librpmbuild%{librpmsover} = %{version}
Requires:       rpm = %{version}
Provides:       rpm:%_bindir/rpmbuild
Provides:       rpmbuild
# SUSE's build essentials
Requires:       binutils
Requires:       bzip2
Requires:       coreutils
Requires:       diffutils
Requires:       dwz
Requires:       file
Requires:       findutils
Requires:       gawk
Requires:       gcc
#Requires:       gcc-PIE
Requires:       /usr/bin/gzip
Requires:       gettext-tools
Requires:       glibc-devel
Requires:       glibc-locale-base
Requires:       grep
Requires:       make
Requires:       patch
Requires:       sed
Requires:       systemd-rpm-macros
Requires:       tar
Requires:       util-linux
Requires:       which
Requires:       xz
# needed for debuginfo generation
Requires:       debugedit >= 5.0
# drop candidates
Requires:       cpio
Requires:       file
# Mandatory generators
Requires:       (%{name}-build-perl if perl-base)
Requires:       (%{name}-build-python if python3-base)
# The point of the split
Conflicts:      rpm < 4.15.0

%description build
If you want to build a rpm, you need this package. It provides rpmbuild
and requires some packages that are usually required.

%package plugin-unshare
Summary:        Rpm plugin for Linux namespace isolation functionality
Requires:       rpm = %{version}

%description plugin-unshare
Rpm plugin for Linux namespace isolation functionality.

%prep
%setup -q -n rpm-%{version}
%ifarch aarch64 ppc64le riscv64 loongarch64
tar xf %{SOURCE14}
%endif
pushd rpmio
tar xf %{SOURCE1}
ln -s rpmpgp_legacy-* rpmpgp_legacy
popd

rm -rf sqlite
%patch -P  5      -P 12 -P 13                         -P 18
%patch                         -P 24 -P 25 -P 26             -P 29
%patch -P 30       -P 32 -P 33 -P 34       -P 36       -P 38
%patch                   -P 43             -P 46
%patch       -P 51
%patch -P 60 -P 61                         -P 66 -P 67       -P 69
%patch -P 70 -P 71       -P 73                   -P 77 -P 78
%patch                               -P 85
%patch                   -P 93 -P 94                         -P 99
%patch -P 100        -P 102 -P 103
%patch                                                  -P 117
%patch -P 122 -P 123
%patch -P 131          -P 133 -P 134 -P 135 -P 136        -P 138
%patch -P 139
%patch -P 141 -P 142
%patch -P 150 -P 151 -P 154 -P 155 -P 156 -P 157 -P 158 -P 159
%patch -P 160 -P 161

%ifarch aarch64 ppc64le riscv64 loongarch64
%patch -P 6464
%endif

rm -f m4/libtool.m4
rm -f m4/lt*.m4

%build
export CFLAGS="%{optflags} -ffunction-sections"
export LDFLAGS="-Wl,-Bsymbolic-functions -ffunction-sections"
%ifarch alpha
export CFLAGS="-g -O0 -fno-strict-aliasing -ffunction-sections"
%endif

cpu="%{_target_cpu}"
# convert to gnu style cpu version, see config.sub
%ifarch ppc ppc64 ppc64le
cpu="${cpu/#ppc/powerpc}"
%endif

mkdir _build
cd _build
cmake .. \
  -DRPM_HOST_SYSTEM_CPU="$cpu" \
%ifarch %arm
  -DRPM_HOST_SYSTEM_ABI=gnueabi \
%endif
  -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
  -DCMAKE_INSTALL_MANDIR:PATH=share/man \
  -DCMAKE_INSTALL_INFODIR:PATH=share/info \
  -DCMAKE_INSTALL_DOCDIR:PATH=%{_defaultdocdir}/%{NAME} \
  -DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
  -DCMAKE_INSTALL_FULL_SYSCONFDIR:PATH=/etc \
  -DCMAKE_INSTALL_FULL_LOCALSTATEDIR:PATH=/var \
  -DCMAKE_INSTALL_SHAREDSTATEDIR:PATH=/var/lib \
  -DCMAKE_INSTALL_FULL_SHAREDSTATEDIR:PATH=/var/lib \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DRPM_VENDOR=suse \
  -DWITH_ARCHIVE=ON \
  -DWITH_READLINE=OFF \
  -DWITH_SELINUX=ON \
  -DWITH_SEQUOIA=OFF \
  -DWITH_LEGACY_OPENPGP=ON \
  -DENABLE_NDB=ON \
  -DENABLE_BDB_RO=ON \
  -DENABLE_SQLITE=OFF \
  -DWITH_AUDIT=OFF \
  -DWITH_DBUS=OFF \
  -DENABLE_PYTHON=%{?with_python:ON}%{?!with_python:OFF} \
  -DENABLE_TESTSUITE=OFF \
  -D__FIND_DEBUGINFO=/usr/lib/rpm/find-debuginfo \
  -D__AR:FILEPATH=ar -D__AS:FILEPATH=as \
  -D__CC:FILEPATH=gcc -D__CPP:FILEPATH="gcc -E" -D__CXX:FILEPATH=g++ \
  -D__GPG:FILEPATH=/usr/bin/gpg2 -D__AWK:FILEPATH=/usr/bin/gawk
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/lib
mkdir -p %{buildroot}/usr/share/locale
ln -s ../share/locale %{buildroot}/usr/lib/locale
pushd _build
%make_install
popd
mkdir -p %{buildroot}/bin
%if 0%{?suse_version} < 1550
ln -s /usr/bin/rpm %{buildroot}/bin/rpm
%endif
mkdir -p %{buildroot}/usr/sbin
install -m 755 %{SOURCE8} %{buildroot}/usr/sbin
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 644 %{SOURCE13} %{buildroot}/usr/lib/systemd/system/
mkdir -p %{buildroot}/usr/lib/rpm/macros.d
mkdir -p %{buildroot}/usr/lib/rpm/suse
for d in BUILD RPMS SOURCES SPECS SRPMS BUILDROOT ; do
  mkdir -p %{buildroot}/usr/src/packages/$d
  chmod 755 %{buildroot}/usr/src/packages/$d
done
for d in %{buildroot}/usr/lib/rpm/platform/*-linux/macros ; do
  dd=${d%%-linux/macros}
  dd=${dd##*/}
  mkdir %{buildroot}/usr/src/packages/RPMS/$dd
  chmod 755 %{buildroot}/usr/src/packages/RPMS/$dd
done
mkdir -p %{buildroot}/usr/lib/sysimage/rpm
export RPM_BUILD_ROOT
%ifarch s390x
[ -f scripts/brp-%_arch-linux ] && sh scripts/brp-%_arch-linux
%endif
rm -f %{buildroot}/usr/lib/rpmpopt
rm -rf %{buildroot}%{_mandir}/{fr,ja,ko,pl,ru,sk}
rm -f %{buildroot}%{_prefix}/share/locale/de/LC_MESSAGES/rpm.mo
mkdir -p %{buildroot}%{_fillupdir}
install -c -m0644 %{SOURCE9} %{buildroot}%{_fillupdir}/
rm -f %{buildroot}/usr/lib/rpm/cpanflute %{buildroot}/usr/lib/rpm/cpanflute2
install -m 755 %{SOURCE5} %{buildroot}/usr/lib/rpm
rm -f %{buildroot}/usr/lib/locale %{buildroot}/usr/lib/rpmrc
mkdir -p %{buildroot}/etc/rpm
chmod 755 %{buildroot}/etc/rpm
# remove some nonsense or non-working scripts
pushd %{buildroot}/usr/lib/rpm/
for f in rpm2cpio.sh rpm.daily rpmdiff* rpm.log rpm.xinetd freshen.sh u_pkg.sh \
         ocaml-find-provides.sh ocaml-find-requires.sh fileattrs/ocaml.attr \
         magic magic.mgc magic.mime* rpmfile *.pl javadeps brp-redhat \
         brp-strip-static-archive vpkg-provides*.sh http.req sql.req tcl.req \
         brp-sparc64-linux brp-strip-comment-note brp-java-gcjcompile
do
    rm -f $f
done
for i in /usr/share/automake-*/*; do
  if test -f "$i" && test -f "${i##*/}"; then
    rm -f "${i##*/}"
  fi
done
popd
%ifarch aarch64 ppc64le riscv64 loongarch64
install -m 755 build-aux/config.guess %{buildroot}/usr/lib/rpm
install -m 755 build-aux/config.sub %{buildroot}/usr/lib/rpm
%endif
rm -rf %{buildroot}/%{_libdir}/python%{py_ver}
bash %{buildroot}/usr/lib/rpm/find-lang.sh %{buildroot} rpm
# On arm the kernel architecture is ignored. Not the best idea, but lets stay compatible with other distros
%ifarch armv7hl armv6hl
# rpm is using the host_cpu as default for the platform, but armv6/7hl is not known by the kernel.
# so we need to enforce the platform here.
echo -n "%{_target_cpu}-suse-linux-gnueabi" > %{buildroot}/etc/rpm/platform
%endif

# disable sysuser handling for now
rm %{buildroot}/usr/lib/rpm/sysusers.sh
rm %{buildroot}/usr/lib/rpm/fileattrs/sysusers.attr
sed -e '/^%%__systemd_sysusers/s/^/#/' -i %{buildroot}/usr/lib/rpm/macros

%post
%{fillup_only -an services}

# var/lib/rpm migration: set forwards compatible symlink for /usr/lib/sysimage/rpm so scriptlets in same transaction will still work
if test ! -L var/lib/rpm -a ! -f usr/lib/sysimage/rpm/Packages -a ! -f usr/lib/sysimage/rpm/Packages.db ; then
  if test -f var/lib/rpm/Packages -o -f var/lib/rpm/Packages.db ; then
    rmdir usr/lib/sysimage/rpm
    ln -s ../../../var/lib/rpm usr/lib/sysimage/rpm
  fi
fi

test -f usr/lib/sysimage/rpm/Packages -o -f usr/lib/sysimage/rpm/Packages.db || rpmdb --initdb
test -e var/lib/rpm || ln -s ../../usr/lib/sysimage/rpm var/lib/rpm

%posttrans
# var/lib/rpm migration
if test ! -L var/lib/rpm ; then
  # delete no longer maintained databases
  rm -f var/lib/rpm/Filemd5s var/lib/rpm/Filedigests var/lib/rpm/Requireversion var/lib/rpm/Provideversion

  if test -f var/lib/rpm/Packages -o -f var/lib/rpm/Packages.db ; then
    echo "migrating rpmdb from /var/lib/rpm to /usr/lib/sysimage/rpm..."

    # remove forwards compatible symlink
    if test -L usr/lib/sysimage/rpm ; then
      rm -f usr/lib/sysimage/rpm
      mkdir -p usr/lib/sysimage/rpm
    fi

    mv -f var/lib/rpm/.[!.]* usr/lib/sysimage/rpm/
    mv -f var/lib/rpm/* usr/lib/sysimage/rpm/
  fi
  test -d var/lib/rpm && rmdir var/lib/rpm
  test -e var/lib/rpm || ln -s ../../usr/lib/sysimage/rpm var/lib/rpm
fi

%files -f rpm.lang
%defattr(-,root,root)
%license 	COPYING
%doc	%{_datadir}/doc/packages/rpm
%exclude %{_datadir}/doc/packages/rpm/API
%exclude /usr/lib/rpm/macros.d/macros.transaction_unshare
%exclude %{_mandir}/man8/rpm-plugin-unshare*
	/etc/rpm
%if 0%{?suse_version} < 1550
	/bin/rpm
%endif
	%{_bindir}/gendiff
	%{_bindir}/rpm
	%{_bindir}/rpm2archive
	%{_bindir}/rpm2cpio
	%{_bindir}/rpmdb
	%{_bindir}/rpmgraph
	%{_bindir}/rpmkeys
	%{_bindir}/rpmlua
	%{_bindir}/rpmqpack
	%{_bindir}/rpmquery
	%{_bindir}/rpmsign
	%{_bindir}/rpmverify
	%{_bindir}/rpmsort
	/usr/sbin/rpmconfigcheck
	/usr/lib/systemd/system/rpmconfigcheck.service
	%dir /usr/lib/rpm
	/usr/lib/rpm/macros
	/usr/lib/rpm/macros.d/
	/usr/lib/rpm/platform/
	/usr/lib/rpm/rpm.supp
	/usr/lib/rpm/rpmdb_*
	/usr/lib/rpm/rpmpopt-*
	/usr/lib/rpm/rpmrc
	/usr/lib/rpm/rpmsort
	/usr/lib/rpm/rpmdump
	/usr/lib/rpm/suse
	/usr/lib/rpm/tgpg
	%{_libdir}/rpm-plugins
	%{_libdir}/librpm.so.*
	%{_libdir}/librpmio.so.*
	%{_libdir}/librpmsign.so.*
%doc	%{_mandir}/man[18]/*.[18]*
%dir 	/usr/lib/sysimage
%dir 	/usr/lib/sysimage/rpm
%ghost	/var/lib/rpm
%dir 	%attr(755,root,root) /usr/src/packages/BUILD
%dir 	%attr(755,root,root) /usr/src/packages/SPECS
%dir 	%attr(755,root,root) /usr/src/packages/SOURCES
%dir 	%attr(755,root,root) /usr/src/packages/SRPMS
%dir	%attr(755,root,root) /usr/src/packages/RPMS
%dir	%attr(755,root,root) /usr/src/packages/BUILDROOT
%dir	%attr(755,root,root) /usr/src/packages/RPMS/*
	%{_fillupdir}/sysconfig.services-rpm

%files -n librpmbuild%{librpmsover}
%{_libdir}/librpmbuild.so.%{librpmsover}
%{_libdir}/librpmbuild.so.%{librpmsover}.*

%files build
%defattr(-,root,root)
/usr/bin/rpmbuild
/usr/lib/rpm/pkgconfigdeps.sh
/usr/lib/rpm/ocamldeps.sh
/usr/lib/rpm/rpm_macros_provides.sh
/usr/lib/rpm/elfdeps
/usr/lib/rpm/rpmdeps
/usr/lib/rpm/rpmuncompress
/usr/bin/rpmspec
/usr/lib/rpm/brp-*
/usr/lib/rpm/check-*
/usr/lib/rpm/*find*
/usr/lib/rpm/fileattrs/
/usr/lib/rpm/*.prov
/usr/lib/rpm/*.req
%ifarch aarch64 ppc64le riscv64 loongarch64
/usr/lib/rpm/config.guess
/usr/lib/rpm/config.sub
%endif

%files devel
%defattr(644,root,root,755)
/usr/include/rpm
%{_libdir}/librpm.so
%{_libdir}/librpmbuild.so
%{_libdir}/librpmio.so
%{_libdir}/librpmsign.so
%{_libdir}/pkgconfig/rpm.pc
%{_libdir}/cmake/rpm
%doc	%{_datadir}/doc/packages/rpm/API

%files plugin-unshare
%defattr(-,root,root)
/usr/lib/rpm/macros.d/macros.transaction_unshare
%doc %{_mandir}/man8/rpm-plugin-unshare*

%changelog
