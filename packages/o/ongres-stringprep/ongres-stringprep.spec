#
# spec file for package ongres-stringprep
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


%global		upstream_name    stringprep
%global		upstream_version 1.1
Name:           ongres-%{upstream_name}
Version:        %(echo %{upstream_version} | sed 's/-/~/g')
Release:        0
Summary:        Preparation of internationalized strings
License:        BSD-2-Clause
URL:            https://github.com/ongres/%{upstream_name}
Source0:        https://github.com/ongres/%{upstream_name}/archive/%{upstream_version}/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:         fix-dir-create.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildArch:      noarch

%description
StringPrep is the preparation of internationalized strings (stringprep, RFC 3454).

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}

%package saslprep
Summary:        SASLprep for %{name}

%description saslprep
SaslPrep is a profile of stringprep for user names and passwords (saslprep, RFC 4013).

%package parent
Summary:        Developement files for %{name}

%description parent
This package contains development files for %{name}

%package codegenerator
Summary:        Codegenerator

%description codegenerator
This package contains a codegenerator for %{name}

%prep
%setup -n %{upstream_name}-%{upstream_version}
%patch0 -p1
find \( -name '*.jar' -o -name '*.class' \) -delete

%pom_remove_dep :velocity-tools codegenerator

%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%build
%{mvn_build} -s -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}


%files -f .mfiles-stringprep
%license LICENSE

%files parent -f .mfiles-parent
%license LICENSE

%files saslprep -f .mfiles-saslprep
%license LICENSE

%files codegenerator -f .mfiles-codegenerator
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
