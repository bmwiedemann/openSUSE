#
# spec file for package maven-jaxb2-plugin
#
# Copyright (c) 2024 SUSE LLC
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


Name:           maven-jaxb2-plugin
Version:        0.14.0
Release:        0
Summary:        Provides the capability to generate java sources from schemas
License:        Apache-2.0 AND BSD-2-Clause
Group:          Development/Libraries/Java
URL:            https://java.net/projects/maven-jaxb2-plugin/pages/Home
Source0:        https://github.com/highsource/jaxb-tools/archive/refs/tags/%{version}.tar.gz
# Don't try to use an internal bundled resolver
Patch0:         %{name}-0.14.0-dont-use-internal-resolver.patch
# Adapt for Maven 3:
Patch1:         %{name}-0.13.0-adapt-for-maven-3.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(com.sun.activation:javax.activation)
BuildRequires:  mvn(com.sun.codemodel:codemodel)
BuildRequires:  mvn(com.sun.istack:istack-commons-runtime)
BuildRequires:  mvn(com.sun.istack:istack-commons-tools)
BuildRequires:  mvn(com.sun.xml.bind.external:rngom)
BuildRequires:  mvn(com.sun.xml.dtd-parser:dtd-parser)
BuildRequires:  mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires:  mvn(com.sun.xsom:xsom)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.glassfish.jaxb:codemodel)
BuildRequires:  mvn(org.glassfish.jaxb:jaxb-runtime)
BuildRequires:  mvn(org.glassfish.jaxb:jaxb-xjc)
BuildRequires:  mvn(org.glassfish.jaxb:jaxb-xjc-jdk9)
BuildRequires:  mvn(org.glassfish.jaxb:txw2)
BuildRequires:  mvn(org.jvnet.staxex:stax-ex)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
BuildRequires:  mvn(xml-resolver:xml-resolver)
BuildArch:      noarch

%description
This Maven 2 plugin wraps the JAXB 2.x XJC compiler and provides the capability
to generate Java sources from XML Schemas.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
The API documentation of %{name}.

%prep
%setup -q -n jaxb-tools-%{version}
%patch -P 0 -p1
%patch -P 1 -p1

# use glassfish-jaxb = 2.0.5
%pom_disable_module plugin-2.0
# use glassfish-jaxb = 2.1.13
%pom_disable_module plugin-2.1

# Add dependency on codemodel:
# because org.glassfish.jaxb:codemodel:2.2.11 have missing classes use @ runtime by these plugins:
%pom_add_dep com.sun.codemodel:codemodel:2.6 plugin
%pom_add_dep com.sun.codemodel:codemodel:2.6 plugin-2.2
%pom_add_dep com.sun.codemodel:codemodel:2.6 plugin-2.3

%pom_remove_dep -r :jaxb-core
%pom_remove_plugin -r :maven-dependency-plugin

%pom_xpath_set -r "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:source" "1.8"
%pom_xpath_set -r "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:target" "1.8"

%build

%{mvn_build} -f -j

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE

%if 0
%files javadoc -f .mfiles-javadoc
%license LICENSE
%endif

%changelog
