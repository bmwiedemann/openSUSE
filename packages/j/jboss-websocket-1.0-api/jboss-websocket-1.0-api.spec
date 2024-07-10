#
# spec file for package jboss-websocket-1.0-api
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


%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:           jboss-websocket-1.0-api
Version:        1.0.0
Release:        0
Summary:        JSR-356: Java WebSocket 1.0 API
License:        CDDL-1.0 OR GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/jboss/jboss-websocket-api_spec
Source0:        https://github.com/jboss/jboss-websocket-api_spec/archive/jboss-websocket-api_1.0_spec-%{namedversion}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildArch:      noarch

%description
The JSR-356: Java WebSocket 1.0 API classes.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-websocket-api_spec-jboss-websocket-api_1.0_spec-%{namedversion}
%pom_remove_plugin :maven-source-plugin

%build
%{mvn_alias} "org.jboss.spec.javax.websocket:jboss-websocket-api_1.0_spec" "javax.websocket:javax.websocket-api" "javax.websocket:javax.websocket-client-api"
%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%dir %{_javadir}/%{name}
%license LICENSE
%doc README

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc README

%changelog
