#
# spec file for package servletapi4
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define	base_name	servletapi
%define full_name	jakarta-%{base_name}
Name:           servletapi4
Version:        4.0.4
Release:        0
Summary:        Java servlet and JSP implementation classes
License:        Apache-1.1
Group:          Development/Libraries/Java
URL:            https://jakarta.apache.org/tomcat/
Source:         %{full_name}-4-src.tar.gz
Patch160:       java160_build.patch
BuildRequires:  ant >= 1.2
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  xml-commons-apis
Provides:       servlet = %{version}
Obsoletes:      servlet22 < %{version}
Obsoletes:      servlet4 < %{version}
Provides:       servlet22 = %{version}
Provides:       servlet4 = %{version}
BuildArch:      noarch

%description
This subproject contains the source code for the implementation classes
of the Java Servlet and JSP APIs (packages javax.servlet).

%package javadoc
Summary:        Javadoc for servletapi4
Group:          Development/Libraries/Java

%description javadoc
This subproject contains the source code for the implementation classes
of the Java Servlet and JSP APIs (packages javax.servlet). This package
contains the javadoc documentation for the Java Servlet and JSP APIs.

%prep
%setup -q -n %{full_name}-4-src
%patch -P 160 -p1

%build
ant dist -Dservletapi.build=build -Dservletapi.dist=dist

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/lib/servlet.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/docs/api/* %{buildroot}%{_javadocdir}/%{name}

%files
%license LICENSE
%doc README.txt
%{_javadir}/*

%files javadoc
%{_javadocdir}/%{name}

%changelog
