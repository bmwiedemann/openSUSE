#
# spec file for package java-11-openjdk
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
%{!?arm6:%global arm6 armv3l armv4b armv4l armv4tl armv5b armv5l armv5teb armv5tel armv5tejl armv6l armv6hl}
%global jit_arches %{ix86} x86_64 ppc64 ppc64le %{aarch64} %{arm} s390x
%global debug 0
%global make make
%if 0%{?suse_version} > 1500
%global add_back_javaee_modules 0
%else
%global add_back_javaee_modules 1
%endif
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
%global featurever      11
%global interimver      0
%global updatever       23
%global buildver        9
%global openjdk_repo    jdk11u
%global openjdk_tag     jdk-%{featurever}.%{interimver}.%{updatever}%{?patchver:.%{patchver}}+%{buildver}
%global openjdk_dir     %{openjdk_repo}-jdk-%{featurever}.%{interimver}.%{updatever}%{?patchver:.%{patchver}}-%{buildver}
# JavaEE modules
%global java_atk_wrapper_version 0.33.2
%global java_activation_repository activation
%global java_activation_tag JAF-1_2_0
%global java_xml_bind_repository jaxb-spec
%global java_xml_bind_tag 2.4.0
%global java_xml_soap_repository javax.xml.soap
%global java_xml_soap_tag 1.4.0
%global java_annotation_repository javax.annotation
%global java_annotation_tag 1.3.2
%global java_xml_ws_repository jax-ws-spec
%global java_xml_ws_tag 2.4.0
%global com_sun_xml_fastinfoset_repository metro-fi
%global com_sun_xml_fastinfoset_tag 1.2.15-RELEASE
%global org_jvnet_staxex_repository metro-stax-ex
%global org_jvnet_staxex_tag 1.8
%global com_sun_istack_runtime_repository jaxb-istack-commons
%global com_sun_istack_runtime_tag 3.0.7-RELEASE
%global jaxb_ri_repository jaxb-v2
%global jaxb_ri_tag 2.3.1
# priority must be 6 digits in total
%if 0%{?suse_version} <= 1315 && ! 0%{?java_bootstrap}
%global priority        0
%else
%global priority        2105
%endif
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
%else
%global with_system_pcsc 0
%endif
%global with_system_harfbuzz 1
%if %{is_release}
%global package_version %{featurever}.%{interimver}.%{updatever}.%{?patchver:%{patchver}}%{!?patchver:0}
%else
%global package_version %{featurever}.%{interimver}.%{updatever}.%{?patchver:%{patchver}}%{!?patchver:0}~%{buildver}
%endif
%global NSS_LIBDIR %(pkg-config --variable=libdir nss)
%bcond_with zero
%bcond_with aot
%if ! %{with zero}
%ifarch x86_64 %{aarch64}
%global _with_aot 1
%endif
%endif
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
# Systemtap tapsets. Zipped up to keep it small.
Source10:       systemtap-tapset.tar.xz
# Desktop files. Adapted from IcedTea.
Source11:       jconsole.desktop.in
# nss configuration file
Source12:       nss.cfg.in
# nss fips configuration file
Source13:       nss.fips.cfg.in
# Ensure we aren't using the limited crypto policy
Source14:       TestCryptoLevel.java
# Ensure ECDSA is working
Source15:       TestECDSA.java
# https://codeload.github.com/javaee/%{java_activation_repository}/tar.gz/%{java_activation_tag}
Source20:       %{java_activation_repository}-%{java_activation_tag}.tar.gz
# https://codeload.github.com/javaee/%{java_xml_bind_repository}/tar.gz/%{java_xml_bind_tag}
Source21:       %{java_xml_bind_repository}-%{java_xml_bind_tag}.tar.gz
# https://codeload.github.com/javaee/%{java_xml_soap_repository}/tar.gz/%{java_xml_soap_tag}
Source22:       %{java_xml_soap_repository}-%{java_xml_soap_tag}.tar.gz
# https://codeload.github.com/javaee/%{java_annotation_repository}/tar.gz/%{java_annotation_tag}
Source23:       %{java_annotation_repository}-%{java_annotation_tag}.tar.gz
# https://codeload.github.com/javaee/%{java_xml_ws_repository}/tar.gz/%{java_xml_ws_tag}
Source24:       %{java_xml_ws_repository}-%{java_xml_ws_tag}.tar.gz
# https://codeload.github.com/javaee/%{com_sun_xml_fastinfoset_repository}/tar.gz/%{com_sun_xml_fastinfoset_tag}
Source25:       %{com_sun_xml_fastinfoset_repository}-%{com_sun_xml_fastinfoset_tag}.tar.gz
# https://codeload.github.com/javaee/%{org_jvnet_staxex_repository}/tar.gz/%{org_jvnet_staxex_tag}
Source26:       %{org_jvnet_staxex_repository}-%{org_jvnet_staxex_tag}.tar.gz
# https://codeload.github.com/javaee/%{com_sun_istack_runtime_repository}/tar.gz/%{com_sun_istack_runtime_tag}
Source27:       %{com_sun_istack_runtime_repository}-%{com_sun_istack_runtime_tag}.tar.gz
# https://codeload.github.com/javaee/%{jaxb_ri_repository}/tar.gz/%{jaxb_ri_tag}
Source28:       %{jaxb_ri_repository}-%{jaxb_ri_tag}.tar.gz
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
# Use SOURCE_DATE_EPOCH in timestamp when writing properties
Patch14:        reproducible-properties.patch
Patch15:        system-pcsclite.patch
Patch16:        missing-return.patch
Patch17:        nss-security-provider.patch
Patch18:        keytool-default-rsa.patch
Patch19:        fips.patch
#
Patch20:        loadAssistiveTechnologies.patch
#
Patch21:        reproducible-javadoc-timestamp.patch
Patch22:        reproducible-jlink.patch
#
Patch30:        JDK-8208602.patch
#
# OpenJDK specific patches
#
Patch100:       s390-java-opts.patch
Patch101:       s390-size_t.patch
#
Patch200:       ppc_stack_overflow_fix.patch
Patch201:       fix_armv6_build.patch
#
Patch302:       disable-doclint-by-default.patch
#
Patch500:       activation-module.patch
Patch501:       annotation-module.patch
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
BuildRequires:  gcc-c++
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
BuildRequires:  liblcms2-devel
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
# Requires rest of java
Requires:       %{name}-headless = %{version}-%{release}
Requires:       fontconfig
Requires(post): file
ExcludeArch:    s390
%if 0%{?suse_version} > 1315 || 0%{?java_bootstrap}
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
Provides:       java-10-openjdk = %{version}-%{release}
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
Obsoletes:      java-10-openjdk < %{version}-%{release}
%endif
%if %{bootcycle}
%if 0%{?suse_version} > 1315 || 0%{?java_bootstrap}
BuildRequires:  java-devel >= 10
BuildConflicts: java-devel >= 12
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
%if %{with_system_harfbuzz}
BuildRequires:  harfbuzz-devel
%endif
%if %{with aot}
BuildRequires:  libelf-devel
%endif

