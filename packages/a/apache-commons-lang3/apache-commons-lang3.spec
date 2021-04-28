#
# spec file for package apache-commons-lang3
#
# Copyright (c) 2021 SUSE LLC
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


%define base_name lang3
%define short_name commons-%{base_name}
Name:           apache-%{short_name}
Version:        3.9
Release:        0
Summary:        Apache Commons Lang Package
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/proper/commons-lang/
Source0:        https://archive.apache.org/dist/commons/lang/source/%{short_name}-%{version}-src.tar.gz
Source1:        build.xml
Source2:        default.properties
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
Provides:       %{short_name} = %{version}-%{release}
BuildArch:      noarch

%description
The standard Java libraries fail to provide enough methods for
manipulation of its core classes. The Commons Lang Component provides
these extra methods.

The Commons Lang Component provides a host of helper utilities for the
java.lang API, notably String manipulation methods, basic numerical
methods, object reflection, creation and serialization, and System
properties. Additionally it contains an inheritable enum type, an
exception structure that supports multiple types of nested-Exceptions
and a series of utilities dedicated to help with building methods, such
as hashCode, toString and equals.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE1} .
cp %{SOURCE2} .
sed -i 's/\r//' *.txt

# Not needed since we don't build with maven
%pom_remove_parent
%pom_xpath_inject "pom:project" "<groupId>org.apache.commons</groupId>"
%pom_xpath_remove pom:project/pom:reporting
%pom_xpath_remove pom:project/pom:build
%pom_xpath_remove pom:project/pom:profiles
%pom_remove_dep :::test

%build
export OPT_JAR_LIST=`cat %{_sysconfdir}/ant.d/junit`
export CLASSPATH=
ant \
    -Dcompile.source=1.8 -Dcompile.target=1.8 \
    -Dfinal.name=%{short_name} \
     jar javadoc

%install

# jars
install -dm 755 %{buildroot}%{_javadir}
install -m 0644  target/%{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar
# pom
install -dm 755 %{buildroot}%{_mavenpomdir}
install -m 0644  pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}/%{name}/

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt
%{_javadir}/%{short_name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
