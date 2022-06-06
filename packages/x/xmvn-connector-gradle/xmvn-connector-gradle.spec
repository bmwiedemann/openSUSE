#
# spec file
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


%global parent xmvn
%global subname connector-gradle
Name:           %{parent}-%{subname}
Version:        4.0.0~20220507.11a6169
Release:        0
Summary:        XMvn Connector for Gradle
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://fedora-java.github.io/xmvn/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  fdupes
# Build this one with the bootstrap package in order to avoid build cycles
BuildRequires:  maven-local
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.apache.ivy:ivy)
BuildRequires:  mvn(org.codehaus.groovy:groovy-all)
BuildRequires:  mvn(org.fedoraproject.xmvn:xmvn-api)
BuildRequires:  mvn(org.gradle:gradle-base-services) >= 4.4.1
BuildRequires:  mvn(org.gradle:gradle-base-services-groovy) >= 4.4.1
BuildRequires:  mvn(org.gradle:gradle-core) >= 4.4.1
BuildRequires:  mvn(org.gradle:gradle-dependency-management) >= 4.4.1
BuildRequires:  mvn(org.gradle:gradle-resources) >= 4.4.1
BuildRequires:  mvn(org.slf4j:slf4j-api)
#!BuildRequires: gradle-bootstrap groovy-bootstrap gpars-bootstrap
BuildArch:      noarch

%description
This package provides XMvn Connector for Gradle, which provides
integration of Gradle with XMvn.  It provides an adapter which allows
XMvn resolver to be used as Gradle resolver.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q

%pom_change_dep :groovy :groovy-all

%{mvn_file} :{*} %{parent}/@1

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE
%doc AUTHORS README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
