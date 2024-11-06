#
# spec file for package jackson-bom
#
# Copyright (c) 2024 SUSE LLC
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


Name:           jackson-bom
Version:        2.17.3
Release:        0
Summary:        Bill of materials POM for Jackson projects
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/FasterXML/jackson-bom
Source0:        https://github.com/FasterXML/jackson-bom/archive/%{name}-%{version}.tar.gz
# Upstream chooses not to include licenses with their pom only projects:
# https://github.com/FasterXML/jackson-parent/issues/1
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  javapackages-local
BuildRequires:  maven-local
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(com.fasterxml.jackson:jackson-parent:pom:)
BuildArch:      noarch

%description
A "bill of materials" POM for Jackson dependencies.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

# Disable plugins not needed during RPM builds
%pom_remove_plugin ":maven-enforcer-plugin" base
%pom_remove_plugin ":nexus-staging-maven-plugin" base
%pom_remove_dep -r :junit-bom

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
install -pm 0644 base/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/jackson-base.pom
%add_maven_depmap %{name}/%{name}.pom
%add_maven_depmap %{name}/jackson-base.pom

%files -f .mfiles
%doc README.md
%license LICENSE

%changelog
