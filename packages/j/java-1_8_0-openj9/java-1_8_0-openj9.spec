#
# spec file for package java-1_8_0-openj9
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
%global bootcycle 1
# Convert an absolute path to a relative path.  Each symbolic link is
# specified relative to the directory in which it is installed so that
# it will resolve properly within chrooted installations.
%global script 'use File::Spec; print File::Spec->abs2rel($ARGV[0], $ARGV[1])'
%global abs2rel perl -e %{script}
%global syslibdir       %{_libdir}
# Standard JPackage naming and versioning defines.
%global updatever       362
%global buildver        b09
%global root_repository https://github.com/ibmruntimes/openj9-openjdk-jdk8/archive
%global root_revision   eebde685ec08dbafdfcddad2782a823b8238a886
%global root_branch     v0.36.0-release
%global omr_repository  https://github.com/eclipse/openj9-omr/archive
%global omr_revision    f491bbf6f6f3f87bfd38a65055589125c13de555
%global omr_branch      v0.36.1-release
%global openj9_repository https://github.com/eclipse/openj9/archive
%global openj9_revision 0592661e480dd108a708689dc56bf1a427677645
%global openj9_branch   v0.36.1-release
%global openj9_tag      openj9-0.36.1
# priority must be 6 digits in total
%global priority        1801
%global javaver         1.8.0
# Standard JPackage directories and symbolic links.
%global sdklnk          java-%{javaver}-openj9
%global archname        %{sdklnk}
%global jrelnk          jre-%{javaver}-openj9
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
# turn zero on non jit arches by default
%ifarch x86_64
%global archinstall amd64
%endif
%ifarch ppc64le
%global archinstall ppc64le
%endif
%ifarch s390x
%global archinstall s390x
%endif
%ifarch %{aarch64}
%global archinstall aarch64
%endif
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
Name:           java-1_8_0-openj9
Version:        %{javaver}.%{updatever}
Release:        0
Summary:        OpenJDK 8 Runtime Environment with Eclipse OpenJ9 virtual machine
License:        Apache-1.1 AND Apache-2.0 AND EPL-2.0 AND GPL-1.0-or-later AND GPL-2.0-only AND GPL-2.0-only WITH Classpath-exception-2.0 AND LGPL-2.0-only AND MPL-1.0 AND MPL-1.1 AND SUSE-Public-Domain AND W3C
Group:          Development/Languages/Java
URL:            https://www.eclipse.org/openj9/
# Sources from upstream OpenJDK8 project.
Source0:        %{root_repository}/%{root_revision}.zip
Source1:        %{omr_repository}/%{omr_revision}.zip
Source2:        %{openj9_repository}/%{openj9_revision}.zip
# Desktop files. Adapated from IcedTea.
Source11:       jconsole.desktop.in
Source12:       policytool.desktop.in
# nss configuration file
Source13:       nss.cfg
# Ensure we aren't using the limited crypto policy
Source14:       TestCryptoLevel.java
Source100:      openj9-nogit.patch.in
Source1000:     %{name}-rpmlintrc
# RPM/distribution specific patches
# Restrict access to java-atk-wrapper classes
Patch1:         java-atk-wrapper-security.patch
# Allow multiple initialization of PKCS11 libraries
Patch2:         multiple-pkcs11-library-init.patch
# Disable doclint for compatibility
Patch3:         disable-doclint-by-default.patch
# Allow building with newer libdwarf
Patch4:         libdwarf-fix.patch
# Fix narrowing conversion error
Patch5:         openj9-no-narrowing.patch
# Patches for system libraries
Patch201:       system-libjpeg.patch
Patch202:       system-libpng.patch
Patch203:       system-lcms.patch
Patch205:       link-with-as-needed.patch
Patch210:       openj9-no-werror.patch
Patch300:       alternative-path-to-tzdb_dat.patch
BuildRequires:  alsa-lib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  fontconfig
BuildRequires:  freetype2-devel
BuildRequires:  giflib-devel
BuildRequires:  gtk2-devel
BuildRequires:  java-ca-certificates
BuildRequires:  libX11-devel
BuildRequires:  libXi-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXt-devel
BuildRequires:  libXtst-devel
BuildRequires:  libdwarf-devel
BuildRequires:  libelf-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libnuma-devel
BuildRequires:  libpng-devel
BuildRequires:  libxslt
BuildRequires:  nasm >= 2.11
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11-proto-devel
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
Requires(post): java-ca-certificates
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
Provides:       java-openjdk-%{bits} = %{version}-%{release}
Provides:       jre-%{bits} = %{javaver}
Provides:       jre-%{javaver}-%{bits}
Provides:       jre-%{javaver}-openj9-%{bits} = %{version}-%{release}
Provides:       jre-%{javaver}-openjdk-%{bits} = %{version}-%{release}
Provides:       jre-openj9-%{bits} = %{version}-%{release}
Provides:       jre-openjdk-%{bits} = %{version}-%{release}
Provides:       jre1.3.x
Provides:       jre1.4.x
Provides:       jre1.5.x
Provides:       jre1.6.x
Provides:       jre1.7.x
Provides:       jre1.8.x
ExclusiveArch:  x86_64 ppc64le s390x aarch64
%if 0%{?suse_version} < 1500
BuildRequires:  gcc7
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc >= 7
BuildRequires:  gcc-c++ >= 7
%endif
%if %{bootcycle}
BuildRequires:  java-devel >= 1.7
BuildConflicts: java >= 9
BuildConflicts: java-devel >= 9
BuildConflicts: java-headless >= 9
%else
BuildRequires:  %{name}-devel
%endif