%description
The OpenJDK %{featurever} runtime environment.

%package headless
Summary:        OpenJDK %{featurever} Runtime Environment
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
Requires(posttrans): java-ca-certificates
# Postun requires update-alternatives to uninstall tool update-alternatives.
Requires(postun): update-alternatives
Obsoletes:      %{name}-accessibility
%if 0%{?suse_version} > 1315 || 0%{?java_bootstrap}
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
Provides:       java-10-openjdk-headless = %{version}-%{release}
Provides:       java-sasl = %{version}
Provides:       jce = %{version}
Provides:       jdbc-stdext = 4.3
Provides:       jndi = %{version}
Provides:       jndi-cos = %{version}
Provides:       jndi-dns = %{version}
Provides:       jndi-ldap = %{version}
Provides:       jndi-rmi = %{version}
Provides:       jsse = %{version}
Obsoletes:      java-10-openjdk-headless < %{version}-%{release}
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
Requires(postun): update-alternatives
%if 0%{?suse_version} > 1315 || 0%{?java_bootstrap}
# Standard JPackage devel provides.
Provides:       java-%{javaver}-devel = %{version}
Provides:       java-10-openjdk-devel = %{version}-%{release}
Provides:       java-devel = %{javaver}
Provides:       java-devel-openjdk = %{version}
Provides:       java-sdk = %{javaver}
Provides:       java-sdk-%{javaver} = %{version}
Provides:       java-sdk-%{javaver}-openjdk = %{version}
Provides:       java-sdk-openjdk = %{version}
Obsoletes:      java-10-openjdk-devel < %{version}-%{release}
%endif

%description devel
The OpenJDK %{featurever} development tools.

%package jmods
Summary:        JMods for OpenJDK %{featurever}
Group:          Development/Languages/Java
Requires:       %{name}-devel = %{version}-%{release}
%if 0%{?suse_version} > 1315 || 0%{?java_bootstrap}
Provides:       java-10-openjdk-jmods = %{version}-%{release}
Obsoletes:      java-10-openjdk-jmods < %{version}-%{release}
%endif

%description jmods
The JMods for OpenJDK %{featurever}.

%package demo
Summary:        OpenJDK %{featurever} Demos
Group:          Development/Languages/Java
Requires:       %{name} = %{version}-%{release}
%if 0%{?suse_version} > 1315 || 0%{?java_bootstrap}
Provides:       java-10-openjdk-demo = %{version}-%{release}
Obsoletes:      java-10-openjdk-demo < %{version}-%{release}
%endif

