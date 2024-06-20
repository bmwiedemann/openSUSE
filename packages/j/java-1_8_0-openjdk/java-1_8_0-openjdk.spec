#
# spec file for package java-1_8_0-openjdk
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


%{!?aarch64:%global aarch64 aarch64 arm64 armv8}
%global jit_arches %{ix86} x86_64 ppc64 ppc64le %{aarch64} %{arm}
%global icedtea_version 3.31.0
%global buildoutputdir openjdk.build/
# Convert an absolute path to a relative path.  Each symbolic link is
# specified relative to the directory in which it is installed so that
# it will resolve properly within chrooted installations.
%global script 'use File::Spec; print File::Spec->abs2rel($ARGV[0], $ARGV[1])'
%global abs2rel perl -e %{script}
%global syslibdir       %{_libdir}
%global archname        %{name}
# Standard JPackage naming and versioning defines.
# priority must be 6 digits in total
%global priority        1805
%global javaver         1.8.0
%global updatever       412
%global buildver        08
# Standard JPackage directories and symbolic links.
%global sdklnk          java-%{javaver}-openjdk
%global archname        %{sdklnk}
%global jrelnk          jre-%{javaver}-openjdk
%global sdkdir          %{sdklnk}-%{javaver}
%global jredir          %{sdkdir}/jre
%global sdkbindir       %{_jvmdir}/%{sdklnk}/bin
%global jrebindir       %{_jvmdir}/%{jrelnk}/bin
%global jvmjardir       %{_jvmjardir}/%{sdkdir}
%global jvmjarlink      %{_jvmjardir}/%{sdklnk}
# Prevent brp-java-repack-jars from being run.
%global __jar_repack 0
# cacert symlink
%global cacerts  %{_jvmdir}/%{jredir}/lib/security/cacerts
# real file made by update-ca-certificates
%global javacacerts %{_var}/lib/ca-certificates/java-cacerts
%if 0%{?suse_version} >= 1330
%global with_improved_font_rendering 1
%else
%global with_improved_font_rendering 0
%endif
%if 0%{?suse_version} >= 1220
%global with_system_lcms 1
%else
%global with_system_lcms 0
%endif
%if 0%{?suse_version} > 1310
%global with_system_kerberos 1
%else
%global with_system_kerberos 0
%endif
%if 0%{?suse_version} > 1320
%global with_system_pcsc 1
%else
%global with_system_pcsc 0
%endif
%if 0%{?suse_version} > 1320
%global with_system_sctp 1
%else
%global with_system_sctp 0
%endif
%ifarch x86_64
%global archinstall amd64
%endif
%ifarch ppc
%global archinstall ppc
%endif
%ifarch ppc64
%global archinstall ppc64
%endif
%ifarch ppc64le
%global archinstall ppc64le
%endif
%ifarch %{ix86}
%global archinstall i386
%endif
%ifarch ia64
%global archinstall ia64
%endif
%ifarch s390
%global archinstall s390
%endif
%ifarch s390x
%global archinstall s390x
%endif
%ifarch %{arm}
%global archinstall aarch32
%endif
%ifarch %{aarch64}
%global archinstall aarch64
%endif
# 32 bit sparc, optimized for v9
%ifarch sparcv9
%global archinstall sparc
%endif
# 64 bit sparc
%ifarch sparc64
%global archinstall sparcv9
%endif
%ifnarch %{jit_arches}
%global archinstall %{_arch}
# turn zero on non jit arches by default
%global _with_zero 1
%endif
# bnc#542545
# 32-bit versus 64-bit specific provides:
%ifarch %{ix86} ppc s390
%global bits 32
%endif
%ifarch x86_64 ia64 s390x
%global bits 64
%endif
%if 0%{?__isa_bits}
%global bits %{__isa_bits}
%endif
#if 0%{?suse_version} > 1500 && !0%{?sle_version}
#global with_shenandoah 1
#else
%global with_shenandoah 0
#endif
%global NSS_LIBDIR %(pkg-config --variable=libdir nss)
%bcond_without bootstrap
%bcond_with zero
# Turn on/off some features depending on openSUSE version
%if 0%{?suse_version} >= 1130
%if ! %{with zero}
%global with_systemtap 1
%else
%global with_systemtap 0
%endif
%else
%global with_systemtap 0
%endif
%if %{with_systemtap}
# Where to install systemtap tapset (links)
# We would like these to be in a package specific subdir,
# but currently systemtap doesn't support that, so we have to
# use the root tapset dir for now. To distinquish between 64
# and 32 bit architectures we place the tapsets under the arch
# specific dir (note that systemtap will only pickup the tapset
# for the primary arch for now). Systemtap uses the machine name
# aka build_cpu as architecture specific directory name.
%global tapsetroot %{_datadir}/systemtap
%global tapsetdir %{tapsetroot}/tapset/%{_build_cpu}
%endif
Name:           java-1_8_0-openjdk
Version:        %{javaver}.%{updatever}
Release:        0
Summary:        OpenJDK 8 Runtime Environment
License:        Apache-1.1 AND Apache-2.0 AND GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-only WITH Classpath-exception-2.0 AND LGPL-2.0-only AND MPL-1.0 AND MPL-1.1 AND SUSE-Public-Domain AND W3C
Group:          Development/Languages/Java
URL:            https://openjdk.java.net/
Source0:        https://icedtea.classpath.org/download/source/icedtea-%{icedtea_version}.tar.xz
Source1:        https://icedtea.classpath.org/download/drops/icedtea8/%{icedtea_version}/openjdk-git.tar.xz
Source2:        https://icedtea.classpath.org/download/drops/icedtea8/%{icedtea_version}/aarch32-git.tar.xz
Source3:        https://icedtea.classpath.org/download/drops/icedtea8/%{icedtea_version}/shenandoah-git.tar.xz
# nss fips configuration file
Source17:       nss.fips.cfg.in
# RPM/distribution specific patches
# bsc#1211968
Patch1:         bsc1211968.patch
# RHBZ 1015432
Patch2:         1015432.patch
# Restrict access to java-atk-wrapper classes
Patch3:         java-atk-wrapper-security.patch
# Fix use of unintialized memory in adlc parser
Patch12:        adlc-parser.patch
# Fix different integer/pointer type mismatches that are fatal with gcc14
Patch13:        fix-build-with-gcc14.patch
# Avoid triggering inactivity timeout while generating javadoc in zero VM
Patch14:        zero-javadoc-verbose.patch
# Fix detection of jobserver support
Patch15:        make-jobserver-detection.patch
#
# OpenJDK specific patches
#
# Patch for PPC
Patch103:       ppc-zero-hotspot.patch
Patch1001:      java-1_8_0-openjdk-suse-desktop-files.patch
Patch1002:      icedtea-3.8.0-s390.patch
Patch2001:      disable-doclint-by-default.patch
Patch2002:      JDK_1_8_0-8208602.patch
Patch3000:      tls13extensions.patch
Patch4000:      riscv64-zero.patch
Patch5001:      fips.patch
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  gtk2-devel
BuildRequires:  javapackages-tools
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libpng-devel
BuildRequires:  libxslt
BuildRequires:  mozilla-nss-devel >= 3.53
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xz
BuildRequires:  zip
# Requires rest of java
Requires:       %{name}-headless = %{version}-%{release}
Requires:       fontconfig
# Standard JPackage base provides.
Provides:       java = %{javaver}
Provides:       java-%{javaver} = %{version}-%{release}
Provides:       java-openjdk = %{version}-%{release}
Provides:       jre = %{javaver}
Provides:       jre-%{javaver} = %{version}-%{release}
Provides:       jre-%{javaver}-openjdk = %{version}-%{release}
Provides:       jre-openjdk = %{version}-%{release}
# Standard JPackage extensions provides.
Provides:       java-fonts = %{version}
# Required at least by fop
Provides:       java-%{bits} = %{javaver}
Provides:       java-%{javaver}-%{bits}
Provides:       java-openjdk-%{bits} = %{version}-%{release}
Provides:       jre-%{bits} = %{javaver}
Provides:       jre-%{javaver}-%{bits}
Provides:       jre-%{javaver}-openjdk-%{bits} = %{version}-%{release}
Provides:       jre-openjdk-%{bits} = %{version}-%{release}
Provides:       jre1.3.x
Provides:       jre1.4.x
Provides:       jre1.5.x
Provides:       jre1.6.x
Provides:       jre1.7.x
Provides:       jre1.8.x
%if %{with bootstrap}
BuildRequires:  java-devel >= 1.7
BuildConflicts: java-devel >= 1.9
BuildConflicts: java-devel-openj9
%else
BuildRequires:  %{name}-devel
%endif
%if %{with_system_kerberos}
BuildRequires:  krb5-devel
%endif
# Zero-assembler build requirement.
%if %{with zero}
BuildRequires:  libffi-devel
%endif
%if 0%{?suse_version} <= 1130
BuildRequires:  xorg-x11-devel
%else
BuildRequires:  libX11-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
%endif
# runtime certificates generation available in 11.3+ - bnc#596177
%if 0%{?suse_version} >= 1130
BuildRequires:  java-ca-certificates
Requires(post): file
Requires(post): java-ca-certificates
%else
BuildRequires:  openssl-certs
# the certificates will converted in a prep to standard keystore file - cacerts
# The openssl requirment seems to be necessary for build only.
Requires:       openssl
%endif
%if %{with_systemtap}
BuildRequires:  systemtap-sdt-devel
%endif
%if %{with_system_pcsc}
BuildRequires:  pcsc-lite-devel
%endif
%if %{with_system_sctp}
BuildRequires:  lksctp-tools-devel
%endif

