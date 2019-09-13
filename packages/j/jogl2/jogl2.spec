#
# spec file for package jogl2
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


%define src_name jogl-v%{version}
Name:           jogl2
Version:        2.3.2
Release:        0
Summary:        Java bindings for the OpenGL API
License:        BSD-2-Clause
Group:          Development/Libraries/Java
Url:            http://jogamp.org/jogl/www/
Source0:        http://jogamp.org/deployment/v%{version}/archive/Sources/%{src_name}.tar.xz
Patch0:         %{name}-0000-update-antlr-ant-contrib-jars.patch
Patch1:         %{name}-0001-update-ant-contrib-tasks.patch
Patch2:         jogl2-disable-tests.patch
Patch3:         jogl2-ppc64.patch
Patch4:         jogl2-getPeer.patch
Patch5:         jogl2-nojavah.patch
BuildRequires:  ant >= 1.9.8
BuildRequires:  ant-contrib
BuildRequires:  eclipse-swt
BuildRequires:  gluegen2-devel = %{version}
BuildRequires:  java-devel >= 1.8
BuildRequires:  jpackage-utils
BuildRequires:  libXcursor-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libXxf86vm-devel
Requires:       gluegen2 = %{version}
Requires:       java
Requires:       jpackage-utils

%description
The JOGL project hosts the development version of the Java Binding for
the OpenGL API, and is designed to provide hardware-supported 3D graphics
to applications written in Java.

JOGL provides full access to the APIs in the OpenGL 1.3 - 3.0, 3.1 - 3.3,
≥ 4.0, ES 1.x and ES 2.x specification as well as nearly all vendor
extensions. OpenGL Evolution & JOGL (UML) gives you a brief overview
of OpenGL, its profiles and how we map them to JOGL.

%prep
%setup -q -n %{src_name}

# Remove bundled dependencies
find -name "*.jar" -type f -print -exec rm {} \;
find -name "*.apk" -type f -print -exec rm {} \;
rm -fr make/lib
# Also remove experimantal applets that requires a bundled jar for building
rm -fr src/newt/classes/com/jogamp/newt/util/applet/JOGLNewtApplet3Run.java
rm -fr src/newt/classes/com/jogamp/newt/util/applet/VersionApplet3.java

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# Fix wrong-script-end-of-line-encoding
rm make/scripts/*.bat

# Fix spurious-executable-perm
chmod -x LICENSE.txt

#
find make/scripts -type f -not -name "*.sh" -print -exec chmod -x {} \;

# Fix non-executable-script
find make/scripts -type f -name "*.sh" -print -exec chmod +x {} \;

# Fix script-without-shebang
find make/scripts -type f -name "*.sh" -print -exec sed -i -e '1i#!/bin/sh' {} \;

# Restore the gluegen2 source code from gluegen2-commons
cp -r %{_datadir}/gluegen2 ../gluegen

# git executable should not be used, use true (to avoid checkout) instead
sed -i 's/executable="git"/executable="true"/' make/build-common.xml

%build
cd make
export CLASSPATH=""
# force cross compilation support to use native root (noop on anything but ARM)
export TARGET_PLATFORM_ROOT=/
ant	-Dcommon.gluegen.build.done=true \
	-Djavacdebug=true \
    -Djavacdebuglevel=lines,vars,source \
    -Dc.compiler.debug=true \
    -Djava.version=1.6 -Dant.java.version=1.6 \
    -Dantlr.jar=$(build-classpath antlr) \
    -Djunit.jar=$(build-classpath junit) \
    -Dant.jar$(build-classpath ant) \
    -Dant-junit.jar=$(build-classpath ant-junit) \
    -Dgluegen.jar=$(build-classpath gluegen2) \
    -Dgluegen-rt.jar=$(build-classpath gluegen2-rt) \
    -Dswt.jar=$(build-classpath swt) \
    -Dcflags_extra.native="%{optflags}" \
    all

%install
mkdir -p %{buildroot}%{_javadir}/%{name} \
    %{buildroot}%{_libdir}/%{name} \
    %{buildroot}%{_jnidir}

install build/jar/jogl-all.jar %{buildroot}%{_jnidir}/%{name}.jar
ln -s ../../..%{_jnidir}/%{name}.jar %{buildroot}%{_libdir}/%{name}/
install -t %{buildroot}%{_libdir}/%{name}/ build/lib/*.so

%files
%doc README.txt LICENSE.txt CHANGELOG.txt
%{_libdir}/%{name}
%{_jnidir}/%{name}.jar

%changelog
