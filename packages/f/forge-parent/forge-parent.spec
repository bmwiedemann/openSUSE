#
# spec file for package forge-parent
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


Name:           forge-parent
Version:        38
Release:        0
Summary:        Sonatype Forge Parent Pom
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://docs.sonatype.org/display/FORGE/Index
Source0:        http://repo1.maven.org/maven2/org/sonatype/forge/%{name}/%{version}/%{name}-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
Sonatype Forge is a community dedicated to the creation of
development tools and technologies.

%prep
%setup -qcT
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE
# We don't have nexus-staging-maven-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
# We don't use source JARs
%pom_remove_plugin :maven-source-plugin

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom

%files -f .mfiles
%license LICENSE

%changelog
