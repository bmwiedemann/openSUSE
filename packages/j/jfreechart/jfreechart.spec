#
# spec file for package jfreechart
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


Name:           jfreechart
Version:        1.0.19
Release:        0
Summary:        Java chart library
License:        LGPL-2.1-or-later
URL:            http://www.jfree.org/jfreechart/
Source0:        http://download.sourceforge.net/sourceforge/jfreechart/%{name}-%{version}.zip
Patch0:         build_swt_encoding_fix.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(javax.servlet:javax.servlet-api) >= 2.5
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jfree:jcommon) >= 1.0.23
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
JFreeChart is a free 100% Java chart library that makes it easy for
developers to display professional quality charts in their applications.

%package javadoc
Summary:        Javadocs for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
# Erase prebuilt files
find \( -name '*.jar' -o -name '*.class' \) -exec rm -f '{}' \;
%patch0 -p2

MVN_BUNDLE_PLUGIN_EXTRA_XML="<extensions>true</extensions>
        <configuration>
          <instructions>
            <Bundle-SymbolicName>org.jfree.jfreechart</Bundle-SymbolicName>
            <Bundle-Vendor>Fedora Project</Bundle-Vendor>
            <Bundle-Version>%{version}</Bundle-Version>
            <!-- Do not autogenerate uses clauses in Manifests -->
            <Import-Package>
              !javax.servlet,
              !javax.servlet.http,
              *
            </Import-Package>
            <_nouses>true</_nouses>
          </instructions>
        </configuration>"
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-jxr-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_change_dep javax.servlet:servlet-api: javax.servlet:javax.servlet-api:

%pom_add_plugin org.apache.felix:maven-bundle-plugin . "$MVN_BUNDLE_PLUGIN_EXTRA_XML"
# Change to packaging type bundle so as to be able to use it
# as an OSGi bundle.
%pom_xpath_set "pom:packaging" "bundle"

rm -rf source/org/jfree/chart/fx

%build
%{mvn_build} -f  -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8 \
%endif
	-Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc ChangeLog NEWS README.txt

%files javadoc -f .mfiles-javadoc

%changelog
