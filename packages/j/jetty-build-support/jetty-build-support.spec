#
# spec file for package jetty-build-support
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


Name:           jetty-build-support
Version:        1.5
Release:        0
Summary:        Jetty build support files
License:        Apache-2.0 OR EPL-1.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/jetty/
Source0:        %{name}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        http://www.eclipse.org/org/documents/epl-v10.html
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  xz
BuildRequires:  mvn(org.apache.maven.enforcer:enforcer-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-toolchain:pom:)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
BuildArch:      noarch

%description
Build Support for Jetty. Contains enforcer rules, PMD rulesets, etc.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description    javadoc
%{summary}.

%prep
%setup -q
cp %{SOURCE1} .
cp %{SOURCE2} .

%pom_remove_plugin :maven-javadoc-plugin

%pom_xpath_set pom:properties/pom:maven.version 3.8.1
%pom_remove_dep :maven-project

%pom_xpath_remove pom:project/pom:parent/pom:relativePath
%pom_add_dep org.apache.maven.shared:maven-shared-utils

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE-2.0.txt epl-v10.html

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.txt epl-v10.html

%changelog
