#
# spec file
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


%{!?aarch64:%global aarch64 aarch64 arm64 armv8}
%{!?arm6:%global arm6 armv3l armv4b armv4l armv4tl armv5b armv5l armv5teb armv5tel armv5tejl armv6l armv6hl}
%global jit_arches %{ix86} x86_64 ppc64 ppc64le %{aarch64} %{arm} s390x riscv64
%global debug 0
%global is_release 1
%global buildoutputdir build
# Convert an absolute path to a relative path.  Each symbolic link is
# specified relative to the directory in which it is installed so that
# it will resolve properly within chrooted installations.
%global script 'use File::Spec; print File::Spec->abs2rel($ARGV[0], $ARGV[1])'
%global abs2rel perl -e %{script}
%global syslibdir       %{_libdir}
%global archname        %{name}
# Standard JPackage naming and versioning defines.
%global featurever      19
%global interimver      0
%global updatever       1
%global buildver        10
%global openjdk_repo    jdk19u
%global openjdk_tag     jdk-%{featurever}.%{interimver}.%{updatever}%{?patchver:.%{patchver}}+%{buildver}
%global openjdk_dir     %{openjdk_repo}-jdk-%{featurever}.%{interimver}.%{updatever}%{?patchver:.%{patchver}}-%{buildver}
# JavaEE modules
%global java_atk_wrapper_version 0.33.2
# priority must be 6 digits in total
# % global priority        2705
%global priority        0
%global javaver         %{featurever}
# Standard JPackage directories and symbolic links.
%global sdklnk          java-%{javaver}-openjdk
%global archname        %{sdklnk}
%global jrelnk          jre-%{javaver}-openjdk
%global jrebindir       %{_jvmdir}/%{jrelnk}/bin
%global sdkdir          %{sdklnk}-%{javaver}
%global sdkbindir       %{_jvmdir}/%{sdklnk}/bin
# Prevent brp-java-repack-jars from being run.
%global __jar_repack 0
# cacert symlink
%global cacerts  %{_jvmdir}/%{sdkdir}/lib/security/cacerts
# real file made by update-ca-certificates
%global javacacerts %{_var}/lib/ca-certificates/java-cacerts
%global bootcycle 1
# turn zero on non jit arches by default
%ifnarch %{jit_arches}
%global _with_zero 1
%endif
%ifarch %{arm6}
%global _with_zero 1
%endif
%if %{debug}
%global debugbuild slowdebug
%else
%global debugbuild release
%endif
%if %{bootcycle}
%global imagesdir bootcycle-build/images
%global imagestarget bootcycle-images all
%else
%global imagesdir images
%global imagestarget all
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
# Turn on/off some features depending on openSUSE version
%if 0%{?suse_version} > 1320
%global with_system_pcsc 1
%global with_system_lcms 1
%else
%global with_system_pcsc 0
%global with_system_lcms 0
%endif
%if %{is_release}
%global package_version %{featurever}.%{interimver}.%{updatever}.%{?patchver:%{patchver}}%{!?patchver:0}
%else
%global package_version %{featurever}.%{interimver}.%{updatever}.%{?patchver:%{patchver}}%{!?patchver:0}~%{buildver}
%endif
%global NSS_LIBDIR %(pkg-config --variable=libdir nss)
%bcond_with zero
%if ! %{with zero}
%global with_systemtap 1
%else
%global with_systemtap 0
%endif
%if %{with_systemtap}
%global tapsetroot      %{_datadir}/systemtap
%global tapsetdir %{tapsetroot}/tapset/%{_build_cpu}
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
Name:           java-%{featurever}-openjdk
Version:        %{package_version}
Release:        0
Summary:        OpenJDK %{featurever} Runtime Environment
License:        Apache-1.1 AND Apache-2.0 AND GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-only WITH Classpath-exception-2.0 AND LGPL-2.0-only AND MPL-1.0 AND MPL-1.1 AND SUSE-Public-Domain AND W3C
Group:          Development/Languages/Java
URL:            https://openjdk.java.net/
# Sources from upstream OpenJDK project.
Source0:        https://github.com/openjdk/%{openjdk_repo}/archive/%{openjdk_tag}.tar.gz
# Accessibility support
Source8:        https://download.gnome.org/sources/java-atk-wrapper/0.33/java-atk-wrapper-%{java_atk_wrapper_version}.tar.xz
# Systemtap tapsets. Zipped up to keep it small.
Source10:       systemtap-tapset.tar.xz
# Desktop files. Adapated from IcedTea.
Source11:       jconsole.desktop.in
# nss configuration file
Source12:       nss.cfg.in
# nss fips configuration file
Source13:       nss.fips.cfg.in
# Ensure we aren't using the limited crypto policy
Source14:       TestCryptoLevel.java
# Ensure ECDSA is working
Source15:       TestECDSA.java
# Fresh config.guess and config.sub files
# wget -O config.guess 'http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.guess;hb=HEAD'
Source100:      config.guess
# wget -O config.sub 'http://git.savannah.gnu.org/gitweb/?p=config.git;a=blob_plain;f=config.sub;hb=HEAD'
Source101:      config.sub
# Restrict access to java-atk-wrapper classes
Patch3:         java-atk-wrapper-security.patch
# RHBZ 808293
Patch4:         PStack-808293.patch
# Allow multiple initialization of PKCS11 libraries
Patch5:         multiple-pkcs11-library-init.patch
# Fix instantiation of VM on ZERO
Patch8:         zero-ranges.patch
# From icedtea: Increase default memory limits
Patch10:        memory-limits.patch
# Fix use of unintialized memory in adlc parser
Patch12:        adlc-parser.patch
# Fix: implicit-pointer-decl
Patch13:        implicit-pointer-decl.patch
Patch15:        system-pcsclite.patch
Patch16:        system-crypto-policy.patch
Patch17:        nss-security-provider.patch
Patch18:        fips.patch
#
Patch20:        loadAssistiveTechnologies.patch
#
# OpenJDK specific patches
#
Patch200:       ppc_stack_overflow_fix.patch
#
Patch302:       disable-doclint-by-default.patch
Patch303:       alternative-tzdb_dat.patch
#
Patch400:       jaw-misc.patch
Patch401:       jaw-jdk10.patch
Patch402:       jaw-nogtk.patch
#
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bc
BuildRequires:  binutils
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  giflib-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  java-ca-certificates
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  mozilla-nss-devel >= 3.53
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xprop
BuildRequires:  zip
BuildRequires:  pkgconfig(atk) >= 2.14.0
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(atspi-2) >= 2.14.0
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
# Requires rest of java
Requires:       %{name}-headless = %{version}-%{release}
Requires:       fontconfig
Requires(post): file
%if 0%{?suse_version} > 1500 || 0%{?java_bootstrap}
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
Provides:       jre1.10.x
Provides:       jre1.3.x
Provides:       jre1.4.x
Provides:       jre1.5.x
Provides:       jre1.6.x
Provides:       jre1.7.x
Provides:       jre1.8.x
Provides:       jre1.9.x
%endif
%if 0%{?suse_version} < 1500
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc >= 7
BuildRequires:  gcc-c++ >= 7
%endif
%if %{with_system_lcms}
BuildRequires:  liblcms2-devel
%endif
%if %{bootcycle}
%if 0%{?suse_version} > 1500 || 0%{?java_bootstrap}
BuildRequires:  java-devel >= 18
BuildConflicts: java-devel >= 20
%else
BuildRequires:  %{name}-devel
%endif
%else
BuildRequires:  %{name}-devel
%endif
# Zero-assembler build requirement.
%if %{with zero}
BuildRequires:  libffi-devel
%endif
%if %{with_systemtap}
BuildRequires:  systemtap-sdt-devel
%endif
%if %{with_system_pcsc}
BuildRequires:  pcsc-lite-devel
%endif