%description
The OpenJDK 8 with Eclipse OpenJ9 virtual machine. Eclipse OpenJ9
is a Java Virtual Machine for OpenJDK that is optimized for small
footprint, fast start-up, and high throughput.

Supported architectures are ppc64le, s390x and x86_64

%package headless
Summary:        OpenJDK 8 Runtime Environment with Eclipse OpenJ9
# Require jpackage-utils for ownership of /usr/lib/jvm/
Group:          Development/Languages/Java
Requires:       jpackage-utils
# Post requires update-alternatives to install tool update-alternatives.
Requires(post): update-alternatives
# Postun requires update-alternatives to uninstall tool update-alternatives.
Requires(postun):update-alternatives
Recommends:     tzdata-java8
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
Provides:       jdbc-stdext = 4.2
Provides:       jndi = %{version}
Provides:       jndi-cos = %{version}
Provides:       jndi-dns = %{version}
Provides:       jndi-ldap = %{version}
Provides:       jndi-rmi = %{version}
Provides:       jsse = %{version}

%description headless
The OpenJDK 8 runtime environment without audio and video support.

Supported architectures are ppc64le, s390x and x86_64

%package devel
Summary:        OpenJDK 8 Development Environment with Eclipse OpenJ9
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
The OpenJDK 8 development tools.

Supported architectures are ppc64le, s390x and x86_64

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
Requires(postun):update-alternatives
# Standard JPackage javadoc provides.
Provides:       java-%{javaver}-javadoc = %{version}-%{release}
Provides:       java-javadoc = %{version}-%{release}
BuildArch:      noarch

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
%setup -q -n openj9-openjdk-jdk8-%{root_revision} -a 1 -a 2

# Set up the build tree using the subrepository tarballs
pwd
mv openj9-omr-%{omr_revision} omr
mv openj9-%{openj9_revision} openj9

cp openj9/LICENSE LICENSE.openj9

# Remove libraries that are linked
rm -rvf jdk/src/share/native/java/util/zip/zlib-*
find jdk/src/share/native/sun/awt/image/jpeg ! -name imageioJPEG.c ! -name jpegdecoder.c -type f -delete
rm -rvf jdk/src/share/native/sun/awt/libpng
rm -rvf jdk/src/share/native/sun/awt/giflib
rm -rvf jdk/src/share/native/sun/java2d/cmm/lcms/cms*
rm -rvf jdk/src/share/native/sun/java2d/cmm/lcms/lcms2*

%patch201 -p1
%patch202 -p1
%patch203 -p1
%patch205 -p1

%patch210

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%patch300 -p1

cat %{SOURCE100} \
    | sed "s/@OPENJ9_SHA@/%{openj9_revision}/g" \
    | sed "s/@OPENJ9_BRANCH@/%{openj9_branch}/g" \
    | sed "s/@OPENJ9_TAG@/%{openj9_tag}/g" \
    | sed "s/@OPENJ9OMR_SHA@/%{omr_revision}/g" \
    | sed "s/@OPENJDK_SHA@/%{root_revision}/g" \
    | sed "s/@OPENSSL_SHA@//g" \
    | patch -p1 -u -l

