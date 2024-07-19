#
# spec file for package xmvn-parent
#
# Copyright (c) 2024 SUSE LLC
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
%global subname parent
Name:           %{parent}-%{subname}
Version:        4.2.0
Release:        0
Summary:        XMvn Parent POM
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://fedora-java.github.io/xmvn/
Source0:        https://github.com/fedora-java/%{parent}/releases/download/%{version}/%{parent}-%{version}.tar.xz
Patch0:         0001-Do-not-leave-a-stray-options-file-in-the-generated-j.patch
Patch1:         0002-Make-metadata-UUIDs-reproducible-if-SOURCE_DATE_EPOC.patch
Patch2:         0003-Reproducible-javadoc-notimestamp-option-and-some-aut.patch
BuildRequires:  javapackages-local
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
Provides:       %{name}-pom
Obsoletes:      %{name}-pom
BuildArch:      noarch

%description
This package provides XMvn parent POM.

%prep
%setup -q -n %{parent}-%{version}

%autopatch -p1

%pom_remove_plugin -r :maven-site-plugin

# Upstream code quality checks, not relevant when building RPMs
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :jacoco-maven-plugin

# remove dependency plugin maven-binaries execution
# we provide apache-maven by symlink
%pom_xpath_remove "pom:executions/pom:execution[pom:id[text()='maven-binaries']]"

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{parent}
install -pm 0644 xmvn-parent/pom.xml %{buildroot}%{_mavenpomdir}/%{parent}/%{name}.pom
%add_maven_depmap %{parent}/%{name}.pom

%files -f .mfiles
%license LICENSE NOTICE
%doc AUTHORS README.md

%changelog
