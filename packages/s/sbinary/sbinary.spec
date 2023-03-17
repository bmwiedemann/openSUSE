#
# spec file for package sbinary
#
# Copyright (c) 2023 SUSE LLC
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


%global sbinary_version 0.4.2
%global scala_version 2.10
%global scala_long_version 2.10.6
%global build_with_sbt 0
%global want_scalacheck 0
Name:           sbinary
Version:        %{sbinary_version}
Release:        0
Summary:        Library for describing binary formats for Scala types
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/harrah/sbinary
Source0:        https://github.com/harrah/sbinary/archive/v%{sbinary_version}.tar.gz
Source1:        https://raw.github.com/willb/climbing-nemesis/master/climbing-nemesis.py
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  scala >= 2.10.7
BuildRequires:  mvn(net.sourceforge.fmpp:fmpp)
BuildRequires:  mvn(org.beanshell:bsh)
BuildRequires:  mvn(org.freemarker:freemarker)
BuildRequires:  mvn(xml-resolver:xml-resolver)
BuildConflicts: java < 1.8
BuildConflicts: java-devel < 1.8
BuildConflicts: java-headless < 1.8
Requires:       javapackages-tools
Requires:       scala
BuildArch:      noarch
%if %{build_with_sbt}
BuildRequires:  python
BuildRequires:  sbt
%endif

%description

SBinary is a library for describing binary protocols, in the form of
mappings between Scala types and binary formats. It can be used as a
robust serialization mechanism for Scala objects or a way of dealing
with existing binary formats found in the wild.

It started out life as a loose port of Haskell's Data.Binary. It's
since evolved a bit from there to take advantage of the features Scala
implicits offer over Haskell type classes, but the core idea has
remained the same.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q

%if %{build_with_sbt}
sed -i -e 's/2[.]10[.]2/2.10.6/g' project/SBinaryProject.scala

sed -i -e 's|"scalacheck" % "1[.]10[.]0"|"scalacheck" % "1.11.0"|g' project/SBinaryProject.scala
sed -i -e 's|[.]identity||g' project/SBinaryProject.scala
sed -i -e 's/0[.]13[.]0/0.13.1/g' project/build.properties || echo sbt.version=0.13.1 > project/build.properties

cp -r %{_datadir}/java/sbt/ivy-local .
mkdir boot

cp %{SOURCE1} .

chmod 755 climbing-nemesis.py

%if %{want_scalacheck}
./climbing-nemesis.py --jarfile %{_datadir}/java/scalacheck.jar org.scalacheck scalacheck ivy-local --version 1.11.0 --scala %{scala_version}
%endif

./climbing-nemesis.py net.sourceforge.fmpp fmpp ivy-local
./climbing-nemesis.py org.freemarker freemarker ivy-local
./climbing-nemesis.py org.beanshell bsh ivy-local --override org.beanshell:bsh
./climbing-nemesis.py xml-resolver xml-resolver ivy-local
%endif

%build

%if %{build_with_sbt}

export SBT_BOOT_DIR=boot
export SBT_IVY_DIR=ivy-local
sbt package deliverLocal publishM2Configuration

%else # build without sbt

mkdir -p core/target/scala-%{scala_version}/src_managed
mkdir -p core/target/scala-%{scala_version}/classes
mkdir -p core/target/scala-%{scala_version}/api

java -cp $(build-classpath fmpp freemarker bsh2 oro) fmpp.tools.CommandLine -S core/src -O core/target/scala-%{scala_version}/src_managed

scalac \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-nobootcp \
%endif
	core/target/scala-%{scala_version}/src_managed/*.scala -d core/target/scala-%{scala_version}/classes
jar -cvf core/target/scala-%{scala_version}/%{name}_%{scala_version}-%{version}.jar -C core/target/scala-%{scala_version}/classes .

scaladoc \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-nobootcp \
%endif
	core/target/scala-2.10/src_managed/*.scala -d core/target/scala-2.10/api

cat << EOF > core/target/scala-%{scala_version}/%{name}_%{scala_version}-%{version}.pom
<?xml version='1.0' encoding='UTF-8'?>
<project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://maven.apache.org/POM/4.0.0">
    <modelVersion>4.0.0</modelVersion>
    <groupId>org.scala-tools.sbinary</groupId>
    <artifactId>sbinary_%{scala_version}</artifactId>
    <packaging>jar</packaging>
    <description>SBinary</description>
    <version>%{version}</version>
    <name>SBinary</name>
    <organization>
        <name>org.scala-tools.sbinary</name>
    </organization>
    <dependencies>
        <dependency>
            <groupId>org.scala-lang</groupId>
            <artifactId>scala-library</artifactId>
            <version>%{scala_long_version}</version>
        </dependency>
    </dependencies>
</project>
EOF

%endif

%install
mkdir -p %{buildroot}/%{_javadir}
mkdir -p %{buildroot}/%{_mavenpomdir}

mkdir -p %{buildroot}/%{_javadocdir}/%{name}

install -pm 644 core/target/scala-%{scala_version}/%{name}_%{scala_version}-%{version}.jar %{buildroot}/%{_javadir}/%{name}.jar
install -pm 644 core/target/scala-%{scala_version}/%{name}_%{scala_version}-%{version}.pom %{buildroot}/%{_mavenpomdir}/JPP-%{name}.pom

cp -rp core/target/scala-%{scala_version}/api/* %{buildroot}/%{_javadocdir}/%{name}
%fdupes -s %{buildroot}/%{_javadocdir}/%{name}

%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files -f .mfiles
%license LICENSE
%doc README

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
