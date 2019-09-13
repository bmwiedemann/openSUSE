#
# spec file for package apache-commons-jxpath
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


%define base_name       jxpath
%define short_name      commons-%{base_name}
Name:           apache-%{short_name}
Version:        1.3
Release:        0
Summary:        Simple XPath interpreter
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:         %{short_name}-mockrunner.patch
Patch1:         build.xml.patch
Patch2:         %{short_name}-%{version}-manifest.patch
BuildRequires:  ant
BuildRequires:  apache-commons-beanutils
BuildRequires:  fdupes
BuildRequires:  glassfish-servlet-api
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  jdom
BuildRequires:  tomcat-jsp-2_3-api
Requires:       java >= 1.8
Requires:       jdom >= 1.0
Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{version}-%{release}
Provides:       %{short_name} = %{version}-%{release}
BuildArch:      noarch

%description
Defines a simple interpreter of an expression language called XPath.
JXPath applies XPath expressions to graphs of objects of all kinds:
JavaBeans, Maps, Servlet contexts, DOM etc, including mixtures thereof.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0 -p1
%patch1
%patch2 -p1

%pom_remove_parent

%build
mkdir -p target/lib
build-jar-repository -s target/lib commons-beanutils jdom glassfish-servlet-api tomcat-jsp-2.3-api
%{ant}  \
	-Dant.build.javac.source=8 -Dant.build.javac.target=8 \
	-lib %{_javadir} \
	jar javadoc

sed -i "s/@name@/%{short_name}/g" src/conf/MANIFEST.MF
sed -i "s/@fragment@/%{base_name}/g" src/conf/MANIFEST.MF
sed -i "s/@version@/%{version}/g" src/conf/MANIFEST.MF
jar ufm target/%{short_name}.jar src/conf/MANIFEST.MF

%install
#jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 644 target/%{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -Dpm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a org.apache.commons:%{short_name}
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt
%{_javadir}/%{short_name}.jar

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}

%changelog
