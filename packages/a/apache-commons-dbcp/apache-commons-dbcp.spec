#
# spec file for package apache-commons-dbcp
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


%define base_name       dbcp
%define short_name      commons-%{base_name}2
Name:           apache-commons-dbcp
Version:        2.1.1
Release:        0
Summary:        Jakarta Commons DataBase Pooling Package
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/proper/commons-dbcp/
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source100:      http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz.asc
Source101:      commons.keyring
Patch0:         apache-commons-dbcp-sourcetarget.patch
Patch1:         apache-commons-dbcp-javadoc.patch
BuildRequires:  ant >= 1.6.5
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-pool2
BuildRequires:  fdupes
BuildRequires:  geronimo-jta-1_1-api
BuildRequires:  java-devel >= 1.7
BuildRequires:  javapackages-local
BuildRequires:  jdbc-stdext >= 2.0
BuildRequires:  junit >= 3.8.1
BuildRequires:  xerces-j2
Requires:       commons-collections >= 3.2
Requires:       commons-pool2
Requires:       jta_api >= 1.1
Requires(post): update-alternatives
Requires(preun): update-alternatives
Provides:       %{short_name} = %{version}-%{release}
Obsoletes:      %{short_name} < %{version}-%{release}
Provides:       hibernate_jdbc_cache
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
%patch0 -p1
%patch1 -p1
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%pom_remove_parent .

%build
ant \
        -Dcommons-pool.jar=$(build-classpath commons-pool2) \
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
install -m 644 dist/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}2-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|apache-||g"`; done)
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -m 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}2-%{version}.pom
%add_maven_depmap %{name}2-%{version}.pom %{name}2-%{version}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}
# hibernate_jdbc_cache ghost symlink
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
ln -sf %{_sysconfdir}/alternatives/hibernate_jdbc_cache.jar %{buildroot}%{_javadir}/hibernate_jdbc_cache.jar

%post
update-alternatives --install %{_javadir}/hibernate_jdbc_cache.jar \
  hibernate_jdbc_cache %{_javadir}/%{name}2.jar 60

%preun
if [ $1 -eq 0 ] ; then
  update-alternatives --remove hibernate_jdbc_cache %{_javadir}/%{name}2.jar
fi

%files
%license LICENSE.txt
%{_javadir}/%{name}2.jar
%{_javadir}/%{name}2-%{version}.jar
%{_javadir}/%{short_name}.jar
%{_javadir}/%{short_name}-%{version}.jar
%{_javadir}/hibernate_jdbc_cache.jar
%ghost %{_sysconfdir}/alternatives/hibernate_jdbc_cache.jar
%{_mavenpomdir}/%{name}2-%{version}.pom
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml*
%endif

%files javadoc
%{_javadocdir}/%{name}

%changelog