%description
The OpenJDK 8 runtime environment.

%package headless
Summary:        OpenJDK 8 Runtime Environment
# Require jpackage-utils for ownership of /usr/lib/jvm/
Group:          Development/Languages/Java
Requires:       jpackage-utils
# mozilla-nss has to be installed to prevent
# java.security.ProviderException: Could not initialize NSS
# ...
# java.io.FileNotFoundException: /usr/lib64/libnss3.so
#was bnc#634793
Requires:       mozilla-nss
# Post requires update-alternatives to install tool update-alternatives.
Requires(post): update-alternatives
# Postun requires update-alternatives to uninstall tool update-alternatives.
Requires(postun): update-alternatives
# Standard JPackage base provides.
Provides:       java-%{javaver}-headless = %{version}-%{release}
Provides:       java-headless = %{javaver}
Provides:       java-openjdk-headless = %{version}-%{release}
Provides:       jre-%{javaver}-headless = %{version}-%{release}
Provides:       jre-%{javaver}-openjdk-headless = %{version}-%{release}
Provides:       jre-headless = %{javaver}
Provides:       jre-openjdk-headless = %{version}-%{release}
# Standard JPackage extensions provides.
Provides:       jaas = %{version}
Provides:       java-sasl = %{version}
Provides:       jce = %{version}
Provides:       jdbc-stdext = 4.2
Provides:       jndi = %{version}
Provides:       jndi-cos = %{version}
Provides:       jndi-dns = %{version}
Provides:       jndi-ldap = %{version}
Provides:       jndi-rmi = %{version}
Provides:       jsse = %{version}

%description headless
The OpenJDK 8 runtime environment without audio and video support.

