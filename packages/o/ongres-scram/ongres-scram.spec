#
# spec file for package ongres-scram
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


%global		upstream_name    scram
%global		upstream_version 3.2
Name:           ongres-%{upstream_name}
Version:        %(echo %{upstream_version} | sed 's/-/~/g')
Release:        0
Summary:        Salted Challenge Response Authentication Mechanism - Java Implementation
License:        BSD-2-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/ongres/%{upstream_name}
Source0:        https://github.com/ongres/%{upstream_name}/archive/%{upstream_version}/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 11
BuildRequires:  maven-local
BuildRequires:  mvn(com.ongres.stringprep:saslprep) >= 2.2
BuildRequires:  mvn(org.jetbrains:annotations)
Requires:       mvn(com.ongres.stringprep:stringprep) >= 2.2
BuildArch:      noarch

%description
This is a Java implementation of SCRAM (Salted Challenge Response
Authentication Mechanism) which is part of the family of Simple
Authentication and Security Layer (SASL, RFC 4422) authentication
mechanisms. It is described as part of RFC 5802 and RFC7677.

%package client
Summary:        Client for %{name}

%description client
This package contains the client for %{name}

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}

%prep
%autosetup -p1 -n "%{upstream_name}-%{upstream_version}"
find \( -name '*.jar' -o -name '*.class' \) -delete

%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :flatten-maven-plugin
%pom_remove_plugin -r :maven-invoker-plugin
%pom_remove_dep -r :junit-bom

%{mvn_package} com.ongres.scram:scram-aggregator __noinstall
%{mvn_package} com.ongres.scram:scram-parent __noinstall

%pom_xpath_remove \
    'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:executions/pom:execution/pom:configuration/pom:multiReleaseOutput' \
    scram-parent

%build
%{mvn_build} -s -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-scram-common
%license LICENSE

%files client -f .mfiles-scram-client
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
