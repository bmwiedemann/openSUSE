#
# spec file for package jaf
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


Name:           jaf
Version:        1.2.0
Release:        0
Summary:        JavaBeans Activation Framework
License:        (BSD-3-Clause AND GPL-2.0-only WITH Classpath-exception-2.0) OR CDDL-1.1
Group:          Development/Libraries/Java
URL:            https://github.com/javaee/activation
Source0:        activation-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildArch:      noarch

%description
The JavaBeans Activation Framework (JAF) is a standard extension to the
Java platform that lets you take advantage of standard services to:
determine the type of an arbitrary piece of data; encapsulate access to it;
discover the operations available on it; and instantiate the appropriate
bean to perform the operation(s).

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
%{summary}.

%prep
%setup -q -n activation-%{version}

%pom_disable_module demo

# maven-dependency-plugin doesn't work correctly without access to remote repos
%pom_remove_plugin :maven-dependency-plugin activationapi

%pom_remove_parent
%pom_remove_plugin org.codehaus.mojo:build-helper-maven-plugin
%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

%pom_remove_plugin -r :osgiversion-maven-plugin
%pom_xpath_inject pom:project/pom:properties "<activation.osgiversion>\${project.version}</activation.osgiversion>" activation

%{mvn_alias} :javax.activation-api :activation

%build
%{mvn_build} -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=6 \
%endif
	-Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt
%doc README.md

%changelog
