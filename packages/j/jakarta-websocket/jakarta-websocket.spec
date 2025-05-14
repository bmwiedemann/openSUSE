#
# spec file for package jakarta-websocket
#
# Copyright (c) 2025 SUSE LLC
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


%global short_name websocket
Name:           jakarta-%{short_name}
Version:        2.2.0
Release:        0
Summary:        Jakarta WebSocket
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://projects.eclipse.org/projects/ee4j.%{short_name}
Source0:        https://github.com/jakartaee/%{short_name}/archive/refs/tags/%{version}-RELEASE.tar.gz
Source1:        %{name}-build.tar.xz
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
Jakarta WebSocket defines a set of Java APIs for the development of WebSocket
applications.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{short_name}-%{version}-RELEASE -a1

%build
ant -f api/build.xml jar javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 api/client/target/jakarta.websocket-client-api-%{version}.jar %{buildroot}%{_javadir}/%{name}/jakarta.websocket-client-api.jar
install -pm 0644 api/server/target/jakarta.websocket-api-%{version}.jar %{buildroot}%{_javadir}/%{name}/jakarta.websocket-api.jar
# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} api/client/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/jakarta.websocket-client-api.pom
%add_maven_depmap %{name}/jakarta.websocket-client-api.pom %{name}/jakarta.websocket-client-api.jar
%{mvn_install_pom} api/server/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/jakarta.websocket-api.pom
%add_maven_depmap %{name}/jakarta.websocket-api.pom %{name}/jakarta.websocket-api.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r api/client/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/jakarta.websocket-client-api
cp -r api/server/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/jakarta.websocket-api
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license {NOTICE,LICENSE}.md
%doc websocket-1.1-changes.txt {SECURITY,CONTRIBUTING,README}.md

%files javadoc
%{_javadocdir}/%{name}
%license {NOTICE,LICENSE}.md

%changelog
