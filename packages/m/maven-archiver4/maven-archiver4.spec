#
# spec file for package maven-archiver4
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


%global base_name maven-archiver
%global base_ver 4.0.0
%global ver_suffix 4
%global beta_ver 5
%global file_ver %{base_ver}-beta-%{beta_ver}
%bcond_with tests
Name:           %{base_name}%{ver_suffix}
Version:        %{base_ver}~beta%{beta_ver}
Release:        0
Summary:        Maven Archiver
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/shared/maven-archiver/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/shared/%{base_name}/%{file_ver}/%{base_name}-%{file_ver}-source-release.zip
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 17
BuildRequires:  javapackages-local >= 6
BuildRequires:  maven4-lib
BuildRequires:  plexus-archiver >= 4.2.0
BuildRequires:  plexus-interpolation >= 1.25
BuildRequires:  plexus-utils
BuildRequires:  unzip
BuildArch:      noarch

%description
The Maven Archiver is used by other Maven plugins
to handle packaging

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{base_name}-%{file_ver}
cp %{SOURCE1} build.xml

%pom_xpath_remove pom:project/pom:parent/pom:relativePath

%build
mkdir -p lib
build-jar-repository -s lib \
  maven/maven-api-core \
  maven/maven-api-model \
  maven/maven-api-xml \
  plexus/archiver \
  plexus/interpolation \
  plexus/utils

ant jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{base_name}
install -pm 0644 target/%{base_name}-%{file_ver}.jar %{buildroot}%{_javadir}/%{base_name}/%{base_name}-%{ver_suffix}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{base_name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{base_name}/%{base_name}-%{ver_suffix}.pom
%add_maven_depmap %{base_name}/%{base_name}-%{ver_suffix}.pom %{base_name}/%{base_name}-%{ver_suffix}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc NOTICE

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE
%doc NOTICE

%changelog
