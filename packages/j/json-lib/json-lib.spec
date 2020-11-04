#
# spec file for package json-lib
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


Name:           json-lib
Version:        2.4
Release:        0
Summary:        JSON library for Java
License:        Apache-2.0
URL:            http://json-lib.sourceforge.net/
Source0:        %{name}-%{version}.tar.xz
# Jenkins sources/patches
# tarball comming from not yet released upstream git repo
# it contains changes from Jenkins upstream
Source100:      jenkins-%{name}-%{version}.tar.xz
Patch0:         %{name}-%{version}-antrun-plugin.patch
Patch100:       %{name}-%{version}-Use-Jenkins-default-values.patch
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  maven-local
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(asm:asm)
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j:1.2.14)
BuildRequires:  mvn(net.sf.ezmorph:ezmorph)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.codehaus.groovy:groovy-all:1.8)
BuildRequires:  mvn(org.codehaus.groovy:groovy:1.8)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-nop)
BuildRequires:  mvn(oro:oro)
BuildRequires:  mvn(xom:xom)
BuildArch:      noarch

%description
JSON-lib is a java library for transforming beans, maps, collections, java
arrays and XML to JSON and back again to beans and DynaBeans.

%package -n jenkins-json-lib
Summary:        Jenkins JSON library

%description -n jenkins-json-lib
JSON-lib is a java library for transforming beans, maps, collections, java
arrays and XML to JSON and back again to beans and DynaBeans.

This package contains JSON library used in Jenkins.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q

tar xf %{SOURCE100}

# compile: src/main/groovy/net/sf/json/groovy/GJson.groovy
#          src/main/jdk15/net/sf/json/util/EnumMorpher.java
%patch0 -p1

%pom_remove_plugin :maven-compiler-plugin
%pom_remove_plugin :gmaven-plugin

%pom_xpath_remove "pom:project/pom:prerequisites"
%pom_xpath_remove "pom:project/pom:reporting"

# error: duplicate class
rm -r src/main/jdk15/net/sf/json/JSON*.java
%pom_add_plugin org.apache.maven.plugins:maven-javadoc-plugin . '
<configuration>
  <charset>UTF-8</charset>
  <docencoding>UTF-8</docencoding>
  <sourcepath>${basedir}/src/main</sourcepath>
</configuration>'

# should be removed from distribution
%pom_remove_dep :commons-httpclient

%pom_change_dep org.codehaus.groovy:: org.codehaus.groovy::1.8

# Remove the -SNAPSHOT postfix
%pom_xpath_set pom:project/pom:version "2.4-jenkins-3" jenkins-%{name}-%{version}/pom.xml

pushd jenkins-%{name}-%{version}
%patch100 -p1

%pom_change_dep org.codehaus.groovy:groovy-all org.codehaus.groovy:groovy-all:1.8

%{mvn_file} org.kohsuke.stapler:json-lib jenkins-%{name}
%{mvn_package} org.kohsuke.stapler:json-lib jenkins-json-lib

popd

%build
%{mvn_file} : %{name}
%{mvn_build} -f -- -Dproject.build.sourceEncoding=UTF-8 \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=6
%endif

# build Jenkins JSON lib
pushd jenkins-%{name}-%{version}
%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

popd

%install
%mvn_install

# install Jenkins JSON lib
pushd jenkins-%{name}-%{version}
%mvn_install
popd

%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt

%files -n jenkins-json-lib -f jenkins-%{name}-%{version}/.mfiles-jenkins-json-lib
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
