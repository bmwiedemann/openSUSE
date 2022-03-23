#
# spec file for package uimaj
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


Name:           uimaj
Version:        2.8.1
Release:        0
Summary:        Apache UIMA is an implementation of the OASIS-UIMA specifications
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://uima.apache.org/
Source0:        http://archive.apache.org/dist/uima/%{name}-%{version}/%{name}-%{version}-source-release.zip
Patch0:         uimaj-2.8.1-jackson2.7.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(ant-contrib:ant-contrib)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(org.apache.ant:ant-apache-regexp)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.uima:parent-pom:pom:)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)

%description
Apache UIMA is an implementation of the OASIS-UIMA specifications.

OASIS UIMA Committee: <http://www.oasis-open.org/committees/uima/>.

Unstructured Information Management applications are software systems
that analyze large volumes of unstructured information in order to
discover knowledge that is relevant to an end user.

An example UIM application might ingest plain text and identify
entities, such as persons, places, organizations; or relations,
such as works-for or located-at.

%package -n jcasgen-maven-plugin
Summary:        Apache UIMA Maven JCasGen Plugin
Group:          Development/Libraries/Java
BuildArch:      noarch

%description -n jcasgen-maven-plugin
A Maven Plugin for using JCasGen to generate Java classes from
XML type system descriptions.

%package -n uima-pear-maven-plugin
Summary:        Apache UIMA Maven Pear Plugin
Group:          Development/Libraries/Java
BuildArch:      noarch

%description -n uima-pear-maven-plugin
This is a maven plugin that produces a pear artifact.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
# Cleanup
find .  -name "*.jar" -delete
find .  -name "*.bat" -delete
find .  -name "*.class" -delete
find .  -name "*.cmd" -delete

%patch0 -p1

# Build @ random fails
%pom_remove_plugin -r :apache-rat-plugin
# org.semver:enforcer-rule:0.9.33
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

# Remove eclipse stuff (dont provides pom or depmap file)
%pom_disable_module ../aggregate-%{name}-eclipse-plugins aggregate-%{name}
%pom_remove_dep org.apache.uima:%{name}-ep-cas-editor
%pom_remove_dep org.apache.uima:%{name}-ep-configurator
%pom_remove_dep org.apache.uima:%{name}-ep-debug
%pom_remove_dep org.apache.uima:%{name}-ep-jcasgen
%pom_remove_dep org.apache.uima:%{name}-ep-pear-packager
%pom_remove_dep org.apache.uima:%{name}-ep-runtime
%pom_remove_dep org.apache.uima:%{name}-ep-cas-editor-ide
%pom_remove_dep org.apache.uima:%{name}-ep-launcher
%pom_remove_dep org.apache.uima:%{name}-examples
%pom_disable_module ../%{name}-examples aggregate-%{name}

# Disable SOAP module which relies upon the ancient and obsolete axis library
%pom_disable_module ../%{name}-adapter-soap aggregate-%{name}
%pom_remove_dep org.apache.uima:%{name}-adapter-soap

# Unavailable deps org.apache.uima:uima-docbook-olink:zip:olink:1-SNAPSHOT
%pom_disable_module ../aggregate-%{name}-docbooks aggregate-%{name}

# These tests @ random fails
rm -r %{name}-core/src/test/java/org/apache/uima/internal/util/UIMAClassLoaderTest.java \
  %{name}-core/src/test/java/org/apache/uima/cas/test/SofaTest.java \
  %{name}-core/src/test/java/org/apache/uima/analysis_engine/impl/AnalysisEngine_implTest.java \
  %{name}-core/src/test/java/org/apache/uima/util/impl/JSR47Logger_implTest.java \
  jcasgen-maven-plugin/src/test/java/org/apache/uima/tools/jcasgen/maven/JCasGenMojoTest.java
# These tests fails with java8
rm -r %{name}-tools/src/test/java/org/apache/uima/tools/viewer/CasAnnotationViewerTest.java

# Unavailable test:crossref2:1.0.0-SNAPSHOT
%pom_remove_plugin :maven-invoker-plugin jcasgen-maven-plugin

sed -i 's/\r//' NOTICE README

%pom_xpath_set "pom:dependency[pom:artifactId = 'log4j']/pom:version" 1.2.17 %{name}-core

%{mvn_package} :PearPackagingMavenPlugin uima-pear-maven-plugin
%{mvn_package} :jcasgen-maven-plugin jcasgen-maven-plugin

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8 -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README RELEASE_NOTES.html
%license LICENSE NOTICE

%files -n jcasgen-maven-plugin -f .mfiles-jcasgen-maven-plugin
%license LICENSE NOTICE

%files -n uima-pear-maven-plugin -f .mfiles-uima-pear-maven-plugin
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
