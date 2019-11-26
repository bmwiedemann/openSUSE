#
# spec file for package felix-scr
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


%global bundle  org.apache.felix.scr
Name:           felix-scr
Version:        2.0.14
Release:        0
Summary:        Apache Felix Service Component Runtime (SCR)
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://felix.apache.org/documentation/subprojects/apache-felix-service-component-runtime.html
# svn export http://svn.apache.org/repos/asf/felix/releases/%{bundle}-%{version}/
# tar caJf %{bundle}-%{version}.tar.xz %{bundle}-%{version}
Source0:        %{bundle}-%{version}.tar.xz
Source1:        http://svn.apache.org/repos/asf/felix/releases/1.0.0/LICENSE
Source2:        http://svn.apache.org/repos/asf/felix/releases/1.0.0/NOTICE
# Don't embed deps, use import-package instead
Patch0:         osgi-metadata.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  xz
BuildRequires:  mvn(net.sf.kxml:kxml2)
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.gogo.runtime)
BuildRequires:  mvn(org.apache.felix:org.apache.felix.shell)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.osgi:osgi.annotation)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildRequires:  mvn(xpp3:xpp3)
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
cp %{SOURCE1} %{SOURCE2} .
%patch0

# All these OSGi deps are provided in the compendium jar
%pom_add_dep org.osgi:osgi.cmpn:6.0.0:provided
%pom_remove_dep org.osgi:org.osgi.service.component
%pom_remove_dep org.osgi:org.osgi.service.cm
%pom_remove_dep org.osgi:org.osgi.service.log
%pom_remove_dep org.osgi:org.osgi.service.metatype
%pom_remove_dep org.osgi:org.osgi.namespace.extender
%pom_remove_dep org.osgi:osgi.promise

# Many test deps are not in Fedora
%pom_xpath_remove "pom:project/pom:dependencies/pom:dependency[pom:scope='test']"
%pom_remove_dep org.ops4j.base:

# Animal sniffer is unnecessary since we always know JRE level on Fedora
%pom_remove_dep :animal-sniffer-annotations
sed -i -e '/IgnoreJRERequirement/d' src/main/java/org/apache/felix/scr/impl/manager/ThreadDump.java

# Upstream kxml bundles xpp3. Since RHBZ#1299774 kxml no longer
# bundles xpp3 packages. Add the dep to the pom. kxml requires xpp3
# already.
%pom_add_dep xpp3:xpp3:1.1.4c:compile
# And since we are not bundling kxml, need to make it 'compile' scope
# instead of 'provided' scope so it's pulled in by RPM requires
%pom_change_dep net.sf.kxml:kxml2 net.sf.kxml:kxml2:2.2.2:compile

%{mvn_file} : felix/%{bundle}

%build
%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
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
