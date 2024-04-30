#
# spec file for package apache-commons-pool
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
%define short_name      commons-%{base_name}
Name:           apache-commons-pool
Version:        1.6
Release:        0
Summary:        Apache Commons Pool
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/proper/commons-pool/
Source0:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:         jakarta-commons-pool-build.patch
Patch1:         commons-pool-1.6-sourcetarget.patch
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  junit
Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{version}-%{release}
Provides:       %{short_name} = %{version}-%{release}
Obsoletes:      %{short_name} < %{version}-%{release}
BuildArch:      noarch

%description
The goal of the Pool package is to create and maintain an object
(instance) pooling package to be distributed under the ASF license. The
package supports a variety of pool implementations, but encourages
support of an interface that makes these implementations
interchangeable.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
The goal of Pool package it to create and maintain an object (instance)
pooling package to be distributed under the ASF license. The package
should support a variety of pool implementations, but encourage support
of an interface that makes these implementations interchangeable.

This package contains the javadoc documentation for the Apache Commons
Pool Package.

%prep
%setup -q -n %{short_name}-%{version}-src
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
%patch -P 0
%patch -P 1 -p1

dos2unix README.txt

%build
ant -Djava.io.tmpdir=. clean dist

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -m 0644 dist/%{short_name}-%{version}-SNAPSHOT.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{_javadir}/%{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar

# pom
install -d -m 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt
%doc README.txt
%{_javadir}/%{short_name}.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
