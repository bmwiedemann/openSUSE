#
# spec file for package jakarta-servlet
#
# Copyright (c) 2021 SUSE LLC
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


%global artifactId jakarta.servlet-api
Name:           jakarta-servlet
Version:        5.0.0
Release:        0
Summary:        Server-side API for handling HTTP requests and responses
License:        Apache-2.0 AND (EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0)
URL:            https://github.com/eclipse-ee4j/servlet-api
Source0:        https://github.com/eclipse-ee4j/servlet-api/archive/%{version}-RELEASE/servlet-api-%{version}.tar.gz
Source1:        %{name}-api-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
Jakarta Servlet defines a server-side API for handling HTTP requests
and responses.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n servlet-api-%{version}-RELEASE
cp LICENSE.md api/src/main/resources/META-INF/
cp NOTICE.md api/src/main/resources/META-INF/

# remove unnecessary dependency on parent POM
%pom_remove_parent . api

cp %{SOURCE1} api/build.xml

# remove unnecessary maven plugins
%pom_remove_plugin -r :formatter-maven-plugin
%pom_remove_plugin -r :impsort-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin

%build
pushd api
%{ant} jar javadoc
popd

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 api/target/%{artifactId}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{artifactId}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 api/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{artifactId}.pom
%add_maven_depmap %{name}/%{artifactId}.pom %{name}/%{artifactId}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr api/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.md NOTICE.md

%changelog
