#
# spec file for package openjfx8
#
# Copyright (c) 2020 SUSE LLC
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


%global openjfxdir %{_jvmdir}/%{name}
%global oldname java-1_8_0-openjfx
%global archinstall %{_arch}
%ifarch x86_64
%global archinstall amd64
%endif
%ifarch %{ix86}
%global archinstall i386
%endif
%ifarch %{arm}
%global archinstall aarch32
%endif
%ifarch %{aarch64}
%global archinstall aarch64
%endif
Name:           openjfx8
Version:        8.0.202
Release:        0
Summary:        Rich client application platform for Java
License:        GPL-2.0-only WITH Classpath-exception-2.0 AND BSD-3-Clause
URL:            https://openjdk.java.net/projects/openjfx/
Source0:        http://hg.openjdk.java.net/openjfx/8u-dev/rt/archive/8u202-b07.tar.bz2
Source1:        README.install
Source2:        pom-base.xml
Source3:        pom-builders.xml
Source4:        pom-controls.xml
Source5:        pom-fxml.xml
Source6:        pom-fxpackager.xml
Source7:        pom-graphics.xml
Source8:        pom-graphics_compileDecoraCompilers.xml
Source9:        pom-graphics_compileDecoraJavaShaders.xml
Source10:       pom-graphics_compileJava.xml
Source11:       pom-graphics_compilePrismCompilers.xml
Source12:       pom-graphics_compilePrismJavaShaders.xml
Source13:       pom-graphics_libdecora.xml
Source14:       pom-graphics_libglass.xml
Source15:       pom-graphics_libglassgtk2.xml
Source16:       pom-graphics_libglassgtk3.xml
Source17:       pom-graphics_libjavafx_font.xml
Source18:       pom-graphics_libjavafx_font_freetype.xml
Source19:       pom-graphics_libjavafx_font_pango.xml
Source20:       pom-graphics_libjavafx_iio.xml
Source21:       pom-graphics_libprism_common.xml
Source22:       pom-graphics_libprism_es2.xml
Source23:       pom-graphics_libprism_sw.xml
Source24:       pom-jmx.xml
Source25:       pom-media.xml
Source26:       pom-openjfx.xml
Source27:       pom-swing.xml
Source28:       pom-swt.xml
Source29:       pom-web.xml
Source30:       shade.xml
Source31:       build.xml
Source32:       buildSrc.xml
Source33:       fxpackager-native.xml
Source34:       fxpackager-so.xml
Source35:       build-sources.xml
Patch0:         0000-Fix-wait-call-in-PosixPlatform.patch
Patch1:         0003-fix-cast-between-incompatible-function-types.patch
Patch2:         0004-Fix-Compilation-Flags.patch
Patch3:         0005-fxpackager-extract-jre-accept-symlink.patch
Patch100:       openjfx-antlr.patch
Patch101:       openjfx-icedtea8.patch
Patch102:       openjfx-nowerror.patch
Patch103:       openjfx-pango.patch
Patch104:       openjfx-architectures.patch
BuildRequires:  ant
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  maven-local
BuildRequires:  pkgconfig
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(org.antlr:antlr)
BuildRequires:  mvn(org.antlr:stringtemplate)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:native-maven-plugin)
BuildRequires:  mvn(org.eclipse.swt:swt)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xxf86vm)
BuildConflicts: java-devel >= 9
#!BuildIgnore:  antlr3-tool-bootstrap
#!BuildRequires: antlr3-tool
#!BuildIgnore:  stringtemplate4-bootstrap
Requires:       java >= 1.8
Provides:       %{oldname}
Obsoletes:      %{oldname}
#!BuildRequires: stringtemplate4

%description
JavaFX/OpenJFX is a set of graphics and media APIs that enables Java
developers to design, create, test, debug, and deploy rich client
applications that operate consistently across diverse platforms.

The media and web module have been removed due to missing dependencies.

%package devel
Summary:        OpenJFX development tools and libraries
Requires:       %{name} = %{version}-%{release}
Requires:       java-devel >= 1.8
Provides:       %{oldname}-devel
Obsoletes:      %{oldname}-devel

%description devel
%{summary}.

%package src
Summary:        OpenJFX Source Bundle
Requires:       %{name} = %{version}-%{release}
Provides:       %{oldname}-src
Obsoletes:      %{oldname}-src

%description src
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Provides:       %{oldname}-javadoc
Obsoletes:      %{oldname}-javadoc
BuildArch:      noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n rt-8u202-b07
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1

cp %{SOURCE1} .

#Drop *src/test folders
rm -rf modules/{base,builders,controls,fxml,fxpackager,graphics,jmx,media,swing,swt,web}/src/test/
rm -rf buildSrc/src/test/

