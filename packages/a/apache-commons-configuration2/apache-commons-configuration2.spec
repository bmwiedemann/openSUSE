#
# spec file for package apache-commons-configuration2
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


%global base_name       configuration2
%global short_name      commons-%{base_name}
Name:           apache-commons-configuration2
Version:        2.9.0
Release:        0
Summary:        Java library providing a generic Configuration interface
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-configuration/
Source0:        https://archive.apache.org/dist/commons/configuration/source/%{short_name}-%{version}-src.tar.gz
Source10:       %{name}-build.xml
BuildRequires:  ant
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-jexl
BuildRequires:  apache-commons-jxpath
BuildRequires:  apache-commons-lang3
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-text
BuildRequires:  apache-commons-vfs2
BuildRequires:  fdupes
BuildRequires:  glassfish-servlet-api
BuildRequires:  jackson-core
BuildRequires:  jackson-databind
BuildRequires:  javacc
BuildRequires:  javapackages-local >= 6
BuildRequires:  reload4j
BuildRequires:  snakeyaml
BuildRequires:  xml-resolver
BuildArch:      noarch

%description
The Commons Configuration library provides a generic Configuration
interface which enables a Java application to read configuration data
from a variety of sources.

Configuration parameters may be loaded from the following sources:

 * Properties files
 * XML documents
 * Windows INI files
 * Property list files (plist)
 * JNDI
 * JDBC Datasource
 * System properties
 * Applet parameters
 * Servlet parameters

Configuration objects are created using configuration builders. Different
configuration sources can be mixed using a CombinedConfigurationBuilder and
a CombinedConfiguration. Additional sources of configuration parameters
can be created by using custom configuration objects. This customization
can be achieved by extending AbstractConfiguration or
AbstractHierarchicalConfiguration.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE10} build.xml

%pom_remove_dep org.springframework:
rm -r src/main/java/org/apache/commons/configuration2/spring \
 src/test/java/org/apache/commons/configuration2/spring

%pom_change_dep javax.servlet:servlet-api javax.servlet:javax.servlet-api:3.1.0

%build
mkdir -p lib
build-jar-repository -s -p lib \
    apache-commons-text \
    commons-beanutils \
    commons-codec \
    commons-jexl \
    commons-jxpath \
    commons-lang3 \
    commons-logging \
    commons-vfs2 \
    glassfish-servlet-api \
    jackson-core \
    jackson-databind \
    javacc \
    reload4j \
    snakeyaml \
    xml-resolver
%{ant} jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -sf %{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt
%{_javadir}/%{name}.jar

%files javadoc
%license LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
