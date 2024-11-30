#
# spec file for package glassfish-servlet-api
#
# Copyright (c) 2024 SUSE LLC
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


%global artifactId javax.servlet-api
Name:           glassfish-servlet-api
Version:        4.0.1
Release:        0
Summary:        Java Servlet API
License:        Apache-2.0 AND (CDDL-1.0 OR GPL-2.0-only WITH Classpath-exception-2.0)
Group:          Development/Libraries/Java
URL:            http://servlet-spec.java.net
Source0:        https://github.com/javaee/servlet-spec/archive/%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        glassfish-servlet-api-build.xml
Source3:        glassfish-servlet-api-build.properties
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
The javax.servlet package contains a number of classes
and interfaces that describe and define the contracts between
a servlet class and the runtime environment provided for
an instance of such a class by a conforming servlet container.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n servlet-spec-%{version}
%pom_remove_plugin :maven-remote-resources-plugin
%pom_remove_plugin :maven-javadoc-plugin
cp -p %{SOURCE1} src/main/resources/META-INF/
cp -p %{SOURCE2} build.xml
cp -p %{SOURCE3} build.properties

# README contains also part of javax.servlet-api license
cp -p src/main/resources/META-INF/README .

%build
ant package javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{artifactId}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a javax.servlet:servlet-api,org.apache.geronimo.specs:geronimo-servlet_3.0_spec,org.eclipse.jetty.orbit:javax.servlet
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README
%license src/main/resources/META-INF/LICENSE-2.0.txt

%files javadoc
%{_javadocdir}/%{name}
%doc README
%license src/main/resources/META-INF/LICENSE-2.0.txt

%changelog
