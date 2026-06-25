#
# spec file for package apache-commons-logging
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2000-2007, JPackage Project
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


%define base_name  logging
%define short_name commons-%{base_name}
Name:           apache-%{short_name}
Version:        1.4.0
Release:        0
Summary:        Apache Commons Logging
License:        Apache-2.0
URL:            https://commons.apache.org/%{base_name}
Source0:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  avalon-framework-api
BuildRequires:  avalon-logkit
BuildRequires:  fdupes
BuildRequires:  glassfish-servlet-api
BuildRequires:  jakarta-servlet
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  reload4j
Requires:       java >= 1.8
Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{version}
Provides:       %{short_name} = %{version}-%{release}
Obsoletes:      %{short_name} < %{version}
BuildArch:      noarch

%description
The commons-logging package provides a simple, component oriented
interface (org.apache.commons.logging.Log) together with wrappers for
logging systems. The user can choose at runtime which system they want
to use. In addition, a small number of basic implementations are
provided to allow users to use the package standalone.
commons-logging was heavily influenced by Avalon's Logkit and Log4J. The
commons-logging abstraction is meant to minimize the differences between
the two, and to allow a developer to not tie himself to a particular
logging implementation.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src

cp %{SOURCE1} build.xml
%pom_remove_dep :log4j-api
rm src/main/java/org/apache/commons/logging/impl/Log4jApiLogFactory.java
%pom_remove_dep :slf4j-api
rm src/main/java/org/apache/commons/logging/impl/Slf4jLogFactory.java

%pom_change_dep org.apache.logging.log4j:log4j-1.2-api ch.qos.reload4j:reload4j:1.2.25
%pom_change_dep :avalon-framework ::avalon-framework-api:4.3

sed -i 's/\r//' RELEASE-NOTES.txt LICENSE.txt

%build
mkdir -p lib
build-jar-repository -s lib \
    avalon-framework-api \
    avalon-logkit \
    glassfish-servlet-api \
    jakarta-servlet/jakarta.servlet-api \
    reload4j/reload4j
ant jar javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
install -pm 0644 target/%{short_name}-%{version}-api.jar %{buildroot}%{_javadir}/%{name}-api.jar
install -pm 0644 target/%{short_name}-%{version}-adapters.jar %{buildroot}%{_javadir}/%{name}-adapters.jar

pushd %{buildroot}%{_javadir}
for jar in %{name}*; do
    ln -sf ${jar} `echo $jar| sed "s|apache-||g"`
done
popd

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}/%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar -a "org.apache.commons:%{short_name}","apache:%{short_name}"
%add_maven_depmap %{short_name}:%{short_name}::api:%{version} %{short_name}-api.jar -a "%{short_name}:%{short_name}-api","org.apache.commons:%{short_name}-api","apache:%{short_name}-api"
%add_maven_depmap %{short_name}:%{short_name}::adapters:%{version} %{short_name}-adapters.jar -a "%{short_name}:%{short_name}-adapters","org.apache.commons:%{short_name}-adapters","apache:%{short_name}-adapters"

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}/%{name}/

%files -f .mfiles
%{_javadir}/%{name}*.jar
%license LICENSE.txt
%doc PROPOSAL.html RELEASE-NOTES.txt NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}

%changelog
