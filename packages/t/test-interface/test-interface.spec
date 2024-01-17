#
# spec file for package test-interface
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


%global test_interface_version 1.0
Name:           test-interface
Version:        %{test_interface_version}
Release:        0
Summary:        Uniform interface to Scala and Java test frameworks
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/sbt/test-interface
Source0:        https://github.com/sbt/test-interface/archive/v%{test_interface_version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/scala-sbt/%{name}/%{version}/%{name}-%{version}.pom
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildArch:      noarch

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

%build
mkdir -p classes target/api
%javac -source 8 -target 8 -d classes $(find src/main/java -name "*.java")

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

%{javadoc} -source 8 -d target/api -classpath $PWD/target/%{name}.jar $(find src/main/java -name "*.java")

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{name}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
