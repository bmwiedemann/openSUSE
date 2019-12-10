#
# spec file for package template-resolver
#
# Copyright (c) 2019 SUSE LLC
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


Name:           template-resolver
Version:        0.1
Release:        0
Summary:        Contract API for template resolvers
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/sbt/template-resolver
Source0:        %{name}-%{version}.tar.xz
Source1:        http://central.maven.org/maven2/org/scala-sbt/%{name}/%{version}/%{name}-%{version}.pom
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
Contract API for template resolvers.

%package javadoc
Summary:        API Documentation for %{name}
Group:          Documentation/HTML

%description javadoc
JavaDoc documentation for %{name}

%prep
%setup -q

%build
# jar
mkdir -p target/classes
javac -d target/classes -source 6 -target 6 $(find src/main -name \*.java | xargs)
jar -cf target/%{name}-%{version}.jar -C target/classes .
# javadoc
mkdir -p target/site/apidocs
javadoc -d target/site/apidocs -source 6 -notimestamp $(find src/main -name \*.java | xargs)
%{mvn_artifact} %{SOURCE1} target/%{name}-%{version}.jar

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README.markdown

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
