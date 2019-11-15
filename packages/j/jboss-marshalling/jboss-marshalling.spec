#
# spec file for package jboss-marshalling
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
Name:           jboss-marshalling
Version:        1.4.11
Release:        0
Summary:        JBoss Marshalling
License:        Apache-2.0 AND LGPL-2.1-or-later
URL:            https://jbossmarshalling.jboss.org/
Source0:        https://github.com/jboss-remoting/jboss-marshalling/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jboss.modules:jboss-modules)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildArch:      noarch

%description
JBoss Marshalling is an alternative serialization API that fixes many
of the problems found in the JDK serialization API while remaining
fully compatible with java.io.Serializable and its relatives, and adds
several new tunable parameters and additional features, all of which
are pluggable via factory configuration (externalizers, class/instance
lookup tables, class resolution, and object replacement, to name a
few).

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains %{summary}.

%package osgi
Summary:        JBoss Marshalling OSGi Bundle

%description osgi
JBoss Marshalling OSGi Bundle.

%prep
%setup -q -n %{name}-%{namedversion}

%pom_remove_plugin -r :maven-shade-plugin
%pom_disable_module tests

# Remove dependency on apiviz
%pom_remove_plugin :maven-javadoc-plugin

%{mvn_package} :jboss-marshalling-osgi osgi

%build
%{mvn_build} -f -- -Dsource=7

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%files osgi -f .mfiles-osgi

%changelog
