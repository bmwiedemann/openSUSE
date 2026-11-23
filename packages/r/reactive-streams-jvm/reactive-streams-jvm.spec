#
# spec file for package reactive-streams-jvm
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


Name:           reactive-streams-jvm
Version:        1.0.4
Release:        0
Summary:        Reactive Streams Specification for the JVM
License:        MIT-0
Group:          Development/Libraries/Java
URL:            https://www.reactive-streams.org/
Source0:        https://github.com/reactive-streams/%{name}/archive/refs/tags/v%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/reactivestreams/reactive-streams/%{version}/reactive-streams-%{version}.pom
Source2:        https://repo1.maven.org/maven2/org/reactivestreams/reactive-streams-tck/%{version}/reactive-streams-tck-%{version}.pom
Source3:        https://repo1.maven.org/maven2/org/reactivestreams/reactive-streams-tck-flow/%{version}/reactive-streams-tck-flow-%{version}.pom
Source4:        https://repo1.maven.org/maven2/org/reactivestreams/reactive-streams-examples/%{version}/reactive-streams-examples-%{version}.pom
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.testng:testng)
BuildArch:      noarch

%description
The purpose of Reactive Streams is to provide a standard for asynchronous
stream processing with non-blocking backpressure.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q

sed -i -e 's/\r//' README.md

mv api/src/main/java9/org/reactivestreams/FlowAdapters.java api/src/main/java/org/reactivestreams/FlowAdapters.java

cat >pom.xml <<__POM__
<project
		xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd"
		xmlns="http://maven.apache.org/POM/4.0.0"
		xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	>
	<modelVersion>4.0.0</modelVersion>
	<groupId>org.reactivestreams</groupId>
	<artifactId>reactive-streams-parent</artifactId>
	<version>%{version}</version>
	<packaging>pom</packaging>
	<modules>
		<module>api</module>
		<module>examples</module>
		<module>tck</module>
		<module>tck-flow</module>
	</modules>
</project>
__POM__

cp %{SOURCE1} api/pom.xml
cp %{SOURCE2} tck/pom.xml
cp %{SOURCE3} tck-flow/pom.xml
cp %{SOURCE4} examples/pom.xml

%pom_xpath_inject pom:project \
'<parent>
	<groupId>org.reactivestreams</groupId>
	<artifactId>reactive-streams-parent</artifactId>
	<version>%{version}</version>
</parent>' api examples tck{,-flow}

%pom_remove_dep org.reactivestreams:reactive-streams examples tck
%pom_add_dep org.reactivestreams:reactive-streams:%{version} examples tck
%pom_remove_dep org.reactivestreams:reactive-streams-examples tck
%pom_add_dep org.reactivestreams:reactive-streams-examples:%{version} tck

%{mvn_file} :{*} reactive-streams/@1

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE
%doc {README,RELEASE-NOTES,CONTRIBUTING}.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
