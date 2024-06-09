#
# spec file for package atinject
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


Name:           atinject
Version:        1.0.5
Release:        0
Summary:        Dependency injection specification for Java (JSR-330)
License:        Apache-2.0
URL:            https://github.com/jakartaee/inject/
Source0:        https://github.com/jakartaee/inject/archive/%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
Obsoletes:      %{name}-tck
BuildArch:      noarch

%description
This package specifies a means for obtaining objects in such a way as
to maximize reusability, testability and maintainability compared to
traditional approaches such as constructors, factories, and service
locators (e.g., JNDI). This process, known as dependency injection, is
beneficial to most nontrivial applications.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n inject-%{version}
cp %{SOURCE1} build.xml

%build
%{ant} package javadoc

%install
# jars
install -dm 755 %{buildroot}%{_javadir}/javax.inject
install -m 0644 target/javax.inject-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
(cd %{buildroot}%{_javadir}/javax.inject && ln -s ../%{name}.jar .)
%add_maven_depmap javax.inject:javax.inject:%{version} %{name}.jar

# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt NOTICE.md
%{_javadir}/javax.inject

%files javadoc
%{_javadocdir}/%{name}

%changelog
