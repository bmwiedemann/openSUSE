#
# spec file for package jboss-logging-tools
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2020 Stasiek Michalski <stasiek@michalski.cc>.
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
Name:           jboss-logging-tools
Version:        2.2.1
Release:        0
Summary:        JBoss Logging I18n Annotation Processor
License:        Apache-2.0 AND LGPL-2.0-or-later
URL:            https://github.com/jboss-logging/jboss-logging-tools
Source0:        %{url}/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
Patch0:         reproducible.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.jboss.jdeparser:jdeparser)
BuildRequires:  mvn(org.jboss.logging:jboss-logging)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildArch:      noarch

%description
This package contains JBoss Logging I18n Annotation Processor

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{namedversion}
%patch0 -p1

%pom_remove_dep -r org.jboss.forge.roaster:
rm processor/src/test/java/org/jboss/logging/processor/generated/GeneratedSourceAnalysisTest.java

# Skip docs module
%pom_disable_module docs

%build
%{mvn_build} -f -- -Dsource=8

%fdupes -s %{buildroot}/%{_javadocdir}

%install
%mvn_install

%files -f .mfiles
%doc README.adoc

%files javadoc -f .mfiles-javadoc
%doc README.adoc

%changelog
