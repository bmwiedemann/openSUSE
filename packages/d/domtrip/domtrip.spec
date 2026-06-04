#
# spec file for package domtrip
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           domtrip
Version:        1.5.2
Release:        0
Summary:        Lossless XML Editing for Java
License:        EPL-2.0
URL:            https://github.com/maveniverse/domtrip
Source0:        https://github.com/maveniverse/%{name}/archive/refs/tags/%{version}.tar.gz
Patch0:         %{name}-ant-build-system.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildRequires:  jaxen
BuildArch:      noarch

%description
DomTrip is a Java library for lossless XML editing that preserves every detail of your XML
documents during round-trip operations. Perfect for configuration file editing, document
transformation, and any scenario where maintaining original formatting is crucial.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch -P 0 -p1

%pom_xpath_inject pom:project/pom:properties "
<nisse.jgit.dynamicVersion>%{version}</nisse.jgit.dynamicVersion>"

%build
mkdir -p lib
build-jar-repository -s lib jaxen
ant jar javadoc

%install
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
for i in core jaxen maven; do
  install -pm 0644 ${i}/target/%{name}-${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${i}.jar
  %{mvn_install_pom} ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar
  cp -r ${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${i}
done
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
