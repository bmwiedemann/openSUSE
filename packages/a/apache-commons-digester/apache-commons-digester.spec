#
# spec file for package apache-commons-digester
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


%define base_name       digester
%define short_name      commons-%{base_name}
%bcond_with tests
Name:           apache-%{short_name}
Version:        2.1
Release:        0
Summary:        Jakarta Commons Digester Package
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://apache.apache.org/commons/digester/
Source0:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  commons-beanutils
BuildRequires:  commons-logging
BuildRequires:  fdupes
BuildRequires:  javapackages-local
Requires:       mvn(commons-beanutils:commons-beanutils)
Requires:       mvn(commons-logging:commons-logging)
Provides:       %{short_name} = %{version}-%{release}
Obsoletes:      %{short_name} < %{version}-%{release}
Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{version}-%{release}
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit
BuildRequires:  commons-collections
%endif

%description
The goal of the Jakarta Commons Digester project is to create and
maintain an XML to Java object mapping package written in the Java
language to be distributed under the ASF license.

%package javadoc
Summary:        Javadoc for apache-commons-digester
Group:          Development/Libraries/Java

%description javadoc
The goal of the Jakarta Commons Digester project is to create and
maintain a XML -> Java object mapping package written in the Java
language to be distributed under the ASF license.

This package contains the javadoc documentation for the Jakarta Commons
Digester Package.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE1} build.xml

mkdir -p lib
build-jar-repository -s lib commons-beanutils commons-logging
%if %{with tests}
  build-jar-repository -s lib commons-collections
%endif

%pom_remove_parent

%build
ant \
%if %{without tests}
    -Dtest.skip=true \
%endif
    jar javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar
# pom
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a org.apache.commons:%{short_name}
# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}/%{name}/

%files -f .mfiles
%license LICENSE.txt
%doc NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
