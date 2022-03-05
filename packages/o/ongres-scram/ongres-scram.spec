#
# spec file for package ongres-scram
#
# Copyright (c) 2020 SUSE LLC
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
%global		upstream_version 2.1
Name:           ongres-%{upstream_name}
Version:        %(echo %{upstream_version} | sed 's/-/~/g')
Release:        0
Summary:        Salted Challenge Response Authentication Mechanism - Java Implementation
License:        BSD-2-Clause
URL:            https://github.com/ongres/%{upstream_name}
Source0:        https://github.com/ongres/%{upstream_name}/archive/%{upstream_version}/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.code.findbugs:annotations)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.ongres.stringprep:saslprep)
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

%package parent
Summary:        Parent POM of %{name}

%description parent
This package contains the %{name} parent POM.

%prep
%autosetup -p1 -n "%{upstream_name}-%{upstream_version}"
find \( -name '*.jar' -o -name '*.class' \) -delete
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-dependency-plugin client
%pom_remove_plugin -r :maven-javadoc-plugin

%build
%{mvn_build} -s -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-common
%license LICENSE

%files client -f .mfiles-client
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%files parent -f .mfiles-parent
%license LICENSE

%changelog