%description
The OpenJDK %{featurever} runtime environment.

%package headless
Summary:        OpenJDK %{featurever} Runtime Environment
Group:          Development/Languages/Java
Requires:       jpackage-utils
Requires:       mozilla-nss
Requires(post): java-ca-certificates
# Post requires update-alternatives to install tool update-alternatives.
Requires(post): update-alternatives
# Postun requires update-alternatives to uninstall tool update-alternatives.
Requires(postun):update-alternatives
Recommends:     tzdata-java8
%if 0%{?suse_version} > 1500 || 0%{?java_bootstrap}
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
Provides:       jdbc-stdext = 4.3
Provides:       jndi = %{version}
Provides:       jndi-cos = %{version}
Provides:       jndi-dns = %{version}
Provides:       jndi-ldap = %{version}
Provides:       jndi-rmi = %{version}
Provides:       jsse = %{version}
%endif

%description headless
The OpenJDK %{featurever} runtime environment without audio and video support.

%package devel
Summary:        OpenJDK %{featurever} Development Environment
# Require base package.
Group:          Development/Languages/Java
Requires:       %{name} = %{version}-%{release}
# Post requires update-alternatives to install tool update-alternatives.
Requires(post): update-alternatives
# Postun requires update-alternatives to uninstall tool update-alternatives.
Requires(postun):update-alternatives
%if 0%{?suse_version} > 1500 || 0%{?java_bootstrap}
# Standard JPackage devel provides.
Provides:       java-%{javaver}-devel = %{version}
Provides:       java-devel = %{javaver}
Provides:       java-devel-openjdk = %{version}
Provides:       java-sdk = %{javaver}
Provides:       java-sdk-%{javaver} = %{version}
Provides:       java-sdk-%{javaver}-openjdk = %{version}
Provides:       java-sdk-openjdk = %{version}
%endif

%description devel
The OpenJDK %{featurever} development tools.

%package jmods
Summary:        JMods for OpenJDK %{featurever}
Group:          Development/Languages/Java
Requires:       %{name}-devel = %{version}-%{release}

%description jmods
The JMods for OpenJDK %{featurever}.

%package demo
Summary:        OpenJDK %{featurever} Demos
Group:          Development/Languages/Java
Requires:       %{name} = %{version}-%{release}

%description demo
The OpenJDK %{featurever} demos.

%package src
Summary:        OpenJDK %{featurever} Source Bundle
Group:          Development/Languages/Java
Requires:       %{name} = %{version}-%{release}

