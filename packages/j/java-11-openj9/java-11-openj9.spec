#
# spec file
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{!?aarch64:%global aarch64 aarch64 arm64 armv8}
%global debug 0
%if 0%{?suse_version} > 1500
%global add_back_javaee_modules 0
%else
%global add_back_javaee_modules 1
%endif
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
%global updatever       18
%global patchver        0
%global buildver        10
%global root_repository https://github.com/ibmruntimes/openj9-openjdk-jdk11/archive
%global root_revision   4e060ceb0bbbbf5fa0432db08e0b38292cbbe1ba
%global root_branch     v0.36.1-release
%global omr_repository  https://github.com/eclipse/openj9-omr/archive
%global omr_revision    f491bbf6f6f3f87bfd38a65055589125c13de555
%global omr_branch      v0.36.1-release
%global openj9_repository https://github.com/eclipse/openj9/archive
%global openj9_revision 0592661e480dd108a708689dc56bf1a427677645
%global openj9_branch   v0.36.1-release
%global openj9_tag      openj9-0.36.1
# JavaEE modules
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
%global priority        2101
%global javaver         %{featurever}
# Standard JPackage directories and symbolic links.
%global sdklnk          java-%{javaver}-openj9
%global archname        %{sdklnk}
%global jrelnk          jre-%{javaver}-openj9
%global jrebindir       %{_jvmdir}/%{jrelnk}/bin
%global sdkdir          %{sdklnk}-%{javaver}
%global sdkbindir       %{_jvmdir}/%{sdklnk}/bin
# Prevent brp-java-repack-jars from being run.
%global __jar_repack 0
# cacert symlink
%global cacerts  %{_jvmdir}/%{sdkdir}/lib/security/cacerts
# real file made by update-ca-certificates
%global javacacerts %{_var}/lib/ca-certificates/java-cacerts
%global bootcycle 0
%if %{debug}
%global debugbuild slowdebug
%else
%global debugbuild release
%endif
%if %{bootcycle}
%global imagesdir build/%{debugbuild}/bootcycle-build/images
%global imagestarget bootcycle-images
%else
%global imagesdir build/%{debugbuild}/images
%global imagestarget images
%endif
%global bits 64
# Turn on/off some features
%global with_system_pcsc 1
%global with_system_harfbuzz 1
Name:           java-%{featurever}-openj9
Version:        %{featurever}.%{interimver}.%{updatever}.%{patchver}
Release:        0
Summary:        OpenJDK %{featurever} Runtime Environment with Eclipse OpenJ9 virtual machine
License:        Apache-1.1 AND Apache-2.0 AND EPL-2.0 AND GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-only WITH Classpath-exception-2.0 AND LGPL-2.0-only AND MPL-1.0 AND MPL-1.1 AND SUSE-Public-Domain AND W3C
Group:          Development/Languages/Java
URL:            https://openjdk.java.net/
# Sources from upstream OpenJ9 project.
Source0:        %{root_repository}/%{root_revision}.zip
Source1:        %{omr_repository}/%{omr_revision}.zip
Source2:        %{openj9_repository}/%{openj9_revision}.zip
# Desktop files. Adapted from IcedTea.
Source11:       jconsole.desktop.in
# nss configuration file
Source13:       nss.cfg
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
Source100:      openj9-nogit.patch.in
Source1000:     %{name}-rpmlintrc
# Restrict access to java-atk-wrapper classes
Patch3:         java-atk-wrapper-security.patch
# Allow building with newer libdwarf
Patch4:         libdwarf-fix.patch
# Allow multiple initialization of PKCS11 libraries
Patch5:         multiple-pkcs11-library-init.patch
# Fix narrowing conversion error
Patch6:         openj9-no-narrowing.patch
# Fix: implicit-pointer-decl
Patch13:        implicit-pointer-decl.patch
#
Patch15:        system-pcsclite.patch
#
Patch20:        loadAssistiveTechnologies.patch
#
Patch30:        JDK-8208602.patch
Patch31:        aarch64.patch
#
Patch32:        stringop-overflow.patch
#
# OpenJDK specific patches
#
Patch302:       disable-doclint-by-default.patch
Patch303:       alternative-tzdb_dat.patch
#
Patch500:       activation-module.patch
Patch501:       annotation-module.patch
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bc
BuildRequires:  binutils
BuildRequires:  cmake
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
BuildRequires:  libdwarf-devel
BuildRequires:  libelf-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libnuma-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  nasm
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  xprop
BuildRequires:  zip
# Requires rest of java
Requires:       %{name}-headless = %{version}-%{release}
Requires:       fontconfig
# mozilla-nss has to be installed to prevent
# java.security.ProviderException: Could not initialize NSS
# ...
# java.io.FileNotFoundException: /usr/lib64/libnss3.so
#was bnc#634793
Requires:       mozilla-nss
Requires(post): file
# Standard JPackage base provides.
Provides:       java = %{javaver}
Provides:       java-%{javaver} = %{version}-%{release}
Provides:       java-openj9 = %{version}-%{release}
Provides:       java-openjdk = %{version}-%{release}
Provides:       jre = %{javaver}
Provides:       jre-%{javaver} = %{version}-%{release}
Provides:       jre-%{javaver}-openj9 = %{version}-%{release}
Provides:       jre-%{javaver}-openjdk = %{version}-%{release}
Provides:       jre-openj9 = %{version}-%{release}
Provides:       jre-openjdk = %{version}-%{release}
# Standard JPackage extensions provides.
Provides:       java-fonts = %{version}
# Required at least by fop
Provides:       java-%{bits} = %{javaver}
Provides:       java-%{javaver}-%{bits}
Provides:       java-openj9-%{bits} = %{version}-%{release}
Provides:       java-openjdk-%{bits} = %{version}-%{release}
Provides:       jre-%{bits} = %{javaver}
Provides:       jre-%{javaver}-%{bits}
Provides:       jre-%{javaver}-openj9-%{bits} = %{version}-%{release}
Provides:       jre-%{javaver}-openjdk-%{bits} = %{version}-%{release}
Provides:       jre-openj9-%{bits} = %{version}-%{release}
Provides:       jre-openjdk-%{bits} = %{version}-%{release}
Provides:       jre1.10.x
Provides:       jre1.3.x
Provides:       jre1.4.x
Provides:       jre1.5.x
Provides:       jre1.6.x
Provides:       jre1.7.x
Provides:       jre1.8.x
Provides:       jre1.9.x
ExclusiveArch:  x86_64 ppc64le s390x aarch64
%if 0%{?suse_version} < 1500
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc >= 7
BuildRequires:  gcc-c++ >= 7
%endif
%if %{bootcycle}
BuildRequires:  java-devel >= 10
BuildConflicts: java-devel >= 12
%else
BuildRequires:  java-%{javaver}-devel
%endif
%if %{with_system_harfbuzz}
BuildRequires:  harfbuzz-devel
%endif
%if %{with_system_pcsc}
BuildRequires:  pcsc-lite-devel
%endif

