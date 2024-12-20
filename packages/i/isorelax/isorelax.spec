#
# spec file for package isorelax
#
# Copyright (c) 2024 SUSE LLC
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


%define	cvsversion	20041111
Name:           isorelax
Version:        0.1
Release:        0
Summary:        Public interfaces useful for applications to support RELAX Core
License:        Apache-2.0 AND MIT
Group:          Development/Libraries/Java
URL:            https://iso-relax.sourceforge.net/
Source0:        %{name}.%{cvsversion}.zip
Source1:        %{name}-build.xml
Source2:        isorelax-maven-project.xml
Source3:        isorelax-maven-project.xsd
Source4:        https://repo1.maven.org/maven2/%{name}/%{name}/20030108/%{name}-20030108.pom
Patch0:         isorelax-java5-compatibility.patch
BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  unzip
BuildRequires:  xerces-j2
BuildRequires:  xml-apis
Requires:       xerces-j2
Requires:       xml-apis
Obsoletes:      isorelax-bootstrap
Provides:       isorelax-bootstrap
Obsoletes:      %{name}-javadoc
BuildArch:      noarch

%description
The ISO RELAX project is started to host the public interfaces useful
for applications to support RELAX Core. But nowadays some of the stuff
we have is schema language neutral.

%prep
%setup -q -T -c
unzip -q %{SOURCE0}
mkdir src
(cd src; unzip -q ../src.zip)
rm -f src.zip
cp %{SOURCE1} build.xml
mkdir test
cp %{SOURCE2} test
cp %{SOURCE3} test
chmod -R go=u-w *
find . -name "*.jar" -exec rm -f {} \;
rm -rf src/jp/gr/xml/relax/swift
%patch -P 0 -b .sav0

%build
export CLASSPATH=$(build-classpath \
xerces-j2 \
xml-apis \
)
ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 \
    -Dbuild.sysclasspath=only release

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 %{name}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE4} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

%files -f .mfiles
%license COPYING.txt

%changelog
