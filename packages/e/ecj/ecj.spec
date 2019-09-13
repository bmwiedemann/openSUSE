#
# spec file for package ecj
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global qualifier R-4.4-201406061215
Name:           ecj
Version:        4.4.0
Release:        0
Summary:        Eclipse Compiler for Java
License:        EPL-1.0
Group:          Development/Languages/Java
Url:            http://www.eclipse.org
Source0:        http://download.eclipse.org/eclipse/downloads/drops4/%{qualifier}/%{name}src-4.4.jar
Source1:        ecj.sh.in
# Use ECJ for GCJ
# cvs -d:pserver:anonymous@sourceware.org:/cvs/rhug \
# export -D 2009-09-28 eclipse-gcj
# tar cjf ecj-gcj.tar.bz2 eclipse-gcj
Source2:        %{name}-gcj.tar.bz2
#Patched from http://central.maven.org/maven2/org/eclipse/jdt/core/compiler/ecj/4.4/ecj-4.4.pom
# No dependencies are needed for ecj, dependencies are for using of jdt.core which makes no sense outside of eclipse
Source3:        ecj-4.4.pom
Source4:        ecj.1
# http://git.eclipse.org/c/jdt/eclipse.jdt.core.git/plain/org.eclipse.jdt.core/scripts/binary/META-INF/MANIFEST.MF
Source5:        META-INF/MANIFEST.MF
# Always generate debug info when building RPMs (Andrew Haley)
Patch0:         %{name}-rpmdebuginfo.patch
# build.xml fails to include a necessary .props file in the built ecj.jar
Patch1:         %{name}-include-props.patch
# Patches Source2 for compatibility with newer ecj
Patch2:         eclipse-gcj-compat4.2.1.patch
Patch3:         eclipse-gcj-nodummysymbol.patch
BuildRequires:  ant
BuildRequires:  gzip
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  unzip
Conflicts:      ecj-bootstrap
Provides:       eclipse-ecj = %{version}-%{release}
Obsoletes:      eclipse-ecj < 3.4.2-4
BuildArch:      noarch

%description
ECJ is the Java bytecode compiler of the Eclipse Platform.  It is also known as
the JDT Core batch compiler.

%prep
%setup -q -c
%patch0 -p1
%patch1 -b .sav

sed -i -e 's|debuglevel=\"lines,source\"|debug=\"yes\"|g' build.xml
sed -i -e "s/Xlint:none/Xlint:none -encoding cp1252/g" build.xml

%if 0%{?suse_version} < 1200
sed -i -e 's|source=\"1.6\"|source=\"1.5\"|g' build.xml
sed -i -e 's|target=\"1.6\"|target=\"1.5\"|g' build.xml
%endif

cp %{SOURCE3} pom.xml
mkdir -p scripts/binary/META-INF/
cp %{SOURCE5} scripts/binary/META-INF/MANIFEST.MF

# Use ECJ for GCJ's bytecode compiler
tar jxf %{SOURCE2}
mv eclipse-gcj/org/eclipse/jdt/internal/compiler/batch/GCCMain.java \
  org/eclipse/jdt/internal/compiler/batch/
%patch2 -p1
%patch3 -p1
cat eclipse-gcj/gcc.properties >> \
  org/eclipse/jdt/internal/compiler/batch/messages.properties
rm -rf eclipse-gcj

# Remove bits of JDT Core we don't want to build
rm -r org/eclipse/jdt/internal/compiler/tool
rm -r org/eclipse/jdt/internal/compiler/apt
rm -f org/eclipse/jdt/core/BuildJarIndex.java

# JDTCompilerAdapter isn't used by the batch compiler
rm -f org/eclipse/jdt/core/JDTCompilerAdapter.java
cp %{SOURCE4} ecj.1

%build
ant
gzip ecj.1

%install
mkdir -p %{buildroot}%{_javadir}
install -m0644 ecj.jar %{buildroot}%{_javadir}/%{name}.jar
pushd %{buildroot}%{_javadir}
ln -s %{name}.jar eclipse-%{name}.jar
ln -s %{name}.jar jdtcore.jar
popd

# Install the ecj wrapper script
install -p -D -m0755 %{SOURCE1} %{buildroot}%{_bindir}/ecj
sed --in-place "s:@JAVADIR@:%{_javadir}:" %{buildroot}%{_bindir}/ecj

# Install manpage
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 -p ecj.1.gz %{buildroot}%{_mandir}/man1/ecj.1.gz

# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml \
    %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom

%add_maven_depmap -a "org.eclipse.tycho:org.eclipse.jdt.core,org.eclipse.tycho:org.eclipse.jdt.compiler.apt,org.eclipse.jdt:core,org.eclipse.jdt:org.eclipse.jdt.core,org.eclipse.jdt.core.compiler:ecj,org.eclipse.jdt:ecj" JPP-%{name}.pom %{name}.jar

%files -f .mfiles
%doc about.html
%{_mavenpomdir}/JPP-%{name}.pom
%{_bindir}/%{name}
%{_javadir}/%{name}.jar
%{_javadir}/eclipse-%{name}.jar
%{_javadir}/jdtcore.jar
%{_mandir}/man1/ecj.1%{ext_man}

%changelog