%description
The OpenJDK %{featurever} with Eclipse OpenJ9 virtual machine. Eclipse OpenJ9
is a Java Virtual Machine for OpenJDK that is optimized for small
footprint, fast start-up, and high throughput.

Supported architectures are ppc64le, s390x and x86_64

%package headless
Summary:        OpenJDK %{featurever} Runtime Environment with Eclipse OpenJ9
Group:          Development/Languages/Java
Requires:       jpackage-utils
Requires(post): java-ca-certificates
# Post requires update-alternatives to install tool update-alternatives.
Requires(post): update-alternatives
# Postun requires update-alternatives to uninstall tool update-alternatives.
Requires(postun):update-alternatives
Recommends:     tzdata-java8
Obsoletes:      %{name}-accessibility
# Standard JPackage base provides.
Provides:       java-%{javaver}-headless = %{version}-%{release}
Provides:       java-headless = %{javaver}
Provides:       java-openj9-headless = %{version}-%{release}
Provides:       java-openjdk-headless = %{version}-%{release}
Provides:       jre-%{javaver}-headless = %{version}-%{release}
Provides:       jre-%{javaver}-openj9-headless = %{version}-%{release}
Provides:       jre-%{javaver}-openjdk-headless = %{version}-%{release}
Provides:       jre-headless = %{javaver}
Provides:       jre-openj9-headless = %{version}-%{release}
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

