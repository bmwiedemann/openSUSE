#
# spec file for package jakarta-expression-language
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


%global base_name expression-language
Name:           jakarta-%{base_name}
Version:        6.0.1
Release:        0
Summary:        Jakarta Expression Language
License:        EPL-2.0
Group:          Development/Libraries/Java
URL:            https://jakarta.ee/specifications/base_name
Source0:        https://github.com/jakartaee/%{base_name}/archive/refs/tags/%{version}-RELEASE-api.tar.gz
Source1:        %{name}-build.xml
Patch0:         no-anonymous-inner-classes.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 17
BuildRequires:  javapackages-local >= 6
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
Jakarta Expression Language defines an expression language for Java applications.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{base_name}-%{version}-RELEASE-api
cp %{SOURCE1} api/build.xml
%patch -P 0 -p1

%build
pushd api
mkdir -p lib
ant package javadoc
popd

%install
#jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 api/target/jakarta.enterprise.lang-model-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} api/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr api/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.md NOTICE.md

%changelog
