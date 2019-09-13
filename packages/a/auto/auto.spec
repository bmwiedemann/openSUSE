#
# spec file for package auto
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


Name:           auto
Version:        1.3
Release:        0
Summary:        A collection of source code generators for Java
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/google/auto
Source0:        https://github.com/google/auto/archive/auto-value-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.squareup:javapoet)
BuildRequires:  mvn(javax.annotation:jsr250-api)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
The Auto sub-projects are a collection of code generators
that automate those types of tasks.

%package common
Summary:        Auto Common Utilities
Group:          Development/Libraries/Java

%description common
Common utilities for creating annotation processors.

%package factory
Summary:        JSR-330-compatible factories
Group:          Development/Libraries/Java

%description factory
A source code generator for JSR-330-compatible factories.

%package service
Summary:        Provider-configuration files for ServiceLoader
Group:          Development/Libraries/Java

%description service
A configuration/meta-data generator for
java.util.ServiceLoader-style service
providers.

%package value
Summary:        Auto Value
Group:          Development/Libraries/Java

%description value
Immutable value-type code generation for Java 1.6+.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n auto-auto-value-%{version}
find -name '*.class' -print -delete
find -name '*.jar' -print -delete

%pom_xpath_inject "pom:project" "
<modules>
  <module>common</module>
  <module>factory</module>
  <module>service</module>
  <module>value</module>
</modules>"

%pom_xpath_set "pom:project/pom:version" %{version}
for p in common factory service value ;do
  %pom_xpath_set "pom:parent/pom:version" %{version} ${p}
  %pom_xpath_set "pom:project/pom:version" %{version} ${p}
  %pom_xpath_remove "pom:dependency[pom:scope = 'test']" ${p}
done

%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin
%pom_remove_plugin :maven-shade-plugin value
%pom_remove_plugin :maven-invoker-plugin value
%pom_remove_plugin :maven-invoker-plugin factory

%pom_xpath_set "pom:dependency[pom:artifactId = 'auto-common']/pom:version" %{version} factory service value
%pom_xpath_set "pom:dependency[pom:artifactId = 'auto-service']/pom:version" %{version} factory value
%pom_xpath_set "pom:dependency[pom:artifactId = 'auto-value']/pom:version" %{version} factory

%pom_add_dep javax.annotation:jsr250-api value

%build

# Unavailable test deps
%{mvn_build} -sf -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-%{name}-parent
%dir %{_javadir}/%{name}
%doc README.md
%license LICENSE.txt

%files common -f .mfiles-%{name}-common
%doc common/README.md
%license LICENSE.txt

%files factory -f .mfiles-%{name}-factory
%doc factory/README.md
%license LICENSE.txt

%files service -f .mfiles-%{name}-service
%doc service/README.md
%license LICENSE.txt

%files value -f .mfiles-%{name}-value
%doc value/README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