%description headless
The OpenJDK %{featurever} runtime environment without audio and video support.

Supported architectures are ppc64le, s390x and x86_64

%package devel
Summary:        OpenJDK %{featurever} Development Environment
# Require base package.
Group:          Development/Languages/Java
Requires:       %{name} = %{version}-%{release}
# Post requires update-alternatives to install tool update-alternatives.
Requires(post): update-alternatives
# Postun requires update-alternatives to uninstall tool update-alternatives.
Requires(postun):update-alternatives
# Standard JPackage devel provides.
Provides:       java-%{javaver}-devel = %{version}
Provides:       java-devel = %{javaver}
Provides:       java-devel-openj9 = %{version}
Provides:       java-devel-openjdk = %{version}
Provides:       java-sdk = %{javaver}
Provides:       java-sdk-%{javaver} = %{version}
Provides:       java-sdk-%{javaver}-openj9 = %{version}
Provides:       java-sdk-%{javaver}-openjdk = %{version}
Provides:       java-sdk-openj9 = %{version}
Provides:       java-sdk-openjdk = %{version}

%description devel
The OpenJDK %{featurever} development tools.

Supported architectures are ppc64le, s390x and x86_64

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
# Standard JPackage javadoc provides.
Provides:       java-%{javaver}-javadoc = %{version}-%{release}
Provides:       java-javadoc = %{version}-%{release}
BuildArch:      noarch

%description javadoc
The OpenJDK %{featurever} API documentation.

%prep
%setup -q -n openj9-openjdk-jdk11-%{root_revision} -a 1 -a 2
%setup -q -D -n openj9-openjdk-jdk11-%{root_revision} -T -a 20
%setup -q -D -n openj9-openjdk-jdk11-%{root_revision} -T -a 21
%setup -q -D -n openj9-openjdk-jdk11-%{root_revision} -T -a 22
%setup -q -D -n openj9-openjdk-jdk11-%{root_revision} -T -a 23
%setup -q -D -n openj9-openjdk-jdk11-%{root_revision} -T -a 24
%setup -q -D -n openj9-openjdk-jdk11-%{root_revision} -T -a 25
%setup -q -D -n openj9-openjdk-jdk11-%{root_revision} -T -a 26
%setup -q -D -n openj9-openjdk-jdk11-%{root_revision} -T -a 27
%setup -q -D -n openj9-openjdk-jdk11-%{root_revision} -T -a 28

# Set up the build tree using the subrepository tarballs
pwd
mv openj9-omr-%{omr_revision} omr
mv openj9-%{openj9_revision} openj9

cp openj9/LICENSE LICENSE.openj9

# Remove libraries that are linked
rm -rvf src/java.base/share/native/libzip/zlib-*
find src/java.desktop/share/native/libjavajpeg ! -name imageioJPEG.c ! -name jpegdecoder.c -type f -delete
rm -rvf src/java.desktop/share/native/libsplashscreen/libpng
rm -rvf src/java.desktop/share/native/libsplashscreen/giflib
rm -rvf src/java.desktop/share/native/liblcms/cms*
rm -rvf src/java.desktop/share/native/liblcms/lcms2*

%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch13 -p1

%if %{with_system_pcsc}
%patch15 -p1
%endif

%patch20 -p1

%patch30 -p1
%patch31 -p1
%patch32 -p1

%patch302 -p1
%patch303 -p1

%patch500
%patch501

cat %{SOURCE100} \
    | sed "s/@OPENJ9_SHA@/%{openj9_revision}/g" \
    | sed "s/@OPENJ9_BRANCH@/%{openj9_branch}/g" \
    | sed "s/@OPENJ9_TAG@/%{openj9_tag}/g" \
    | sed "s/@OPENJ9OMR_SHA@/%{omr_revision}/g" \
    | sed "s/@OPENJDK_SHA@/%{root_revision}/g" \
    | patch -p1 -u -l

