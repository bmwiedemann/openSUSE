#
# spec file for package apache-commons-pool2
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


%define base_name       pool
%define short_name      commons-%{base_name}2
Name:           apache-commons-pool2
Version:        2.4.2
Release:        0
Summary:        Apache Commons Pool 2.x series
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/proper/commons-pool/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:         jakarta-commons-pool-build.patch
BuildRequires:  ant
BuildRequires:  cglib
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  junit
Requires:       cglib
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
# remove all binary libs
find . -name "*.jar" -print -delete
%patch -P 0

%build
echo "cglib.jar=$(build-classpath cglib)" >> build.properties
ant \
    -Djavac.target.version=8 -Djavac.src.version=8 \
    -Djava.io.tmpdir=. clean dist

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{_javadir}/%{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt
%doc README.txt
%{_javadir}/%{short_name}.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
