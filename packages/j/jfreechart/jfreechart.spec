#
# spec file for package jfreechart
#
# Copyright (c) 2025 SUSE LLC
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
Version:        1.5.5
Release:        0
Summary:        Java chart library
License:        LGPL-2.1-or-later
URL:            https://www.jfree.org/%{name}/
Source0:        https://github.com/jfree/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(javax.servlet:javax.servlet-api) >= 2.5
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jfree:jcommon) >= 1.0.23
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
JFreeChart is a comprehensive free chart library for the Java™ platform that
can be used on the client-side (JavaFX and Swing) or the server side, with
export to multiple formats including SVG, PNG and PDF.

%package javadoc
Summary:        Javadocs for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

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
%pom_remove_plugin :maven-jxr-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_change_dep javax.servlet:servlet-api: javax.servlet:javax.servlet-api:

%pom_add_plugin org.apache.felix:maven-bundle-plugin . "$MVN_BUNDLE_PLUGIN_EXTRA_XML"
# Change to packaging type bundle so as to be able to use it
# as an OSGi bundle.
%pom_xpath_set "pom:packaging" "bundle"

%{mvn_file} : %{name}

%build
%{mvn_build} -f  -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license licence-LGPL.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license licence-LGPL.txt

%changelog
