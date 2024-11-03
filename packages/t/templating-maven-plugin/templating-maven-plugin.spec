#
# spec file for package templating-maven-plugin
#
# Copyright (c) 2023 SUSE LLC
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


Name:           templating-maven-plugin
Version:        1.0.0
Release:        0
Summary:        Templating Maven Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/mojohaus/%{name}
Source:         %{url}/archive/refs/tags/%{name}-%{version}.tar.gz
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-invoker-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.shared:maven-filtering)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
BuildArch:      noarch

%description
The Templating Maven Plugin handles copying files from a source to a given
output directory, while filtering them. This plugin is useful to filter Java
Source Code if you need for example to have things in that code replaced with
some properties values.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# migrate to maven 3
%pom_xpath_set //pom:mavenVersion 3.8.6
%pom_remove_dep :maven-project
%pom_change_dep org.apache.maven: :::provided

%build
%{mvn_build} -f -- -Dmojo.java.target=8

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