%description demo
The OpenJDK %{featurever} demos.

%package src
Summary:        OpenJDK %{featurever} Source Bundle
Group:          Development/Languages/Java
Requires:       %{name} = %{version}-%{release}
%if 0%{?suse_version} > 1315 || 0%{?java_bootstrap}
Provides:       java-10-openjdk-src = %{version}-%{release}
Obsoletes:      java-10-openjdk-src < %{version}-%{release}
%endif

%description src
The OpenJDK %{featurever} source bundle.

%package javadoc
Summary:        OpenJDK %{featurever} API Documentation
Group:          Development/Languages/Java
Requires:       jpackage-utils
# Post requires update-alternatives to install javadoc alternative.
Requires(post): update-alternatives
# Postun requires update-alternatives to uninstall javadoc alternative.
Requires(postun): update-alternatives
BuildArch:      noarch
%if 0%{?suse_version} > 1315 || 0%{?java_bootstrap}
# Standard JPackage javadoc provides.
Provides:       java-%{javaver}-javadoc = %{version}-%{release}
Provides:       java-10-openjdk-javadoc = %{version}-%{release}
Provides:       java-javadoc = %{version}-%{release}
Obsoletes:      java-10-openjdk-javadoc < %{version}-%{release}
%endif

%description javadoc
The OpenJDK %{featurever} API documentation.

%prep
%setup -q -n %{openjdk_dir}
%setup -q -D -n %{openjdk_dir} -T -a 20
%setup -q -D -n %{openjdk_dir} -T -a 21
%setup -q -D -n %{openjdk_dir} -T -a 22
%setup -q -D -n %{openjdk_dir} -T -a 23
%setup -q -D -n %{openjdk_dir} -T -a 24
%setup -q -D -n %{openjdk_dir} -T -a 25
%setup -q -D -n %{openjdk_dir} -T -a 26
%setup -q -D -n %{openjdk_dir} -T -a 27
%setup -q -D -n %{openjdk_dir} -T -a 28

# Replace config.sub and config.guess with fresh versions
cp %{SOURCE100} make/autoconf/build-aux/
cp %{SOURCE101} make/autoconf/build-aux/

# Remove libraries that are linked
rm -rvf src/java.base/share/native/libzip/zlib-*
find src/java.desktop/share/native/libjavajpeg ! -name imageioJPEG.c ! -name jpegdecoder.c -type f -delete
rm -rvf src/java.desktop/share/native/libsplashscreen/libpng
rm -rvf src/java.desktop/share/native/libsplashscreen/giflib
rm -rvf src/java.desktop/share/native/liblcms/cms*
rm -rvf src/java.desktop/share/native/liblcms/lcms2*

%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 8 -p1
%patch -P 10 -p1
%patch -P 12 -p1
%patch -P 13 -p1
%patch -P 14 -p1

%if %{with_system_pcsc}
%patch -P 15 -p1
%endif

%patch -P 16 -p1
%patch -P 17 -p1
%patch -P 18 -p1

%patch -P 19 -p1

%patch -P 20 -p1

%patch -P 21 -p1
%patch -P 22 -p1

%patch -P 30 -p1

# s390 build fixes

%ifarch s390
%patch -P 100 -p1
%patch -P 101 -p1
%endif

%patch -P 200 -p1

%ifarch %{arm6}
%patch -P 201
%endif

%patch -P 302 -p1

%patch -P 500
%patch -P 501

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
sed -i -e "s:@NSS_SECMOD@:sql\:%{_sysconfdir}/pki/nssdb:g" nss.fips.cfg

%build

%ifarch s390x sparc64 alpha ppc64 ppc64le %{aarch64}
export ARCH_DATA_MODEL=64
%endif

%ifarch alpha
export CFLAGS="$CFLAGS -mieee"
%endif

EXTRA_CFLAGS="-Wno-error"
EXTRA_CPP_FLAGS="-Wno-error"

%ifarch ppc64 ppc64le ppc
EXTRA_CFLAGS="${EXTRA_CFLAGS} -fno-strict-aliasing"
%endif

%if 0%{?suse_version} >= 1330
EXTRA_CFLAGS="${EXTRA_CFLAGS} -fno-delete-null-pointer-checks -fno-lifetime-dse -fpermissive"
EXTRA_CPP_FLAGS="${EXTRA_CPP_FLAGS} -std=gnu++98 -fno-delete-null-pointer-checks -fno-lifetime-dse"
%endif

%ifarch %{ix86}
EXTRA_CFLAGS="${EXTRA_CFLAGS} -mstackrealign -mincoming-stack-boundary=2 -mpreferred-stack-boundary=4"
EXTRA_CPP_FLAGS="${EXTRA_CPP_FLAGS} -mstackrealign -mincoming-stack-boundary=2 -mpreferred-stack-boundary=4"
%endif