%description src
The OpenJDK %{featurever} source bundle.

%package javadoc
Summary:        OpenJDK %{featurever} API Documentation
Group:          Development/Languages/Java
Requires:       jpackage-utils
# Post requires update-alternatives to install javadoc alternative.
Requires(post): update-alternatives
# Postun requires update-alternatives to uninstall javadoc alternative.
Requires(postun):update-alternatives
BuildArch:      noarch
%if 0%{?suse_version} > 1500 || 0%{?java_bootstrap}
# Standard JPackage javadoc provides.
Provides:       java-%{javaver}-javadoc = %{version}-%{release}
Provides:       java-javadoc = %{version}-%{release}
%endif

%description javadoc
The OpenJDK %{featurever} API documentation.

%package accessibility
Summary:        OpenJDK %{featurever} accessibility connector
Group:          Development/Languages/Java
Requires:       %{name} = %{version}-%{release}
Requires:       xprop

%description accessibility
Enables accessibility support in OpenJDK %{featurever} by using java-atk-wrapper. This allows
compatible at-spi2 based accessibility programs to work for AWT and Swing-based
programs.

Please note, the java-atk-wrapper is still in beta, and OpenJDK itself is still
being tuned to be working with accessibility features. There are known issues
with accessibility on, so please do not install this package unless you really
need to.

%prep
%setup -q -n %{openjdk_dir}
%setup -q -D -n %{openjdk_dir} -T -a 8

# Replace config.sub and config.guess with fresh versions
cp %{SOURCE100} make/autoconf/build-aux/
cp %{SOURCE101} make/autoconf/build-aux/

# Remove libraries that are linked
rm -rvf src/java.base/share/native/libzip/zlib-*
find src/java.desktop/share/native/libjavajpeg ! -name imageioJPEG.c ! -name jpegdecoder.c -type f -delete
rm -rvf src/java.desktop/share/native/libsplashscreen/libpng
rm -rvf src/java.desktop/share/native/libsplashscreen/giflib
%if %{with_system_lcms}
rm -rvf src/java.desktop/share/native/liblcms/cms*
rm -rvf src/java.desktop/share/native/liblcms/lcms2*
%endif

%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch8 -p1
%patch10 -p1
%patch12 -p1
%patch13 -p1

%if %{with_system_pcsc}
%patch15 -p1
%endif

%patch16 -p1
%patch17 -p1
%patch18 -p1

%patch20 -p1

%patch200 -p1

%patch302 -p1
%patch303 -p1

%patch400
%patch401
%patch402

# Extract systemtap tapsets

%if %{with_systemtap}

tar -x -I xz -f %{SOURCE10}

