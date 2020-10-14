#
# spec file for package mybatis
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_with test
Name:           mybatis
Version:        3.5.6
Release:        0
Summary:        SQL Mapping Framework for Java
# http://code.google.com/p/mybatis/
License:        Apache-2.0
URL:            https://www.mybatis.org/
Source0:        https://github.com/mybatis/mybatis-3/archive/%{name}-%{version}.tar.gz
Patch0:         mybatis-3.5.3-commons-ognl.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(cglib:cglib)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(log4j:log4j:1.2.17)
BuildRequires:  mvn(org.apache.commons:commons-ognl)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-core)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-ssh)
BuildRequires:  mvn(org.javassist:javassist)
BuildRequires:  mvn(org.mybatis:mybatis-parent:pom:)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-log4j12)
BuildArch:      noarch

%description
The MyBatis data mapper framework makes it easier
to use a relational database with object-oriented
applications. MyBatis couples objects with stored
procedures or SQL statements using a XML descriptor
or annotations. Simplicity is the biggest advantage
of the MyBatis data mapper over object relational
mapping tools.

To use the MyBatis data mapper, you rely on your
own objects, XML, and SQL. There is little to
learn that you don't already know. With the
MyBatis data mapper, you have the full power of
both SQL and stored procedures at your fingertips.

The MyBatis project is developed and maintained by
a team that includes the original creators of the
"iBATIS" data mapper. The Apache project was retired
and continued here.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-3-%{name}-%{version}

%pom_change_dep ognl:ognl org.apache.commons:commons-ognl:4.0-SNAPSHOT
%patch0 -p1

%pom_remove_plugin :maven-pdf-plugin
%pom_remove_plugin :maven-shade-plugin

sed -i 's/\r//' LICENSE NOTICE

%{mvn_file} :%{name} %{name}

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8 \
%endif
	-Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