mkdir -p %{buildoutputdir}

pushd %{buildoutputdir}

bash ../configure \
%if %{is_release}
    --with-version-pre="" \
%endif
    --with-version-build="%{buildver}" \
    --with-version-opt="suse-%{release}-%{_arch}" \
    --disable-warnings-as-errors \
%if %{with zero}
    --with-jvm-variants=zero \
%else
%ifarch %{arm6}
    --with-jvm-variants=client \
%endif
%endif
%if %{with aot}
    --enable-aot \
%else
    --disable-aot \
%endif
    --disable-keep-packaged-modules \
    --with-debug-level=%{debugbuild} \
    --with-native-debug-symbols=internal \
    --enable-sysconf-nss \
    --with-zlib=system \
    --with-libjpeg=system \
    --with-giflib=system \
    --with-libpng=system \
    --with-lcms=system \
%if %{with_system_pcsc}
    --with-pcsclite=system \
%endif
%if %{with_system_harfbuzz}
    --with-harfbuzz=system \
%endif
    --with-stdc++lib=dynamic \
%ifarch s390
    --with-boot-jdk-jvmargs="-Xms256M -Xmx768M" \
%endif
%ifarch x86_64
    --with-jvm-features=zgc,shenandoahgc \
%endif
    --with-extra-cxxflags="${EXTRA_CPP_FLAGS}" \
    --with-extra-cflags="${EXTRA_CFLAGS}" \
    --disable-javac-server

# The combination of FULL_DEBUG_SYMBOLS=0 and ALT_OBJCOPY=/does_not_exist
# disables FDS for all build configs and reverts to pre-FDS make %{?_smp_mflags} logic.
# STRIP_POLICY=none says don't do any stripping. DEBUG_BINARIES=true says
# ignore all the other logic about which debug options and just do '-g'.

%{make} \
    JAVAC_FLAGS=-g \
    LOG=trace \
    DEBUG_BINARIES=true \
    STRIP_POLICY=no_strip \
    POST_STRIP_CMD="" \
    WARNINGS_ARE_ERRORS="-Wno-error" \
    CFLAGS_WARNINGS_ARE_ERRORS="-Wno-error" \
    %{imagestarget} docs

# remove redundant *diz and *debuginfo files
find %{imagesdir}/jdk -iname '*.diz' -exec rm {} \;
find %{imagesdir}/jdk -iname '*.debuginfo' -exec rm {} \;

popd >& /dev/null

export JAVA_HOME=$(pwd)/%{buildoutputdir}/%{imagesdir}/jdk

# Install nss.cfg right away as we will be using the JRE above
install -m 644 nss.cfg $JAVA_HOME/conf/security/

# Install nss.fips.cfg: NSS configuration for global FIPS mode (crypto-policies)
install -m 644 nss.fips.cfg $JAVA_HOME/conf/security/

%if %{add_back_javaee_modules}

# Merge back some Java EE modules removed in OpenJDK 11 by JEP 320

# Build the java.activation framework

