#
# spec file for package jetty-distribution-remote-resources
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


Name:           jetty-distribution-remote-resources
Version:        1.2
Release:        0
Summary:        Jetty toolchain artifact for distribution remote resources
License:        Apache-2.0 OR EPL-1.0
Group:          Development/Libraries/Java
URL:            http://www.eclipse.org/jetty/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.eclipse.jetty.toolchain:jetty-toolchain:pom:)
BuildRequires:  xz
#!BuildRequires: mvn(log4j:log4j)
BuildArch:      noarch

%description
Jetty toolchain artifact for distribution remote distribution resources

%prep
%setup -q

%build
%{mvn_build}

%install
%mvn_install

%files -f .mfiles
%license src/main/resources/license-eplv10-aslv20.html

%changelog
