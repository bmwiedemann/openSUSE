#
# spec file for package jetty-schemas
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


Name:           jetty-schemas
Version:        4.0.3
Release:        0
Summary:        XML Schemas for Jetty
License:        (Apache-2.0 OR EPL-1.0) AND (CDDL-1.1 OR GPL-2.0-only WITH Classpath-exception-2.0)
URL:            https://www.eclipse.org/jetty/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  maven-local
BuildRequires:  xz
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-artifact-remote-resources)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-toolchain:pom:)
BuildArch:      noarch

%description
%{summary}.

%prep
%setup -q

%pom_remove_plugin :maven-source-plugin

%build
%{mvn_build}

%install
%mvn_install

%files -f .mfiles
%license target/maven-shared-archive-resources/META-INF/LICENSE
%license target/maven-shared-archive-resources/META-INF/NOTICE.txt

%changelog