%package devel
Summary:        OpenJDK 8 Development Environment
# Require base package.
Group:          Development/Languages/Java
Requires:       %{name} = %{version}-%{release}
# Post requires update-alternatives to install tool update-alternatives.
Requires(post): update-alternatives
# Postun requires update-alternatives to uninstall tool update-alternatives.
Requires(postun): update-alternatives
# Standard JPackage devel provides.
Provides:       java-%{javaver}-devel = %{version}
Provides:       java-devel = %{javaver}
Provides:       java-devel-openjdk = %{version}
Provides:       java-sdk = %{javaver}
Provides:       java-sdk-%{javaver} = %{version}
Provides:       java-sdk-%{javaver}-openjdk = %{version}
Provides:       java-sdk-openjdk = %{version}

%description devel
The OpenJDK 8 development tools.

%package demo
Summary:        OpenJDK 8 Demos
Group:          Development/Languages/Java
Requires:       %{name} = %{version}-%{release}

%description demo
The OpenJDK 8 demos.

%package src
Summary:        OpenJDK 8 Source Bundle
Group:          Development/Languages/Java
Requires:       %{name} = %{version}-%{release}

%description src
The OpenJDK 8 source bundle.

%package javadoc
Summary:        OpenJDK 8 API Documentation
Group:          Development/Languages/Java
Requires:       jpackage-utils
# Post requires update-alternatives to install javadoc alternative.
Requires(post): update-alternatives
# Postun requires update-alternatives to uninstall javadoc alternative.
Requires(postun): update-alternatives
# Standard JPackage javadoc provides.
Provides:       java-%{javaver}-javadoc = %{version}-%{release}
Provides:       java-javadoc = %{version}-%{release}
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description javadoc
The OpenJDK 8 API documentation.

%package accessibility
Summary:        OpenJDK 8 accessibility connector
Group:          Development/Languages/Java
Requires:       %{name} = %{version}-%{release}
Requires:       java-atk-wrapper

%description accessibility
Enables accessibility support in OpenJDK 8 by using java-atk-wrapper.
This allows compatible at-spi2 based accessibility programs to work
for AWT and Swing-based programs.

Please note, the java-atk-wrapper is still in beta, and OpenJDK 8
itself is still being tuned to be working with accessibility features.
There are known issues with accessibility on, so please do not install
this package unless you really need to.

%prep
%setup -q -n icedtea-%{icedtea_version}

%patch -P 1001 -p1
%ifarch s390
%patch -P 1002 -p1
%endif

# Setup nss.fips.cfg
sed -e "s:@NSS_LIBDIR@:%{NSS_LIBDIR}:g" %{SOURCE17} > nss.fips.cfg
sed -i -e "s:@NSS_SECMOD@:sql\:/etc/pki/nssdb:g" nss.fips.cfg

%build
%define _lto_cflags %{nil}
export LANG=C
unset JAVA_HOME

# How many cpu's do we have?
export NUM_PROC=`%{_bindir}/getconf _NPROCESSORS_ONLN 2> /dev/null || :`
export NUM_PROC=${NUM_PROC:-1}

# handle zlib packages without pkg-config file
%if 0%{?suse_version} <= 1130
export ZLIB_CFLAGS=" "
export ZLIB_LIBS="-L/%{_lib} -lz"
%endif

CFLAGS=$(rpm -E '%{optflags}' | sed 's/-Wall\>//')
CFLAGS="$CFLAGS -Wno-error"
CXXFLAGS=${CFLAGS}
%ifarch ppc64 ppc64le ppc
CFLAGS="$CFLAGS -fno-strict-aliasing"
%endif
%if 0%{?suse_version} >= 1330
CFLAGS="$CFLAGS -fno-delete-null-pointer-checks -fno-lifetime-dse -fcommon"
CXXFLAGS="$CXXFLAGS -std=gnu++98 -fno-delete-null-pointer-checks -fno-lifetime-dse -fcommon"
%endif
export CFLAGS
export CXXFLAGS

sh autogen.sh
%configure \
        --disable-downloading \
        --with-tzdata-dir=%{_datadir}/javazi \
        --with-pkgversion="build %{javaver}_%{updatever}-b%{buildver} suse-%{release}-%{_arch}" \
        --with-jdk-home="%{_sysconfdir}/alternatives/java_sdk" \
        --disable-nss \
        --enable-sysconf-nss \
        --enable-non-nss-curves \
%if %{with bootstrap}
        --enable-bootstrap \
%else
        --disable-bootstrap \
%endif
%ifnarch %{arm} %{aarch64}
        --with-parallel-jobs="${NUM_PROC}" \
%endif
%ifarch s390
        --with-boot-jdk-jvmargs="-Xms256M -Xmx768M" \
%endif
%if %{with zero}
        --enable-zero \
        --disable-jfr \
%endif
%if 0%{?suse_version} <= 1110
        --disable-system-gio \
        --disable-system-gconf \
%endif
%if %{with_system_lcms}
        --enable-system-lcms \
%else
        --disable-system-lcms \
%endif
%if %{with_system_pcsc}
        --enable-system-pcsc \
%else
        --disable-system-pcsc \
%endif
%if %{with_system_sctp}
        --enable-system-sctp \
%else
        --disable-system-sctp \
%endif
%if %{with_system_kerberos}
        --enable-system-kerberos \
%else
        --disable-system-kerberos \
%endif
%if %{with_improved_font_rendering}
        --enable-improved-font-rendering \
%else
        --disable-improved-font-rendering \
%endif
%ifarch %{arm}
        --with-hotspot-src-zip=%{SOURCE2} \
%else
%if %{without zero} && %{with_shenandoah}
        --with-hotspot-src-zip=%{SOURCE3} \
        --with-hotspot-build=shenandoah \
%endif
%endif
        --with-openjdk-src-zip=%{SOURCE1}

make patch %{?_smp_mflags}

patch -p0 -i %{PATCH1}
patch -p0 -i %{PATCH2}
patch -p0 -i %{PATCH3}
patch -p0 -i %{PATCH12}
patch -p0 -i %{PATCH13}

