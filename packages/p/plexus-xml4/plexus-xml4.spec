#
# spec file for package plexus-xml4
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global base_name plexus-xml
%global version_suffix 4
Name:           %{base_name}%{version_suffix}
Version:        4.1.0
Release:        0
Summary:        Plexus XML Utilities
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/%{base_name}
Source0:        https://github.com/codehaus-plexus/%{base_name}/archive/refs/tags/%{base_name}-%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 17
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven4-bootstrap
BuildRequires:  xz
BuildArch:      noarch

%description
A collection of various utility classes to ease working with XML in Maven 4.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{base_name}-%{base_name}-%{version}
cp -p %{SOURCE1} build.xml

%build
mkdir -p lib
build-jar-repository -s lib \
  maven/maven-api-xml \
  maven/maven-xml
%{ant} \
  jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/plexus
install -pm 0644 target/%{base_name}-%{version}.jar %{buildroot}%{_javadir}/plexus/xml.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/plexus
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/plexus/xml.pom
%add_maven_depmap plexus/xml.pom plexus/xml.jar -v %{version_suffix},%{version}
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE.txt NOTICE.txt

%files javadoc
%license LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
