#
# spec file for package woodstox-core
#
# Copyright (c) 2020 SUSE LLC
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


%global base_name woodstox
%global core_name %{base_name}-core
Name:           %{core_name}
Version:        6.1.1
Release:        0
Summary:        XML processor
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/FasterXML/woodstox
Source0:        https://github.com/FasterXML/%{base_name}/archive/%{name}-%{version}.tar.gz
Patch0:         0001-Allow-building-against-OSGi-APIs-newer-than-R4.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml:oss-parent:pom:)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java.dev.msv:msv-core)
BuildRequires:  mvn(net.java.dev.msv:xsdlib)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.codehaus.woodstox:stax2-api)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(relaxngDatatype:relaxngDatatype)
BuildArch:      noarch

%description
Woodstox is a validating namespace-aware StAX-compliant (JSR-173) XML
processor written in Java. XML processor means that it handles both
input (= parsing) and output (= writing, serialization)), as well as
supporting tasks such as validation.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{base_name}-%{name}-%{version}

%patch0 -p1

%pom_remove_plugin :nexus-staging-maven-plugin

# we don't care about Java 9 modules (yet)
%pom_remove_plugin :moditect-maven-plugin

# replace felix-osgi-core with osgi-core
%pom_change_dep -r :org.osgi.core org.osgi:osgi.core

%{mvn_alias} ":{woodstox-core}" :@1-lgpl :@1-asl :wstx-asl :wstx-lgpl \
    org.codehaus.woodstox:@1 org.codehaus.woodstox:@1-asl \
    org.codehaus.woodstox:@1-lgpl org.codehaus.woodstox:wstx-lgpl \
    org.codehaus.woodstox:wstx-asl

%{mvn_file} : %{name}{,-asl,-lgpl}

%build
%{mvn_build} -f -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
