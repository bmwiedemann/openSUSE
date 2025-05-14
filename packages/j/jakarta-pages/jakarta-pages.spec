#
# spec file for package jakarta-pages
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


%global short_name pages
%global artifact_name jakarta.servlet.jsp-api
Name:           jakarta-%{short_name}
Version:        4.0.0
Release:        0
Summary:        Jakarta Server Pages
License:        BSD-3-Clause OR EPL-2.0
Group:          Development/Libraries/Java
URL:            http://eclipse.org/ee4j/jsp
Source0:        https://github.com/jakartaee/%{short_name}/archive/refs/tags/%{version}-RELEASE.tar.gz
Source1:        %{name}-build.xml
Patch0:         %{name}-source8.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  jakarta-expression-language
BuildRequires:  jakarta-servlet
BuildRequires:  javapackages-local >= 6
BuildConflicts: java-devel < 17
BuildArch:      noarch

%description
Jakarta Pages defines a template engine for web applications.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{short_name}-%{version}-RELEASE -p1

cp %{SOURCE1} api/build.xml

%build
pushd api
mkdir -p lib
build-jar-repository -s lib jakarta-expression-language jakarta-servlet
ant jar javadoc
popd

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 api/target/%{artifact_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{artifact_name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} api/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{artifact_name}.pom
%add_maven_depmap %{name}/%{artifact_name}.pom %{name}/%{artifact_name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr api/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license {NOTICE,LICENSE}.md
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license {NOTICE,LICENSE}.md

%changelog
