#
# spec file for package rpm
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


#Compat macro for new _fillupdir macro introduced in Nov 2017
%{?!_fillupdir:%define _fillupdir /var/adm/fillup-templates}

%global librpmsover 8

Name:           rpm
BuildRequires:  binutils
BuildRequires:  bzip2
BuildRequires:  file-devel
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel
BuildRequires:  gzip
BuildRequires:  libacl-devel
BuildRequires:  libbz2-devel
BuildRequires:  libcap-devel
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
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
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(libzstd)
#!BuildIgnore:  rpmlint-Factory
Provides:       rpminst
Requires(post): %fillup_prereq
Requires:       rpm-config-SUSE
# awk is needed for rpm --last
Requires:       /usr/bin/awk
Summary:        The RPM Package Manager
License:        GPL-2.0-or-later
Group:          System/Packages
Version:        4.14.2.1
Release:        0
URL:            https://rpm.org/
#Git-Clone:     https://github.com/rpm-software-management/rpm
Source:         http://ftp.rpm.org/releases/rpm-4.14.x/rpm-%{version}.tar.bz2
Source1:        RPM-HOWTO.tar.bz2
Source5:        rpmsort
Source8:        rpmconfigcheck
Source9:        sysconfig.services-rpm
Source10:       beecrypt-4.1.2.tar.bz2
Source11:       db-4.8.30.tar.bz2
Source12:       baselibs.conf
Source13:       rpmconfigcheck.service
Patch1:         beecrypt-4.1.2.diff
Patch2:         db.diff
Patch3:         rpm-4.12.0.1-fix-bashisms.patch
Patch4:         beecrypt-4.1.2-build.diff
Patch5:         usr-lib-sysimage-rpm.patch
# quilt patches start here
Patch11:        debugedit.diff
Patch13:        ignore-auxv.diff
Patch12:        localetag.diff
Patch14:        nameversioncompare.diff
Patch15:        dbfsync.diff
Patch16:        dbrointerruptable.diff
Patch18:        refreshtestarch.diff
Patch20:        waitlock.diff
Patch21:        suspendlock.diff
Patch24:        brp.diff
Patch25:        brpcompress.diff
Patch26:        checkfilesnoinfodir.diff
Patch27:        finddebuginfo.diff
Patch29:        findlang.diff
Patch30:        macrosin.diff
Patch32:        platformin.diff
Patch33:        rpmpopt.diff
Patch34:        rpmrc.diff
Patch35:        taggedfileindex.diff
Patch36:        rpmqpack.diff
Patch38:        build.diff
Patch43:        rpm-shorten-changelog.diff
Patch45:        whatrequires-doc.diff
Patch46:        remove-brp-strips.diff
Patch47:        requires-ge-macro.diff
Patch49:        finddebuginfo-absolute-links.diff
Patch51:        specfilemacro.diff
Patch55:        debugsubpkg.diff
Patch56:        debuglink.diff
Patch57:        debuginfo-mono.patch
Patch58:        lazystatfs.diff
Patch60:        safeugid.diff
Patch61:        noprereqdeprec.diff
Patch66:        remove-translations.diff
Patch67:        headeradddb.diff
Patch68:        dbprivate.diff
Patch69:        nobuildcolor.diff
Patch70:        fileattrs.diff
Patch71:        nomagiccheck.diff
Patch73:        assumeexec.diff
Patch74:        mono-find-requires.diff
Patch75:        rpm-deptracking.patch
Patch77:        langnoc.diff
Patch78:        headerchk2.diff
Patch85:        brp-compress-no-img.patch
Patch93:        weakdepscompat.diff
Patch94:        checksepwarn.diff
Patch99:        enable-postin-scripts-error.diff
Patch100:       rpm-findlang-inject-metainfo.patch
Patch102:       emptymanifest.diff
Patch103:       find-lang-qt-qm.patch
Patch108:       debugedit-macro.diff
Patch109:       pythondistdeps.diff
Patch114:       source_date_epoch_buildtime.diff
Patch117:       findsupplements.diff
Patch118:       dwz-compression.patch
Patch119:       getncpus.diff
Patch120:       rpmfc-push-name-epoch-version-release-macro-before-invoking-depgens.patch
Patch121:       adopt-language-specific-build_fooflags-macros-from-F.patch
Patch122:       0001-Stop-papering-over-the-security-disaster-known-as-pr.patch
Patch123:       0002-Fix-use-after-free-introduced-in-0f21bdd0d7b2c45564d.patch
Patch124:       set-flto=auto-by-default.patch
Patch6464:      auto-config-update-aarch64-ppc64le.diff
Patch6465:      auto-config-update-riscv64.diff
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
Requires:       gettext-tools
Requires:       glibc-devel
Requires:       glibc-locale
Requires:       grep
Requires:       gzip
Requires:       make
Requires:       patch
Requires:       perl-base
Requires:       sed
Requires:       systemd-rpm-macros
Requires:       tar
Requires:       util-linux
Requires:       which
Requires:       xz
# drop candidates
Requires:       cpio
Requires:       file

