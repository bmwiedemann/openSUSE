#
# spec file for package felix-shell
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


%global bundle org.apache.felix.shell
Name:           felix-shell
Version:        1.4.3
Release:        0
Summary:        Apache Felix Shell Service
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://felix.apache.org
Source0:        http://archive.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.osgi:org.osgi.compendium)
BuildRequires:  mvn(org.osgi:org.osgi.core)
BuildArch:      noarch

%description
A simple OSGi command shell service.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}

%pom_remove_plugin org.codehaus.mojo:rat-maven-plugin

%pom_add_dep junit:junit::test

%{mvn_file} :%{bundle} "felix/%{bundle}"

%build
%{mvn_build} -f 

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc NOTICE DEPENDENCIES

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE

%changelog
