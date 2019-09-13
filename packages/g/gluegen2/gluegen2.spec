#
# spec file for package gluegen2
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define src_name gluegen-v%{version}
%define jcppsrc_name jcpp-v%{version}
%global gluegen_devel_dir %{_datadir}/%{name}
%global inst_srcdir %{buildroot}%{gluegen_devel_dir}
Name:           gluegen2
Version:        2.3.2
Release:        0
Summary:        Tool for automatic generation the Java and JNI code
License:        BSD-2-Clause
Group:          Development/Libraries/Java
Url:            http://jogamp.org/gluegen/www/
Source0:        http://jogamp.org/deployment/v%{version}/archive/Sources/%{src_name}.tar.xz
Source1:        http://jogamp.org/deployment/v%{version}/archive/Sources/%{jcppsrc_name}.tar.xz
Patch0:         gluegen2-jar-paths.patch
Patch1:         gluegen2-0001-renamed-library.patch
Patch2:         gluegen2-0003-disable-executable-tmp-tests.patch
Patch3:         gluegen2-0004-add-antlr-jar-to-all-targets.patch
# FIXME: Disable all junit tests because it requires packages not yet packaged in obs
# PATCH-FIX-OPENSUSE gluegen2-disable-tests.patch badshah400@gmail.com -- Remove junit tests from the "all" targets as this requires additional dependencies (jardiff)
Patch5:         gluegen2-disable-tests.patch
Patch6:         gluegen2-add-ppc64-aarch64.patch
# PATCH-FIX-UPSTREAM gluegen2-no-static-libstdc++.patch badshah400@gmail.com -- Do not use -static-libstdc++ option for linker, causes build failures
Patch7:         gluegen2-no-static-libstdc++.patch
Patch8:         gluegen2-0001-Remove-version-overrides-for-memcpy.patch
Patch9:         gluegen2-jdk9.patch
Patch10:        gluegen2-jdk10.patch
BuildRequires:  ant >= 1.9.8
BuildRequires:  ant-antlr
BuildRequires:  ant-contrib
BuildRequires:  ant-findbugs
BuildRequires:  ant-junit
BuildRequires:  cpptasks
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
Requires:       java

%description
GlueGen is a tool which automatically generates the Java and JNI code
necessary to call C libraries. It reads as input ANSI C header files and
separate configuration files which provide control over many aspects of
the glue code generation. GlueGen uses a complete ANSI C parser and
an internal representation (IR) capable of representing all C types
to represent the APIs for which it generates interfaces. It has
the ability to perform significant transformations on the IR before
glue code emission. GlueGen is currently powerful enough to bind even
low-level APIs such as the Java Native Interface (JNI) and
the AWT Native Interface (JAWT) back up to the Java programming language.

%package devel
Summary:        Tool for automatic generation the Java and JNI code
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}
Requires:       ant-antlr
Requires:       ant-contrib
Requires:       ant-junit
Requires:       cpptasks
BuildArch:      noarch

%description devel
This package contains gluegen source code needed to build packages.

%prep
%setup -q -n %{jcppsrc_name} -T -b 1
%setup -q -n %{src_name} -T -b 0
cp -pr ../%{jcppsrc_name}/src ./jcpp/
rm -rf src/java/net/highteq/nativetaglet/

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

# Fix wrong-script-end-of-line-encoding
rm make/scripts/*.bat

# Fix spurious-executable-perm
chmod -x LICENSE.txt
chmod -x doc/manual/index.html

#chmod -x make/stub_includes/*/*
find make/stub_includes/ -type f -print -exec chmod -x {} \;
find make/stub_includes/ -type d -print -exec chmod +x {} \;

#chmod -x src/native/*/*
find src/native/ -type f -print -exec chmod -x {} \;
find src/native/ -type f -print -exec chmod +x {} \;

find src/java/ -type f -exec chmod -x {} \;
find make/scripts -type f -not -name "*.sh" -print -exec chmod -x {} \;

# Fix non-executable-script
find make/scripts -type f -name "*.sh" -print -exec chmod +x {} \;

# Fix script-without-shebang
find make/scripts -type f -name "*.sh" -print -exec sed -i -e '1i#!/bin/sh' {} \;

# Remove bundled dependencies
find -name "*.jar" -type f -print -exec rm {} \;
find -name "*.apk" -type f -print -exec rm {} \;
rm -fr make/lib

# Remove hardcoded classpath
sed -i '/Class-Path/I d' make/Manifest

# git executable should not be used, use true (to avoid checkout) instead
sed -i 's/executable="git"/executable="true"/' make/build.xml

# 7z executable is not provided, use true (to avoid archive) instead
sed -i 's/executable="7z"/executable="true"/' make/jogamp-archivetasks.xml

# mvn executable should not be used, use true (to avoid install) instead
sed -i 's/executable="mvn"/executable="true"/' make/build.xml

%build
cd make
ant -Djava.version=1.8 -Dant.java.version=1.8 \
    -Djavacdebug=true \
    -Djavacdebuglevel=lines,vars,source \
    -Dc.compiler.debug=true \
    all

%install
# arch independent jars
install -Dm 644 build/gluegen.jar %{buildroot}%{_javadir}/%{name}.jar
install -Dm 644 build/gluegen-rt.jar %{buildroot}%{_javadir}/%{name}-rt.jar
# arch specific jars
install -Dm 644 build/gluegen-rt-natives-*.jar %{buildroot}%{_jnidir}/%{name}-rt-natives.jar
# native libraries
install -Dm 755 build/obj/libgluegen-rt.so %{buildroot}%{_libdir}/lib%{name}-rt.so

# source code
mkdir -p %{inst_srcdir} %{inst_srcdir}/build
cp -rdf -t %{inst_srcdir} make
find %{inst_srcdir} -name '*.orig' -type f -delete -print
cp build/artifact.properties %{inst_srcdir}/build/artifact.properties

# Fix spurious executable perms
chmod -x %{buildroot}%{_datadir}/%{name}/make/*.xml
chmod -x %{buildroot}%{_datadir}/%{name}/make/*.cfg
chmod -x %{buildroot}%{_datadir}/%{name}/make/Manifest*
chmod -x %{buildroot}%{_datadir}/%{name}/make/gluegen.properties

%files
%doc LICENSE.txt
%{_javadir}/%{name}-rt.jar
%{_jnidir}/%{name}-rt-natives.jar
%{_libdir}/lib%{name}-rt.so

%files devel
%doc LICENSE.txt
%{_javadir}/%{name}.jar
%{gluegen_devel_dir}/

%changelog