%description build
If you want to build a rpm, you need this package. It provides rpmbuild
and requires some packages that are usually required.

%prep
%setup -q -n rpm-%{version}
rm -rf sqlite
rm -rf beecrypt
tar xjf %{SOURCE10}
tar xjf %{SOURCE11}
ln -s db-4.8.30 db
cd db
%patch2 -p1
cd ..
ln -s beecrypt-4.1.2 beecrypt
chmod -R u+w db/*
rm -f rpmdb/db.h
%patch -P 1
%patch3 -p1
%patch -P 4
%patch5 -p1
%patch       -P 11 -P 12 -P 13 -P 14 -P 15 -P 16       -P 18
%patch -P 20 -P 21             -P 24 -P 25 -P 26 -P 27       -P 29
%patch -P 30       -P 32 -P 33 -P 34 -P 35 -P 36       -P 38
%patch                   -P 43       -P 45 -P 46 -P 47       -P 49
%patch       -P 51                   -P 55 -P 56 -P 57 -P 58
%patch -P 60 -P 61                         -P 66 -P 67 -P 68 -P 69
%patch -P 70 -P 71       -P 73 -P 74 -P 75       -P 77 -P 78
%patch                               -P 85
%patch                   -P 93 -P 94                         -P 99
%patch -P 100        -P 102 -P 103                             -P 108
%patch -P 109                      -P 114               -P 117 -P 118
%patch -P 119 -P 120
%patch121 -p1
%patch122 -p1
%patch123 -p1
%patch124 -p1

%ifarch aarch64 ppc64le riscv64
%patch6464
%endif
%ifarch riscv64
%patch6465
%endif

cp config.guess config.sub db/dist/
cp config.guess config.sub beecrypt/
tar -xjvf %{SOURCE1}
rm -f m4/libtool.m4
rm -f m4/lt*.m4

%build
export CFLAGS="%{optflags} -ffunction-sections"
export LDFLAGS="-Wl,-Bsymbolic-functions -ffunction-sections"
%ifarch alpha
export CFLAGS="-g -O0 -fno-strict-aliasing -ffunction-sections"
%endif

%ifarch %arm
BUILDTARGET="--build=%{_target_cpu}-suse-linux-gnueabi"
%else
BUILDTARGET="--build=%{_target_cpu}-suse-linux"
%endif

#cp -p /usr/share/gettext/config.rpath .
cp autogen.sh beecrypt
pushd beecrypt
./autogen.sh --disable-dependency-tracking --with-pic --without-python $BUILDTARGET
make %{?_smp_mflags}
popd

autoreconf -fi
./configure --disable-dependency-tracking --prefix=%{_prefix} --mandir=%{_mandir} --infodir=%{_infodir} \
--libdir=%{_libdir} --sysconfdir=/etc --localstatedir=/var --sharedstatedir=/var/lib --with-lua \
--without-external-db \
--with-vendor=suse \
--with-rundir=/run \
--without-archive \
--with-selinux --with-internal-beecrypt \
--with-acl --with-cap --enable-shared %{?with_python: --enable-python} $BUILDTARGET

rm po/de.gmo
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/lib
mkdir -p %{buildroot}/usr/share/locale
ln -s ../share/locale %{buildroot}/usr/lib/locale
%make_install
mkdir -p %{buildroot}/bin
ln -s /usr/bin/rpm %{buildroot}/bin/rpm
install -m 644 db3/db.h %{buildroot}/usr/include/rpm
# remove .la file and the static variant of libpopt
# have to remove the dependency from other .la files as well
for f in %{buildroot}/%{_libdir}/*.la; do
    sed -i -e "s,/%_lib/libpopt.la,-lpopt,g" $f
done
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
mkdir -p %{buildroot}/var/lib/rpm
gzip -9 %{buildroot}/%{_mandir}/man[18]/*.[18]
export RPM_BUILD_ROOT
%ifarch s390x
[ -f scripts/brp-%_arch-linux ] && sh scripts/brp-%_arch-linux
%endif
chmod 755 doc/manual
rm -rf doc/manual/Makefile*
rm -f %{buildroot}/usr/lib/rpmpopt
rm -rf %{buildroot}%{_mandir}/{fr,ja,ko,pl,ru,sk}
rm -f %{buildroot}%{_prefix}/share/locale/de/LC_MESSAGES/rpm.mo
mkdir -p %{buildroot}%{_fillupdir}
install -c -m0644 %{SOURCE9} %{buildroot}%{_fillupdir}/
rm -f %{buildroot}/usr/lib/rpm/cpanflute %{buildroot}/usr/lib/rpm/cpanflute2
install -m 755 %{SOURCE5} %{buildroot}/usr/lib/rpm
install -m 755 scripts/debuginfo.prov %{buildroot}/usr/lib/rpm
rm -f %{buildroot}/usr/lib/locale %{buildroot}/usr/lib/rpmrc
mkdir -p %{buildroot}/etc/rpm
chmod 755 %{buildroot}/etc/rpm
# remove some nonsense or non-working scripts
pushd %{buildroot}/usr/lib/rpm/
for f in rpm2cpio.sh rpm.daily rpmdiff* rpm.log rpm.xinetd freshen.sh u_pkg.sh \
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
%ifarch aarch64 ppc64le riscv64
install -m 755 config.guess %{buildroot}/usr/lib/rpm
install -m 755 config.sub %{buildroot}/usr/lib/rpm
%endif
rm -rf %{buildroot}/%{_libdir}/python%{py_ver}
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/rpm-plugins/*.la
sh %{buildroot}/usr/lib/rpm/find-lang.sh %{buildroot} rpm
# On arm the kernel architecture is ignored. Not the best idea, but lets stay compatible with other distros
%ifarch armv7hl armv6hl
# rpm is using the host_cpu as default for the platform, but armv6/7hl is not known by the kernel.
# so we need to enforce the platform here.
echo -n "%{_target_cpu}-suse-linux-gnueabi" > %{buildroot}/etc/rpm/platform
%endif

%post
%{fillup_only -an services}

# var/lib/rpm migration: set forwards compatible symlink for /usr/lib/sysimage/rpm so scriptlets in same transaction will still work
if test ! -L var/lib/rpm -a -f var/lib/rpm/Packages -a ! -f usr/lib/sysimage/rpm/Packages ; then
  rmdir usr/lib/sysimage/rpm
  ln -s ../../../var/lib/rpm usr/lib/sysimage/rpm
fi

test -f usr/lib/sysimage/rpm/Packages || rpmdb --initdb

%posttrans
# var/lib/rpm migration
if test ! -L var/lib/rpm ; then
  # delete no longer maintained databases
  rm -f var/lib/rpm/Filemd5s var/lib/rpm/Filedigests var/lib/rpm/Requireversion var/lib/rpm/Provideversion

  if test -f var/lib/rpm/Packages ; then
    echo "migrating rpmdb from /var/lib/rpm to /usr/lib/sysimage/rpm..."

    # remove forwards compatible symlink
    if test -L usr/lib/sysimage/rpm ; then
      rm -f usr/lib/sysimage/rpm
      mkdir -p usr/lib/sysimage/rpm
    fi

    mv -f var/lib/rpm/.[!.]* usr/lib/sysimage/rpm/
    mv -f var/lib/rpm/* usr/lib/sysimage/rpm/
  fi
  rmdir var/lib/rpm && ln -s ../../usr/lib/sysimage/rpm var/lib/rpm
fi

%files -f rpm.lang
%defattr(-,root,root)
%license 	COPYING
%doc 	doc/manual
%doc    RPM-HOWTO
	/etc/rpm
	/bin/rpm
	/usr/bin/*
	%exclude /usr/bin/rpmbuild
	%exclude %{_libdir}/librpmbuild.so.*
	%exclude /usr/lib/rpm/elfdeps
	%exclude /usr/lib/rpm/rpmdeps
	%exclude /usr/lib/rpm/debugedit
	%exclude /usr/lib/rpm/sepdebugcrcfix
	%exclude /usr/bin/rpmspec
	%exclude /usr/lib/rpm/*.prov
	%exclude /usr/lib/rpm/*.req
	%exclude /usr/lib/rpm/brp-*
	%exclude /usr/lib/rpm/check-*
	%exclude /usr/lib/rpm/*find*
	/usr/sbin/rpmconfigcheck
	/usr/lib/systemd/system/rpmconfigcheck.service
	/usr/lib/rpm
	%{_libdir}/rpm-plugins
	%{_libdir}/librpm.so.*
	%{_libdir}/librpmio.so.*
	%{_libdir}/librpmsign.so.*
%doc	%{_mandir}/man[18]/*.[18]*
%dir 	/usr/lib/sysimage
%dir 	/usr/lib/sysimage/rpm
%dir 	/var/lib/rpm
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
/usr/lib/rpm/elfdeps
/usr/lib/rpm/rpmdeps
/usr/lib/rpm/debugedit
/usr/lib/rpm/sepdebugcrcfix
/usr/bin/rpmspec
/usr/lib/rpm/*.prov
/usr/lib/rpm/*.req
/usr/lib/rpm/brp-*
/usr/lib/rpm/check-*
/usr/lib/rpm/*find*

%files devel
%defattr(644,root,root,755)
	/usr/include/rpm
        %{_libdir}/librpm.so
        %{_libdir}/librpmbuild.so
        %{_libdir}/librpmio.so
        %{_libdir}/librpmsign.so
        %{_libdir}/pkgconfig/rpm.pc

%changelog