#prep for graphics
##cp -a modules/javafx.graphics/src/jslc/antlr modules/javafx.graphics/src/main/antlr3
cp -a modules/graphics/src/main/resources/com/sun/javafx/tk/quantum/*.properties modules/graphics/src/main/java/com/sun/javafx/tk/quantum

#prep for base
cp -a modules/base/src/main/java8/javafx modules/base/src/main/java

#prep for swt
cp -a modules/builders/src/main/java/javafx/embed/swt/CustomTransferBuilder.java modules/swt/src/main/java/javafx/embed/swt

find -name '*.class' -delete
find -name '*.jar' -delete

#copy maven files
cp -a %{_sourcedir}/pom-*.xml .
mv pom-openjfx.xml pom.xml

for MODULE in base graphics controls swing swt fxml media web builders fxpackager jmx
do
	mv pom-$MODULE.xml ./modules/$MODULE/pom.xml
done

#shade
mkdir shade
cp -a %{_sourcedir}/shade.xml ./shade/pom.xml

#fxpackager native exe
mkdir ./modules/fxpackager/native
cp -a %{_sourcedir}/fxpackager-native.xml ./modules/fxpackager/native/pom.xml
#fxpackager libpackager.so
mkdir ./modules/fxpackager/so
cp -a %{_sourcedir}/fxpackager-so.xml ./modules/fxpackager/so/pom.xml

cp -a %{_sourcedir}/buildSrc.xml ./buildSrc/pom.xml

mkdir ./modules/graphics/{compileJava,compilePrismCompilers,compilePrismJavaShaders,compileDecoraCompilers,compileDecoraJavaShaders,libdecora,libjavafx_font,libjavafx_font_freetype,libjavafx_font_pango,libglass,libglassgtk2,libglassgtk3,libjavafx_iio,libprism_common,libprism_es2,libprism_sw}
for GRAPHMOD in compileJava compilePrismCompilers compilePrismJavaShaders compileDecoraCompilers compileDecoraJavaShaders libdecora libjavafx_font libjavafx_font_freetype libjavafx_font_pango libglass libglassgtk2 libglassgtk3 libjavafx_iio libprism_common libprism_es2 libprism_sw
do
	mv pom-graphics_$GRAPHMOD.xml ./modules/graphics/$GRAPHMOD/pom.xml
done

#set VersionInfo
cp -a %{_sourcedir}/build.xml .
ant -f build.xml

cp -a %{_sourcedir}/build-sources.xml .

%build
%{mvn_build} -f -- -Dbuild.java.arch=%{archinstall}

ant -f build-sources.xml

%install
install -d -m 755 %{buildroot}%{openjfxdir}
mkdir -p %{buildroot}%{openjfxdir}/bin
mkdir -p %{buildroot}%{openjfxdir}/lib
mkdir -p %{buildroot}%{openjfxdir}/rt/lib/{%{archinstall},ext}

cp -a shade/target/jfxrt.jar %{buildroot}%{openjfxdir}/rt/lib/ext
cp -a modules/swt/target/jfxswt.jar %{buildroot}%{openjfxdir}/rt/lib
cp -a modules/graphics/libdecora/target/libdecora_sse.so %{buildroot}%{openjfxdir}/rt/lib/%{archinstall}
cp -a modules/graphics/libglass/target/libglass.so %{buildroot}%{openjfxdir}/rt/lib/%{archinstall}
cp -a modules/graphics/libglassgtk2/target/libglassgtk2.so %{buildroot}%{openjfxdir}/rt/lib/%{archinstall}
cp -a modules/graphics/libglassgtk3/target/libglassgtk3.so %{buildroot}%{openjfxdir}/rt/lib/%{archinstall}
cp -a modules/graphics/libjavafx_font/target/libjavafx_font.so %{buildroot}%{openjfxdir}/rt/lib/%{archinstall}
cp -a modules/graphics/libjavafx_font_freetype/target/libjavafx_font_freetype.so %{buildroot}%{openjfxdir}/rt/lib/%{archinstall}
cp -a modules/graphics/libjavafx_font_pango/target/libjavafx_font_pango.so %{buildroot}%{openjfxdir}/rt/lib/%{archinstall}
cp -a modules/graphics/libjavafx_iio/target/libjavafx_iio.so %{buildroot}%{openjfxdir}/rt/lib/%{archinstall}
cp -a modules/graphics/libprism_common/target/libprism_common.so %{buildroot}%{openjfxdir}/rt/lib/%{archinstall}
cp -a modules/graphics/libprism_es2/target/libprism_es2.so %{buildroot}%{openjfxdir}/rt/lib/%{archinstall}
cp -a modules/graphics/libprism_sw/target/libprism_sw.so %{buildroot}%{openjfxdir}/rt/lib/%{archinstall}
cp -a modules/jmx/target/javafx-mx.jar %{buildroot}%{openjfxdir}/lib
cp -a modules/fxpackager/target/fxpackager-ant-javafx.jar %{buildroot}%{openjfxdir}/lib/ant-javafx.jar
cp -a modules/fxpackager/target/fxpackager-packager.jar %{buildroot}%{openjfxdir}/lib/packager.jar
cp -a modules/fxpackager/src/main/native/javapackager/shell/javapackager %{buildroot}%{openjfxdir}/bin
cp -a modules/fxpackager/src/main/native/javapackager/shell/javapackager %{buildroot}%{openjfxdir}/bin/javafxpackager

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 modules/fxpackager/src/main/man/man1/* %{buildroot}%{_mandir}/man1

install -m 644 javafx-src.zip %{buildroot}%{openjfxdir}/javafx-src.zip

install -d 755 %{buildroot}%{_javadocdir}/%{name}
cp -a target/site/apidocs/. %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_bindir}
ln -s %{openjfxdir}/bin/javafxpackager %{buildroot}%{_bindir}
ln -s %{openjfxdir}/bin/javapackager %{buildroot}%{_bindir}

%files
%dir %{openjfxdir}
%{openjfxdir}/rt
%license LICENSE
%doc README
%doc README.install

%files devel
%{openjfxdir}/lib
%{openjfxdir}/bin
%{_bindir}/javafxpackager
%{_bindir}/javapackager
%{_mandir}/man1/javafxpackager.1%{?ext_man}
%{_mandir}/man1/javapackager.1%{?ext_man}
%license LICENSE
%doc README
%doc README.install

%files src
%{openjfxdir}/javafx-src.zip

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
