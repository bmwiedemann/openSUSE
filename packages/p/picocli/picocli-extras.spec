#
# spec file for package picocli-extras
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
%global base_name picocli
Name:           %{base_name}-extras
Version:        4.7.6
Release:        0
Summary:        Tiny Command Line Interface
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://picocli.info/
Source0:        %{base_name}-%{version}.tar.xz
Source1:        %{name}-build.xml
Source2:        https://repo1.maven.org/maven2/info/%{base_name}/%{base_name}-shell-jline3/%{version}/%{base_name}-shell-jline3-%{version}.pom
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildRequires:  jline3
BuildRequires:  picocli
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
Java command line parser with both an annotations API and a programmatic API.
Usage help with ANSI styles and colors. Autocomplete. Nested subcommands.
Easily included as source to avoid adding a dependency.

%package -n %{base_name}-shell-jline3
Summary:        Picocli Shell JLine3
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description -n %{base_name}-shell-jline3
Java command line parser with both an annotations API and a programmatic API.
Usage help with ANSI styles and colors. Autocomplete. Nested subcommands.
Easily included as source to avoid adding a dependency.

Library to build interactive shell applications with JLine 3 and picocli.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{base_name}-%{version}
cp %{SOURCE1} build.xml

%build
%{ant} \
	-Dproject.version=%{version} \
	-Djline3.jar=$(find-jar jline3/jline) \
    -Dpicocli.jar=$(find-jar picocli/picocli) \
	jar javadoc

%install
#jar
install -dm0755 %{buildroot}%{_javadir}/%{base_name}
install -pm0644 target/%{base_name}-shell-jline3-%{version}.jar %{buildroot}%{_javadir}/%{base_name}/%{base_name}-shell-jline3.jar

#pom
install -dm0755 %{buildroot}%{_mavenpomdir}/%{base_name}
%{mvn_install_pom} %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{base_name}/%{base_name}-shell-jline3.pom

%add_maven_depmap %{base_name}/%{base_name}-shell-jline3.pom %{base_name}/%{base_name}-shell-jline3.jar -f shell-jline3

#javadoc
install -dm0755 %{buildroot}%{_javadocdir}/%{name}
cp -r target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -n %{base_name}-shell-jline3 -f .mfiles-shell-jline3

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
