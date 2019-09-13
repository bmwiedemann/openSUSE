#
# spec file for package maven-install-plugin
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           maven-install-plugin
Version:        2.5.2
Release:        0
Summary:        Maven Install Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://maven.apache.org/plugins/maven-install-plugin
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.apache.maven:maven-artifact-manager)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  unzip
BuildArch:      noarch

%description
Copies the project artifacts to the user's local repository.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
Requires:       jpackage-utils

%description javadoc
API documentation for %{name}.

%prep
%setup -q
# maven-core has scope "provided" in Plugin Testing Harness, so we
# need to provide it or tests will fail to compile.  This works for
# upstream because upstream uses a different version of Plugin Testing
# Harness in which scope of maven-core dependency is "compile".
%pom_add_dep org.apache.maven:maven-core::test

%pom_add_dep org.apache.maven:maven-compat

%build
%{mvn_build} -f -- -DmavenVersion=3.1.1

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE

%changelog