for file in tapset/*.in; do

    OUTPUT_FILE=`echo $file | sed -e s:\.in$::g`
    sed -e s:@ABS_SERVER_LIBJVM_SO@:%{_jvmdir}/%{sdkdir}/lib/server/libjvm.so:g $file > $file.1
# TODO find out which architectures other than ix86 have a client vm

%ifarch %{ix86}
    sed -e s:@ABS_CLIENT_LIBJVM_SO@:%{_jvmdir}/%{sdkdir}/lib/client/libjvm.so:g $file.1 > $OUTPUT_FILE
%else
    sed -e '/@ABS_CLIENT_LIBJVM_SO@/d' $file.1 > $OUTPUT_FILE
%endif
    sed -i -e s:@ABS_JAVA_HOME_DIR@:%{_jvmdir}/%{sdkdir}:g $OUTPUT_FILE

done

%endif

# Prepare desktop files
for file in %{SOURCE11} ; do
    OUTPUT_FILE=`basename $file | sed -e s:\.in$::g`
    sed -e s:@JAVA_HOME@:%{_jvmdir}/%{sdkdir}:g $file > $OUTPUT_FILE
    sed -i -e s:@VERSION@:%{javaver}:g $OUTPUT_FILE
done

# Setup nss.cfg
sed -e "s:@NSS_LIBDIR@:%{NSS_LIBDIR}:g" %{SOURCE12} > nss.cfg

# Setup nss.fips.cfg
sed -e "s:@NSS_LIBDIR@:%{NSS_LIBDIR}:g" %{SOURCE13} > nss.fips.cfg
sed -i -e "s:@NSS_SECMOD@:sql\:/etc/pki/nssdb:g" nss.fips.cfg

%build

%ifarch s390x sparc64 alpha ppc64 ppc64le %{aarch64}
export ARCH_DATA_MODEL=64
%endif

mkdir -p %{buildoutputdir}

pushd %{buildoutputdir}

bash ../configure \
%if 0%{?suse_version} < 1500
    CPP=cpp-7 \
    CXX=g++-7 \
    CC=gcc-7 \
    NM=gcc-nm-7 \
%endif
%if %{is_release}
    --with-version-pre="" \
%endif
    --with-version-opt="suse-%{release}-%{_arch}" \
%if %{with zero}
    --with-jvm-variants=zero \
%else
%ifarch %{arm6}
    --with-jvm-variants=client \
%endif
%endif
    --disable-keep-packaged-modules \
    --with-debug-level=%{debugbuild} \
    --with-native-debug-symbols=internal \
    --with-zlib=system \
    --with-libjpeg=system \
    --with-giflib=system \
    --with-libpng=system \
%if %{with_system_lcms}
    --with-lcms=system \
%endif
%if %{with_system_pcsc}
    --with-pcsclite=system \
%endif
    --with-stdc++lib=dynamic \
    --disable-javac-server \
    --disable-warnings-as-errors

make --no-print-directory \
    LOG=trace \
    %{imagestarget}

# remove redundant *diz and *debuginfo files
find %{imagesdir}/jdk -iname '*.diz' -exec rm {} \;
find %{imagesdir}/jdk -iname '*.debuginfo' -exec rm {} \;

popd >& /dev/null

export JAVA_HOME=$(pwd)/%{buildoutputdir}/%{imagesdir}/jdk

# Install nss.cfg right away as we will be using the JRE above
install -m 644 nss.cfg $JAVA_HOME/conf/security/

# Install nss.fips.cfg: NSS configuration for global FIPS mode (crypto-policies)
install -m 644 nss.fips.cfg $JAVA_HOME/conf/security/

# Copy tz.properties
echo "sun.zoneinfo.dir=%{_datadir}/javazi" >> $JAVA_HOME/conf/tz.properties

# Build the accessibility plugin
pushd java-atk-wrapper-%{java_atk_wrapper_version}
autoreconf --force --install
rm wrapper/org/GNOME/Accessibility/AtkWrapper.java
%configure \
    --without-jdk-auto-detect \
    JDK_SRC=$JAVA_HOME
rm wrapper/org/GNOME/Accessibility/AtkWrapper.java
make %{?_smp_mflags}
cp wrapper/java-atk-wrapper.jar $JAVA_HOME/../jmods/
cp jni/src/.libs/libatk-wrapper.so $JAVA_HOME/lib/
popd
# Merge the java-atk-wrapper into the JDK
source $JAVA_HOME/release; export MODULES
$JAVA_HOME/bin/jlink --module-path $JAVA_HOME/../jmods --add-modules "atk.wrapper,${MODULES//\ /,}" --output $JAVA_HOME/../newjdk
cp -rf $JAVA_HOME/../newjdk/* $JAVA_HOME/
rm -rf $JAVA_HOME/../newjdk

# cacerts are generated in runtime in openSUSE
if [ -f %{buildoutputdir}/%{imagesdir}/jdk/lib/security/cacerts ]; then
        rm %{buildoutputdir}/%{imagesdir}/jdk/lib/security/cacerts
fi

# Check debug symbols are present and can identify code
SERVER_JVM="$JAVA_HOME/lib/server/libjvm.so"
if [ -f "$SERVER_JVM" ] ; then
  nm -aCl "$SERVER_JVM" | grep javaCalls.cpp
fi
CLIENT_JVM="$JAVA_HOME/lib/client/libjvm.so"
if [ -f "$CLIENT_JVM" ] ; then
  nm -aCl "$CLIENT_JVM" | grep javaCalls.cpp
fi
ZERO_JVM="$JAVA_HOME/lib/zero/libjvm.so"
if [ -f "$ZERO_JVM" ] ; then
  nm -aCl "$ZERO_JVM" | grep javaCalls.cpp
fi

# Check unlimited policy has been used
$JAVA_HOME/bin/javac -d . %{SOURCE14}
$JAVA_HOME/bin/java --add-opens java.base/javax.crypto=ALL-UNNAMED TestCryptoLevel

# Check ECC is working
$JAVA_HOME/bin/javac -d . %{SOURCE15}
#FIXME make it run after system NSS support?
$JAVA_HOME/bin/java $(echo $(basename %{SOURCE15})|sed "s|\.java||") || true

%install
export LANG=en_US.UTF-8
#bnc#530046
export STRIP_KEEP_SYMTAB=libjvm*
# skip /usr/lib/rpm/brp-check-bytecode-version:
export NO_BRP_CHECK_BYTECODE_VERSION=true

%if %{with_systemtap}
  # Install systemtap support files.
  install -dm 755 %{buildroot}%{_jvmdir}/%{sdkdir}/tapset
  cp -a tapset/*.stp %{buildroot}%{_jvmdir}/%{sdkdir}/tapset/
  install -d -m 755 %{buildroot}%{tapsetdir}
  pushd %{buildroot}%{tapsetdir}
    RELATIVE=$(%{abs2rel} %{_jvmdir}/%{sdkdir}/tapset %{tapsetdir})
    ln -sf $RELATIVE/*.stp .
  popd
%endif

pushd %{buildoutputdir}/%{imagesdir}/jdk

  # Install main files.
  install -d -m 755 %{buildroot}%{_jvmdir}/%{sdkdir}
  cp -a bin include lib conf release %{buildroot}%{_jvmdir}/%{sdkdir}

  # Install JCE policy symlinks.
  install -d -m 755 %{buildroot}%{_jvmprivdir}/%{archname}/jce/vanilla

  # Install versionless symlinks.
  pushd %{buildroot}%{_jvmdir}
    ln -sf %{sdkdir} %{jrelnk}
    ln -sf %{sdkdir} %{sdklnk}
  popd

  # Remove javaws man page
  rm -f man/man1/javaws*

  # Install man pages.
  install -d -m 755 %{buildroot}%{_mandir}/man1
  rm -f man/man1/javah*.1
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

popd

pushd %{buildoutputdir}/%{imagesdir}

  # Install jmods
  cp -a jmods %{buildroot}%{_jvmdir}/%{sdkdir}

popd

# Install Javadoc documentation.
install -d -m 755 %{buildroot}%{_javadocdir}
cp -a %{buildoutputdir}/images/docs %{buildroot}%{_javadocdir}/%{sdklnk}

# Install icons and menu entries.
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
    src/java.desktop/unix/classes/sun/awt/X11/java-icon${s}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}.png
done

# Install desktop file.
install -d -m 0755 %{buildroot}%{_datadir}/{applications,pixmaps}
install -d -m 0755 %{buildroot}/%{_jvmdir}/%{sdkdir}/lib/desktop/
install -m 0644 jconsole.desktop %{buildroot}/%{_jvmdir}/%{sdkdir}/lib/desktop/
%suse_update_desktop_file %{buildroot}/%{_jvmdir}/%{sdkdir}/lib/desktop/jconsole.desktop

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

# Create a config file to  enable java-atk-wrapper
pushd %{buildroot}/%{_jvmdir}/%{sdkdir}/conf/
  echo "#Config file to  enable java-atk-wrapper" > accessibility.properties
  echo "" >> accessibility.properties
  echo "assistive_technologies=org.GNOME.Accessibility.AtkWrapper" >> accessibility.properties
  echo "" >> accessibility.properties
popd

# fdupes links the files from JDK to JRE, so it breaks a JRE
# use it carefully :))
%fdupes -s %{buildroot}/%{_jvmdir}/%{sdkdir}/
%fdupes -s %{buildroot}/%{_jvmdir}/%{sdkdir}/demo
%fdupes -s %{buildroot}%{_javadocdir}/%{sdklnk}

%post headless
ext=.gz
update-alternatives \
  --install %{_bindir}/java java %{jrebindir}/java %{priority} \
  --slave %{_jvmdir}/jre jre %{_jvmdir}/%{jrelnk} \
  --slave %{_bindir}/keytool keytool %{jrebindir}/keytool \
  --slave %{_bindir}/rmiregistry rmiregistry %{jrebindir}/rmiregistry \
  --slave %{_mandir}/man1/java.1$ext java.1$ext \
  %{_mandir}/man1/java-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/keytool.1$ext keytool.1$ext \
  %{_mandir}/man1/keytool-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/rmiregistry.1$ext rmiregistry.1$ext \
  %{_mandir}/man1/rmiregistry-%{sdklnk}.1$ext

update-alternatives \
  --install %{_jvmdir}/jre-openjdk \
  jre_openjdk %{_jvmdir}/%{jrelnk} %{priority}
update-alternatives \
  --install %{_jvmdir}/jre-%{javaver} \
  jre_%{javaver} %{_jvmdir}/%{jrelnk} %{priority}

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
if [ 0`stat -c "%{s}" %{cacerts} 2>/dev/null` = "032" ] ; then
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

%post devel
ext=.gz
update-alternatives \
  --install %{_bindir}/javac javac %{sdkbindir}/javac %{priority} \
  --slave %{_jvmdir}/java java_sdk %{_jvmdir}/%{sdklnk} \
  --slave %{_bindir}/jar jar %{sdkbindir}/jar \
  --slave %{_bindir}/jarsigner jarsigner %{sdkbindir}/jarsigner \
  --slave %{_bindir}/javadoc javadoc %{sdkbindir}/javadoc \
  --slave %{_bindir}/javap javap %{sdkbindir}/javap \
  --slave %{_bindir}/jcmd jcmd %{sdkbindir}/jcmd \
  --slave %{_bindir}/jconsole jconsole %{sdkbindir}/jconsole \
  --slave %{_bindir}/jdb jdb %{sdkbindir}/jdb \
  --slave %{_bindir}/jdeprscan jdeprscan %{sdkbindir}/jdeprscan \
  --slave %{_bindir}/jdeps jdeps %{sdkbindir}/jdeps \
%if ! %{with zero}
%ifnarch s390x
  --slave %{_bindir}/jhsdb jhsdb %{sdkbindir}/jhsdb \
%endif
%endif
  --slave %{_bindir}/jimage jimage %{sdkbindir}/jimage \
  --slave %{_bindir}/jinfo jinfo %{sdkbindir}/jinfo \
  --slave %{_bindir}/jlink jlink %{sdkbindir}/jlink \
  --slave %{_bindir}/jmap jmap %{sdkbindir}/jmap \
  --slave %{_bindir}/jmod jmod %{sdkbindir}/jmod \
  --slave %{_bindir}/jps jps %{sdkbindir}/jps \
  --slave %{_bindir}/jrunscript jrunscript %{sdkbindir}/jrunscript \
  --slave %{_bindir}/jshell jshell %{sdkbindir}/jshell \
  --slave %{_bindir}/jstack jstack %{sdkbindir}/jstack \
  --slave %{_bindir}/jstat jstat %{sdkbindir}/jstat \
  --slave %{_bindir}/jstatd jstatd %{sdkbindir}/jstatd \
  --slave %{_bindir}/jwebserver jwebserver %{sdkbindir}/jwebserver \
  --slave %{_bindir}/serialver serialver %{sdkbindir}/serialver \
  --slave %{_mandir}/man1/jar.1$ext jar.1$ext \
  %{_mandir}/man1/jar-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jarsigner.1$ext jarsigner.1$ext \
  %{_mandir}/man1/jarsigner-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/javac.1$ext javac.1$ext \
  %{_mandir}/man1/javac-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/javadoc.1$ext javadoc.1$ext \
  %{_mandir}/man1/javadoc-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/javap.1$ext javap.1$ext \
  %{_mandir}/man1/javap-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jcmd.1$ext jcmd.1$ext \
  %{_mandir}/man1/jcmd-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jconsole.1$ext jconsole.1$ext \
  %{_mandir}/man1/jconsole-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jdb.1$ext jdb.1$ext \
  %{_mandir}/man1/jdb-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jdeprscan.1$ext jdeprscan.1$ext \
  %{_mandir}/man1/jdeprscan-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jdeps.1$ext jdeps.1$ext \
  %{_mandir}/man1/jdeps-%{sdklnk}.1$ext \
%if ! %{with zero}
%ifnarch s390x
  --slave %{_mandir}/man1/jhsdb.1$ext jhsdb.1$ext \
  %{_mandir}/man1/jhsdb-%{sdklnk}.1$ext \
%endif
%endif
  --slave %{_mandir}/man1/jinfo.1$ext jinfo.1$ext \
  %{_mandir}/man1/jinfo-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jlink.1$ext jlink.1$ext \
  %{_mandir}/man1/jlink-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jmap.1$ext jmap.1$ext \
  %{_mandir}/man1/jmap-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jmod.1$ext jmod.1$ext \
  %{_mandir}/man1/jmod-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jpackage.1$ext jpackage.1$ext \
  %{_mandir}/man1/jpackage-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jps.1$ext jps.1$ext \
  %{_mandir}/man1/jps-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jrunscript.1$ext jrunscript.1$ext \
  %{_mandir}/man1/jrunscript-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jshell.1$ext jshell.1$ext \
  %{_mandir}/man1/jshell-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jstack.1$ext jstack.1$ext \
  %{_mandir}/man1/jstack-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jstat.1$ext jstat.1$ext \
  %{_mandir}/man1/jstat-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jstatd.1$ext jstatd.1$ext \
  %{_mandir}/man1/jstatd-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jwebserver.1$ext jwebserver.1$ext \
  %{_mandir}/man1/jwebserver-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/serialver.1$ext serialver.1$ext \
  %{_mandir}/man1/serialver-%{sdklnk}.1$ext \
  --slave %{_datadir}/applications/jconsole.desktop jconsole.desktop \
  %{_jvmdir}/%{sdkdir}/lib/desktop/jconsole.desktop

update-alternatives \
  --install %{_jvmdir}/java-openjdk \
  java_sdk_openjdk %{_jvmdir}/%{sdklnk} %{priority}
update-alternatives \
  --install %{_jvmdir}/java-%{javaver} \
  java_sdk_%{javaver} %{_jvmdir}/%{sdklnk} %{priority}

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

%files
%dir %{_jvmdir}/%{sdkdir}/lib
%{_jvmdir}/%{sdkdir}/lib/libawt_xawt.so
%{_jvmdir}/%{sdkdir}/lib/libjawt.so
%{_jvmdir}/%{sdkdir}/lib/libsplashscreen.so
%dir %{_datadir}/icons/hicolor
%{_datadir}/icons/hicolor/*x*/apps/java-%{javaver}.png

