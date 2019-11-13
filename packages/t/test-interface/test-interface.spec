#
# spec file for package test-interface
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


%global test_interface_version 1.0
%global build_with_sbt 0
Name:           test-interface
Version:        %{test_interface_version}
Release:        0
Summary:        Uniform interface to Scala and Java test frameworks
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/sbt/test-interface
Source0:        https://github.com/sbt/test-interface/archive/v%{test_interface_version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildArch:      noarch
%if ! %{build_with_sbt}
Source1:        http://central.maven.org/maven2/org/scala-sbt/%{name}/%{version}/%{name}-%{version}.pom
%endif
%if %{build_with_sbt}
BuildRequires:  sbt
%else
BuildRequires:  java-devel
%endif

%description

Uniform test interface to Scala/Java test frameworks (specs,
ScalaCheck, ScalaTest, JUnit and other)

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
%{mvn_file} org.scala-sbt:test-interface %{name}

%if %{build_with_sbt}
sed -i -e 's/2[.]10[.]2/2.10.3/g' build.sbt
sed -i -e '/scalatest_2.10/d' build.sbt

sed -i -e 's/0[.]12[.]4/0.13.1/g' project/build.properties
rm project/plugins.sbt

cp -r %{_datadir}/java/sbt/ivy-local .
mkdir boot
%else # building without sbt

cp -p %{SOURCE1} pom.xml
# Remove unavailable test dep
%pom_remove_dep :scalatest_2.10

%endif

%build

%if %{build_with_sbt}
export SBT_BOOT_DIR=boot
export SBT_IVY_DIR=ivy-local
sbt package deliverLocal publishM2Configuration
%else # building without sbt
mkdir -p classes target/api
%javac -source 6 -target 6 -d classes $(find src/main/java -name "*.java")

(
cd classes
mkdir -p META-INF
cat > META-INF/MANIFEST.MF << 'EOF'
Manifest-Version: 1.0
Implementation-Vendor: org.scala-sbt
Implementation-Title: %{name}
Implementation-Version: %{version}
Implementation-Vendor-Id: org.scala-sbt
Specification-Vendor: org.scala-sbt
Specification-Title: %{name}
Specification-Version: %{version}
EOF
%jar -cMf ../target/%{name}.jar *
)

%{javadoc} -source 6 -d target/api -classpath $PWD/target/%{name}.jar $(find src/main/java -name "*.java")

cp pom.xml target/%{name}-%{version}.pom

%{mvn_artifact} target/%{name}-%{version}.pom target/%{name}.jar

%endif

%install

%mvn_install -J target/api
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
