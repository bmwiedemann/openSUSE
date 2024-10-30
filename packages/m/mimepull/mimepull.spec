#
# spec file for package mimepull
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

%global project metro
Name:           mimepull
Version:        1.10.0
Release:        0
Summary:        MIME streaming extension
License:        BSD-3-Clause
URL:            https://github.com/eclipse-ee4j/metro-mimepull
Source0:        https://github.com/eclipse-ee4j/%{project}-%{name}/archive/refs/tags/%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.eclipse.ee4j:project:pom:)
BuildArch:      noarch

%description
Provides a streaming API to access attachments parts in a MIME message.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{project}-%{name}-%{version}

# Unavailable plugins
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :build-helper-maven-plugin
%pom_remove_plugin :buildnumber-maven-plugin
%pom_xpath_remove pom:Implementation-Build-Id

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
