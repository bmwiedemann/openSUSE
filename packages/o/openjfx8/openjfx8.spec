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
Name:           openjfx8
Version:        8.0.202
Release:        0
Summary:        Rich client application platform for Java
License:        GPL-2.0-only WITH Classpath-exception-2.0 AND BSD-3-Clause
URL:            https://openjdk.java.net/projects/openjfx/
Source0:        http://hg.openjdk.java.net/openjfx/8u-dev/rt/archive/8u202-b07.tar.bz2
Source1:        README.install
Patch0:         0000-Fix-wait-call-in-PosixPlatform.patch
Patch1:         0001-Change-SWT-and-Lucene.patch
Patch2:         0002-Allow-build-to-work-on-newer-gradles.patch
Patch3:         0003-fix-cast-between-incompatible-function-types.patch
Patch4:         0004-Fix-Compilation-Flags.patch
Patch5:         0005-fxpackager-extract-jre-accept-symlink.patch
Patch100:       openjfx-antlr.patch
Patch101:       openjfx-icedtea8.patch
Patch102:       openjfx-nowerror.patch
Patch103:       openjfx-pango.patch
Patch104:       openjfx-architectures.patch
Patch105:       openjfx8-sysctl.patch
BuildRequires:  bison
BuildRequires:  eclipse-swt
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  gradle-local
BuildRequires:  java-devel >= 1.8
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.antlr:antlr)
BuildRequires:  mvn(org.antlr:stringtemplate)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xxf86vm)
BuildConflicts: java-devel >= 9
Requires:       java >= 1.8
Provides:       %{oldname}
Obsoletes:      %{oldname}
#!BuildIgnore:  antlr3-tool-bootstrap
#!BuildRequires: antlr3-tool
#!BuildIgnore:  gradle-bootstrap
#!BuildRequires: gradle
#!BuildIgnore:  stringtemplate4-bootstrap
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
%patch4 -p1
%patch5 -p1

%patch100 -p1
%patch101 -p1
%patch102 -p1
%patch103 -p1
%patch104 -p1
%patch105 -p1

cp %{SOURCE1} .

cat > gradle.properties << EOF
COMPILE_WEBKIT = false
COMPILE_MEDIA = false
BUILD_JAVADOC = true
BUILD_SRC_ZIP = true
GRADLE_VERSION_CHECK = false
CONF = DebugNative
EOF

find -name '*.class' -delete
find -name '*.jar' -delete

#Bundled libraries
rm -rf modules/media/src/main/native/gstreamer/3rd_party/glib
rm -rf modules/media/src/main/native/gstreamer/gstreamer-lite

%build
gradle-local --no-daemon --offline

%install
install -d -m 755 %{buildroot}%{openjfxdir}
cp -a build/sdk/{bin,lib,rt} %{buildroot}%{openjfxdir}

install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 644 build/sdk/man/man1/* %{buildroot}%{_mandir}/man1

install -m 644 build/sdk/javafx-src.zip %{buildroot}%{openjfxdir}/javafx-src.zip

install -d 755 %{buildroot}%{_javadocdir}/%{name}
cp -a build/sdk/docs/api/. %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_bindir}
ln -s %{openjfxdir}/bin/javafxpackager %{buildroot}%{_bindir}
ln -s %{openjfxdir}/bin/javapackager %{buildroot}%{_bindir}

%files
%dir %{openjfxdir}
%{openjfxdir}/rt
%license LICENSE
%doc README README.install

%files devel
%{openjfxdir}/lib
%{openjfxdir}/bin
%{_bindir}/javafxpackager
%{_bindir}/javapackager
%{_mandir}/man1/javafxpackager.1%{?ext_man}
%{_mandir}/man1/javapackager.1%{?ext_man}
%license LICENSE
%doc README README.install

%files src
%{openjfxdir}/javafx-src.zip

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
