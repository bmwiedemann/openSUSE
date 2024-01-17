#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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
%define short_name      commons-%{base_name}
Name:           apache-%{short_name}1
Version:        1.4
Release:        0
Summary:        Jakarta Commons DataBase Pooling Package
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/proper/commons-dbcp/
Source0:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source100:      https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz.asc
Source101:      commons.keyring
Patch0:         apache-commons-dbcp-sourcetarget.patch
Patch1:         apache-commons-dbcp-javadoc.patch
Patch2:         apache-commons-dbcp-jdbc41.patch
BuildRequires:  ant >= 1.6.5
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-pool
BuildRequires:  fdupes
BuildRequires:  geronimo-jta-1_1-api
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  jdbc-stdext >= 2.0
BuildRequires:  junit >= 3.8.1
BuildRequires:  xerces-j2
Requires(post): update-alternatives
Requires(preun):update-alternatives
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
Summary:        Javadoc for jakarta-commons-dbcp
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%build
ant \
        -Dcommons-pool.jar=$(build-classpath commons-pool) \
        -Djdbc20ext.jar=$(build-classpath jdbc-stdext) \
        -Djunit.jar=$(build-classpath junit) \
        -Dxerces.jar=$(build-classpath xerces-j2) \
        -Dxml-apis.jar=$(build-classpath xml-commons-jaxp-1.3-apis) \
        -Dcommons-logging.jar=$(build-classpath commons-logging) \
        -Djava.io.tmpdir=. \
        -Djta-impl.jar=$(build-classpath geronimo-jta-1.1-api) \
        dist

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/%{short_name}.jar %{buildroot}%{_javadir}/apache-%{short_name}.jar
ln -sf %{_javadir}/apache-%{short_name}.jar %{buildroot}%{_javadir}/%{short_name}.jar
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/apache-%{short_name}.pom
%add_maven_depmap apache-%{short_name}.pom apache-%{short_name}.jar
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt
%{_javadir}/%{short_name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
