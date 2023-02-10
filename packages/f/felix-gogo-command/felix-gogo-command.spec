#
# spec file for package felix-gogo-command
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


%global bundle  org.apache.felix.gogo.command
Name:           felix-gogo-command
Version:        1.1.2
Release:        0
Summary:        Apache Felix Gogo command line shell for OSGi
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://felix.apache.org/documentation/subprojects/apache-felix-gogo.html
Source0:        https://repo1.maven.org/maven2/org/apache/felix/org.apache.felix.gogo.command/%{version}/%{bundle}-%{version}-source-release.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:gogo-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.gogo.runtime)
BuildRequires:  mvn(org.osgi:org.osgi.service.log)
BuildRequires:  mvn(org.osgi:osgi.annotation)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildArch:      noarch

%description
Apache Felix Gogo is a subproject of Apache Felix implementing a command
line shell for OSGi. It is used in many OSGi runtimes and servers.

This package implements a set of basic commands.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%{mvn_file} : felix/%{bundle}

# Use provided scope because this is useful on OSGi frameworks other than Felix
%pom_change_dep :osgi.core :::provided
%pom_change_dep :osgi.annotation :::provided
%pom_change_dep :junit :::test
%pom_change_dep :mockito-core :::test

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
