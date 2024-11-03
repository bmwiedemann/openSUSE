#
# spec file for package jakarta-servlet
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


%global short_name servlet
%global artifactId jakarta.servlet-api
Name:           jakarta-%{short_name}
Version:        6.1.0
Release:        0
Summary:        Server-side API for handling HTTP requests and responses
License:        Apache-2.0 AND (EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0)
Group:          Development/Libraries/Java
URL:            https://projects.eclipse.org/projects/ee4j.%{short_name}
Source0:        https://github.com/jakartaee/%{short_name}/archive/refs/tags/%{version}-RELEASE.tar.gz
Source1:        %{name}-api-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
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
%setup -q -n %{short_name}-%{version}-RELEASE
mkdir -p api/src/main/resources/META-INF/
cp {NOTICE,LICENSE}.md api/src/main/resources/META-INF/

cp %{SOURCE1} api/build.xml

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
%{mvn_install_pom} api/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{artifactId}.pom
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