# Prepare desktop files
for file in %{SOURCE11} ; do
    OUTPUT_FILE=`basename $file | sed -e s:\.in$::g`
    sed -e s:@JAVA_HOME@:%{_jvmdir}/%{sdkdir}:g $file > $OUTPUT_FILE
    sed -i -e s:@VERSION@:%{javaver}:g $OUTPUT_FILE
done

%build
export ARCH_DATA_MODEL=64

EXTRA_CFLAGS="-Wno-error -Wno-maybe-uninitialized -fno-delete-null-pointer-checks -fno-lifetime-dse"
EXTRA_CPP_FLAGS="-Wno-error -Wno-maybe-uninitialized -std=gnu++98 -fno-delete-null-pointer-checks -fno-lifetime-dse"

%ifarch ppc64le
EXTRA_CFLAGS="$EXTRA_CFLAGS -fno-strict-aliasing"
%endif

bash configure \
%if 0%{?suse_version} < 1500
    CPP=cpp-7 \
    CXX=g++-7 \
    CC=gcc-7 \
    NM=gcc-nm-7 \
%endif
    --with-version-pre="" \
    --with-version-opt="suse-%{release}-%{_arch}" \
    --disable-warnings-as-errors \
    --disable-warnings-as-errors-omr \
    --disable-warnings-as-errors-openj9 \
    --disable-keep-packaged-modules \
    --with-debug-level=%{debugbuild} \
    --with-conf-name=%{debugbuild} \
    --with-zlib=system \
    --with-libjpeg=system \
    --with-giflib=system \
    --with-libpng=system \
    --with-lcms=system \
	--with-openssl=system \
%if %{with_system_pcsc}
    --with-pcsclite=system \
%endif
%if %{with_system_harfbuzz}
    --with-harfbuzz=system \
%endif
    --with-stdc++lib=dynamic \
    --with-extra-cxxflags="$EXTRA_CPP_FLAGS" \
    --with-extra-cflags="$EXTRA_CFLAGS" \
    --disable-javac-server \
    --enable-demos

make \
    LOG=trace \
    %{imagestarget} docs

# remove redundant *diz and *debuginfo files
find %{imagesdir}/jdk -iname '*.diz' -exec rm {} \;
find %{imagesdir}/jdk -iname '*.debuginfo' -exec rm {} \;

export JAVA_HOME=$(pwd)/%{imagesdir}/jdk

# Copy tz.properties
echo "sun.zoneinfo.dir=%{_datadir}/javazi" >> $JAVA_HOME/conf/tz.properties

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
if [ -f %{imagesdir}/jdk/lib/security/cacerts ]; then
        rm %{imagesdir}/jdk/lib/security/cacerts
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

pushd %{imagesdir}/jdk

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
  rm -f man/man1/jinfo.1*
  rm -f man/man1/jstatd.1*
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

pushd %{imagesdir}

  # Install jmods
  cp -a jmods %{buildroot}%{_jvmdir}/%{sdkdir}

# Install nss.cfg
install -m 644 %{SOURCE13} %{buildroot}%{_jvmdir}/%{sdkdir}/conf/security/

# Install Javadoc documentation.
install -d -m 755 %{buildroot}%{_javadocdir}
cp -a docs %{buildroot}%{_javadocdir}/%{sdklnk}

popd

# Install icons and menu entries.
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
    src/java.desktop/unix/classes/sun/awt/X11/java-icon${s}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}-openj9.png
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
  --slave %{_bindir}/jimage jimage %{sdkbindir}/jimage \
  --slave %{_bindir}/jlink jlink %{sdkbindir}/jlink \
  --slave %{_bindir}/jmap jmap %{sdkbindir}/jmap \
  --slave %{_bindir}/jmod jmod %{sdkbindir}/jmod \
  --slave %{_bindir}/jps jps %{sdkbindir}/jps \
  --slave %{_bindir}/jrunscript jrunscript %{sdkbindir}/jrunscript \
  --slave %{_bindir}/jshell jshell %{sdkbindir}/jshell \
  --slave %{_bindir}/jstack jstack %{sdkbindir}/jstack \
  --slave %{_bindir}/jstat jstat %{sdkbindir}/jstat \
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
  --slave %{_mandir}/man1/jconsole.1$ext jconsole.1$ext \
  %{_mandir}/man1/jconsole-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jdb.1$ext jdb.1$ext \
  %{_mandir}/man1/jdb-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jdeps.1$ext jdeps.1$ext \
  %{_mandir}/man1/jdeps-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jrunscript.1$ext jrunscript.1$ext \
  %{_mandir}/man1/jrunscript-%{sdklnk}.1$ext \
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
%{_datadir}/icons/hicolor/*x*/apps/java-%{javaver}-openj9.png

