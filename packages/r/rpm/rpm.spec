#
# spec file for package rpm
#
# Copyright (c) 2022 SUSE LLC
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

%global librpmsover 9

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
Version:        4.18.0
Release:        0
URL:            https://rpm.org/
#Git-Clone:     https://github.com/rpm-software-management/rpm
Source:         http://ftp.rpm.org/releases/rpm-4.17.x/rpm-%{version}.tar.bz2
Source5:        rpmsort
Source8:        rpmconfigcheck
Source9:        sysconfig.services-rpm
Source12:       baselibs.conf
Source13:       rpmconfigcheck.service
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
# touches a generated file
Patch180:       whatrequires-doc.diff
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
Requires:       debugedit = 5.0
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

%package build-perl
Summary:        RPM dependency generator for Perl
Group:          Development/Languages/Perl
Requires:       perl-base

%description build-perl
Provides and requires generator for .pl files and modules.

%prep
%setup -q -n rpm-%{version}

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
%patch -P 122 -P 123               -P 131        -P 133 -P 134
%patch -P 135 -P 180

%ifarch aarch64 ppc64le riscv64
%patch6464
%endif

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
export __FIND_DEBUGINFO=/usr/lib/rpm/find-debuginfo

autoreconf -fi
./configure --disable-dependency-tracking --prefix=%{_prefix} --mandir=%{_mandir} --infodir=%{_infodir} \
--libdir=%{_libdir} --sysconfdir=/etc --localstatedir=/var --sharedstatedir=/var/lib \
--with-lua \
--with-vendor=suse \
--with-rundir=/run \
--without-archive \
--with-selinux \
--with-crypto=libgcrypt \
--with-acl \
--with-cap \
--enable-shared \
--enable-ndb \
--enable-bdb-ro \
--enable-zstd \
--enable-sqlite=no \
%{?with_python: --enable-python} \
$BUILDTARGET

rm po/de.gmo
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/usr/lib
mkdir -p %{buildroot}/usr/share/locale
ln -s ../share/locale %{buildroot}/usr/lib/locale
%make_install
mkdir -p %{buildroot}/bin
%if !0%{?usrmerged}
ln -s /usr/bin/rpm %{buildroot}/bin/rpm
%endif
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
gzip -9 %{buildroot}/%{_mandir}/man[18]/*.[18]
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
%ifarch aarch64 ppc64le riscv64
install -m 755 build-aux/config.guess %{buildroot}/usr/lib/rpm
install -m 755 build-aux/config.sub %{buildroot}/usr/lib/rpm
%endif
rm -rf %{buildroot}/%{_libdir}/python%{py_ver}
rm -f %{buildroot}%{_libdir}/*.la
rm -f %{buildroot}%{_libdir}/rpm-plugins/*.la
bash %{buildroot}/usr/lib/rpm/find-lang.sh %{buildroot} rpm
# On arm the kernel architecture is ignored. Not the best idea, but lets stay compatible with other distros
%ifarch armv7hl armv6hl
# rpm is using the host_cpu as default for the platform, but armv6/7hl is not known by the kernel.
# so we need to enforce the platform here.
echo -n "%{_target_cpu}-suse-linux-gnueabi" > %{buildroot}/etc/rpm/platform
%endif

# make ndb the default database backend
echo "setting the default database backend to 'ndb'"
sed -i -e '/_db_backend/s/sqlite/ndb/' %{buildroot}/usr/lib/rpm/macros

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
%doc 	docs/manual
	/etc/rpm
%if !0%{?usrmerged}
	/bin/rpm
%endif
	%{_bindir}/gendiff
	%{_bindir}/rpm
	%{_bindir}/rpm2cpio
	%{_bindir}/rpmdb
	%{_bindir}/rpmgraph
	%{_bindir}/rpmkeys
	%{_bindir}/rpmlua
	%{_bindir}/rpmqpack
	%{_bindir}/rpmquery
	%{_bindir}/rpmsign
	%{_bindir}/rpmverify
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
	/usr/lib/rpm/rpmuncompress
	/usr/lib/rpm/rpm_macros_provides.sh
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
/usr/lib/rpm/elfdeps
/usr/lib/rpm/rpmdeps
/usr/bin/rpmspec
/usr/lib/rpm/brp-*
/usr/lib/rpm/check-*
/usr/lib/rpm/*find*
/usr/lib/rpm/fileattrs/
%exclude /usr/lib/rpm/fileattrs/perl*.attr
/usr/lib/rpm/*.prov
%exclude /usr/lib/rpm/perl.prov
/usr/lib/rpm/*.req
%exclude /usr/lib/rpm/perl.req
%ifarch aarch64 ppc64le riscv64
/usr/lib/rpm/config.guess
/usr/lib/rpm/config.sub
%endif

%files build-perl
%defattr(-,root,root)
/usr/lib/rpm/fileattrs/perl*.attr
/usr/lib/rpm/perl.prov
/usr/lib/rpm/perl.req

%files devel
%defattr(644,root,root,755)
/usr/include/rpm
%{_libdir}/librpm.so
%{_libdir}/librpmbuild.so
%{_libdir}/librpmio.so
%{_libdir}/librpmsign.so
%{_libdir}/pkgconfig/rpm.pc

%changelog
