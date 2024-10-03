#
# spec file for package jline
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


Name:           jline
Version:        2.14.6
Release:        0
Summary:        Java library for reading and editing user input in console applications
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/jline/jline2
Source0:        https://github.com/jline/jline2/archive/jline-%{version}.tar.gz
Source1:        %{name}-build.xml
Patch0:         jline-java8compat.patch
Patch1:         jline-jansi2.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  jansi
BuildRequires:  javapackages-local >= 6
#!BuildIgnore:  ant-antlr
BuildArch:      noarch

%description
JLine is a java library for reading and editing user input in console
applications. It features tab-completion, command history, password
masking, customizable keybindings, and pass-through handlers to use to
chain to other console applications.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jline2-jline-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%pom_change_dep org.fusesource.jansi:jansi org.fusesource.jansi:jansi:1.12
cp %{SOURCE1} build.xml
mkdir -p lib

%build
build-jar-repository -s lib jansi
ant package javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{name}

%changelog
