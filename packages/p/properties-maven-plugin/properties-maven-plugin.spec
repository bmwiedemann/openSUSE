#
# spec file for package properties-maven-plugin
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


Name:           properties-maven-plugin
Version:        1.1.0
Release:        0
Summary:        The Properties Maven Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://www.mojohaus.org/%{name}/
Source0:        https://github.com/mojohaus/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildArch:      noarch

%description
The Properties Maven Plugin is here to make life a little easier when dealing
with properties. It provides goals to read properties from files and URLs and
write properties to files, and also to set system properties.

It’s main use-case is loading properties from files or URLs instead of
declaring them in pom.xml, something that comes in handy when dealing with
different environments.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_parent
%pom_xpath_inject pom:project '<groupId>org.codehaus.mojo</groupId>'

%{mvn_file} : %{name}

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
