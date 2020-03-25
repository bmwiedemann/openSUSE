#
# spec file for package auto
#
# Copyright (c) 2020 SUSE LLC
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


%global auto_ver 1.5.4
%global common_ver 0.10
%global service_ver 1.0-rc4
%global parent_ver 6
Name:           auto
Version:        %{auto_ver}
Release:        0
Summary:        A collection of source code generators for Java
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/google/auto
Source0:        https://github.com/google/auto/archive/auto-value-%{version}.tar.gz
Source1:        https://github.com/google/auto/archive/auto-common-%{common_ver}.tar.gz
Source2:        https://github.com/google/auto/archive/auto-service-%{service_ver}.tar.gz
Source3:        https://github.com/google/auto/archive/auto-parent-%{parent_ver}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(com.squareup:javapoet)
BuildArch:      noarch

%description
The Auto sub-projects are a collection of code generators
that automate those types of tasks.

%package common
Summary:        Auto Common Utilities
Group:          Development/Libraries/Java
Obsoletes:      %{name}-factory < %{version}-%{release}

%description common
Common utilities for creating annotation processors.

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
%setup -q -n auto-auto-value-%{version} -a1 -a2 -a3
rm -rf pom.xml factory/ common/ service/
mv auto-auto-parent-%{parent_ver}/pom.xml .
mv auto-auto-common-%{common_ver}/common common
mv auto-auto-service-%{service_ver}/service service

# remove unnecessary dependency on parent POM
%pom_remove_parent

# Disable factory module due to missing dep:
# com.google.googlejavaformat:google-java-format
%pom_disable_module factory build-pom.xml

# Fix deps in service module
%pom_xpath_set "pom:parent/pom:version" 6 service
%pom_change_dep com.google.auto:auto-common com.google.auto:auto-common:0.10 service

%pom_remove_plugin org.apache.maven.plugins:maven-checkstyle-plugin
%pom_remove_plugin :maven-shade-plugin value
%pom_remove_plugin :maven-invoker-plugin value

# Broader guava compatibility
sed -i -e 's/23.5-jre/20.0/' pom.xml
sed -i -e 's/toImmutableMap/toMap/' -e 's/static com.google.common.collect.ImmutableMap/static java.util.stream.Collectors/' \
  -e '/elementValues/s/ImmutableMap/Map/' \
  common/src/main/java/com/google/auto/common/SimpleAnnotationMirror.java
sed -i -e 's/toImmutableSet/toSet/' -e 's/static com.google.common.collect.ImmutableSet/static java.util.stream.Collectors/' \
  -e '/ImmutableSet</s/ImmutableSet/Set/' \
  service/src/main/java/com/google/auto/service/processor/AutoServiceProcessor.java

%{mvn_package} :build-only __noinstall

%build
%{mvn_build} -sf -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8 \
%endif
	-f build-pom.xml -Dsource=8 -Dfile.encoding=UTF-8

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

%files service -f .mfiles-%{name}-service
%doc service/README.md
%license LICENSE.txt

%files value -f .mfiles-%{name}-value
%doc value/README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
