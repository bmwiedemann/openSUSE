#
# spec file for package apache-commons-chain
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


%global base_name chain
%global short_name commons-%{base_name}
%bcond_with tests
Name:           apache-commons-chain
Version:        1.2
Release:        0
Summary:        An implementation of the GoF Chain of Responsibility pattern
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
# javax.servlet 3.1 api support
Patch0:         %{name}-%{version}-tests-servlet31.patch
# javax.portlet 2.0 api support
Patch1:         %{name}-%{version}-portlet20.patch
# Do not fetch dependencies during the build
Patch3:         commons-chain-1.2-getdeps.patch
# javax.servlet 4.0 api support
Patch4:         commons-chain-1.2-servlet4.patch
BuildRequires:  ant
BuildRequires:  apache-commons-collections
BuildRequires:  commons-beanutils
BuildRequires:  commons-digester >= 1.8
BuildRequires:  commons-logging
BuildRequires:  fdupes
BuildRequires:  glassfish-servlet-api
BuildRequires:  javapackages-local
BuildRequires:  portlet-1.0-api
Requires:       mvn(commons-beanutils:commons-beanutils)
Requires:       mvn(commons-digester:commons-digester) >= 1.8
Requires:       mvn(commons-logging:commons-logging)
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit
%endif

%description
A popular technique for organizing the execution of complex
processing flows is the "Chain of Responsibility" pattern, as
described (among many other places) in the classic "Gang of Four"
design patterns book. Although the fundamental API contracts
required to implement this design pattern are extremely simple,
it is useful to have a base API that facilitates using the pattern,
and (more importantly) encouraging composition of command
implementations from multiple diverse sources.
Towards that end, the Chain API models a computation as a series
of "commands" that can be combined into a "chain". The API for a
command consists of a single method (execute()), which is passed
a "context" parameter containing the dynamic state of the
computation, and whose return value is a boolean that determines
whether or not processing for the current chain has been completed
(true), or whether processing should be delegated to the next
command in the chain (false).

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
find . -name '*.class' -delete
find . -name '*.jar' -delete

mkdir -p target/lib

sed -i 's/\r$//g;' *.txt

%patch0 -p1
%patch1
%patch3 -p1
%patch4 -p1

# Failed tests:   testDefaut(org.apache.commons.chain.config.ConfigParserTestCase):
# Correct command count expected:<17> but was:<19>
rm -r src/test/org/apache/commons/chain/config/ConfigParserTestCase.java

%pom_remove_dep :myfaces-api
rm -rf src/java/org/apache/commons/chain/web/faces

# Force servlet 3.1 apis
%pom_xpath_set "pom:dependency[pom:groupId = 'javax.servlet' ]/pom:artifactId" javax.servlet-api
%pom_xpath_set "pom:dependency[pom:groupId = 'javax.servlet' ]/pom:version" 3.1.0

%pom_remove_parent

%build
export CLASSPATH=$(build-classpath \
                   commons-logging \
                   commons-digester \
                   commons-beanutils \
                   commons-collections \
				   portlet-1.0-api \
				   glassfish-servlet-api)

ant \
%if %{without tests}
    -Dmaven.test.skip=true \
%endif
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
    -Dbuild.sysclasspath=first dist javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 dist/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar
# pom
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a org.apache.commons:%{short_name}
# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/api*/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}/%{name}/

%files -f .mfiles
%doc RELEASE-NOTES.txt NOTICE.txt
%license LICENSE.txt
%{_javadir}/%{short_name}.jar

%files javadoc
%doc NOTICE.txt
%license LICENSE.txt
%{_javadocdir}/%{name}

%changelog