pushd %{java_activation_repository}-%{java_activation_tag}
if [ -e build ]; then rm -rf build; fi
mkdir -p build
$JAVA_HOME/bin/javac -d build `find activation -name \*.java | xargs`
$JAVA_HOME/bin/jmod create --do-not-resolve-by-default --class-path=build:activation/src/main/resources $JAVA_HOME/../jmods/java.activation.jmod
popd
# Merge the java activation framework into the JDK
source $JAVA_HOME/release; export MODULES
$JAVA_HOME/bin/jlink --module-path $JAVA_HOME/../jmods --add-modules "java.activation,${MODULES//\ /,}" --release-info $JAVA_HOME/release --output $JAVA_HOME/../newjdk
cp -rf $JAVA_HOME/../newjdk/* $JAVA_HOME/
rm -rf $JAVA_HOME/../newjdk

# Build the java.xml.bind

pushd %{java_xml_bind_repository}-%{java_xml_bind_tag}
if [ -e build ]; then rm -rf build; fi
mkdir -p build
$JAVA_HOME/bin/javac -d build `find jaxb-api/src/main/java/ -name \*.java | xargs`
$JAVA_HOME/bin/jmod create --do-not-resolve-by-default --class-path=build:jaxb-api/src/main/resources $JAVA_HOME/../jmods/java.xml.bind.jmod
popd
# Merge java.xml.bind into the JDK
source $JAVA_HOME/release; export MODULES
$JAVA_HOME/bin/jlink --module-path $JAVA_HOME/../jmods --add-modules "java.xml.bind,${MODULES//\ /,}" --release-info $JAVA_HOME/release --output $JAVA_HOME/../newjdk
cp -rf $JAVA_HOME/../newjdk/* $JAVA_HOME/
rm -rf $JAVA_HOME/../newjdk

# Build the java.xml.soap

pushd %{java_xml_soap_repository}-%{java_xml_soap_tag}
if [ -e build ]; then rm -rf build; fi
mkdir -p build
$JAVA_HOME/bin/javac -d build `find src/main/ -name \*.java | xargs`
$JAVA_HOME/bin/jmod create --do-not-resolve-by-default --class-path=build $JAVA_HOME/../jmods/java.xml.soap.jmod
popd
# Merge java.xml.soap into the JDK
source $JAVA_HOME/release; export MODULES
$JAVA_HOME/bin/jlink --module-path $JAVA_HOME/../jmods --add-modules "java.xml.soap,${MODULES//\ /,}" --release-info $JAVA_HOME/release --output $JAVA_HOME/../newjdk
cp -rf $JAVA_HOME/../newjdk/* $JAVA_HOME/
rm -rf $JAVA_HOME/../newjdk

# Build the java.annotation

pushd %{java_annotation_repository}-%{java_annotation_tag}
if [ -e build ]; then rm -rf build; fi
mkdir -p build
$JAVA_HOME/bin/javac -d build `find src/main/java -name \*.java | xargs`
$JAVA_HOME/bin/jmod create --do-not-resolve-by-default --class-path=build $JAVA_HOME/../jmods/java.annotation.jmod
popd
# Merge java.annotation into the JDK
source $JAVA_HOME/release; export MODULES
$JAVA_HOME/bin/jlink --module-path $JAVA_HOME/../jmods --add-modules "java.annotation,${MODULES//\ /,}" --release-info $JAVA_HOME/release --output $JAVA_HOME/../newjdk
cp -rf $JAVA_HOME/../newjdk/* $JAVA_HOME/
rm -rf $JAVA_HOME/../newjdk

# Build the java.xml.ws

pushd %{java_xml_ws_repository}-%{java_xml_ws_tag}
if [ -e build ]; then rm -rf build; fi
mkdir -p build
$JAVA_HOME/bin/javac -d build `find api/src/main -name \*.java | xargs`
$JAVA_HOME/bin/jmod create --do-not-resolve-by-default --class-path=build:api/src/main/resources $JAVA_HOME/../jmods/java.xml.ws.jmod
popd
# Merge java.xml.ws into the JDK
source $JAVA_HOME/release; export MODULES
$JAVA_HOME/bin/jlink --module-path $JAVA_HOME/../jmods --add-modules "java.xml.ws,${MODULES//\ /,}" --release-info $JAVA_HOME/release --output $JAVA_HOME/../newjdk
cp -rf $JAVA_HOME/../newjdk/* $JAVA_HOME/
rm -rf $JAVA_HOME/../newjdk

# Build the com.sum.xml.fastinfoset

pushd %{com_sun_xml_fastinfoset_repository}-%{com_sun_xml_fastinfoset_tag}
if [ -e build ]; then rm -rf build; fi
mkdir -p build
$JAVA_HOME/bin/javac -d build `find code/fastinfoset/src/main/java -name \*.java | xargs`
$JAVA_HOME/bin/jmod create --do-not-resolve-by-default --class-path=build:code/fastinfoset/src/main/resources $JAVA_HOME/../jmods/com.sun.xml.fastinfoset.jmod
popd
# Merge com.sun.xml.fastinfoset into the JDK
source $JAVA_HOME/release; export MODULES
$JAVA_HOME/bin/jlink --module-path $JAVA_HOME/../jmods --add-modules "com.sun.xml.fastinfoset,${MODULES//\ /,}" --release-info $JAVA_HOME/release --output $JAVA_HOME/../newjdk
cp -rf $JAVA_HOME/../newjdk/* $JAVA_HOME/
rm -rf $JAVA_HOME/../newjdk

# Build the org.jvnet.staxex

pushd %{org_jvnet_staxex_repository}-%{org_jvnet_staxex_tag}
if [ -e build ]; then rm -rf build; fi
mkdir -p build
$JAVA_HOME/bin/javac -d build `find stax-ex/src/java -name \*.java | xargs`
$JAVA_HOME/bin/jmod create --do-not-resolve-by-default --class-path=build $JAVA_HOME/../jmods/org.jvnet.staxex.jmod
popd
# Merge org.jvnet.staxex into the JDK
source $JAVA_HOME/release; export MODULES
$JAVA_HOME/bin/jlink --module-path $JAVA_HOME/../jmods --add-modules "org.jvnet.staxex,${MODULES//\ /,}" --release-info $JAVA_HOME/release --output $JAVA_HOME/../newjdk
cp -rf $JAVA_HOME/../newjdk/* $JAVA_HOME/
rm -rf $JAVA_HOME/../newjdk

# Build the com.sun.istack.runtime

pushd %{com_sun_istack_runtime_repository}-%{com_sun_istack_runtime_tag}
if [ -e build ]; then rm -rf build; fi
mkdir -p build
$JAVA_HOME/bin/javac -d build `find istack-commons/runtime/src/main/java -name \*.java | xargs`
$JAVA_HOME/bin/jmod create --do-not-resolve-by-default --class-path=build $JAVA_HOME/../jmods/com.sun.istack.runtime.jmod
popd
# Merge com.sun.istack into the JDK
source $JAVA_HOME/release; export MODULES
$JAVA_HOME/bin/jlink --module-path $JAVA_HOME/../jmods --add-modules "com.sun.istack.runtime,${MODULES//\ /,}" --release-info $JAVA_HOME/release --output $JAVA_HOME/../newjdk
cp -rf $JAVA_HOME/../newjdk/* $JAVA_HOME/
rm -rf $JAVA_HOME/../newjdk

# Build the com.sun.xml.txw2

pushd %{jaxb_ri_repository}-%{jaxb_ri_tag}
if [ -e build ]; then rm -rf build; fi
mkdir -p build
$JAVA_HOME/bin/javac -d build `find jaxb-ri/txw/runtime/src/main/java -name \*.java | xargs`
$JAVA_HOME/bin/jmod create --do-not-resolve-by-default --class-path=build $JAVA_HOME/../jmods/com.sun.xml.txw2.jmod
popd
# Merge org.jvnet.staxex into the JDK
source $JAVA_HOME/release; export MODULES
$JAVA_HOME/bin/jlink --module-path $JAVA_HOME/../jmods --add-modules "com.sun.xml.txw2,${MODULES//\ /,}" --release-info $JAVA_HOME/release --output $JAVA_HOME/../newjdk
cp -rf $JAVA_HOME/../newjdk/* $JAVA_HOME/
rm -rf $JAVA_HOME/../newjdk

# Build the com.sun.xml.bind

pushd %{jaxb_ri_repository}-%{jaxb_ri_tag}
if [ -e build ]; then rm -rf build; fi
mkdir -p build
$JAVA_HOME/bin/javac -d build `find jaxb-ri/runtime/impl/src/main/java -name \*.java | xargs`
$JAVA_HOME/bin/jmod create --do-not-resolve-by-default --class-path=build:jaxb-ri/runtime/impl/src/main/resources $JAVA_HOME/../jmods/com.sun.xml.bind.jmod
popd
# Merge org.jvnet.staxex into the JDK
source $JAVA_HOME/release; export MODULES
$JAVA_HOME/bin/jlink --module-path $JAVA_HOME/../jmods --add-modules "com.sun.xml.bind,${MODULES//\ /,}" --release-info $JAVA_HOME/release --output $JAVA_HOME/../newjdk
cp -rf $JAVA_HOME/../newjdk/* $JAVA_HOME/
rm -rf $JAVA_HOME/../newjdk

%endif # add_back_javaee_modules

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
    %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}-openjdk.png
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
  --slave %{_bindir}/jjs jjs %{jrebindir}/jjs \
  --slave %{_bindir}/keytool keytool %{jrebindir}/keytool \
  --slave %{_bindir}/pack200 pack200 %{jrebindir}/pack200 \
  --slave %{_bindir}/rmid rmid %{jrebindir}/rmid \
  --slave %{_bindir}/rmiregistry rmiregistry %{jrebindir}/rmiregistry \
  --slave %{_bindir}/unpack200 unpack200 %{jrebindir}/unpack200 \
  --slave %{_mandir}/man1/java.1$ext java.1$ext \
  %{_mandir}/man1/java-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jjs.1$ext jjs.1$ext \
  %{_mandir}/man1/jjs-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/keytool.1$ext keytool.1$ext \
  %{_mandir}/man1/keytool-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/pack200.1$ext pack200.1$ext \
  %{_mandir}/man1/pack200-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/rmid.1$ext rmid.1$ext \
  %{_mandir}/man1/rmid-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/rmiregistry.1$ext rmiregistry.1$ext \
  %{_mandir}/man1/rmiregistry-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/unpack200.1$ext unpack200.1$ext \
  %{_mandir}/man1/unpack200-%{sdklnk}.1$ext \
  || :

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

%post devel
ext=.gz
update-alternatives \
  --install %{_bindir}/javac javac %{sdkbindir}/javac %{priority} \
  --slave %{_jvmdir}/java java_sdk %{_jvmdir}/%{sdklnk} \
%if %{with aot}
  --slave %{_bindir}/jaotc jaotc %{sdkbindir}/jaotc \
%endif
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
  --slave %{_bindir}/rmic rmic %{sdkbindir}/rmic \
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
  --slave %{_mandir}/man1/jdeps.1$ext jdeps.1$ext \
  %{_mandir}/man1/jdeps-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jinfo.1$ext jinfo.1$ext \
  %{_mandir}/man1/jinfo-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jmap.1$ext jmap.1$ext \
  %{_mandir}/man1/jmap-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jps.1$ext jps.1$ext \
  %{_mandir}/man1/jps-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jrunscript.1$ext jrunscript.1$ext \
  %{_mandir}/man1/jrunscript-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jstack.1$ext jstack.1$ext \
  %{_mandir}/man1/jstack-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jstat.1$ext jstat.1$ext \
  %{_mandir}/man1/jstat-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jstatd.1$ext jstatd.1$ext \
  %{_mandir}/man1/jstatd-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/rmic.1$ext rmic.1$ext \
  %{_mandir}/man1/rmic-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/serialver.1$ext serialver.1$ext \
  %{_mandir}/man1/serialver-%{sdklnk}.1$ext \
  --slave %{_datadir}/applications/jconsole.desktop jconsole.desktop \
  %{_jvmdir}/%{sdkdir}/lib/desktop/jconsole.desktop \
  || :

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
%{_datadir}/icons/hicolor/*x*/apps/java-%{javaver}-openjdk.png

