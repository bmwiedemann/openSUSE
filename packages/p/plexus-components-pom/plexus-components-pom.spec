#
# spec file for package plexus
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


%global short_name plexus-components
Name:           %{short_name}-pom
Version:        1.3.1
Release:        0
Summary:        Plexus Components POM
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/plexus-components
Source0:        http://repo.maven.apache.org/maven2/org/codehaus/plexus/%{short_name}/%{version}/%{short_name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  javapackages-local
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildArch:      noarch

%description
This package provides Plexus Components parent POM used by different
Plexus packages.

%prep
%setup -qcT
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{short_name}.pom
%add_maven_depmap %{name}/%{short_name}.pom

%files -f .mfiles
%license LICENSE

%changelog