%if %{with zero}
patch -p0 -i %{PATCH14}
%endif

patch -p0 -i %{PATCH15}

%ifarch ppc ppc64 ppc64le
# PPC fixes
patch -p0 -i %{PATCH103}
%endif

patch -p0 -i %{PATCH2001}
patch -p0 -i %{PATCH2002}

patch -p0 -i %{PATCH3000}

patch -p0 -i %{PATCH4000}

patch -p0 -i %{PATCH5001}

(cd openjdk/common/autoconf
 bash ./autogen.sh
)

make %{?_smp_mflags}

export JAVA_HOME=$(pwd)/%{buildoutputdir}images/j2sdk-image

# cacerts are generated in runtime in openSUSE
if [ -f %{buildoutputdir}images/j2sdk-image/jre/lib/security/cacerts ]; then
        rm -f %{buildoutputdir}images/j2sdk-image/jre/lib/security/cacerts
fi

%if 0%{?suse_version} < 1130
# ========== a default keystore ==========
# a cacerts generation - 11.3+ use java-ca-certificates package
for PEM in %{_sysconfdir}/ssl/certs/*.pem; do
    ALIAS=$(basename ${PEM} .pem)
    awk '/-----BEGIN CERTIFICATE-----/,/-----END CERTIFICATE-----/{ print $0; }' ${PEM} > ${ALIAS}.pem

    yes | $JAVA_HOME/jre/bin/keytool -import -alias ${ALIAS} -keystore %{buildoutputdir}images/j2sdk-image/jre/lib/security/cacerts -storepass 'changeit' -file ${ALIAS}.pem || :
    rm ${ALIAS}.pem
done
%endif

# Check debug symbols are present and can identify code
SERVER_JVM="$JAVA_HOME/jre/lib/%{archinstall}/server/libjvm.so"
if [ -f "$SERVER_JVM" ] ; then
  nm -aCl "$SERVER_JVM" | grep javaCalls.cpp
fi
CLIENT_JVM="$JAVA_HOME/jre/lib/%{archinstall}/client/libjvm.so"
if [ -f "$CLIENT_JVM" ] ; then
  nm -aCl "$CLIENT_JVM" | grep javaCalls.cpp
fi
ZERO_JVM="$JAVA_HOME/jre/lib/%{archinstall}/zero/libjvm.so"
if [ -f "$ZERO_JVM" ] ; then
  nm -aCl "$ZERO_JVM" | grep javaCalls.cpp
fi

%install
export LANG=en_US.UTF-8
#bnc#530046
export STRIP_KEEP_SYMTAB=libjvm*
# skip /usr/lib/rpm/brp-check-bytecode-version:
export NO_BRP_CHECK_BYTECODE_VERSION=true

pushd %{buildoutputdir}images/j2sdk-image

  # Install main files.
  install -d -m 755 %{buildroot}%{_jvmdir}/%{sdkdir}
  cp -a bin include lib src.zip %{buildroot}%{_jvmdir}/%{sdkdir}
  install -d -m 755 %{buildroot}%{_jvmdir}/%{jredir}
  cp -a jre/bin jre/lib %{buildroot}%{_jvmdir}/%{jredir}

  # Install extension symlinks.
  install -d -m 755 %{buildroot}%{jvmjardir}
  pushd %{buildroot}%{jvmjardir}
    RELATIVE=$(%{abs2rel} %{_jvmdir}/%{jredir}/lib %{jvmjardir})
    ln -sf $RELATIVE/jsse.jar jsse-%{version}.jar
    ln -sf $RELATIVE/jce.jar jce-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-ldap-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-cos-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-rmi-%{version}.jar
    ln -sf $RELATIVE/rt.jar jaas-%{version}.jar
    ln -sf $RELATIVE/rt.jar jdbc-stdext-%{version}.jar
    ln -sf jdbc-stdext-%{version}.jar jdbc-stdext-3.0.jar
    ln -sf $RELATIVE/rt.jar sasl-%{version}.jar
    for jar in *-%{version}.jar
    do
      if [ x%{version} != x%{javaver} ]
      then
        ln -sf $jar $(echo $jar | sed "s|-%{version}.jar|-%{javaver}.jar|g")
      fi
      ln -sf $jar $(echo $jar | sed "s|-%{version}.jar|.jar|g")
    done
  popd

  # Install JCE policy symlinks.
  install -d -m 755 %{buildroot}%{_jvmprivdir}/%{archname}/jce/vanilla

  # Install versionless symlinks.
  pushd %{buildroot}%{_jvmdir}
    ln -sf %{jredir} %{jrelnk}
    ln -sf %{sdkdir} %{sdklnk}
  popd

  pushd %{buildroot}%{_jvmjardir}
    ln -sf %{sdkdir} %{jrelnk}
    ln -sf %{sdkdir} %{sdklnk}
  popd

  # Remove javaws man page
  rm -f man/man1/javaws*

  # Install man pages.
  install -d -m 755 %{buildroot}%{_mandir}/man1
  for manpage in man/man1/*
  do
    # Convert man pages to UTF8 encoding.
    iconv -f ISO_8859-1 -t UTF8 $manpage -o $manpage.tmp
    mv -f $manpage.tmp $manpage
    install -m 644 -p $manpage %{buildroot}%{_mandir}/man1/$(basename \
      $manpage .1)-%{sdklnk}.1
  done

  # Install demos and samples.
  cp -a demo %{buildroot}%{_jvmdir}/%{sdkdir}
  # enable short-circuit
  mkdir -p sample/rmi
  [ -f bin/java-rmi.cgi ] && mv bin/java-rmi.cgi sample/rmi
  cp -a sample %{buildroot}%{_jvmdir}/%{sdkdir}

%if %{with_systemtap}
  # Install systemtap support files.
  cp -a tapset %{buildroot}%{_jvmdir}/%{sdkdir}
  pushd %{buildroot}%{_jvmdir}/%{sdkdir}/tapset
    for i in *.stp; do
      mv $i $(basename $i .stp)-%{javaver}.stp
    done
  popd
  install -d -m 755 %{buildroot}%{tapsetdir}
  pushd %{buildroot}%{tapsetdir}
    RELATIVE=$(%{abs2rel} %{_jvmdir}/%{sdkdir}/tapset %{tapsetdir})
    ln -sf $RELATIVE/*.stp .
  popd
%endif

popd

# Install nss.fips.cfg: NSS configuration for global FIPS mode (crypto-policies)
install -m 644 nss.fips.cfg %{buildroot}%{_jvmdir}/%{jredir}/lib/security/

# Install Javadoc documentation.
install -d -m 755 %{buildroot}%{_javadocdir}
cp -a %{buildoutputdir}/docs %{buildroot}%{_javadocdir}/%{sdklnk}

# Install icons and menu entries.
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
    openjdk/jdk/src/solaris/classes/sun/awt/X11/java-icon${s}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}-openjdk.png
done

# Install desktop files.
install -d -m 0755 %{buildroot}%{_datadir}/{applications,pixmaps}
install -d -m 0755 %{buildroot}/%{_jvmdir}/%{jredir}/lib/desktop/
for d in jconsole policytool; do
    install -m 0644 $d.desktop %{buildroot}/%{_jvmdir}/%{jredir}/lib/desktop/
    %suse_update_desktop_file %{buildroot}/%{_jvmdir}/%{jredir}/lib/desktop/$d.desktop
done

# Find JRE directories.
find %{buildroot}%{_jvmdir}/%{jredir} -type d \
  | grep -v jre/lib/security \
  | sed 's|'%{buildroot}'|%dir |' \
  > %{name}.files.headless
# Find JRE files.
find %{buildroot}%{_jvmdir}/%{jredir} -type f -o -type l \
  | grep -v jre/lib/security \
  | sed 's|'%{buildroot}'||' \
  >> %{name}.files.all
#split %{name}.files to %{name}.files-headless and %{name}.files
#see https://bugzilla.redhat.com/show_bug.cgi?id=875408
NOT_HEADLESS=\
"%{_jvmdir}/%{jredir}/lib/%{archinstall}/libjsoundalsa.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libsplashscreen.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libawt_xawt.so
%{_jvmdir}/%{jredir}/lib/%{archinstall}/libjawt.so"
#filter %{name}.files from %{name}.files.all to %{name}.files-headless
ALL=`cat %{name}.files.all`
for file in $ALL ; do
  INLCUDE="NO" ;
  for blacklist in $NOT_HEADLESS ; do
    # we can not match normally, because rpmbuild will evaluate !0 result as script failure
    q=`expr match "$file" "$blacklist"` || :
    l=`expr length "$blacklist"` || :
    if [ $q -eq $l ]; then
       INLCUDE="YES" ;
    fi;
  done
  if [ "x$INLCUDE" = "xNO" ]; then
    echo "$file" >> %{name}.files-headless
  else
    echo "$file" >> %{name}.files
  fi
done
# Find demo directories.
find %{buildroot}%{_jvmdir}/%{sdkdir}/demo \
  %{buildroot}%{_jvmdir}/%{sdkdir}/sample -type d \
  | sed 's|'%{buildroot}'|%dir |' \
  > %{name}-demo.files

# FIXME: remove SONAME entries from demo DSOs.  See
# https://bugzilla.redhat.com/show_bug.cgi?id=436497

# Find non-documentation demo files.
find %{buildroot}%{_jvmdir}/%{sdkdir}/demo \
  %{buildroot}%{_jvmdir}/%{sdkdir}/sample \
  -type f -o -type l | sort \
  | grep -v README \
  | sed 's|'%{buildroot}'||' \
  >> %{name}-demo.files
# Find documentation demo files.
find %{buildroot}%{_jvmdir}/%{sdkdir}/demo \
  %{buildroot}%{_jvmdir}/%{sdkdir}/sample \
  -type f -o -type l | sort \
  | grep README \
  | sed 's|'%{buildroot}'||' \
  | sed 's|^|%doc |' \
  >> %{name}-demo.files

# Create links which leads to separately installed java-atk-bridge and allow configuration
# links points to java-atk-wrapper - an dependence
# mvyskocil: links are handled in post, lets make ghost files there
  touch %{buildroot}/%{_jvmdir}/%{jredir}/lib/%{archinstall}/libatk-wrapper.so
  touch %{buildroot}/%{_jvmdir}/%{jredir}/lib/ext/java-atk-wrapper.jar
  pushd %{buildroot}/%{_jvmdir}/%{jredir}/lib/
    echo "#Config file to  enable java-atk-wrapper" > accessibility.properties
    echo "" >> accessibility.properties
    echo "assistive_technologies=org.GNOME.Accessibility.AtkWrapper" >> accessibility.properties
    echo "" >> accessibility.properties
  popd

# fdupes links the files from JDK to JRE, so it breaks a JRE
# use it carefully :))
%fdupes -s %{buildroot}/%{_jvmdir}/%{jredir}/
%fdupes -s %{buildroot}/%{_jvmdir}/%{sdkdir}/demo
%fdupes -s %{buildroot}%{_javadocdir}/%{sdklnk}

%if 0%{?suse_version} <= 1130
# bnc496378 - check the size of installed cacerts
# 32 bytes means a default empty one
if [[ $(stat -c "%%s" %{buildroot}/%{cacerts}) == "32" ]]; then
    echo "ERROR: Default keystore seems empty"
    exit 1
fi
%endif

%post headless
ext=.gz
update-alternatives \
  --install %{_bindir}/java java %{jrebindir}/java %{priority} \
  --slave %{_jvmdir}/jre jre %{_jvmdir}/%{jrelnk} \
  --slave %{_jvmjardir}/jre jre_exports %{_jvmjardir}/%{jrelnk} \
  --slave %{_bindir}/keytool keytool %{jrebindir}/keytool \
  --slave %{_bindir}/orbd orbd %{jrebindir}/orbd \
  --slave %{_bindir}/policytool policytool %{jrebindir}/policytool \
  --slave %{_bindir}/rmid rmid %{jrebindir}/rmid \
  --slave %{_bindir}/rmiregistry rmiregistry %{jrebindir}/rmiregistry \
  --slave %{_bindir}/servertool servertool %{jrebindir}/servertool \
  --slave %{_bindir}/tnameserv tnameserv %{jrebindir}/tnameserv \
  --slave %{_bindir}/pack200 pack200 %{jrebindir}/pack200 \
  --slave %{_bindir}/unpack200 unpack200 %{jrebindir}/unpack200 \
  --slave %{_mandir}/man1/java.1$ext java.1$ext \
  %{_mandir}/man1/java-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/keytool.1$ext keytool.1$ext \
  %{_mandir}/man1/keytool-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/orbd.1$ext orbd.1$ext \
  %{_mandir}/man1/orbd-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/policytool.1$ext policytool.1$ext \
  %{_mandir}/man1/policytool-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/rmid.1$ext rmid.1$ext \
  %{_mandir}/man1/rmid-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/rmiregistry.1$ext rmiregistry.1$ext \
  %{_mandir}/man1/rmiregistry-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/servertool.1$ext servertool.1$ext \
  %{_mandir}/man1/servertool-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/tnameserv.1$ext tnameserv.1$ext \
  %{_mandir}/man1/tnameserv-%{sdklnk}.1$ext  \
  --slave %{_mandir}/man1/pack200.1$ext pack200.1$ext \
  %{_mandir}/man1/pack200-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/unpack200.1$ext unpack200.1$ext \
  %{_mandir}/man1/unpack200-%{sdklnk}.1$ext \
  --slave %{_datadir}/applications/policytool.desktop policytool.desktop \
  %{_jvmdir}/%{jredir}/lib/desktop/policytool.desktop \
  || :

update-alternatives \
  --install %{_jvmdir}/jre-openjdk \
  jre_openjdk %{_jvmdir}/%{jrelnk} %{priority} \
  --slave %{_jvmjardir}/jre-openjdk \
  jre_openjdk_exports %{_jvmjardir}/%{jrelnk}
update-alternatives \
  --install %{_jvmdir}/jre-%{javaver} \
  jre_%{javaver} %{_jvmdir}/%{jrelnk} %{priority} \
  --slave %{_jvmjardir}/jre-%{javaver} \
  jre_%{javaver}_exports %{_jvmjardir}/%{jrelnk}

%postun headless
if [ $1 -eq 0 ]
then
  if test -f /proc/sys/fs/binfmt_misc/jarexec
  then
    echo '-1' > /proc/sys/fs/binfmt_misc/jarexec
  fi
  update-alternatives --remove java %{jrebindir}/java
  update-alternatives --remove jre_openjdk %{_jvmdir}/%{jrelnk}
  update-alternatives --remove jre_%{javaver} %{_jvmdir}/%{jrelnk}
fi

%if 0%{?suse_version} >= 1130
%posttrans headless
# bnc#781690#c11: don't trust user defined JAVA_HOME and use the current VM
# XXX: this might conflict between various versions of openjdk
export JAVA_HOME=%{_jvmdir}/%{jrelnk}

# check if the java-cacerts is a valid keystore (bnc#781690)
if [ X"`%{_bindir}/file --mime-type -b %{javacacerts}`" \
    != "Xapplication/x-java-keystore;" ]; then
%if 0%{?suse_version} <= 1310
    # workaround for bnc#847952 - pre 13.1 keyring.jar attempts to load invalid keystore and fail on it
    rm -f "%{javacacerts}"
%endif
    %{_sbindir}/update-ca-certificates
fi

# remove the default empty cacert file, if it's installed
if [ 0`stat -c "%%s" %{cacerts} 2>/dev/null` = "032" ] ; then
    rm -f %{cacerts}
fi

# if cacerts does exists, neither does not contain/point to a
# valid keystore (bnc#781690) ...
if [ X"`%{_bindir}/file --mime-type -b -L %{cacerts}`" \
    != "Xapplication/x-java-keystore;" ]; then
    # bnc#727223
    rm -f %{cacerts}
    ln -s %{javacacerts} %{cacerts}
fi
%endif

%post devel
ext=.gz
update-alternatives \
  --install %{_bindir}/javac javac %{sdkbindir}/javac %{priority} \
  --slave %{_jvmdir}/java java_sdk %{_jvmdir}/%{sdklnk} \
  --slave %{_jvmjardir}/java java_sdk_exports %{jvmjarlink} \
  --slave %{_bindir}/appletviewer appletviewer %{sdkbindir}/appletviewer \
  --slave %{_bindir}/extcheck extcheck %{sdkbindir}/extcheck \
  --slave %{_bindir}/jar jar %{sdkbindir}/jar \
  --slave %{_bindir}/jarsigner jarsigner %{sdkbindir}/jarsigner \
  --slave %{_bindir}/javadoc javadoc %{sdkbindir}/javadoc \
  --slave %{_bindir}/javah javah %{sdkbindir}/javah \
  --slave %{_bindir}/javap javap %{sdkbindir}/javap \
  --slave %{_bindir}/jcmd jcmd %{sdkbindir}/jcmd \
  --slave %{_bindir}/jconsole jconsole %{sdkbindir}/jconsole \
  --slave %{_bindir}/jdb jdb %{sdkbindir}/jdb \
  --slave %{_bindir}/jhat jhat %{sdkbindir}/jhat \
  --slave %{_bindir}/jinfo jinfo %{sdkbindir}/jinfo \
  --slave %{_bindir}/jmap jmap %{sdkbindir}/jmap \
  --slave %{_bindir}/jps jps %{sdkbindir}/jps \
  --slave %{_bindir}/jrunscript jrunscript %{sdkbindir}/jrunscript \
  --slave %{_bindir}/jsadebugd jsadebugd %{sdkbindir}/jsadebugd \
  --slave %{_bindir}/jstack jstack %{sdkbindir}/jstack \
  --slave %{_bindir}/jstat jstat %{sdkbindir}/jstat \
  --slave %{_bindir}/jstatd jstatd %{sdkbindir}/jstatd \
  --slave %{_bindir}/native2ascii native2ascii %{sdkbindir}/native2ascii \
  --slave %{_bindir}/rmic rmic %{sdkbindir}/rmic \
  --slave %{_bindir}/schemagen schemagen %{sdkbindir}/schemagen \
  --slave %{_bindir}/serialver serialver %{sdkbindir}/serialver \
  --slave %{_bindir}/wsgen wsgen %{sdkbindir}/wsgen \
  --slave %{_bindir}/wsimport wsimport %{sdkbindir}/wsimport \
  --slave %{_bindir}/xjc xjc %{sdkbindir}/xjc \
  --slave %{_mandir}/man1/appletviewer.1$ext appletviewer.1$ext \
  %{_mandir}/man1/appletviewer-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/extcheck.1$ext extcheck.1$ext \
  %{_mandir}/man1/extcheck-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jar.1$ext jar.1$ext \
  %{_mandir}/man1/jar-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jarsigner.1$ext jarsigner.1$ext \
  %{_mandir}/man1/jarsigner-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/javac.1$ext javac.1$ext \
  %{_mandir}/man1/javac-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/javadoc.1$ext javadoc.1$ext \
  %{_mandir}/man1/javadoc-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/javah.1$ext javah.1$ext \
  %{_mandir}/man1/javah-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/javap.1$ext javap.1$ext \
  %{_mandir}/man1/javap-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jconsole.1$ext jconsole.1$ext \
  %{_mandir}/man1/jconsole-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jcmd.1$ext jcmd.1$ext \
  %{_mandir}/man1/jcmd-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jdb.1$ext jdb.1$ext \
  %{_mandir}/man1/jdb-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jhat.1$ext jhat.1$ext \
  %{_mandir}/man1/jhat-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jinfo.1$ext jinfo.1$ext \
  %{_mandir}/man1/jinfo-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jmap.1$ext jmap.1$ext \
  %{_mandir}/man1/jmap-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jps.1$ext jps.1$ext \
  %{_mandir}/man1/jps-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jrunscript.1$ext jrunscript.1$ext \
  %{_mandir}/man1/jrunscript-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jsadebugd.1$ext jsadebugd.1$ext \
  %{_mandir}/man1/jsadebugd-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jstack.1$ext jstack.1$ext \
  %{_mandir}/man1/jstack-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jstat.1$ext jstat.1$ext \
  %{_mandir}/man1/jstat-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jstatd.1$ext jstatd.1$ext \
  %{_mandir}/man1/jstatd-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/native2ascii.1$ext native2ascii.1$ext \
  %{_mandir}/man1/native2ascii-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/rmic.1$ext rmic.1$ext \
  %{_mandir}/man1/rmic-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/schemagen.1$ext schemagen.1$ext \
  %{_mandir}/man1/schemagen-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/serialver.1$ext serialver.1$ext \
  %{_mandir}/man1/serialver-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/wsgen.1$ext wsgen.1$ext \
  %{_mandir}/man1/wsgen-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/wsimport.1$ext wsimport.1$ext \
  %{_mandir}/man1/wsimport-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/xjc.1$ext xjc.1$ext \
  %{_mandir}/man1/xjc-%{sdklnk}.1$ext \
  --slave %{_datadir}/applications/jconsole.desktop jconsole.desktop \
  %{_jvmdir}/%{jredir}/lib/desktop/jconsole.desktop \
  || :

update-alternatives \
  --install %{_jvmdir}/java-openjdk \
  java_sdk_openjdk %{_jvmdir}/%{sdklnk} %{priority} \
  --slave %{_jvmjardir}/java-openjdk \
  java_sdk_openjdk_exports %{jvmjarlink}
update-alternatives \
  --install %{_jvmdir}/java-%{javaver} \
  java_sdk_%{javaver} %{_jvmdir}/%{sdklnk} %{priority} \
  --slave %{_jvmjardir}/java-%{javaver} \
  java_sdk_%{javaver}_exports %{jvmjarlink}

%postun devel
if [ $1 -eq 0 ]
then
  update-alternatives --remove javac %{sdkbindir}/javac
  update-alternatives --remove java_sdk_openjdk %{_jvmdir}/%{sdklnk}
  update-alternatives --remove java_sdk_%{javaver} %{_jvmdir}/%{sdklnk}
fi

%post javadoc
# in some settings, the %{_javadocdir}/%{sdklnk}/api does not exist
# and the update-alternatives call ends up in error. So, filter this
# cases out.
if [ -d %{_javadocdir}/%{sdklnk}/api ]
then
  update-alternatives \
    --install %{_javadocdir}/java javadocdir %{_javadocdir}/%{sdklnk}/api \
    %{priority}
fi

%postun javadoc
if [ $1 -eq 0 ]
then
# in some settings, the %{_javadocdir}/%{sdklnk}/api does not exist
# and the update-alternatives call ends up in error. So, filter this
# cases out.
  if [ -d %{_javadocdir}/%{sdklnk}/api ]
  then
    update-alternatives --remove javadocdir %{_javadocdir}/%{sdklnk}/api
  fi
fi

%post accessibility
# create links to java-atk-wrapper
if [ ! -e %{_jvmdir}/%{jredir}/lib/%{archinstall}/libatk-wrapper.so ]; then
    if [ -e %{_libdir}/java-atk-wrapper/libatk-wrapper.so ]; then
        ln -sf %{_libdir}/java-atk-wrapper/libatk-wrapper.so  %{_jvmdir}/%{jredir}/lib/%{archinstall}/libatk-wrapper.so
    else
        ln -sf %{_libdir}/java-atk-wrapper/libatk-wrapper.so.0  %{_jvmdir}/%{jredir}/lib/%{archinstall}/libatk-wrapper.so
    fi
fi
if [ ! -e %{_jvmdir}/%{jredir}/lib/ext/java-atk-wrapper.jar ]; then
    ln -sf %{_libdir}/java-atk-wrapper/java-atk-wrapper.jar %{_jvmdir}/%{jredir}/lib/ext/java-atk-wrapper.jar
fi

%files -f %{name}.files
%dir %{_jvmdir}/%{jredir}/lib/%{archinstall}
%dir %{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/*x*/apps/java-%{javaver}-openjdk.png

