#
# spec file for package jboss-logmanager
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


%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:           jboss-logmanager
Version:        2.0.4
Release:        0
Summary:        JBoss Log Manager
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/jboss-logging/jboss-logmanager
Source0:        https://github.com/jboss-logging/jboss-logmanager/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jboss.modules:jboss-modules)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildArch:      noarch

%description
This package contains the JBoss Log Manager

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}

# Unneeded task
%pom_remove_plugin :maven-source-plugin

%build
%{mvn_build} -f -- -Dsource=7

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
