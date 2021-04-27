#
# spec file for package openjfx
#
# Copyright (c) 2021 SUSE LLC
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


%global priority        2105
%global build_number 1
Name:           openjfx
Version:        11.0.10
Release:        0
Summary:        Rich client application platform for Java
License:        BSD-3-Clause AND GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://openjdk.java.net/projects/openjfx/
Source0:        http://hg.openjdk.java.net/openjfx/11-dev/rt/archive/%{version}+%{build_number}.tar.bz2
Patch0:         0000-Fix-wait-call-in-PosixPlatform.patch
Patch1:         0001-Change-SWT-and-Lucene.patch
Patch2:         0002-Allow-build-to-work-on-newer-gradles.patch
Patch4:         0004-Fix-Compilation-Flags.patch
Patch5:         0005-fxpackager-extract-jre-accept-symlink.patch
Patch100:       openjfx-antlr.patch
Patch101:       openjfx-gradle441.patch
Patch102:       openjfx-nowerror.patch
Patch103:       openjfx-pango.patch
Patch104:       openjfx-architectures.patch
Patch105:       openjfx-no-return-in-nonvoid-function.patch
Patch200:       openjfx-rpm-build.patch
BuildRequires:  eclipse-swt
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gradle-local
BuildRequires:  java-devel >= 10
BuildRequires:  java-javadoc >= 10
BuildRequires:  pkgconfig
BuildRequires:  mvn(org.antlr:antlr4)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xxf86vm)
#!BuildRequires: gradle stringtemplate4
#!BuildIgnore: gradle-bootstrap stringtemplate4-bootstrap

%description
JavaFX/OpenJFX is a set of graphics and media APIs that enables Java
developers to design, create, test, debug, and deploy rich client
applications that operate consistently across diverse platforms.

%package devel
Summary:        OpenJFX development tools and libraries
Requires:       %{name} = %{version}-%{release}

%description devel
%{summary}.

%package jmods
Summary:        OpenJFX Jmods

%description jmods
%{summary}.

%package src
Summary:        OpenJFX Source Bundle

%description src
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n rt-%{version}+%{build_number}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch4 -p1
%patch5 -p1

%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1

%patch200 -p1

cat > gradle.properties << EOF
COMPILE_WEBKIT = false
COMPILE_MEDIA = false
BUILD_JAVADOC = true
BUILD_SRC_ZIP = true
GRADLE_VERSION_CHECK = false
CONF = DebugNative
EOF

find -name '*.class' -type f -delete
find -name '*.jar' -type f -delete

#Bundled libraries
rm -rf modules/javafx.media/src/main/native/gstreamer/3rd_party/glib
rm -rf modules/javafx.media/src/main/native/gstreamer/gstreamer-lite

%mvn_package org.openjfx:::linux:

%build
export SOURCE_DATE_EPOCH=$(date -r %{SOURCE0} +%s)
env | grep SOURCE_DATE_EPOCH
gradle-local --no-daemon --offline sdk generatePomFileForMavenPublication generatePomFileForJavafxPublication javadoc jmod

%install
%mvn_artifact modules/javafx.base/build/publications/javafx/pom-default.xml
for i in base controls fxml graphics media swing web; do
  %pom_xpath_remove pom:project/pom:packaging modules/javafx.${i}/build/publications/maven/pom-default.xml
  %pom_xpath_set pom:classifier linux modules/javafx.${i}/build/publications/maven/pom-default.xml
  %mvn_artifact modules/javafx.${i}/build/publications/maven/pom-default.xml build/publications/javafx.${i}.jar
  %mvn_artifact org.openjfx:javafx-${i}::linux:%{version} build/publications/javafx.${i}-linux.jar
done

%mvn_install -J build/javadoc
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

install -dm 0755 %{buildroot}%{_datadir}/%{name}
cp -a build/sdk/lib %{buildroot}%{_datadir}/%{name}/lib
cp -a build/jmods %{buildroot}%{_datadir}/%{name}/jmods

mv %{buildroot}%{_datadir}/%{name}/lib/src.zip %{buildroot}%{_datadir}/%{name}/src.zip

install -dm 0755 %{buildroot}%{_libdir}/%{name}

mv %{buildroot}%{_datadir}/%{name}/lib/*.so %{buildroot}%{_libdir}/%{name}

for i in base controls fxml graphics media swing web; do
  if [ -e %{buildroot}%{_javadir}/%{name}/javafx-${i}-linux.jar ]; then
    rm -f %{buildroot}%{_datadir}/%{name}/lib/javafx.${i}.jar;
	ln -sf %{_javadir}/%{name}/javafx-${i}-linux.jar %{buildroot}%{_datadir}/%{name}/lib/javafx.${i}.jar
  elif [ -e %{buildroot}%{_jnidir}/%{name}/javafx-${i}-linux.jar ]; then
    rm -f %{buildroot}%{_datadir}/%{name}/lib/javafx.${i}.jar;
	ln -sf %{_jnidir}/%{name}/javafx-${i}-linux.jar %{buildroot}%{_datadir}/%{name}/lib/javafx.${i}.jar
  fi
done

%files -f .mfiles
%license LICENSE
%doc README

%files devel
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/lib
%{_libdir}/%{name}
%license LICENSE
%doc README

%files src
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/src.zip

%files jmods
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/jmods

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
