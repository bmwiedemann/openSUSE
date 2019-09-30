#
# spec file for package jline
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
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  hawtjni-runtime
BuildRequires:  jansi
BuildRequires:  jansi-native
BuildRequires:  javapackages-local
#!BuildIgnore:  ant-antlr
Requires:       mvn(org.fusesource.jansi:jansi)
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
%patch0 -p1
%pom_change_dep org.fusesource.jansi:jansi org.fusesource.jansi:jansi:1.12
cp %{SOURCE1} build.xml
mkdir -p lib

# Remove maven-shade-plugin usage
%pom_remove_plugin "org.apache.maven.plugins:maven-shade-plugin"
# Remove animal sniffer plugin in order to reduce deps
%pom_remove_plugin "org.codehaus.mojo:animal-sniffer-maven-plugin"

# Remove unavailable and unneeded deps
%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin

%pom_remove_parent

%build
build-jar-repository -s lib jansi jansi-native hawtjni/hawtjni-runtime
%{ant} package javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{name}

%changelog
