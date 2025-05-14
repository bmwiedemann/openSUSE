#
# spec file for package jakarta-annotations
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


# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Name:           jakarta-annotations
Version:        3.0.0
Release:        0
Summary:        Jakarta Annotations
License:        EPL-2.0 OR GPL-2.0-with-classpath-exception
URL:            https://github.com/jakartaee/common-annotations-api
Source0:        https://github.com/jakartaee/common-annotations-api/archive/%{version}/common-annotations-api-%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
Jakarta Annotations defines a collection of annotations representing
common semantic concepts that enable a declarative style of programming
that applies across a variety of Java technologies.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n common-annotations-api-%{version}
cp %{SOURCE1} api/build.xml

%build
pushd api
%{ant} package javadoc
popd

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 api/target/jakarta.annotation-api-%{version}.jar %{buildroot}%{_javadir}/%{name}/jakarta.annotation-api.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} api/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/jakarta.annotation-api.pom
%add_maven_depmap %{name}/jakarta.annotation-api.pom %{name}/jakarta.annotation-api.jar
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
