#
# spec file for package jetty-alpn
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           jetty-alpn
Version:        8.1.13.v20181017
Release:        0
Summary:        Jetty implementation of ALPN API
License:        GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/jetty-project/jetty-alpn
Source0:        https://github.com/jetty-project/%{name}/archive/alpn-project-%{version}.tar.gz
Patch0:         Unshade-alpn-api.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty.alpn:alpn-api)
BuildRequires:  mvn(org.eclipse.jetty:jetty-parent:pom:)
BuildConflicts: java-devel >= 9
BuildArch:      noarch

%description
A pure Java(TM) implementation of the Application Layer Protocol
Negotiation TLS Extension

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-alpn-project-%{version}

# unshade jetty-alpn-api
%patch0 -p1
%pom_remove_plugin -r :maven-shade-plugin

%pom_remove_plugin -r :maven-enforcer-plugin

%pom_disable_module alpn-tests

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md

%files javadoc -f .mfiles-javadoc

%changelog