# Prepare desktop files
for file in %{SOURCE11} %{SOURCE12} ; do
    OUTPUT_FILE=`basename $file | sed -e s:\.in$::g`
    sed -e s:@JAVA_HOME@:%{_jvmdir}/%{sdkdir}:g $file > $OUTPUT_FILE
    sed -i -e s:@VERSION@:%{javaver}.%{_arch}:g $OUTPUT_FILE
done

%build
export ARCH_DATA_MODEL=64

(cd common/autoconf
 bash ./autogen.sh
)

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
    --disable-warnings-as-errors-omr \
    --disable-warnings-as-errors-openj9 \
    --enable-demos \
    --disable-zip-debug-info \
    --with-milestone="fcs" \
    --with-update-version=%{updatever} \
    --with-build-number=%{buildver} \
    --with-debug-level=%{debugbuild} \
    --with-conf-name=%{debugbuild} \
    --enable-unlimited-crypto \
    --with-zlib=system \
    --with-libjpeg=system \
    --with-giflib=system \
    --with-libpng=system \
    --with-lcms=system \
	--with-openssl=system \
    --with-stdc++lib=dynamic \
    --with-native-debug-symbols=internal \
    --with-boot-jdk=%{_sysconfdir}/alternatives/java_sdk

make \
    JAVAC_FLAGS=-g \
    LOG=trace \
    DEBUG_BINARIES=true \
    STRIP_POLICY=no_strip \
    POST_STRIP_CMD="" \
    WARNINGS_ARE_ERRORS="-Wno-error" \
    CFLAGS_WARNINGS_ARE_ERRORS="-Wno-error" \
    %{imagestarget} docs

# remove redundant *diz and *debuginfo files
find %{imagesdir}/j2sdk-image -iname '*.diz' -exec rm {} \;
find %{imagesdir}/j2sdk-image -iname '*.debuginfo' -exec rm {} \;

export JAVA_HOME=$(pwd)/%{imagesdir}/j2sdk-image

# Copy tz.properties
echo "sun.zoneinfo.dir=%{_datadir}/javazi" >> $JAVA_HOME/jre/lib/tz.properties

# cacerts are generated in runtime in openSUSE
if [ -f %{imagesdir}/j2sdk-image/jre/lib/security/cacerts ]; then
        rm %{imagesdir}/j2sdk-image/jre/lib/security/cacerts
fi

# Check unlimited policy has been used
$JAVA_HOME/bin/javac -d . %{SOURCE14}
$JAVA_HOME/bin/java TestCryptoLevel

%if 0
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
%endif

%install
export LANG=en_US.UTF-8
#bnc#530046
export STRIP_KEEP_SYMTAB=libjvm*
# skip /usr/lib/rpm/brp-check-bytecode-version:
export NO_BRP_CHECK_BYTECODE_VERSION=true

pushd %{imagesdir}/j2sdk-image

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
  # These tree tools are not built,
  # so disregard their manpages too.
  rm -f man/man1/jhat.1*
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

# Install nss.cfg
install -m 644 %{SOURCE13} %{buildroot}%{_jvmdir}/%{jredir}/lib/security/

# Install Javadoc documentation.
install -d -m 755 %{buildroot}%{_javadocdir}
cp -a build/%{debugbuild}/docs %{buildroot}%{_javadocdir}/%{sdklnk}

# Install icons and menu entries.
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
    jdk/src/solaris/classes/sun/awt/X11/java-icon${s}.png \
    %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}-openj9.png
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

%posttrans headless
# bnc#781690#c11: don't trust user defined JAVA_HOME and use the current VM
# XXX: this might conflict between various versions of openjdk
export JAVA_HOME=%{_jvmdir}/%{jrelnk}

