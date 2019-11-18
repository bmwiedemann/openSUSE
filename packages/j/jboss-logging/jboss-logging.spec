#
# spec file for package jboss-logging
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
Name:           jboss-logging
Version:        3.3.0
Release:        0
Summary:        The JBoss Logging Framework
License:        Apache-2.0
URL:            https://github.com/jboss-logging/jboss-logging
Source0:        https://github.com/jboss-logging/jboss-logging/archive/%{namedversion}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-api)
BuildRequires:  mvn(org.jboss.logmanager:jboss-logmanager)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildArch:      noarch

%description
This package contains the JBoss Logging Framework.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-logging-%{namedversion}

%pom_xpath_set pom:properties/pom:version.org.apache.log4j 12

# SLF4j 1.7 upgrade
sed -i "s|map = MDC.getCopyOfContextMap();|map = (Map) MDC.getCopyOfContextMap();|" \
 src/main/java/org/jboss/logging/Slf4jLoggerProvider.java

# Unneeded task
%pom_remove_plugin :maven-source-plugin

# Javadoc broken with apiviz taglet
%pom_remove_plugin :maven-javadoc-plugin

cp -p src/main/resources/META-INF/LICENSE.txt .
sed -i 's/\r//' LICENSE.txt

%build
%{mvn_build} -f -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
