#
# spec file for package ecj
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global qualifier R-4.12-201906051800
%global jdk10_revision 45b1d041a4ef
Name:           ecj
Version:        4.12
Release:        0
Summary:        Eclipse Compiler for Java
License:        EPL-2.0 AND GPL-2.0 WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org
Source0:        http://download.eclipse.org/eclipse/downloads/drops4/%{qualifier}/ecjsrc-%{version}.jar
# Jdk10 sources to build Java API stubs for newer JDKs
# wget http://hg.openjdk.java.net/jdk-updates/jdk10u/archive/45b1d041a4ef.tar.bz2 -O jdk10u.tar.bz2
# tar xf jdk10u.tar.bz2 && rm jdk10u.tar.bz2
# mv jdk10u-45b1d041a4ef/src/java.compiler/share/classes java10api-src && rm -rf jdk10u-45b1d041a4ef
# tar cJf java10api-src.tar.xz java10api-src && rm -rf java10api-src
Source1:        java10api-src.tar.xz
Source2:        https://repo1.maven.org/maven2/org/eclipse/jdt/ecj/3.18.0/ecj-3.18.0.pom
# Simple pom file to declare org.eclipse:java10api artifact
Source3:        java10api.pom
# Extracted from https://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/%%{qualifier}/ecj-%%{version}.jar
Source4:        MANIFEST.MF
# Always generate debug info when building RPMs
Patch0:         %{name}-rpmdebuginfo.patch
# Include java API stubs in build with java < 9
Patch1:         javaAPI.patch
# Fix build with java >= 9
Patch2:         ecj-encoding.patch
# Patch out deprecation annotation not understood by java 8
Patch3:         jdk10u-jdk8compat.patch
BuildRequires:  ant
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  unzip
BuildArch:      noarch

%description
ECJ is the Java bytecode compiler of the Eclipse Platform.  It is also known as
the JDT Core batch compiler.

%prep
%setup -q -c -a 1
%patch0 -p1
%if %{?pkg_vcmp:%pkg_vcmp java-devel < 9}%{!?pkg_vcmp:1}
%patch1
%else
%patch2 -p1
%endif
%patch3

sed -i -e 's|debuglevel=\"lines,source\"|debug=\"yes\"|g' build.xml

mkdir -p scripts/binary/META-INF/
cp %{SOURCE4} scripts/binary/META-INF/MANIFEST.MF

# JDTCompilerAdapter isn't used by the batch compiler
rm -f org/eclipse/jdt/core/JDTCompilerAdapter.java

# Not compatible with non-modular Java
%if %{?pkg_vcmp:%pkg_vcmp java-devel < 9}%{!?pkg_vcmp:1}
rm -f java10api-src/javax/tools/ToolProvider.java
%endif

%build

mkdir -p build/classes
javac -d build/classes -source 8 -target 8 \
  $(find java10api-src/javax -name \*.java | xargs)
jar -cf java10api.jar -C build/classes .
# Remove everything except the jar, since ant looks for java files in "."
rm -rf java10api-src build/classes

ant \
%if %{?pkg_vcmp:%pkg_vcmp java-devel < 9}%{!?pkg_vcmp:1}
	-Djavaapi=java10api.jar -Drtjar=%{_jvmdir}/jre/lib/rt.jar \
%endif
	build

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 ecj.jar %{buildroot}%{_javadir}/%{name}/ecj.jar
install -pm 0644 java10api.jar %{buildroot}%{_javadir}/%{name}/java10api.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{name}/ecj.pom
%add_maven_depmap %{name}/ecj.pom %{name}/ecj.jar -a "org.eclipse.jdt:core,org.eclipse.jdt.core.compiler:ecj,org.eclipse.tycho:org.eclipse.jdt.core,org.eclipse.tycho:org.eclipse.jdt.compiler.apt"
install -pm 0644 %{SOURCE3} %{buildroot}%{_mavenpomdir}/%{name}/java10api.pom
%add_maven_depmap %{name}/java10api.pom %{name}/java10api.jar -a "org.eclipse:java9api"

# Install the ecj wrapper script
%jpackage_script org.eclipse.jdt.internal.compiler.batch.Main '' '' ecj ecj true

# Install manpage
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 -p ecj.1 %{buildroot}%{_mandir}/man1/ecj.1

%files -f .mfiles
%license about.html
%{_bindir}/ecj
%{_mandir}/man1/ecj*

%changelog
