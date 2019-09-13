#
# spec file for package maven-remote-resources-plugin
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           maven-remote-resources-plugin
Version:        1.5
Release:        0
Summary:        Maven Remote Resources Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://maven.apache.org/plugins/maven-remote-resources-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-artifact-resolver)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-filtering)
BuildRequires:  mvn(org.apache.maven:maven-artifact:2.2.1)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-model:2.2.1)
BuildRequires:  mvn(org.apache.maven:maven-monitor)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.apache.maven:maven-settings:2.2.1)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  mvn(org.codehaus.plexus:plexus-resources)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
#!BuildRequires: mvn(log4j:log4j)
BuildArch:      noarch

%description
Process resources packaged in JARs that have been deployed to
a remote repository. The primary use case being satisfied is
the consistent inclusion of common resources in a large set of
projects. Maven projects at Apache use this plug-in to satisfy
licensing requirements at Apache where each project much include
license and notice files for each release.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%build
# Tests use Maven 2 APIs
%mvn_build -f

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
