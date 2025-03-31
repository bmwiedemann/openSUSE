#
# spec file for package google-gson
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


Name:           google-gson
Version:        2.8.9
Release:        0
Summary:        Java lib for conversion of Java objects into JSON representation
License:        Apache-2.0
URL:            https://github.com/google/gson
Source0:        https://github.com/google/gson/archive/gson-parent-%{version}.tar.gz
Source1:        %{name}-build.tar.xz
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  glassfish-annotation-api
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildRequires:  jsr-305
# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Requires:       java-headless >= 1.8
BuildArch:      noarch

%description
Gson is a Java library that can be used to convert a Java object into its
JSON representation. It can also be used to convert a JSON string into an
equivalent Java object. Gson can work with arbitrary Java objects including
pre-existing objects that you do not have source-code of.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n gson-gson-parent-%{version} -a1

%build
mkdir -p lib
build-jar-repository -s lib jsr-305 glassfish-annotation-api
ant package javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 gson/target/gson-%{version}.jar %{buildroot}%{_javadir}/%{name}/gson.jar
install -pm 0644 extras/target/gson-extras-%{version}.jar %{buildroot}%{_javadir}/%{name}/gson-extras.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%mvn_install_pom gson/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/gson.pom
%add_maven_depmap %{name}/gson.pom %{name}/gson.jar
%mvn_install_pom extras/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/gson-extras.pom
%add_maven_depmap %{name}/gson-extras.pom %{name}/gson-extras.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
for i in gson extras; do
  cp -r ${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${i}
done
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README.md CHANGELOG.md UserGuide.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
