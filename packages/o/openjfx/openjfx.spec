#
# spec file for package openjfx
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


%global featurever   17
%global interimver   0
%global updatever    7
%global buildver     2
%global jfx_repo     jfx17u
%global jfx_tag      %{featurever}.%{interimver}.%{updatever}%{?patchver:.%{patchver}}+%{buildver}
%global jfx_dir      %{jfx_repo}-%{featurever}.%{interimver}.%{updatever}%{?patchver:.%{patchver}}-%{buildver}
%global jfx_inst_dir %{_jvmdir}/%{name}
%global package_version %{featurever}.%{interimver}.%{updatever}.%{?patchver:%{patchver}}%{!?patchver:0}
Name:           openjfx
Version:        %{package_version}
Release:        0
Summary:        Rich client application platform for Java
License:        BSD-3-Clause AND GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://openjdk.java.net/projects/openjfx/
Source0:        https://github.com/openjdk/%{jfx_repo}/archive/%{jfx_tag}.tar.gz
Source1:        pom-base.xml
Source2:        pom-controls.xml
Source3:        pom-fxml.xml
Source4:        pom-graphics.xml
Source5:        pom-graphics_antlr.xml
Source6:        pom-graphics_decora.xml
Source7:        pom-graphics_compileJava.xml
Source8:        pom-graphics_compileJava-decora.xml
Source9:        pom-graphics_compileJava-java.xml
Source10:       pom-graphics_compileJava-prism.xml
Source11:       pom-graphics_graphics.xml
Source12:       pom-graphics_libdecora.xml
Source13:       pom-graphics_libglass.xml
Source14:       pom-graphics_libglassgtk2.xml
Source15:       pom-graphics_libglassgtk3.xml
Source16:       pom-graphics_libjavafx_font.xml
Source17:       pom-graphics_libjavafx_font_freetype.xml
Source18:       pom-graphics_libjavafx_font_pango.xml
Source19:       pom-graphics_libjavafx_iio.xml
Source20:       pom-graphics_libprism_common.xml
Source21:       pom-graphics_libprism_es2.xml
Source22:       pom-graphics_libprism_sw.xml
Source23:       pom-graphics_prism.xml
Source24:       pom-media.xml
Source25:       pom-openjfx.xml
Source26:       pom-swing.xml
Source27:       pom-swt.xml
Source28:       pom-web.xml
Source29:       build.xml
Patch0:         openjfx-pango.patch
Patch1:         openjfx-no-return-in-nonvoid-function.patch
BuildRequires:  ant
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  java-devel >= 11
BuildRequires:  maven-local
BuildRequires:  mvn(org.antlr:ST4)
BuildRequires:  mvn(org.antlr:antlr)
BuildRequires:  mvn(org.antlr:antlr-runtime)
BuildRequires:  mvn(org.antlr:antlr4)
BuildRequires:  mvn(org.antlr:antlr4-maven-plugin)
BuildRequires:  mvn(org.antlr:antlr4-runtime)
BuildRequires:  mvn(org.antlr:stringtemplate)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:native-maven-plugin)
BuildRequires:  mvn(org.eclipse.swt:swt)
BuildRequires:  pkgconfig
BuildRequires:  xmvn-subst
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xxf86vm)
Obsoletes:      %{name}-javadoc < %{version}
Obsoletes:      %{name}-jmods < %{version}
Obsoletes:      %{name}-src < %{version}
#!BuildRequires: antlr3-tool
#!BuildIgnore:   antlr3-bootstrap-tool

%description
JavaFX/OpenJFX is a set of graphics and media APIs that enables Java
developers to design, create, test, debug, and deploy rich client
applications that operate consistently across diverse platforms.

The media module have been removed due to missing dependencies.

%package devel
Summary:        OpenJFX development tools and libraries
Requires:       %{name} = %{version}-%{release}

%description devel
%{summary}.

%prep
%setup -q -n %{jfx_dir}
%patch0 -p1
%patch1 -p1

#prep for javafx.graphics
cp -a modules/javafx.graphics/src/jslc/antlr modules/javafx.graphics/src/main/antlr3
cp -a modules/javafx.graphics/src/main/resources/com/sun/javafx/tk/quantum/*.properties modules/javafx.graphics/src/main/java/com/sun/javafx/tk/quantum

find -name '*.class' -print -delete
find -name '*.jar' -print -delete

#copy maven files
cp -a %{_sourcedir}/pom-*.xml .
mv pom-openjfx.xml pom.xml

for i in base controls fxml graphics media swing swt web
do
    mv pom-$i.xml ./modules/javafx.$i/pom.xml
done

mkdir ./modules/javafx.graphics/mvn-{antlr,decora,compileJava,graphics,libdecora,libglass,libglassgtk2,libglassgtk3,libjavafx_font,libjavafx_font_freetype,libjavafx_font_pango,libjavafx_iio,libprism_common,libprism_es2,libprism_sw,prism}
for i in antlr decora compileJava graphics libdecora libglass libglassgtk2 libglassgtk3 libjavafx_font libjavafx_font_freetype libjavafx_font_pango libjavafx_iio libprism_common libprism_es2 libprism_sw prism
do
    mv pom-graphics_$i.xml ./modules/javafx.graphics/mvn-$i/pom.xml
done

mkdir ./modules/javafx.graphics/mvn-compileJava/mvn-{decora,java,prism}
for i in decora java prism
do
    mv pom-graphics_compileJava-$i.xml ./modules/javafx.graphics/mvn-compileJava/mvn-$i/pom.xml
done

#set VersionInfo
cp %{SOURCE29} build.xml
%{ant}

mkdir -p ./modules/javafx.graphics/mvn-antlr/src/main
mv ./modules/javafx.graphics/src/main/antlr3 ./modules/javafx.graphics/mvn-antlr/src/main/antlr4

rm -rf ./modules/javafx.web/src/main/native/Source/WTF/icu
rm -rf ./modules/javafx.web/src/main/native/Source/ThirdParty/icu

%{mvn_package} ::so: __noinstall

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"

%{mvn_build} -fj

%install
%mvn_install
install -dm 0755 %{buildroot}%{_libdir}/%{name}
install -pm 0755 \
    modules/javafx.graphics/mvn-lib{decora,javafx_font,javafx_font_freetype,javafx_font_pango,glass,glassgtk2,glassgtk3,javafx_iio,prism_common,prism_es2,prism_sw}/target/*.so \
    %{buildroot}%{_libdir}/%{name}/

install -d -m 755 %{buildroot}%{jfx_inst_dir}
cp -a modules/javafx.{base,controls,fxml,media,swing,swt,web}/target/*.jar %{buildroot}%{jfx_inst_dir}
cp -a modules/javafx.graphics/mvn-compileJava/mvn-java/target/*.jar %{buildroot}%{jfx_inst_dir}
for i in %{buildroot}%{_libdir}/%{name}/*.so; do
    ln -sf %{_libdir}/%{name}/$(basename $i) %{buildroot}%{jfx_inst_dir}/$(basename $i)
done
xmvn-subst -R %{buildroot} -s %{buildroot}%{jfx_inst_dir}

%files -f .mfiles
%{_libdir}/%{name}
%license LICENSE ADDITIONAL_LICENSE_INFO ASSEMBLY_EXCEPTION
%doc README.md

%files devel
%{jfx_inst_dir}
%license LICENSE ADDITIONAL_LICENSE_INFO ASSEMBLY_EXCEPTION

%changelog
