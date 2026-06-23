#
# spec file for package apache-commons-dbcp
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


%define base_name       dbcp
%define short_name      commons-%{base_name}2
Name:           apache-commons-dbcp
Version:        2.14.0
Release:        0
Summary:        Jakarta Commons DataBase Pooling Package
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/proper/commons-dbcp/
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant >= 1.6.5
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-pool2 >= 2.13
BuildRequires:  fdupes
BuildRequires:  glassfish-transaction-api
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
Provides:       %{short_name} = %{version}-%{release}
Obsoletes:      %{short_name} < %{version}-%{release}
Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{version}-%{release}
BuildArch:      noarch

%description
The DBCP package creates and maintains a database connection pool
package written in the Java language to be distributed under the ASF
license. The package is available as a pseudo-JDBC driver and via a
DataSource interface. The package also supports multiple logins to
multiple database systems, reclamation of stale or dead connections,
testing for valid connections, PreparedStatement pooling, and other
features.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains the javadoc documentation for the DBCP package.

The DBCP package shall create and maintain a database connection pool
package written in the Java language to be distributed under the ASF
license. The package shall be available as a pseudo-JDBC driver and via
a DataSource interface. The package shall also support multiple logins
to multiple database systems, reclamation of stale or dead connections,
testing for valid connections, PreparedStatement pooling, and other
features.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE1} build.xml
%pom_change_dep jakarta.transaction:jakarta.transaction-api javax.transaction:javax.transaction-api

%build
mkdir -p lib
build-jar-repository -s lib commons-logging-api commons-pool2 glassfish-transaction-api
ant jar javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}2.jar
ln -sf %{_javadir}/%{name}2.jar %{buildroot}%{_javadir}/%{short_name}.jar
# pom
install -d -m 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}2.pom
%add_maven_depmap %{name}2.pom %{name}2.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt
%{_javadir}/%{short_name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
