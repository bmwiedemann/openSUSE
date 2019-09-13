#
# spec file for package stax2-api
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


Name:           stax2-api
Version:        4.0.0
Release:        0
Summary:        Experimental API extending basic StAX implementation
License:        BSD-2-Clause
Group:          Development/Libraries/Java
URL:            http://wiki.fasterxml.com/WoodstoxStax2
Source0:        https://github.com/FasterXML/%{name}/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml:oss-parent:pom:)
BuildRequires:  mvn(javax.xml.stream:stax-api)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildArch:      noarch

%description
StAX2 is an experimental API that is intended to extend
basic StAX specifications in a way that allows implementations
to experiment with features before they end up in the actual
StAX specification (if they do). As such, it is intended
to be freely implementable by all StAX implementations same way
as StAX, but without going through a formal JCP process.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_xpath_remove pom:Import-Package

%pom_remove_plugin :maven-javadoc-plugin

%build

%{mvn_file} :%{name} %{name}
%{mvn_build} -f -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
