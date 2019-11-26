#
# spec file for package maven-osgi
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


Name:           maven-osgi
Version:        0.2.0
Release:        0
Summary:        Library for Maven-OSGi integration
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://maven.apache.org/shared/maven-osgi
# svn export http://svn.apache.org/repos/asf/maven/shared/tags/maven-osgi-0.2.0 maven-osgi-0.2.0
# find -name *.jar -delete
# tar caf maven-osgi-0.2.0.tar.xz maven-osgi-0.2.0/
Source0:        %{name}-%{version}.tar.xz
# ASL mandates that the licence file be included in redistributed source
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  xz
BuildRequires:  mvn(biz.aQute:bndlib)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildArch:      noarch

%description
Library for Maven-OSGi integration.

This is a replacement package for maven-shared-osgi

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q
cp -p %{SOURCE1} LICENSE

sed -i 's/import aQute\.lib\.osgi/import aQute.bnd.osgi/g' src/main/java/org/apache/maven/shared/osgi/DefaultMaven2OsgiConverter.java

# Replace plexus-maven-plugin with plexus-component-metadata
%pom_xpath_set "pom:plugin[pom:artifactId[text()='plexus-maven-plugin']]//pom:goal[text()='descriptor']" generate-metadata
%pom_xpath_set "pom:artifactId[text()='plexus-maven-plugin']" plexus-component-metadata

%build
%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
