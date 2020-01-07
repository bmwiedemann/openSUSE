#
# spec file for package java-1_8_0-openjfx
#
# Copyright (c) 2019 SUSE LLC.
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


%global javaname java-1_8_0-openjdk
%global openjdk8_install_dir %{_jvmdir}/java-1.8.0-openjdk-1.8.0
%global priority        1805
Name:           java-1_8_0-openjfx
Version:        8.0.202
Release:        0
Summary:        Rich client application platform for Java
License:        GPL-2.0-only WITH Classpath-exception-2.0 AND BSD-3-Clause
URL:            https://openjdk.java.net/projects/openjfx/
Source0:        http://hg.openjdk.java.net/openjfx/8u-dev/rt/archive/8u202-b07.tar.bz2
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
BuildRequires:  %{javaname}-devel
BuildRequires:  bison
BuildRequires:  eclipse-swt
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  gradle-local
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
Requires:       %{javaname}
#!BuildRequires: gradle antlr3-tool stringtemplate4
#!BuildIgnore: gradle-bootstrap antlr3-tool-bootstrap stringtemplate4-bootstrap

%description
JavaFX/OpenJFX is a set of graphics and media APIs that enables Java
developers to design, create, test, debug, and deploy rich client
applications that operate consistently across diverse platforms.

The media and web module have been removed due to missing dependencies.

%package devel
Summary:        OpenJFX development tools and libraries
Requires:       %{javaname}-devel
Requires:       %{name} = %{version}-%{release}

%description devel
%{summary}.

%package src
Summary:        OpenJFX Source Bundle
Requires:       %{name} = %{version}-%{release}

%description src
%{summary}.

%package javadoc
Summary:        Javadoc for %{name}
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
install -d -m 755 %{buildroot}%{openjdk8_install_dir}
cp -a build/sdk/{bin,lib} %{buildroot}%{openjdk8_install_dir}
%fdupes -s %{buildroot}%{openjdk8_install_dir}/bin

install -d -m 755 %{buildroot}%{openjdk8_install_dir}/jre
cp -a build/sdk/rt/* %{buildroot}%{openjdk8_install_dir}/jre

install -d -m 755 %{buildroot}%{openjdk8_install_dir}/man/man1
install -m 644 build/sdk/man/man1/* %{buildroot}%{openjdk8_install_dir}/man/man1/

install -d -m 755 %{buildroot}%{openjdk8_install_dir}/man/ja_JP/man1
install -m 644 build/sdk/man/ja_JP.UTF-8/man1/* %{buildroot}%{openjdk8_install_dir}/man/ja_JP/man1

install -m 644 build/sdk/javafx-src.zip %{buildroot}%{openjdk8_install_dir}/javafx-src.zip

install -d 755 %{buildroot}%{_javadocdir}/%{name}
cp -a build/sdk/docs/api/. %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/javapackager
mkdir -p %{buildroot}%{_bindir}
ln -sf %{_sysconfdir}/alternatives/javapackager %{buildroot}%{_bindir}/javapackager

%post devel
ext=.gz
update-alternatives \
  --install %{_bindir}/javapackager javapackager %{openjdk8_install_dir}/bin/javapackager %{priority}

%postun devel
if [ $1 -eq 0 ]
then
  update-alternatives --remove javapackager %{openjdk8_install_dir}/bin/javapackager
fi

%files
%dir %{openjdk8_install_dir}
%{openjdk8_install_dir}/jre
%license LICENSE
%doc README

%files devel
%dir %{openjdk8_install_dir}/man
%dir %{openjdk8_install_dir}/man/man1
%dir %{openjdk8_install_dir}/man/ja_JP
%dir %{openjdk8_install_dir}/man/ja_JP/man1
%ghost %{_sysconfdir}/alternatives/javapackager
%{_bindir}/javapackager
%{openjdk8_install_dir}/lib
%{openjdk8_install_dir}/bin
%{openjdk8_install_dir}/man/man1/javafxpackager.1*
%{openjdk8_install_dir}/man/man1/javapackager.1*
%{openjdk8_install_dir}/man/ja_JP/man1/javafxpackager.1*
%{openjdk8_install_dir}/man/ja_JP/man1/javapackager.1*
%license LICENSE
%doc README

%files src
%{openjdk8_install_dir}/javafx-src.zip

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
