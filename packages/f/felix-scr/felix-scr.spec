#
# spec file for package felix-scr
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


%global bundle  org.apache.felix.scr
Name:           felix-scr
Version:        2.1.16
Release:        0
Summary:        Apache Felix Service Component Runtime (SCR)
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://felix.apache.org/documentation/subprojects/apache-felix-service-component-runtime.html
Source0:        http://archive.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz
# Don't embed deps, use import-package instead
Patch0:         0001-Use-import-package-instead-of-embedding-dependencies.patch
# Drop dep on kxml/xpp, use the system SAX implementation instead
Patch1:         0002-Drop-the-dependencies-on-kxml-xpp3.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  xz
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.gogo.runtime)
BuildRequires:  mvn(org.osgi:osgi.annotation)
BuildRequires:  mvn(org.osgi:osgi.cmpn) >= 7.0.0
BuildRequires:  mvn(org.osgi:osgi.core) >= 7.0.0
BuildArch:      noarch

%description
Implementation of the OSGi Declarative Services Specification Version 1.3 (R6).

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{bundle}-%{version}
%patch0 -p1
%patch1 -p1

# All these OSGi deps are provided in the compendium jar
%pom_add_dep org.osgi:osgi.cmpn:7.0.0:provided
%pom_remove_dep org.osgi:org.osgi.service.component
%pom_remove_dep org.osgi:org.osgi.service.cm
%pom_remove_dep org.osgi:org.osgi.service.log
%pom_remove_dep org.osgi:org.osgi.service.metatype
%pom_remove_dep org.osgi:org.osgi.namespace.extender
%pom_remove_dep org.osgi:org.osgi.util.promise
%pom_remove_dep org.osgi:org.osgi.util.function

# Remove test deps
%pom_xpath_remove "pom:project/pom:dependencies/pom:dependency[pom:scope='test']"
%pom_remove_dep org.ops4j.base:
%pom_remove_plugin :maven-failsafe-plugin

# Animal sniffer is unnecessary since we always know JRE level
%pom_remove_dep :animal-sniffer-annotations
sed -i -e '/IgnoreJRERequirement/d' src/main/java/org/apache/felix/scr/impl/manager/ThreadDump.java

%{mvn_file} : felix/%{bundle}

%build
%{mvn_build} -f  -- -Dfelix.java.version=7 \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=7
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc changelog.txt
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