%files headless
%dir %{_jvmdir}
%dir %{_jvmdir}/%{sdkdir}/
%dir %{_jvmdir}/%{sdkdir}/bin
%dir %{_jvmdir}/%{sdkdir}/lib
%dir %{_jvmdir}/%{sdkdir}/lib/jfr
%dir %{_jvmdir}/%{sdkdir}/lib/jli
%ifarch %{arm6}
%dir %{_jvmdir}/%{sdkdir}/lib/client
%else
%dir %{_jvmdir}/%{sdkdir}/lib/server
%endif
%dir %{_jvmdir}/%{sdkdir}/lib/desktop
%dir %{_jvmdir}/%{sdkdir}/lib/security

%dir %{_jvmdir}/%{sdkdir}/conf
%dir %{_jvmdir}/%{sdkdir}/conf/security
%dir %{_jvmdir}/%{sdkdir}/conf/security/policy
%dir %{_jvmdir}/%{sdkdir}/conf/security/policy/unlimited
%dir %{_jvmdir}/%{sdkdir}/conf/security/policy/limited
%dir %{_jvmdir}/%{sdkdir}/conf/management

%dir %{_jvmdir}/%{sdkdir}
%{_jvmdir}/%{jrelnk}
%{_jvmprivdir}/*

%{_jvmdir}/%{sdkdir}/release
%{_jvmdir}/%{sdkdir}/bin/java
%{_jvmdir}/%{sdkdir}/bin/jfr
%{_jvmdir}/%{sdkdir}/bin/jjs
%{_jvmdir}/%{sdkdir}/bin/keytool
%{_jvmdir}/%{sdkdir}/bin/pack200
%{_jvmdir}/%{sdkdir}/bin/rmid
%{_jvmdir}/%{sdkdir}/bin/rmiregistry
%{_jvmdir}/%{sdkdir}/bin/unpack200
%{_jvmdir}/%{sdkdir}/conf/logging.properties
%{_jvmdir}/%{sdkdir}/conf/management/jmxremote.access
%{_jvmdir}/%{sdkdir}/conf/management/jmxremote.password.template
%{_jvmdir}/%{sdkdir}/conf/management/management.properties
%{_jvmdir}/%{sdkdir}/conf/net.properties
%{_jvmdir}/%{sdkdir}/conf/security/java.policy
%{_jvmdir}/%{sdkdir}/conf/security/java.security
%{_jvmdir}/%{sdkdir}/conf/security/policy/limited/default_local.policy
%{_jvmdir}/%{sdkdir}/conf/security/policy/limited/default_US_export.policy
%{_jvmdir}/%{sdkdir}/conf/security/policy/limited/exempt_local.policy
%{_jvmdir}/%{sdkdir}/conf/security/policy/README.txt
%{_jvmdir}/%{sdkdir}/conf/security/policy/unlimited/default_local.policy
%{_jvmdir}/%{sdkdir}/conf/security/policy/unlimited/default_US_export.policy
%{_jvmdir}/%{sdkdir}/conf/sound.properties
%if ! %{with zero}
%{_jvmdir}/%{sdkdir}/lib/classlist
%endif
%{_jvmdir}/%{sdkdir}/lib/desktop/jconsole.desktop
%{_jvmdir}/%{sdkdir}/lib/jexec
%{_jvmdir}/%{sdkdir}/lib/jfr/default.jfc
%{_jvmdir}/%{sdkdir}/lib/jfr/profile.jfc
%{_jvmdir}/%{sdkdir}/lib/jli/libjli.so
%{_jvmdir}/%{sdkdir}/lib/jrt-fs.jar
%{_jvmdir}/%{sdkdir}/lib/jspawnhelper
%{_jvmdir}/%{sdkdir}/lib/jvm.cfg
%{_jvmdir}/%{sdkdir}/lib/libawt_headless.so
%{_jvmdir}/%{sdkdir}/lib/libawt.so
%{_jvmdir}/%{sdkdir}/lib/libdt_socket.so
%{_jvmdir}/%{sdkdir}/lib/libextnet.so
%{_jvmdir}/%{sdkdir}/lib/libfontmanager.so
%if ! %{with_system_harfbuzz}
%{_jvmdir}/%{sdkdir}/lib/libharfbuzz.so
%endif
%{_jvmdir}/%{sdkdir}/lib/libinstrument.so
%{_jvmdir}/%{sdkdir}/lib/libj2gss.so
%{_jvmdir}/%{sdkdir}/lib/libj2pcsc.so
%{_jvmdir}/%{sdkdir}/lib/libj2pkcs11.so
%{_jvmdir}/%{sdkdir}/lib/libjaas.so
%{_jvmdir}/%{sdkdir}/lib/libjavajpeg.so
%{_jvmdir}/%{sdkdir}/lib/libjava.so
%{_jvmdir}/%{sdkdir}/lib/libjdwp.so
%{_jvmdir}/%{sdkdir}/lib/libjimage.so
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
%{_jvmdir}/%{sdkdir}/lib/libsunec.so
%{_jvmdir}/%{sdkdir}/lib/libsystemconf.so
%{_jvmdir}/%{sdkdir}/lib/libunpack.so
%{_jvmdir}/%{sdkdir}/lib/libverify.so
%{_jvmdir}/%{sdkdir}/lib/libzip.so
%{_jvmdir}/%{sdkdir}/lib/modules
%{_jvmdir}/%{sdkdir}/lib/psfontj2d.properties
%{_jvmdir}/%{sdkdir}/lib/psfont.properties.ja
%{_jvmdir}/%{sdkdir}/lib/tzdb.dat
%{_jvmdir}/%{sdkdir}/lib/*/libjsig.so
%{_jvmdir}/%{sdkdir}/lib/*/libjvm.so
%{_jvmdir}/%{sdkdir}/lib/*/Xusage.txt