%files headless
%dir %{_jvmdir}
%dir %{_jvmdir}/%{sdkdir}
%dir %{_jvmdir}/%{sdkdir}/bin
%dir %{_jvmdir}/%{sdkdir}/lib
%dir %{_jvmdir}/%{sdkdir}/lib/jli
%dir %{_jvmdir}/%{sdkdir}/lib/server
%dir %{_jvmdir}/%{sdkdir}/lib/default
%dir %{_jvmdir}/%{sdkdir}/lib/desktop
%dir %{_jvmdir}/%{sdkdir}/lib/security
%dir %{_jvmdir}/%{sdkdir}/lib/j9vm
%dir %{_jvmdir}/%{sdkdir}/conf
%dir %{_jvmdir}/%{sdkdir}/conf/security
%dir %{_jvmdir}/%{sdkdir}/conf/security/policy
%dir %{_jvmdir}/%{sdkdir}/conf/security/policy/unlimited
%dir %{_jvmdir}/%{sdkdir}/conf/security/policy/limited
%dir %{_jvmdir}/%{sdkdir}/conf/management
%{_jvmdir}/%{jrelnk}
%{_jvmprivdir}/*

%{_jvmdir}/%{sdkdir}/release
%{_jvmdir}/%{sdkdir}/bin/java
%ifnarch aarch64
%{_jvmdir}/%{sdkdir}/bin/jitserver
%endif
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
%ifarch x86_64
%{_jvmdir}/%{sdkdir}/conf/security/nss.fips.cfg
%endif
%{_jvmdir}/%{sdkdir}/conf/security/policy/limited/default_local.policy
%{_jvmdir}/%{sdkdir}/conf/security/policy/limited/default_US_export.policy
%{_jvmdir}/%{sdkdir}/conf/security/policy/limited/exempt_local.policy
%{_jvmdir}/%{sdkdir}/conf/security/policy/README.txt
%{_jvmdir}/%{sdkdir}/conf/security/policy/unlimited/default_local.policy
%{_jvmdir}/%{sdkdir}/conf/security/policy/unlimited/default_US_export.policy
%{_jvmdir}/%{sdkdir}/conf/sound.properties
%{_jvmdir}/%{sdkdir}/conf/tz.properties
%{_jvmdir}/%{sdkdir}/lib/J9TraceFormat.dat
%{_jvmdir}/%{sdkdir}/lib/OMRTraceFormat.dat
%{_jvmdir}/%{sdkdir}/lib/default/j9ddr.dat
%{_jvmdir}/%{sdkdir}/lib/default/libcuda4j29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9dmp29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9gc29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9gcchk29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9gcchk_full29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9gc_full29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9hookable29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9jextract.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9jit29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9jnichk29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9jvmti29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9prt29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9shr29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9thr29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9trc29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9vm29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9vmchk29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9vrb29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9vrb_full29.so
%{_jvmdir}/%{sdkdir}/lib/default/libj9zlib29.so
%{_jvmdir}/%{sdkdir}/lib/default/libjclse29.so
%{_jvmdir}/%{sdkdir}/lib/default/libmanagement_ext.so
%{_jvmdir}/%{sdkdir}/lib/default/libomrsig.so
%{_jvmdir}/%{sdkdir}/lib/desktop/jconsole.desktop
%{_jvmdir}/%{sdkdir}/lib/java*.properties
%{_jvmdir}/%{sdkdir}/lib/jexec
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
%{_jvmdir}/%{sdkdir}/lib/libjncrypto.so
%{_jvmdir}/%{sdkdir}/lib/libjsig.so
%{_jvmdir}/%{sdkdir}/lib/libjsound.so
%{_jvmdir}/%{sdkdir}/lib/liblcms.so
%{_jvmdir}/%{sdkdir}/lib/libmanagement.so
%{_jvmdir}/%{sdkdir}/lib/libmanagement_agent.so
%{_jvmdir}/%{sdkdir}/lib/libmlib_image.so
%{_jvmdir}/%{sdkdir}/lib/libnet.so
%{_jvmdir}/%{sdkdir}/lib/libnio.so
%{_jvmdir}/%{sdkdir}/lib/libprefs.so
%{_jvmdir}/%{sdkdir}/lib/librmi.so
%{_jvmdir}/%{sdkdir}/lib/libsctp.so
%{_jvmdir}/%{sdkdir}/lib/libsunec.so
%{_jvmdir}/%{sdkdir}/lib/libunpack.so
%{_jvmdir}/%{sdkdir}/lib/libverify.so
%{_jvmdir}/%{sdkdir}/lib/libzip.so
%{_jvmdir}/%{sdkdir}/lib/modules
#%{_jvmdir}/%{sdkdir}/lib/openj9-notices.html
%{_jvmdir}/%{sdkdir}/lib/options.default
%{_jvmdir}/%{sdkdir}/lib/psfontj2d.properties
%{_jvmdir}/%{sdkdir}/lib/psfont.properties.ja
%{_jvmdir}/%{sdkdir}/lib/tzdb.dat
%{_jvmdir}/%{sdkdir}/lib/*/libjsig.so
%{_jvmdir}/%{sdkdir}/lib/*/libjvm.so

%config(noreplace) %{_jvmdir}/%{sdkdir}/lib/security/blocked.certs
%config(noreplace) %{_jvmdir}/%{sdkdir}/conf/security/nss.cfg
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
%{_jvmdir}/%{sdkdir}/bin/jdmpview
%{_jvmdir}/%{sdkdir}/bin/jextract
%{_jvmdir}/%{sdkdir}/bin/jimage
%{_jvmdir}/%{sdkdir}/bin/jlink
%{_jvmdir}/%{sdkdir}/bin/jmap
%{_jvmdir}/%{sdkdir}/bin/jmod
%{_jvmdir}/%{sdkdir}/bin/jpackcore
%{_jvmdir}/%{sdkdir}/bin/jps
%{_jvmdir}/%{sdkdir}/bin/jrunscript
%{_jvmdir}/%{sdkdir}/bin/jshell
%{_jvmdir}/%{sdkdir}/bin/jstack
%{_jvmdir}/%{sdkdir}/bin/jstat
%{_jvmdir}/%{sdkdir}/bin/rmic
%{_jvmdir}/%{sdkdir}/bin/serialver
%{_jvmdir}/%{sdkdir}/bin/traceformat
%{_jvmdir}/%{sdkdir}/include/classfile_constants.h
%{_jvmdir}/%{sdkdir}/include/ibmjvmti.h
%{_jvmdir}/%{sdkdir}/include/jawt.h
%{_jvmdir}/%{sdkdir}/include/jdwpTransport.h
%{_jvmdir}/%{sdkdir}/include/jni.h
%{_jvmdir}/%{sdkdir}/include/jvmticmlr.h
%{_jvmdir}/%{sdkdir}/include/jvmti.h
%{_jvmdir}/%{sdkdir}/lib/ct.sym
%{_jvmdir}/%{sdkdir}/lib/libattach.so
%{_jvmdir}/%{sdkdir}/include/linux/jawt_md.h
%{_jvmdir}/%{sdkdir}/include/linux/jni_md.h

%{_jvmdir}/%{sdklnk}
%{_mandir}/man1/jar-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jarsigner-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/javac-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/javadoc-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/javap-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jconsole-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jdb-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jdeps-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jrunscript-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/rmic-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/serialver-%{sdklnk}.1%{?ext_man}

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