%files headless -f %{name}.files-headless
%dir %{_jvmdir}
%dir %{_jvmdir}/%{jredir}/
%dir %{_jvmdir}/%{jredir}/bin
%dir %{_jvmdir}/%{jredir}/lib
%dir %{_jvmdir}/%{jredir}/lib/%{archinstall}
%dir %{_jvmdir}/%{jredir}/lib/%{archinstall}/jli
%ifnarch %{arm}
%dir %{_jvmdir}/%{jredir}/lib/%{archinstall}/server
%else
%dir %{_jvmdir}/%{jredir}/lib/%{archinstall}/client
%endif
%dir %{_jvmdir}/%{jredir}/lib/cmm
%dir %{_jvmdir}/%{jredir}/lib/desktop
%dir %{_jvmdir}/%{jredir}/lib/ext
%dir %{_jvmdir}/%{jredir}/lib/images
%dir %{_jvmdir}/%{jredir}/lib/images/cursors
%if %{without zero}
%dir %{_jvmdir}/%{jredir}/lib/jfr
%endif
%dir %{_jvmdir}/%{jredir}/lib/management
%dir %{_jvmdir}/%{jredir}/lib/security
%dir %{_jvmdir}/%{jredir}/lib/security/policy
%dir %{_jvmdir}/%{jredir}/lib/security/policy/limited
%dir %{_jvmdir}/%{jredir}/lib/security/policy/unlimited
%dir %{_libdir}/jvm-exports
%dir %{_libdir}/jvm-private

