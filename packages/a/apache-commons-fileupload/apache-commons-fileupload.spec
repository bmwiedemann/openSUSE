#
# spec file for package apache
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


%global base_name fileupload
%global short_name commons-%{base_name}
%bcond_without  portlet
Name:           apache-%{short_name}
Version:        1.4
Release:        0
Summary:        API to work with HTML file upload
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/fileupload/
Source0:        http://archive.apache.org/dist/commons/fileupload/source/commons-fileupload-%{version}-src.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  fdupes
BuildRequires:  glassfish-servlet-api
BuildRequires:  javapackages-local
Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{version}-%{release}
Provides:       %{short_name} = %{version}-%{release}
Obsoletes:      %{short_name} < %{version}-%{release}
Requires:       mvn(commons-io:commons-io)
BuildArch:      noarch
%if %{with portlet}
BuildRequires:  apache-portlet-1_0-api
%endif

%description
The javax.servlet package lacks support for RFC-1867, HTML file
upload.  This package provides a simple to use API for working with
such data.  The scope of this package is to create a package of Java
utility classes to read multipart/form-data within a
javax.servlet.http.HttpServletRequest.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n commons-fileupload-%{version}-src
cp %{SOURCE1} build.xml
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' NOTICE.txt

%if %{with portlet}
# fix gId
sed -i "s|<groupId>portlet-api</groupId>|<groupId>javax.portlet</groupId>|" pom.xml
%else
%pom_remove_dep portlet-api:portlet-api
%pom_xpath_remove pom:properties/pom:commons.osgi.import
%pom_xpath_remove pom:properties/pom:commons.osgi.dynamicImport
rm -r src/main/java/org/apache/commons/fileupload/portlet
%endif

%{pom_remove_parent}

%build
mkdir -p lib
build-jar-repository -s lib \
	commons-io \
	glassfish-servlet-api
%if %{with portlet}
build-jar-repository -s lib \
	portlet-api
%endif
# tests fail to compile because they use an obsolete version of servlet API (2.4)
%{ant} \
	-Dtest.skip=true \
	jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -sf %{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar -a org.apache.commons:commons-fileupload
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%{_javadir}/%{name}.jar

%files javadoc
%license LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