%config(noreplace) %{_jvmdir}/%{sdkdir}/lib/security/blocked.certs
%config(noreplace) %{_jvmdir}/%{sdkdir}/conf/security/nss.cfg
%config(noreplace) %{_jvmdir}/%{sdkdir}/conf/security/nss.fips.cfg
%{_jvmdir}/%{sdkdir}/lib/security/default.policy
%{_jvmdir}/%{sdkdir}/lib/security/public_suffix_list.dat

%{_mandir}/man1/java-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jjs-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/keytool-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/pack200-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/rmid-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/rmiregistry-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/unpack200-%{sdklnk}.1%{?ext_man}

%files devel
%dir %{_jvmdir}/%{sdkdir}/bin
%dir %{_jvmdir}/%{sdkdir}/include
%dir %{_jvmdir}/%{sdkdir}/include/linux
%dir %{_jvmdir}/%{sdkdir}/lib

%if %{with_systemtap}
%dir %{_jvmdir}/%{sdkdir}/tapset
%endif
%if %{with aot}
%{_jvmdir}/%{sdkdir}/bin/jaotc
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
%{_jvmdir}/%{sdkdir}/bin/jps
%{_jvmdir}/%{sdkdir}/bin/jrunscript
%{_jvmdir}/%{sdkdir}/bin/jshell
%{_jvmdir}/%{sdkdir}/bin/jstack
%{_jvmdir}/%{sdkdir}/bin/jstat
%{_jvmdir}/%{sdkdir}/bin/jstatd
%{_jvmdir}/%{sdkdir}/bin/rmic
%{_jvmdir}/%{sdkdir}/bin/serialver
%{_jvmdir}/%{sdkdir}/include/classfile_constants.h
%{_jvmdir}/%{sdkdir}/include/jawt.h
%{_jvmdir}/%{sdkdir}/include/jdwpTransport.h
%{_jvmdir}/%{sdkdir}/include/jni.h
%{_jvmdir}/%{sdkdir}/include/jvmticmlr.h
%{_jvmdir}/%{sdkdir}/include/jvmti.h
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
%{_mandir}/man1/jdeps-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jinfo-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jmap-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jps-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jrunscript-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jstack-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jstat-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jstatd-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/rmic-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/serialver-%{sdklnk}.1%{?ext_man}

%if %{with_systemtap}
%{tapsetroot}
%endif

%files jmods
%dir %{_jvmdir}/%{sdkdir}/jmods
%{_jvmdir}/%{sdkdir}/jmods/*.jmod

%files demo -f %{name}-demo.files

%files src
%{_jvmdir}/%{sdkdir}/lib/src.zip

%files javadoc
%dir %{_javadocdir}
%dir %{_javadocdir}/%{sdklnk}
%{_javadocdir}/%{sdklnk}/*

%changelog
