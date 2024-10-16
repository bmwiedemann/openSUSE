#
# spec file for package google-errorprone-annotations
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


%global source_name error-prone
%global artifactId error_prone_annotations
%global group_name google-errorprone
# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Name:           %{group_name}-annotations
Version:        2.26.1
Release:        0
Summary:        error-prone annotations
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://errorprone.info
Source0:        %{source_name}-%{version}.tar.xz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
Google Error Prone is a static analysis tool for Java that catches
common programming mistakes at compile-time.

This package contains Google Error Prone annotations

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{source_name}-%{version}
cp %{SOURCE1} annotations/build.xml

%build
pushd annotations
%{ant} -Dproject.version=%{version} jar javadoc
popd

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{group_name}
install -p -m 0644 annotations/target/%{artifactId}-%{version}.jar %{buildroot}%{_javadir}/%{group_name}/annotations.jar
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{group_name}
%{mvn_install_pom} annotations/pom.xml %{buildroot}%{_mavenpomdir}/%{group_name}/annotations.pom
%add_maven_depmap %{group_name}/annotations.pom %{group_name}/annotations.jar
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr annotations/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license COPYING

%files javadoc
%{_javadocdir}/%{name}
%license COPYING
%doc README.md

%changelog
