#
# spec file for package jdeparser
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
Name:           jdeparser
Version:        2.0.3
Release:        0
Summary:        Source generator library for Java
License:        Apache-2.0
URL:            https://github.com/jdeparser/jdeparser2
# old repos https://github.com/jdeparser/jdeparser
Source0:        %{url}/archive/%{namedversion}/jdeparser2-%{namedversion}.tar.gz
Patch0:         jdeparser2-reflection-stackwalker.diff
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildArch:      noarch

%description
This project is a fork of Sun's (now Oracle's) com.sun.codemodel project. We
decided to fork the project because by all evidence, the upstream project is
dead and not actively accepting outside contribution. All JBoss projects are
urged to use this project instead for source code generation.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jdeparser2-%{namedversion}
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
%patch0 -p1
%endif

%build
%{mvn_build} -f -- -Dsource=8

%install
%mvn_install

%fdupes -s %{buildroot}/%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
