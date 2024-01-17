#
# spec file for package weld-parent
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


Name:           weld-parent
Version:        34
Release:        0
Summary:        Parent POM for Weld
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://weld.cdi-spec.org
Source0:        https://github.com/weld/parent/archive/%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  javapackages-local
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildArch:      noarch

%description
Parent POM for Weld

%prep
%setup -q -n parent-%{version}
cp %{SOURCE1} LICENSE

%pom_remove_plugin ":maven-enforcer-plugin"
%pom_remove_plugin ":maven-remote-resources-plugin"
%pom_remove_plugin ":maven-eclipse-plugin"
%pom_remove_plugin ":buildnumber-maven-plugin"

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom

%files -f .mfiles
%license LICENSE

%changelog
