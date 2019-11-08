#
# spec file for package jetty-alpn-api
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


Name:           jetty-alpn-api
Version:        1.1.3.v20160715
Release:        0
Summary:        Jetty ALPN API
License:        Apache-2.0 AND EPL-1.0
Group:          Development/Libraries/Java
URL:            http://www.eclipse.org/jetty
Source0:        http://git.eclipse.org/c/jetty/org.eclipse.jetty.alpn.git/snapshot/org.eclipse.jetty.alpn-alpn-api-%{version}.tar.xz
Source1:        http://www.eclipse.org/legal/epl-v10.html
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-build-support)
BuildRequires:  mvn(org.eclipse.jetty:jetty-parent:pom:)
BuildRequires:  xz
BuildArch:      noarch

%description
Jetty API for Application-Layer Protocol Negotiation.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n org.eclipse.jetty.alpn-alpn-api-%{version}

# Use packaging=bundle to get the manifest into jar
%pom_remove_plugin :maven-jar-plugin
%pom_xpath_inject pom:project '<packaging>bundle</packaging>'

cp %{SOURCE1} %{SOURCE2} .

%build
%{mvn_build} -f -- -Dsource=7

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license epl-v10.html LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%license epl-v10.html LICENSE-2.0.txt

%changelog
