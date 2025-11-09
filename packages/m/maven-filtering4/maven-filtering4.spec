#
# spec file for package maven-filtering4
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


%global base_name maven-filtering
%global version_suffix 4
%global file_version 4.0.0-beta-2-SNAPSHOT
Name:           %{base_name}%{version_suffix}
Version:        4.0.0~20250928.git84993b0
Release:        0
Summary:        Shared component providing resource filtering
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/shared/%{name}/index.html
Source0:        %{base_name}-%{version}.tar.xz
Source1:        %{name}-build.xml
Patch0:         %{name}-java8compat.patch
Patch1:         0001-Be-gracious-with-binary-files-among-the-resources-to.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 17
BuildRequires:  javapackages-local
BuildRequires:  maven4-lib
BuildRequires:  plexus-build-api0
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-utils
BuildRequires:  slf4j2
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildArch:      noarch

%description
These Plexus components have been built from the filtering process/code in
Maven Resources Plugin. The goal is to provide a shared component for all
plugins that needs to filter resources.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{base_name}-%{version}
cp %{SOURCE1} build.xml
%patch -P 0 -p1
%patch -P 1 -p1

%pom_xpath_remove pom:project/pom:parent/pom:relativePath

%pom_xpath_set pom:project/pom:properties/pom:slf4jVersion 2

%build
mkdir -p lib
build-jar-repository -s lib \
    maven/maven-api-annotations \
    maven/maven-api-core \
    maven/maven-api-di \
    maven/maven-api-model \
    maven/maven-api-settings \
    plexus/utils \
    plexus/interpolation \
    plexus/plexus-build-api0 \
    slf4j/api-2

ant -Dproject.version=%{version} \
  jar javadoc

%{mvn_file} :{*} %{base_name}/@1
%{mvn_compat_version} : %{version_suffix} %{file_version}

%install

%{mvn_artifact} pom.xml target/%{base_name}-%{version}.jar
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE NOTICE

%changelog
