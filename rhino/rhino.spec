#
# spec file for package rhino
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2000-2009, JPackage Project
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


%define cvs_version     1_7R3
Name:           rhino
Version:        1.7R3
Release:        0
Summary:        JavaScript for Java
License:        MPL-1.1 OR GPL-2.0-or-later
Group:          Development/Libraries/Java
Url:            http://www.mozilla.org/rhino/
# wget ftp://ftp.mozilla.org/pub/mozilla.org/js/rhino%{cvs_version}.zip
# unzip -q rhino%{cvs_version}.zip
# find rhino%{cvs_version}/ -name '*jar' | xargs rm -rf
# tar -czf rhino%{cvs_version}-suse.tar.gz rhino%{cvs_version}/
Source0:        rhino%{cvs_version}-suse.tar.gz
Source2:        rhino.script
Source3:        rhino-debugger.script
Source4:        rhino-idswitch.script
Source5:        rhino-jsc.script
Source6:        rhino-js.pom
Source7:        rhino.pom
Source8:        rhino-component-info.xml
Patch0:         rhino-build.patch
# Add OSGi metadata from Eclipse Orbit project
# Rip out of MANIFEST.MF included in this JAR:
# http://www.eclipse.org/downloads/download.php?r=1&file=/tools/orbit/downloads/drops/R20110523182458/repository/plugins/org.mozilla.javascript_1.7.2.v201005080400.jar
Patch1:         %{name}-addOrbitManifest.patch
Patch2:         %{name}-1.7R3-crosslink.patch
Patch3:         rhino-288467.patch
#PATCH-FIX-OPENSUSE: allow build under gcj
Patch100:       rhino-1.7-gcj.patch
BuildRequires:  ant
BuildRequires:  bea-stax-api
BuildRequires:  java-devel >= 1.6
BuildRequires:  javapackages-local
BuildRequires:  xmlbeans-mini
#!BuildIgnore:  antlr
#!BuildIgnore:  antlr-java
#!BuildIgnore:  xerces-j2
#!BuildIgnore:  xerces-j2-bootstrap
#!BuildIgnore:  xml-commons
#!BuildIgnore:  xml-commons-apis
#!BuildIgnore:  xml-commons-jaxp-1.3-apis
#!BuildIgnore:  xml-commons-resolver
Requires:       bea-stax-api
Requires:       jline1
Requires:       xmlbeans
BuildArch:      noarch

%description
Rhino is an open-source implementation of JavaScript written entirely
in Java. It is typically embedded into Java applications to provide
scripting to end users.

%package demo
Summary:        JavaScript for Java
Group:          Development/Libraries/Java

%description demo
Rhino is an open-source implementation of JavaScript written entirely
in Java. It is typically embedded into Java applications to provide
scripting to end users.

%prep
# % setup -q -n %{name}%{cvs_version} -a 100
%setup -q -n %{name}%{cvs_version}

# Fix build
sed -i -e '/.*<get.*src=.*>$/d' build.xml testsrc/build.xml \
       toolsrc/org/mozilla/javascript/tools/debugger/build.xml xmlimplsrc/build.xml

# Fix manifest
sed -i -e '/^Class-Path:.*$/d' src/manifest

# Add jpp release info to version
sed -i -e 's|^implementation.version: Rhino .* release .* \${implementation.date}|implementation.version: Rhino %{version} release %{release} \${implementation.date}|' build.properties

%setup -q -n %{name}%{cvs_version}
%patch0  -b .build
%patch1 -p1 -b .fixManifest
%patch2 -p1 -b .crosslink
%patch3  -b .sav3
%patch100  -b .gjc

%build
%{ant} \
    -Dxbean.jar=$(build-classpath xmlbeans/xbean | cut -d ':' -f 1) \
    -Djsr173.jar=$(build-classpath bea-stax-api) \
    -Dtarget-jvm=6 -Dsource-level=6 \
    deepclean jar copy-all

export CLASSPATH=`pwd`/build/%{name}%{cvs_version}/js.jar:$(build-classpath xmlbeans/xbean 2>/dev/null)
SOURCEPATH=`pwd`/build/%{name}%{cvs_version}/src
pushd examples
javac -sourcepath ${SOURCEPATH} -source 6 -target 6 *.java
jar cvf ../build/%{name}%{cvs_version}/%{name}-examples.jar *.class
popd

%install

# jars
mkdir -p %{buildroot}%{_javadir}
cp -a build/%{name}%{cvs_version}/js.jar %{buildroot}%{_javadir}
ln -s js.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
mkdir -p %{buildroot}%{_mavenpomdir}
cp -a %{SOURCE6} %{buildroot}%{_mavenpomdir}/js.pom
%add_maven_depmap js.pom js.jar -a "org.mozilla:rhino"

# scripts
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}
install -m 0755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}-debugger
install -m 0755 %{SOURCE4} %{buildroot}%{_bindir}/%{name}-idswitch
install -m 0755 %{SOURCE5} %{buildroot}%{_bindir}/%{name}-jsc

# examples
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -a examples/* %{buildroot}%{_datadir}/%{name}
cp -a build/%{name}%{cvs_version}/%{name}-examples.jar %{buildroot}%{_javadir}/%{name}-examples.jar

%files
%doc LICENSE.txt
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}-debugger
%attr(0755,root,root) %{_bindir}/%{name}-idswitch
%attr(0755,root,root) %{_bindir}/%{name}-jsc
%{_javadir}/*.jar
%{_mavenpomdir}/*.pom
%if %{defined _maven_repository}
%config(noreplace) %{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml
%endif

%files demo
%{_datadir}/%{name}

%changelog
