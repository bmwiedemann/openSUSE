#
# spec file for package ongres-stringprep
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


%global		upstream_name    stringprep
%global		upstream_version 2.2
Name:           ongres-%{upstream_name}
Version:        %(echo %{upstream_version} | sed 's/-/~/g')
Release:        0
Summary:        Preparation of internationalized strings
License:        BSD-2-Clause
URL:            https://github.com/ongres/%{upstream_name}
Source0:        https://github.com/ongres/%{upstream_name}/archive/%{upstream_version}/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 11
BuildRequires:  maven-local
Provides:       ongres-stringprep-parent = %{upstream_version}
Obsoletes:      ongres-stringprep-parent < %{upstream_version}
Provides:       ongres-stringprep-saslprep = %{upstream_version}
Obsoletes:      ongres-stringprep-saslprep < %{upstream_version}
BuildArch:      noarch

%description
StringPrep is the preparation of internationalized strings (stringprep, RFC 3454).

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}

%prep
%autosetup -n %{upstream_name}-%{upstream_version}
find \( -name '*.jar' -o -name '*.class' \) -delete

%pom_remove_dep org.junit:junit-bom parent

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

# codegenerator is only needed at build time, and has extra dependencies
%{mvn_package} com.ongres.stringprep:codegenerator __noinstall

# codegen is only needed for specific build profile that we do not use
rm -r codegen

%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:configuration/pom:archive' '
<manifestEntries>
  <Multi-Release>true</Multi-Release>
</manifestEntries>
' parent

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