%files headless
%dir %{_jvmdir}
%dir %{_jvmdir}/%{sdkdir}/
%dir %{_jvmdir}/%{sdkdir}/bin
%dir %{_jvmdir}/%{sdkdir}/lib
%dir %{_jvmdir}/%{sdkdir}/lib/jfr
%if %{with zero}
%dir %{_jvmdir}/%{sdkdir}/lib/zero
%else
%dir %{_jvmdir}/%{sdkdir}/lib/server
%endif
%dir %{_jvmdir}/%{sdkdir}/lib/desktop
%dir %{_jvmdir}/%{sdkdir}/lib/security

%dir %{_jvmdir}/%{sdkdir}/conf
%dir %{_jvmdir}/%{sdkdir}/conf/management
%dir %{_jvmdir}/%{sdkdir}/conf/sdp
%dir %{_jvmdir}/%{sdkdir}/conf/security
%dir %{_jvmdir}/%{sdkdir}/conf/security/policy
%dir %{_jvmdir}/%{sdkdir}/conf/security/policy/unlimited
%dir %{_jvmdir}/%{sdkdir}/conf/security/policy/limited

%dir %{_jvmdir}/%{sdkdir}
%{_jvmdir}/%{jrelnk}
%{_jvmprivdir}/*

%{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/%{sdkdir}/bin/jfr
%{_jvmdir}/%{sdkdir}/bin/keytool
%{_jvmdir}/%{sdkdir}/bin/rmiregistry
%{_jvmdir}/%{sdkdir}/conf/logging.properties
%{_jvmdir}/%{sdkdir}/conf/management/jmxremote.access
%{_jvmdir}/%{sdkdir}/conf/management/jmxremote.password.template
%{_jvmdir}/%{sdkdir}/conf/management/management.properties
%{_jvmdir}/%{sdkdir}/conf/net.properties
%{_jvmdir}/%{sdkdir}/conf/sdp/sdp.conf.template
%{_jvmdir}/%{sdkdir}/conf/security/java.policy
%{_jvmdir}/%{sdkdir}/conf/security/java.security
%{_jvmdir}/%{sdkdir}/conf/security/policy/limited/default_local.policy
%{_jvmdir}/%{sdkdir}/conf/security/policy/limited/default_US_export.policy
%{_jvmdir}/%{sdkdir}/conf/security/policy/limited/exempt_local.policy
%{_jvmdir}/%{sdkdir}/conf/security/policy/README.txt
%{_jvmdir}/%{sdkdir}/conf/security/policy/unlimited/default_local.policy
%{_jvmdir}/%{sdkdir}/conf/security/policy/unlimited/default_US_export.policy
%{_jvmdir}/%{sdkdir}/conf/sound.properties
%{_jvmdir}/%{sdkdir}/conf/tz.properties
%{_jvmdir}/%{sdkdir}/lib/desktop/jconsole.desktop
%{_jvmdir}/%{sdkdir}/lib/jexec
%{_jvmdir}/%{sdkdir}/lib/jfr/default.jfc
%{_jvmdir}/%{sdkdir}/lib/jfr/profile.jfc
%{_jvmdir}/%{sdkdir}/lib/jrt-fs.jar
%{_jvmdir}/%{sdkdir}/lib/jspawnhelper
%{_jvmdir}/%{sdkdir}/lib/jvm.cfg
%{_jvmdir}/%{sdkdir}/lib/libawt_headless.so
%{_jvmdir}/%{sdkdir}/lib/libawt.so
%{_jvmdir}/%{sdkdir}/lib/libdt_socket.so
%{_jvmdir}/%{sdkdir}/lib/libextnet.so
%{_jvmdir}/%{sdkdir}/lib/libfontmanager.so
%{_jvmdir}/%{sdkdir}/lib/libinstrument.so
%{_jvmdir}/%{sdkdir}/lib/libj2gss.so
%{_jvmdir}/%{sdkdir}/lib/libj2pcsc.so
%{_jvmdir}/%{sdkdir}/lib/libj2pkcs11.so
%{_jvmdir}/%{sdkdir}/lib/libjaas.so
%{_jvmdir}/%{sdkdir}/lib/libjavajpeg.so
%{_jvmdir}/%{sdkdir}/lib/libjava.so
%{_jvmdir}/%{sdkdir}/lib/libjdwp.so
%{_jvmdir}/%{sdkdir}/lib/libjimage.so
%{_jvmdir}/%{sdkdir}/lib/libjli.so
%{_jvmdir}/%{sdkdir}/lib/libjsig.so
%{_jvmdir}/%{sdkdir}/lib/libjsound.so
%{_jvmdir}/%{sdkdir}/lib/liblcms.so
%{_jvmdir}/%{sdkdir}/lib/libmanagement_agent.so
%{_jvmdir}/%{sdkdir}/lib/libmanagement_ext.so
%{_jvmdir}/%{sdkdir}/lib/libmanagement.so
%{_jvmdir}/%{sdkdir}/lib/libmlib_image.so
%{_jvmdir}/%{sdkdir}/lib/libnet.so
%{_jvmdir}/%{sdkdir}/lib/libnio.so
%{_jvmdir}/%{sdkdir}/lib/libprefs.so
%{_jvmdir}/%{sdkdir}/lib/librmi.so
%{_jvmdir}/%{sdkdir}/lib/libsctp.so
%{_jvmdir}/%{sdkdir}/lib/libsystemconf.so
%ifarch x86_64
%{_jvmdir}/%{sdkdir}/lib/libjsvml.so
%endif
%{_jvmdir}/%{sdkdir}/lib/libsyslookup.so
%{_jvmdir}/%{sdkdir}/lib/libverify.so
%{_jvmdir}/%{sdkdir}/lib/libzip.so
%{_jvmdir}/%{sdkdir}/lib/modules
%{_jvmdir}/%{sdkdir}/lib/psfontj2d.properties
%{_jvmdir}/%{sdkdir}/lib/psfont.properties.ja
%{_jvmdir}/%{sdkdir}/lib/tzdb.dat
%{_jvmdir}/%{sdkdir}/lib/*/libjsig.so
%{_jvmdir}/%{sdkdir}/lib/*/libjvm.so
%if ! %{with zero}
%{_jvmdir}/%{sdkdir}/lib/classlist
%{_jvmdir}/%{sdkdir}/lib/*/classes*.jsa
%endif

