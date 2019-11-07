#
# spec file for package glassfish-transaction-api
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


Name:           glassfish-transaction-api
Version:        1.3
Release:        0
Summary:        Java JTA 1.3 API Design Specification
License:        CDDL-1.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://github.com/javaee/javax.transaction
Source0:        https://github.com/javaee/javax.transaction/archive/javax.transaction-api-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(javax.enterprise:cdi-api)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.glassfish.build:spec-version-maven-plugin)
BuildArch:      noarch

%description
Project GlassFish Java Transaction API.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n javax.transaction-javax.transaction-api-%{version}

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-remote-resources-plugin

%{mvn_file} : %{name}

%build

%{mvn_build} -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
