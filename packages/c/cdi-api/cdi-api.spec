#
# spec file for package cdi-api
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


Name:           cdi-api
Version:        2.0.2
Release:        0
Summary:        Contexts and Dependency Injection for Java EE
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://seamframework.org/Weld
Source0:        cdi-%{version}.tar.xz
Source1:        %{name}-build.xml
Patch0:         0001-Remove-dependency-on-glassfish-el.patch
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  jboss-interceptors-1.2-api
BuildArch:      noarch

%description
APIs for JSR-299: Contexts and Dependency Injection for Java EE

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n cdi-%{version}
%patch -P 0 -p1
cp %{SOURCE1} api/build.xml

# Use newer version of interceptors API
%pom_change_dep "jakarta.interceptor:jakarta.interceptor-api" "org.jboss.spec.javax.interceptor:jboss-interceptors-api_1.2_spec" api
%pom_change_dep "jakarta.inject:jakarta.inject-api" "javax.inject:javax.inject" api

%pom_remove_dep :jakarta.el-api api

%build
pushd api/
mkdir -p lib
build-jar-repository -s lib javax.inject jboss-interceptors-1.2-api
%{ant} jar javadoc
popd

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 api/target/jakarta.enterprise.cdi-api-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
install -dm 0755 %{buildroot}%{_javadir}/javax.enterprise.inject
ln -sf ../%{name}/%{name}.jar %{buildroot}%{_javadir}/javax.enterprise.inject/%{name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} api/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar -a "javax.enterprise:cdi-api"
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr api/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%{_javadir}/javax.enterprise.inject
%license LICENSE.txt
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt

%changelog
