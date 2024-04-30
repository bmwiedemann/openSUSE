#
# spec file for package apiguardian
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
Name:           apiguardian
Version:        1.1.2
Release:        0
Summary:        API Guardian Java annotation
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/apiguardian-team/apiguardian
Source0:        https://github.com/apiguardian-team/apiguardian/archive/r%{version}.tar.gz
Source1:        %{name}-build.xml
Source100:      https://repo1.maven.org/maven2/org/apiguardian/apiguardian-api/%{version}/apiguardian-api-%{version}.pom
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
API Guardian indicates the status of an API element and therefore its
level of stability as well.  It is used to annotate public types,
methods, constructors, and fields within a framework or application in
order to publish their API status and level of stability and to
indicate how they are intended to be used by consumers of the API.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-r%{version}
find -name \*.jar -delete
cp -p %{SOURCE1} .

mv src/module/java/*/module-info.java src/main/java/

%build
%{ant} -f %{name}-build.xml jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/apiguardian-api-%{version}.jar %{buildroot}%{_javadir}/%{name}/apiguardian-api.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} %{SOURCE100} %{buildroot}%{_mavenpomdir}/%{name}/apiguardian-api.pom
%add_maven_depmap %{name}/apiguardian-api.pom %{name}/apiguardian-api.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}
install -pdm 0755 target/site/apidocs %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
