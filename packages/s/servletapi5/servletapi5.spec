#
# spec file for package servletapi5
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define	base_name	servletapi
%define full_name	jakarta-%{base_name}
Name:           servletapi5
Version:        5.0.18
Release:        0
Summary:        Java servlet and JSP implementation classes
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://jakarta.apache.org/tomcat/
Source:         %{full_name}-5-src.tar.gz
#!BuildIgnore:  xml-commons xml-commons-resolver xerces-j2 xml-commons-apis
#!BuildIgnore:  xml-commons-jaxp-1.3-apis
BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  xml-commons-apis-bootstrap
Requires(post): update-alternatives
Provides:       servlet = %{version}
Provides:       servlet24 = %{version}
Provides:       servlet5 = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This subproject contains the source code for the implementation classes
of the Java Servlet and JSP APIs (packages javax.servlet).

%prep
%setup -q -c -T -a 0 -n %{full_name}-5-src

%build
# Fix us a license file first
cp -f jakarta-tomcat-%{version}-src/jakarta-servletapi-5/jsr154/LICENSE .
cd jakarta-tomcat-%{version}-src/jakarta-servletapi-5
find . -type f -name "*.jar" -exec rm -f {} \;
pushd .
cd jsr154
ant jar examples -Dservletapi.build=build -Dservletapi.dist=dist -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6
popd
pushd .
cd jsr152
ant jar examples -Dservletapi.build=build -Dservletapi.dist=dist -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6
popd

%install
cd jakarta-tomcat-%{version}-src/jakarta-servletapi-5
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 jsr152/dist/lib/jsp-api.jar %{buildroot}%{_javadir}/jspapi-%{version}.jar
install -m 644 jsr154/dist/lib/servlet-api.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
# alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
ln -sf %{_sysconfdir}/alternatives/servlet.jar %{buildroot}%{_javadir}/servlet.jar

%post
update-alternatives --install %{_javadir}/servlet.jar servlet %{_javadir}/%{name}-%{version}.jar 50

%postun
if [ "$1" = "0" ]; then
    update-alternatives --remove servlet %{_javadir}/%{name}-%{version}.jar
fi

%files
%defattr(-,root,root)
%doc LICENSE
%{_javadir}/*
%{_javadir}/servlet.jar
%ghost %{_sysconfdir}/alternatives/servlet.jar

%changelog
