#
# spec file for package paranamer
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


%global githash cb6709646eed97c271d73f50ad750cc43c8e052a
Name:           paranamer
Version:        2.8
Release:        0
Summary:        Java library for accessing non-private method's parameter names at run-time
License:        BSD-3-Clause
URL:            https://github.com/paul-hammant/paranamer
Source0:        %{url}/archive/%{githash}/%{name}-%{githash}.tar.gz
Patch0:         0001-Port-to-current-qdox.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.thoughtworks.qdox:qdox)
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildArch:      noarch

%description
Paranamer is a Java library that allows the parameter names of non-private
methods and constructors to be accessed at run-time. Most compilers discard
this information; traditional Reflection on JDK <= 7 would show something like
doSomething(mypackage.Person ???) instead of doSomething(mypackage.Person toMe).
The Paranamer library fills this gap for these JDK versions.

%package ant
Summary:        ParaNamer Ant

%description ant
This package contains the ParaNamer Ant tasks.

%package generator
Summary:        ParaNamer Generator

%description generator
This package contains the ParaNamer Generator.

%package maven-plugin
Summary:        ParaNamer Maven plugin

%description maven-plugin
This package contains the ParaNamer Maven plugin.

%package parent
Summary:        ParaNamer Parent POM

%description parent
This package contains the ParaNamer Parent POM.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{githash}

%patch0 -p1

# Cleanup
find -name "*.class" -print -delete
# Do not erase test resources
find -name "*.jar" -print ! -name "test.jar" -delete

chmod -x LICENSE.txt

# remove unnecessary dependency on parent POM
%pom_remove_parent

# Remove wagon extension
%pom_xpath_remove "pom:build/pom:extensions"

%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin

# Disable distribution module
%pom_disable_module %{name}-distribution
# And integration-tests module
%pom_disable_module %{name}-integration-tests

# Unavailable test deps
%pom_remove_dep -r net.sourceforge.f2j:
%pom_xpath_remove -r "pom:dependency[pom:classifier = 'javadoc' ]"
# package org.netlib.blas does not exist
rm -r %{name}/src/test/com/thoughtworks/paranamer/JavadocParanamerTest.java
# testRetrievesParameterNamesFromBootstrapClassLoader java.lang.AssertionError:
#       Should not find names for classes loaded by the bootstrap class loader.
rm -r %{name}/src/test/com/thoughtworks/paranamer/BytecodeReadingParanamerTestCase.java

%build

%{mvn_build} -sf \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-%{name}
%doc README.md
%license LICENSE.txt

%files ant -f .mfiles-%{name}-ant

%files generator -f .mfiles-%{name}-generator
%license LICENSE.txt

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%files parent -f .mfiles-%{name}-parent
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
