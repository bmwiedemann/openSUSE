#
# spec file for package ecj
#
# Copyright (c) 2022 SUSE LLC
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


%global qualifier R-4.18-202012021800
%global jdk15_revision 1055f2102e6e
Name:           ecj
Version:        4.18
Release:        0
Summary:        Eclipse Compiler for Java
License:        EPL-2.0 AND GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org
Source0:        http://download.eclipse.org/eclipse/downloads/drops4/%{qualifier}/ecjsrc-%{version}.jar
# Jdk15 sources to build Java API stubs for newer JDKs
# wget http://hg.openjdk.java.net/jdk-updates/jdk15u/archive/1055f2102e6e.tar.bz2 -O jdk15u.tar.bz2
# tar xf jdk15u.tar.bz2 && rm jdk15u.tar.bz2
# mv jdk15u-1055f2102e6e/src/java.compiler/share/classes java15api-src && mkdir -p java15api-src/jdk/internal/ && mv jdk15u-1055f2102e6e/src/java.base/share/classes/jdk/internal/PreviewFeature.java java15api-src/jdk/internal/
# rm -rf jdk15u-1055f2102e6e
# tar cJf java15api-src.tar.xz java15api-src && rm -rf java15api-src
Source1:        java15api-src.tar.xz
Source2:        https://repo1.maven.org/maven2/org/eclipse/jdt/ecj/3.24.0/ecj-3.24.0.pom
# Simple pom file to declare org.eclipse:java15api artifact
Source3:        java15api.pom
# Extracted from https://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/%%{qualifier}/ecj-%%{version}.jar
Source4:        MANIFEST.MF
# Always generate debug info when building RPMs
Patch0:         %{name}-rpmdebuginfo.patch
Patch1:         encoding.patch
# Include java API stubs in build with java < 15
Patch2:         javaAPI.patch
BuildRequires:  ant
BuildRequires:  java-devel >= 10
BuildRequires:  javapackages-local
BuildRequires:  unzip
BuildArch:      noarch

%description
ECJ is the Java bytecode compiler of the Eclipse Platform.  It is also known as
the JDT Core batch compiler.

%prep
%setup -q -c -a 1
%patch0 -p1
%patch1 -p1
%if %{?pkg_vcmp:%pkg_vcmp java-devel < 15}%{!?pkg_vcmp:1}
%patch2
%endif

sed -i -e 's|debuglevel=\"lines,source\"|debug=\"yes\"|g' build.xml

mkdir -p scripts/binary/META-INF/
cp %{SOURCE4} scripts/binary/META-INF/MANIFEST.MF

# JDTCompilerAdapter isn't used by the batch compiler
rm -f org/eclipse/jdt/core/JDTCompilerAdapter.java

# Cannot sign jar file with eclipse key
rm META-INF/ECLIPSE_*

%build

mkdir -p build/classes
javac --patch-module java.compiler=java15api-src -XDignore.symbol.file=true -d build/classes --release 10 \
  $(find java15api-src/javax -name \*.java | xargs)
jar -cf java15api.jar -C build/classes .
# Remove everything except the jar, since ant looks for java files in "."
rm -rf java15api-src build/classes

%ant \
%if %{?pkg_vcmp:%pkg_vcmp java-devel < 15}%{!?pkg_vcmp:1}
	-Djavaapi=java15api.jar \
%endif
	build

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 ecj.jar %{buildroot}%{_javadir}/%{name}/ecj.jar
install -pm 0644 java15api.jar %{buildroot}%{_javadir}/%{name}/java15api.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{name}/ecj.pom
%add_maven_depmap %{name}/ecj.pom %{name}/ecj.jar -a "org.eclipse.jdt:core,org.eclipse.jdt.core.compiler:ecj,org.eclipse.tycho:org.eclipse.jdt.core,org.eclipse.tycho:org.eclipse.jdt.compiler.apt"
%add_maven_depmap org.eclipse:java15api:15 %{name}/java15api.jar -a "org.eclipse:java9api,org.eclipse:java10api"

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
