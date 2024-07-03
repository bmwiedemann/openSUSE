#
# spec file
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


%global short_name log4j-extras
Name:           apache-%{short_name}
Version:        1.2.17.1
Release:        0
Summary:        Apache Extras Companion for Apache log4j
License:        Apache-2.0
URL:            https://logging.apache.org/log4j/extras
Source0:        https://github.com/apache/%{short_name}/archive/refs/tags/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.geronimo.specs:geronimo-jms_1.1_spec)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildArch:      noarch

%description
Apache Extras Companion for Apache log4j is a collection of appenders,
filters, layouts, and receivers for Apache log4j 1.2

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{name}-%{version}
# Cleanup
find . -name '*.class' -delete
find . -name '*.jar' -delete
# Security problem mitigation
rm -f src/main/java/org/apache/log4j/DBAppender.java

# Unnecessary plugins
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-changes-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-site-plugin

%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:source" "1.8"
%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:target" "1.8"

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
