#
# spec file for package felix-bundlerepository
#
# Copyright (c) 2022 SUSE LLC
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


%global bundle org.apache.felix.bundlerepository
Name:           felix-bundlerepository
Version:        2.0.10
Release:        0
Summary:        Bundle repository service
License:        Apache-2.0 AND MIT
URL:            https://felix.apache.org/documentation/subprojects/apache-felix-osgi-bundle-repository.html
Source0:        https://archive.apache.org/dist/felix/%{bundle}-%{version}-source-release.tar.gz
Source1:        %{bundle}-build.xml
Patch1:         0001-Unbundle-libraries.patch
Patch2:         0002-Compatibility-with-osgi-r6.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  felix-gogo-runtime
BuildRequires:  felix-osgi-obr
BuildRequires:  felix-shell
BuildRequires:  felix-utils
BuildRequires:  javapackages-local
BuildRequires:  kxml
BuildRequires:  osgi-compendium
BuildRequires:  osgi-core
BuildRequires:  xpp3
Requires:       mvn(net.sf.kxml:kxml2)
Requires:       mvn(org.apache.felix:org.apache.felix.utils)
Requires:       mvn(org.osgi:osgi.cmpn)
Requires:       mvn(org.osgi:osgi.core)
Requires:       mvn(xpp3:xpp3)
BuildArch:      noarch

%description
Bundle repository service

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}
cp %{SOURCE1} build.xml
%patch1 -p1
%patch2 -p1

%pom_remove_plugin :maven-source-plugin

# Unbundle xpp3
%pom_add_dep "xpp3:xpp3:1.1.3.4.O" pom.xml

# Make felix utils mandatory dep
%pom_xpath_remove "pom:dependency[pom:artifactId[text()='org.apache.felix.utils']]/pom:optional"

%pom_change_dep :easymock :::test

# Removing and adding is necessary (order matters)
%pom_remove_dep :org.osgi.core
%pom_add_dep org.osgi:osgi.core
%pom_remove_dep :org.osgi.compendium
%pom_add_dep org.osgi:osgi.cmpn

%pom_remove_parent
%pom_xpath_inject pom:project "<groupId>org.apache.felix</groupId>"

%build
mkdir -p lib
build-jar-repository -s lib osgi-core osgi-compendium xpp3 kxml felix
%{ant} package javadoc

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}/felix
install -m 644 target/%{bundle}-%{version}.jar %{buildroot}%{_javadir}/felix/%{bundle}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}/felix
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/felix/%{bundle}.pom
%add_maven_depmap felix/%{bundle}.pom felix/%{bundle}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -r target/site/apidocs/* %{buildroot}/%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE LICENSE.kxml2 NOTICE
%doc DEPENDENCIES

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE LICENSE.kxml2 NOTICE

%changelog