# check if the java-cacerts is a valid keystore (bnc#781690)
if [ X"`%{_bindir}/file --mime-type -b %{javacacerts}`" \
    != "Xapplication/x-java-keystore;" ]; then
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
  --slave %{_jvmjardir}/java java_sdk_exports %{jvmjarlink} \
  --slave %{_bindir}/appletviewer appletviewer %{sdkbindir}/appletviewer \
  --slave %{_bindir}/extcheck extcheck %{sdkbindir}/extcheck \
  --slave %{_bindir}/jar jar %{sdkbindir}/jar \
  --slave %{_bindir}/jarsigner jarsigner %{sdkbindir}/jarsigner \
  --slave %{_bindir}/javadoc javadoc %{sdkbindir}/javadoc \
  --slave %{_bindir}/javah javah %{sdkbindir}/javah \
  --slave %{_bindir}/javap javap %{sdkbindir}/javap \
  --slave %{_bindir}/jconsole jconsole %{sdkbindir}/jconsole \
  --slave %{_bindir}/jdb jdb %{sdkbindir}/jdb \
  --slave %{_bindir}/jmap jmap %{sdkbindir}/jmap \
  --slave %{_bindir}/jps jps %{sdkbindir}/jps \
  --slave %{_bindir}/jrunscript jrunscript %{sdkbindir}/jrunscript \
  --slave %{_bindir}/jsadebugd jsadebugd %{sdkbindir}/jsadebugd \
  --slave %{_bindir}/jstack jstack %{sdkbindir}/jstack \
  --slave %{_bindir}/jstat jstat %{sdkbindir}/jstat \
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
  --slave %{_mandir}/man1/jdb.1$ext jdb.1$ext \
  %{_mandir}/man1/jdb-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jrunscript.1$ext jrunscript.1$ext \
  %{_mandir}/man1/jrunscript-%{sdklnk}.1$ext \
  --slave %{_mandir}/man1/jsadebugd.1$ext jsadebugd.1$ext \
  %{_mandir}/man1/jsadebugd-%{sdklnk}.1$ext \
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
%{_datadir}/icons/hicolor/*x*/apps/java-%{javaver}-openj9.png

%files headless -f %{name}.files-headless
%dir %{_jvmdir}
%dir %{_jvmdir}/%{jredir}/
%dir %{_jvmdir}/%{jredir}/bin
%dir %{_jvmdir}/%{jredir}/lib
%dir %{_jvmdir}/%{jredir}/lib/%{archinstall}
%dir %{_jvmdir}/%{jredir}/lib/%{archinstall}/default
%dir %{_jvmdir}/%{jredir}/lib/%{archinstall}/jli
%dir %{_jvmdir}/%{jredir}/lib/%{archinstall}/j9vm
%dir %{_jvmdir}/%{jredir}/lib/%{archinstall}/server
%dir %{_jvmdir}/%{jredir}/lib/cmm
%dir %{_jvmdir}/%{jredir}/lib/ddr
%dir %{_jvmdir}/%{jredir}/lib/desktop
%dir %{_jvmdir}/%{jredir}/lib/ext
%dir %{_jvmdir}/%{jredir}/lib/images
%dir %{_jvmdir}/%{jredir}/lib/images/cursors
%dir %{_jvmdir}/%{jredir}/lib/management
%dir %{_jvmdir}/%{jredir}/lib/security
%dir %{_jvmdir}/%{jredir}/lib/security/policy
%dir %{_jvmdir}/%{jredir}/lib/security/policy/limited
%dir %{_jvmdir}/%{jredir}/lib/security/policy/unlimited
%dir %{_libdir}/jvm-exports
%dir %{_libdir}/jvm-private

%doc %{imagesdir}/j2sdk-image/jre/ASSEMBLY_EXCEPTION
%license %{imagesdir}/j2sdk-image/jre/LICENSE LICENSE.openj9
%doc %{imagesdir}/j2sdk-image/jre/THIRD_PARTY_README

%dir %{_jvmdir}/%{sdkdir}
%{_jvmdir}/%{jrelnk}
%{_jvmjardir}/%{jrelnk}
%{_jvmprivdir}/*
%{jvmjardir}
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.policy
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/java.security
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/blacklisted.certs
%config(noreplace) %{_jvmdir}/%{jredir}/lib/security/nss.cfg
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
%ifarch x86_64
%{_jvmdir}/%{jredir}/lib/security/nss.fips.cfg
%endif

%files devel
%dir %{_jvmdir}/%{sdkdir}/bin
%dir %{_jvmdir}/%{sdkdir}/include
%dir %{_jvmdir}/%{sdkdir}/lib
%{_jvmdir}/%{sdkdir}/bin/*
%{_jvmdir}/%{sdkdir}/include/*
%{_jvmdir}/%{sdkdir}/lib/*

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
%{_mandir}/man1/jdb-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jdeps-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jrunscript-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/jsadebugd-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/native2ascii-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/rmic-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/schemagen-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/serialver-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/wsgen-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/wsimport-%{sdklnk}.1%{?ext_man}
%{_mandir}/man1/xjc-%{sdklnk}.1%{?ext_man}

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
