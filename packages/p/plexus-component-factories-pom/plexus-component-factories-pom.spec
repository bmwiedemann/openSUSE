#
# spec file for package plexus-component-factories-pom
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global artifactId plexus-component-factories
Name:           plexus-component-factories-pom
Version:        1.0~alpha11
Release:        0
Summary:        Plexus Component Factories POM
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/plexus-component-factories
Source0:        http://repo1.maven.org/maven2/org/codehaus/plexus/%{artifactId}/1.0-alpha-11/%{artifactId}-1.0-alpha-11.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  maven-local
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildArch:      noarch

%description
This package provides Plexus Component Factories parent POM used by different
Plexus packages.

%prep
%setup -q -cT
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%pom_xpath_remove pom:modules

%build
%mvn_alias : plexus:
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%changelog
