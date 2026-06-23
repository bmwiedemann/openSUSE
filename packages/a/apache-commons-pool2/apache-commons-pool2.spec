#
# spec file for package apache-commons-pool2
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define base_name       pool
%define short_name      commons-%{base_name}2
Name:           apache-commons-pool2
Version:        2.13.1
Release:        0
Summary:        Apache Commons Pool 2.x series
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/proper/commons-pool/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  cglib
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
Provides:       %{short_name} = %{version}
Obsoletes:      %{short_name} < %{version}
BuildArch:      noarch

%description
The goal of the Pool 2.x package is to create and maintain an object
(instance) pooling package to be distributed under the ASF license. The
package supports a variety of pool implementations, but encourages
support of an interface that makes these implementations
interchangeable.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
The goal of Pool 2.x package it to create and maintain an object (instance)
pooling package to be distributed under the ASF license. The package
should support a variety of pool implementations, but encourage support
of an interface that makes these implementations interchangeable.

This package contains the javadoc documentation for the Apache Commons
Pool 2.x Package.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE1} build.xml

%build
mkdir -p lib
build-jar-repository -s lib cglib/cglib
ant jar javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{_javadir}/%{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt
%doc README.md
%{_javadir}/%{short_name}.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
