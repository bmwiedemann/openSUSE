#
# spec file for package eclipse-swtchart
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


Name:           eclipse-swtchart
Version:        0.13.0
Release:        0
Summary:        Eclipse SWTChart
License:        EPL-2.0
Group:          Development/Languages/Java
URL:            https://projects.eclipse.org/projects/science.swtchart
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  tycho
BuildConflicts: java >= 12
BuildConflicts: java-devel >= 12
BuildConflicts: java-headless >= 12
BuildArch:      noarch
# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch:    s390 %{arm} %{ix86}

%description
SWTChart is a light-weight charting component for SWT.

%prep
%setup -q

# Target platform and update site are not relevant for RPM builds
%pom_disable_module ../org.eclipse.swtchart.targetplatform org.eclipse.swtchart.cbi
%pom_disable_module ../org.eclipse.swtchart.updatesite org.eclipse.swtchart.cbi
%pom_remove_plugin :target-platform-configuration org.eclipse.swtchart.cbi

# These plugins not relevant for RPM builds
%pom_remove_plugin :maven-pmd-plugin org.eclipse.swtchart.cbi
%pom_remove_plugin :maven-checkstyle-plugin org.eclipse.swtchart.cbi

# Don't build or ship test bundles
%pom_disable_module ../org.eclipse.swtchart.test org.eclipse.swtchart.cbi
%pom_disable_module ../org.eclipse.swtchart.extensions.test org.eclipse.swtchart.cbi

# Drop export bundle not needed at runtime and shrinks the dep tree for this package
%pom_disable_module ../org.eclipse.swtchart.export org.eclipse.swtchart.cbi
%pom_disable_module ../org.eclipse.swtchart.export.extended org.eclipse.swtchart.cbi
%pom_disable_module ../org.eclipse.swtchart.export.extended.test org.eclipse.swtchart.cbi
%pom_disable_module ../org.eclipse.swtchart.export.test org.eclipse.swtchart.cbi
%pom_disable_module ../org.eclipse.swtchart.feature org.eclipse.swtchart.cbi

%{mvn_package} "::pom::" __noinstall

%build
# Qualifier generated from last modification time of source tarball
QUALIFIER=$(date -u -d"$(stat --format=%%y %{SOURCE0})" +v%%Y%%m%%d-%%H%%M)
%{mvn_build} -j -f -- -f org.eclipse.swtchart.cbi/pom.xml -DforceContextQualifier=$QUALIFIER

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md CONTRIBUTING.md NEWS.md

%changelog
