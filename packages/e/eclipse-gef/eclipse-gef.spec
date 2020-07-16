#
# spec file for package eclipse-gef
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


%global git_version R4_0_0
Name:           eclipse-gef
Version:        3.11.0
Release:        0
Summary:        Graphical Editing Framework (GEF) Eclipse plug-in
License:        EPL-1.0
URL:            https://www.eclipse.org/gef/
Source0:        https://github.com/eclipse/gef-legacy/archive/%{git_version}.tar.gz
BuildRequires:  ant-contrib
BuildRequires:  eclipse-license
BuildRequires:  eclipse-pde
BuildRequires:  maven-antrun-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  tycho
Requires:       eclipse-platform
BuildArch:      noarch
# Upstream Eclipse no longer supports non-64bit arches
ExcludeArch:    s390 %{arm} %{ix86}

%description
The Graphical Editing Framework (GEF) allows developers to create a rich
graphical editor from an existing application model. GEF is completely
application neutral and provides the groundwork to build almost any
application, including but not limited to: activity diagrams, GUI builders,
class diagram editors, state machines, and even WYSIWYG text editors.

%package   sdk
Summary:        Eclipse GEF SDK
Requires:       %{name} = %{version}-%{release}
Requires:       eclipse-pde

%description sdk
Documentation and source for the Eclipse Graphical Editing Framework (GEF).

%package   tests
Summary:        Eclipse GEF Tests

%description tests
Tests for the Eclipse Graphical Editing Framework (GEF).

%prep
%setup -q -n gef-legacy-%{git_version}

find -name *.jar -delete
find -name *.class -delete

%pom_remove_plugin org.eclipse.tycho:tycho-packaging-plugin org.eclipse.gef.releng/pom.xml

# Don't ship examples
for m in .flow .logic .shapes .text .ui.capabilities .source-feature -feature ; do
	%pom_disable_module "../org.eclipse.gef.examples$m" org.eclipse.gef.releng
done

# Not needed for RPM builds
%pom_disable_module "../org.eclipse.gef.all-feature" org.eclipse.gef.releng
%pom_disable_module "../org.eclipse.gef.repository" org.eclipse.gef.releng

%{mvn_package} "org.eclipse.gef:" __noinstall
%{mvn_package} ":org.eclipse.*.tests" tests
%{mvn_package} "::jar:sources:" sdk
%{mvn_package} ":*.{sdk,source,capabilities,doc.isv,examples.ui.pde}" sdk
%{mvn_package} ":" core

%build
%{mvn_build} -j -f -- -f org.eclipse.gef.releng/pom.xml -P !MARS.target

%install
%mvn_install

%files -f .mfiles-core

%files sdk -f .mfiles-sdk

%files tests -f .mfiles-tests

%changelog
