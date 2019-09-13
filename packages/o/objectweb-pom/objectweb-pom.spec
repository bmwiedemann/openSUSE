#
# spec file for package objectweb-pom
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


Name:           objectweb-pom
Version:        1.5
Release:        0
Summary:        Objectweb POM
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://gitorious.ow2.org/ow2/pom/
Source0:        http://repo.maven.apache.org/maven2/org/ow2/ow2/%{version}/ow2-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  javapackages-local
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildArch:      noarch

%description
This package provides Objectweb parent POM used by different
Objectweb packages.

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/ow2.pom
%add_maven_depmap %{name}/ow2.pom

%files -f .mfiles
%license LICENSE

%changelog
