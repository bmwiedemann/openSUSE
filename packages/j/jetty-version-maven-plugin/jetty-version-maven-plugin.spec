#
# spec file for package jetty-version-maven-plugin
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


Name:           jetty-version-maven-plugin
Version:        1.0.10
Release:        0
Summary:        Jetty version management Maven plugin
License:        Apache-2.0 OR EPL-1.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org/jetty/
Source0:        %{name}-%{version}.tar.xz
Patch0:         jetty-version-maven-plugin-mpt4.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  xz
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-toolchain:pom:)
BuildArch:      noarch

%description
Jetty version management Maven plugin

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description    javadoc
%{summary}.

%prep
%setup -q
%patch -P 0 -p1
%pom_change_dep org.apache.maven::2.2.1 ::3.9.9:provided
%pom_change_dep :maven-project :maven-core

%pom_add_dep org.apache.maven.plugin-tools:maven-plugin-annotations:3.15.1:provided

# we have java.util stuff in JVM directly now
# https://bugs.eclipse.org/bugs/show_bug.cgi?id=401163
sed -i 's|edu.emory.mathcs.backport.||' \
    src/main/java/org/eclipse/jetty/toolchain/version/Release.java

%pom_xpath_remove pom:project/pom:parent/pom:relativePath

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
