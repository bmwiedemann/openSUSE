#
# spec file for package picocli
#
# Copyright (c) 2025 SUSE LLC
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


# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Name:           picocli
Version:        4.7.6
Release:        0
Summary:        Tiny Command Line Interface
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://picocli.info/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.xml
Source2:        https://repo1.maven.org/maven2/info/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Source3:        https://repo1.maven.org/maven2/info/%{name}/%{name}-codegen/%{version}/%{name}-codegen-%{version}.pom
Source4:        https://repo1.maven.org/maven2/info/%{name}/%{name}-shell-jline2/%{version}/%{name}-shell-jline2-%{version}.pom
BuildRequires:  ant
BuildRequires:  aqute-bnd
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildRequires:  jline >= 2
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
Java command line parser with both an annotations API and a programmatic API.
Usage help with ANSI styles and colors. Autocomplete. Nested subcommands.
Easily included as source to avoid adding a dependency.

%package codegen
Summary:        Picocli Code Generation
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description codegen
Java command line parser with both an annotations API and a programmatic API.
Usage help with ANSI styles and colors. Autocomplete. Nested subcommands.
Easily included as source to avoid adding a dependency.

Tools to generate documentation, configuration, source code and other files
from a picocli model.

%package shell-jline2
Summary:        Picocli Shell JLine2
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description shell-jline2
Java command line parser with both an annotations API and a programmatic API.
Usage help with ANSI styles and colors. Autocomplete. Nested subcommands.
Easily included as source to avoid adding a dependency.

Library to build interactive shell applications with JLine 2 and picocli.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} build.xml

%build
%{ant} \
	-Dproject.version=%{version} \
	-Djline2.jar=$(find-jar jline/jline) \
	jar javadoc

echo "-reproducible: true" >> bnd.bnd
echo "-noextraheaders: true" >> bnd.bnd
echo "-snapshot: SNAPSHOT" >> bnd.bnd

# Convert to OSGi bundle
bnd wrap \
    --force \
    --bsn %{name} \
    --version %{version} \
    --output target/%{name}-%{version}.bar \
    --properties bnd.bnd \
    target/%{name}-%{version}.jar
mv target/%{name}-%{version}.bar target/%{name}-%{version}.jar

%install
#jar
install -dm0755 %{buildroot}%{_javadir}/%{name}
install -pm0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
install -pm0644 target/%{name}-codegen-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-codegen.jar
install -pm0644 target/%{name}-shell-jline2-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-shell-jline2.jar

#pom
install -dm0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%{mvn_install_pom} %{SOURCE3} %{buildroot}%{_mavenpomdir}/%{name}/%{name}-codegen.pom
%{mvn_install_pom} %{SOURCE4} %{buildroot}%{_mavenpomdir}/%{name}/%{name}-shell-jline2.pom

%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
%add_maven_depmap %{name}/%{name}-codegen.pom %{name}/%{name}-codegen.jar -f codegen
%add_maven_depmap %{name}/%{name}-shell-jline2.pom %{name}/%{name}-shell-jline2.jar -f shell-jline2

#javadoc
install -dm0755 %{buildroot}%{_javadocdir}/%{name}
cp -r target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README.md

%files codegen -f .mfiles-codegen

%files shell-jline2 -f .mfiles-shell-jline2

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
