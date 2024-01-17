#
# spec file for package postgresql-jdbc
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2000-2005, JPackage Project
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


Name:           postgresql-jdbc
Version:        42.2.25
Release:        0
Summary:        JDBC driver for PostgreSQL
License:        BSD-2-Clause
URL:            https://jdbc.postgresql.org/
Source0:        https://repo1.maven.org/maven2/org/postgresql/postgresql/%{version}/postgresql-%{version}-jdbc-src.tar.gz
Patch1:         CVE-2022-26520.patch
Patch2:         fix-SQL-Injection-CVE-2022-31197.patch
Patch3:         fix-createTempFile-vulnerability-CVE-2022-41946.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.ongres.scram:client) >= 2.0
BuildArch:      noarch

%description
PostgreSQL is an advanced Object-Relational database management
system. The postgresql-jdbc package includes the .jar files needed for
Java programs to access a PostgreSQL database.

%package javadoc
Summary:        API docs for %{name}

%description javadoc
This package contains the API Documentation for %{name}.

%prep
%setup -q -n postgresql-%{version}-jdbc-src
%patch1 -p1
%patch2 -p1
%patch3 -p2

# Build parent POMs in the same Maven call.
%pom_xpath_remove "pom:plugin[pom:artifactId = 'maven-shade-plugin']"

%{mvn_file} org.postgresql:postgresql %{name}/postgresql %{name}

# For compat reasons, make Maven artifact available under older coordinates.
%{mvn_alias} org.postgresql:postgresql postgresql:postgresql

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
