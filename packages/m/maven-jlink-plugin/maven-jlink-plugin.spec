#
# spec file for package maven-jlink-plugin
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


%global basever 3.0.0
%global opt alpha
%global optver 1
Name:           maven-jlink-plugin
Version:        %{basever}~%{opt}%{optver}
Release:        0
Summary:        Apache Maven JLink Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/plugins/%{name}/
Source0:        https://archive.apache.org/dist/maven/plugins/%{name}-%{basever}-%{opt}-%{optver}-source-release.zip
Patch0:         maven-jlink-plugin-plexus-languages-1.0.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-archiver)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-java)
BuildArch:      noarch

%description
The Maven JLink Plugin is intended to create Modular Run-Time Images.
http://openjdk.java.net/jeps/282, http://openjdk.java.net/jeps/220

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{basever}-%{opt}-%{optver}
%patch -P 0 -p1

%pom_xpath_remove pom:project/pom:parent/pom:relativePath
%pom_add_dep org.apache.maven:maven-compat:\${mavenVersion}
%pom_add_dep org.apache.maven.shared:maven-shared-utils

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
