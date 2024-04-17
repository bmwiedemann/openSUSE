#
# spec file for package snakeyaml
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


%global vertag a34989252e6f
%bcond_with tests
Name:           snakeyaml
Version:        2.2
Release:        0
Summary:        YAML parser and emitter for the Java programming language
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://bitbucket.org/%{name}/%{name}
Source0:        https://bitbucket.org/%{name}/%{name}/get/%{name}-%{version}.tar.bz2
Source1:        %{name}-build.xml
# Replace use of bundled Base64 implementation with java.util.Base64
Patch0:         0001-Remove-external-Base64Coder-and-use-provided-Base64.patch
# We don't have gdata-java, use commons-codec instead
Patch1:         0002-Replace-bundled-gdata-java-client-classes-with-commo.patch
BuildRequires:  ant
BuildRequires:  apache-commons-codec
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
SnakeYAML features:
    * a complete YAML 1.1 parser. In particular,
      SnakeYAML can parse all examples from the specification.
    * Unicode support including UTF-8/UTF-16 input/output.
    * high-level API for serializing and deserializing
      native Java objects.
    * support for all types from the YAML types repository.
    * relatively sensible error messages.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains %{summary}.

%prep
%setup -q -n %{name}-%{name}-%{vertag}
cp %{SOURCE1} build.xml
%patch -P 0 -p1
%patch -P 1 -p1

# Unnecessary test-time only dependency
%pom_change_dep joda-time:joda-time :::test
%pom_change_dep org.projectlombok:lombok :::test
%pom_change_dep org.apache.velocity:velocity-engine-core :::test

%build
mkdir -p lib
build-jar-repository -s lib commons-codec
%{ant} \
  clean package javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}

%changelog
