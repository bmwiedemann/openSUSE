#
# spec file for package xmvn5-parent
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


%global parent xmvn
%global version_suffix 5
%global subname parent
Name:           %{parent}%{version_suffix}-%{subname}
Version:        5.1.0
Release:        0
Summary:        XMvn Parent POM
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://fedora-java.github.io/xmvn/
Source0:        %{parent}-%{version}.tar.xz
BuildRequires:  javapackages-local
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildArch:      noarch

%description
This package provides XMvn parent POM.

%prep
%setup -q -n %{parent}-%{version}

%autopatch -p1

%pom_remove_plugin -r :maven-site-plugin

# Upstream code quality checks, not relevant when building RPMs
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :spotless-maven-plugin

# remove dependency plugin maven-binaries execution
# we provide apache-maven by symlink
%pom_xpath_remove "pom:executions/pom:execution[pom:id[text()='maven-binaries']]"

# Normalize slf4j version to 2
%pom_xpath_set pom:project/pom:properties/pom:slf4jVersion 2 xmvn-parent

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{parent}
install -pm 0644 %{parent}-%{subname}/pom.xml %{buildroot}%{_mavenpomdir}/%{parent}/%{parent}-%{subname}.pom
%add_maven_depmap %{parent}/%{parent}-%{subname}.pom -v %{version_suffix},%{version}

%files -f .mfiles
%license LICENSE NOTICE
%doc AUTHORS README.md

%changelog