%config(noreplace) %{_jvmdir}/%{sdkdir}/lib/security/blocked.certs
%config(noreplace) %{_jvmdir}/%{sdkdir}/conf/security/nss.cfg
%config(noreplace) %{_jvmdir}/%{sdkdir}/conf/security/nss.fips.cfg
%{_jvmdir}/%{sdkdir}/lib/security/default.policy
%{_jvmdir}/%{sdkdir}/lib/security/public_suffix_list.dat

%{_mandir}/man1/java-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jfr-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/keytool-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/rmiregistry-%{sdklnk}.1%{?ext_man}

%files devel
%dir %{_jvmdir}/%{sdkdir}/bin
%dir %{_jvmdir}/%{sdkdir}/include
%dir %{_jvmdir}/%{sdkdir}/include/linux
%dir %{_jvmdir}/%{sdkdir}/lib

%if %{with_systemtap}
%dir %{_jvmdir}/%{sdkdir}/tapset
%endif
%{_jvmdir}/%{sdkdir}/bin/jar
%{_jvmdir}/%{sdkdir}/bin/jarsigner
%{_jvmdir}/%{sdkdir}/bin/javac
%{_jvmdir}/%{sdkdir}/bin/javadoc
%{_jvmdir}/%{sdkdir}/bin/javap
%{_jvmdir}/%{sdkdir}/bin/jcmd
%{_jvmdir}/%{sdkdir}/bin/jconsole
%{_jvmdir}/%{sdkdir}/bin/jdb
%{_jvmdir}/%{sdkdir}/bin/jdeprscan
%{_jvmdir}/%{sdkdir}/bin/jdeps
%if ! %{with zero}
%ifnarch s390x
%{_jvmdir}/%{sdkdir}/bin/jhsdb
%endif
%endif
%{_jvmdir}/%{sdkdir}/bin/jimage
%{_jvmdir}/%{sdkdir}/bin/jinfo
%{_jvmdir}/%{sdkdir}/bin/jlink
%{_jvmdir}/%{sdkdir}/bin/jmap
%{_jvmdir}/%{sdkdir}/bin/jmod
%{_jvmdir}/%{sdkdir}/bin/jpackage
%{_jvmdir}/%{sdkdir}/bin/jps
%{_jvmdir}/%{sdkdir}/bin/jrunscript
%{_jvmdir}/%{sdkdir}/bin/jshell
%{_jvmdir}/%{sdkdir}/bin/jstack
%{_jvmdir}/%{sdkdir}/bin/jstat
%{_jvmdir}/%{sdkdir}/bin/jstatd
%{_jvmdir}/%{sdkdir}/bin/jwebserver
%{_jvmdir}/%{sdkdir}/bin/serialver
%{_jvmdir}/%{sdkdir}/include/classfile_constants.h
%{_jvmdir}/%{sdkdir}/include/jawt.h
%{_jvmdir}/%{sdkdir}/include/jdwpTransport.h
%{_jvmdir}/%{sdkdir}/include/jni.h
%{_jvmdir}/%{sdkdir}/include/jvmticmlr.h
%{_jvmdir}/%{sdkdir}/include/jvmti.h
%{_jvmdir}/%{sdkdir}/include/sizecalc.h
%{_jvmdir}/%{sdkdir}/lib/ct.sym
%{_jvmdir}/%{sdkdir}/lib/libattach.so
%if ! %{with zero}
%ifnarch s390x
%{_jvmdir}/%{sdkdir}/lib/libsaproc.so
%endif
%endif
%{_jvmdir}/%{sdkdir}/include/linux/jawt_md.h
%{_jvmdir}/%{sdkdir}/include/linux/jni_md.h

