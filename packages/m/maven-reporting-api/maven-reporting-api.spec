#
# spec file for package maven-reporting-api
#
# Copyright (c) 2022 SUSE LLC
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


Name:           maven-reporting-api
Version:        3.1.0
Release:        0
Summary:        API to manage report generation
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://maven.apache.org/shared/maven-reporting-api
Source0:        https://dlcdn.apache.org/maven/reporting/%{name}-%{version}-source-release.zip
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  maven-doxia-sink-api
BuildRequires:  unzip
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildArch:      noarch

%description
API to manage report generation. Maven-reporting-api is included in Maven 2.x
core distribution, but moved to shared components to achieve report decoupling
from Maven 3 core.

This is a replacement package for maven-shared-reporting-api

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} LICENSE.txt
cp %{SOURCE2} build.xml

%pom_remove_parent

# Previous package provides groupIds org.apache.maven.shared and org.apache.maven.reporting
%{mvn_alias} : org.apache.maven.shared:maven-reporting-api

%build
mkdir -p lib
build-jar-repository -s lib \
    maven-doxia/doxia-sink-api
%{ant} jar javadoc

%mvn_artifact pom.xml target/%{name}-%{version}.jar

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
