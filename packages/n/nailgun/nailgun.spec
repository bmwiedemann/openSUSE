#
# spec file for package nailgun
#
# Copyright (c) 2019 SUSE LLC
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


%define debug_package %{nil}
Name:           nailgun
Version:        0.9.1
Release:        0
Summary:        Framework for running Java from the cli without the JVM startup overhead
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://martiansoftware.com/nailgun/
Source0:        https://github.com/martylamb/%{name}/archive/%{name}-all-%{version}.zip
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
Nailgun is a client, protocol, and server for running Java programs from the
command line without incurring the JVM startup overhead. Programs run in the
server (which is implemented in Java), and are triggered by the client
(written in C), which handles all I/O.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-all-%{version}

find . -name '*.jar' -delete
find . -name '*.class' -delete

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%build
%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md

%files javadoc -f .mfiles-javadoc

%changelog