%if %{with_systemtap}
%{_jvmdir}/%{sdkdir}/tapset/*.stp
%endif
%{_jvmdir}/%{sdklnk}
%{_mandir}/man1/jar-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jarsigner-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/javac-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/javadoc-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/javap-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jcmd-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jconsole-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jdb-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jdeprscan-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jdeps-%{sdklnk}.1%{?ext_man}
%if ! %{with zero}
%ifnarch s390x
%{_mandir}/man1/jhsdb-%{sdklnk}.1%{?ext_man}
%endif
%endif
%{_mandir}/man1/jinfo-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jlink-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jmap-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jmod-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jpackage-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jps-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jrunscript-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jshell-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jstack-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jstat-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jstatd-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jwebserver-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/serialver-%{sdklnk}.1%{?ext_man}

%if %{with_systemtap}
%{tapsetroot}
%endif

%files jmods
%dir %{_jvmdir}/%{sdkdir}/jmods
%{_jvmdir}/%{sdkdir}/release
%{_jvmdir}/%{sdkdir}/jmods/*.jmod
%{_jvmdir}/%{sdkdir}/jmods/java-atk-wrapper.jar

%files demo -f %{name}-demo.files

%files src
%{_jvmdir}/%{sdkdir}/lib/src.zip

%files javadoc
%dir %{_javadocdir}
%dir %{_javadocdir}/%{sdklnk}
%{_javadocdir}/%{sdklnk}/*

%files accessibility
%config(noreplace) %{_jvmdir}/%{sdkdir}/conf/accessibility.properties
%{_jvmdir}/%{sdkdir}/lib/libatk-wrapper.so

%changelog
