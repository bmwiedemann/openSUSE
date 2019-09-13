#
# spec file for package felix-osgi-compendium
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


%global bundle org.osgi.compendium
Name:           felix-osgi-compendium
Version:        1.4.0
Release:        0
Summary:        Felix OSGi R4 Compendium Bundle
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://felix.apache.org
Source0:        http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz
Source1:        %{name}-build.xml
Patch0:         0001-Fix-servlet-api-dependency.patch
Patch1:         0002-Fix-compile-target.patch
Patch2:         0003-Add-CM_LOCATION_CHANGED-property-to-ConfigurationEve.patch
Patch3:         0004-Add-TARGET-property-to-ConfigurationPermission.patch
# This is an ugly patch that adds getResourceURL method. This prevents jbosgi-framework
# package from bundling osgi files. Once the jbosgi-framework will be updated
# to a new version without the need for this patch, REMOVE it!
Patch4:         0005-Add-getResourceURL-method-to-make-jbosgi-framework-h.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  felix-osgi-core
BuildRequires:  felix-osgi-foundation
BuildRequires:  glassfish-servlet-api
BuildRequires:  java-devel >= 1.7
BuildRequires:  javapackages-local
Requires:       mvn(javax.servlet:javax.servlet-api)
Requires:       mvn(org.apache.felix:org.osgi.core)
Requires:       mvn(org.apache.felix:org.osgi.foundation)
BuildArch:      noarch

%description
OSGi Service Platform Release 4 Compendium Interfaces and Classes.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{bundle}-%{version}
cp %{SOURCE1} build.xml

# fix servlet api properly
%patch0 -p1
# fix compile source/target
%patch1 -p1
# add CM_LOCATION_CHANGED property
%patch2 -p1
# add TARGET property
%patch3 -p1
# add getResourceURL method
%patch4 -p1

%pom_remove_parent .
%pom_xpath_inject "pom:project" "<groupId>org.apache.felix</groupId>" .

mkdir -p lib
build-jar-repository -s lib glassfish-servlet-api felix

%build
%{ant} package javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/felix
install -pm 0644 target/%{bundle}-%{version}.jar %{buildroot}%{_javadir}/felix/%{bundle}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/felix
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/felix/%{bundle}.pom
%add_maven_depmap felix/%{bundle}.pom felix/%{bundle}.jar -a org.osgi:%{bundle}
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}

%changelog