%doc %{buildoutputdir}images/j2sdk-image/jre/ASSEMBLY_EXCEPTION
%license %{buildoutputdir}images/j2sdk-image/jre/LICENSE
%doc %{buildoutputdir}images/j2sdk-image/jre/THIRD_PARTY_README

%dir %{_jvmdir}/%{sdkdir}
%{_jvmdir}/%{jrelnk}
%{_jvmjardir}/%{jrelnk}
%{_jvmprivdir}/*
%{jvmjardir}
%if 0%{?suse_version} <= 1130
%config(noreplace) %{cacerts}
%endif
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.policy
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.security
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/blacklisted.certs
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/nss.cfg
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/nss.fips.cfg
%{_mandir}/man1/java-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jjs-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/keytool-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/orbd-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/pack200-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/policytool-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/rmid-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/rmiregistry-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/servertool-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/tnameserv-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/unpack200-%{sdklnk}.1%{?ext_man}
%{_jvmdir}/%{jredir}/lib/security/policy/limited/US_export_policy.jar
%{_jvmdir}/%{jredir}/lib/security/policy/limited/local_policy.jar
%{_jvmdir}/%{jredir}/lib/security/policy/unlimited/US_export_policy.jar
%{_jvmdir}/%{jredir}/lib/security/policy/unlimited/local_policy.jar

%files devel
%dir %{_jvmdir}/%{sdkdir}/bin
%dir %{_jvmdir}/%{sdkdir}/include
%dir %{_jvmdir}/%{sdkdir}/lib
%if %{with_systemtap}
%dir %{_jvmdir}/%{sdkdir}/tapset
%endif
%{_jvmdir}/%{sdkdir}/bin/*
%{_jvmdir}/%{sdkdir}/include/*
%{_jvmdir}/%{sdkdir}/lib/*

%if %{with_systemtap}
%{_jvmdir}/%{sdkdir}/tapset/*.stp
%endif
%{_jvmdir}/%{sdklnk}
%{_jvmjardir}/%{sdklnk}
%{_mandir}/man1/appletviewer-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/extcheck-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/idlj-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jar-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jarsigner-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/javac-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/javadoc-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/javah-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/javap-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jconsole-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jcmd-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jdb-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jdeps-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jhat-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jinfo-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jmap-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jps-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jrunscript-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jsadebugd-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jstack-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jstat-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jstatd-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/native2ascii-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/rmic-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/schemagen-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/serialver-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/wsgen-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/wsimport-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/xjc-%{sdklnk}.1%{?ext_man}

%if %{with_systemtap}
%{tapsetroot}
%endif

%files demo -f %{name}-demo.files

%files src
%{_jvmdir}/%{sdkdir}/src.zip

%files javadoc
%dir %{_javadocdir}
%dir %{_javadocdir}/%{sdklnk}
%{_javadocdir}/%{sdklnk}/*

%files accessibility
%dir %{_jvmdir}/%{jredir}/lib/ext
%config(noreplace) %{_jvmdir}/%{jredir}/lib/accessibility.properties
%ghost %{_jvmdir}/%{jredir}/lib/%{archinstall}/libatk-wrapper.so
%ghost %{_jvmdir}/%{jredir}/lib/ext/java-atk-wrapper.jar

%changelog
