#
# spec file for package jcip-annotations
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


Name:           jcip-annotations
Version:        1.0.1
Release:        0
Summary:        A clean room implementation of the JCIP Annotations
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/stephenc/jcip-annotations
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
A clean room implementation of the JCIP Annotations based entirely on the
specification provided by the javadocs.

%package javadoc
Summary:        API documentation for %{name}
Group:          Development/Libraries/Java

%description javadoc
A clean room implementation of the JCIP Annotations based entirely on the
specification provided by the javadocs.

This package contains the API documentation.

%prep
%setup -q
cp %{SOURCE1} build.xml

# Remove unnecessary dependency on parent POM
%pom_remove_parent

# Remove unnecessary dependency on JUnit
%pom_remove_dep junit:junit

%build
ant jar javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "net.jcip:%{name}"

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt

%changelog
