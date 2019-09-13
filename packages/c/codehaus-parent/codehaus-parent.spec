#
# spec file for package codehaus-parent
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


Name:           codehaus-parent
Version:        4
Release:        0
Summary:        Parent pom file for codehaus projects
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://codehaus.org/
#Next version with license is at https://github.com/sonatype/codehaus-parent/blob/master/pom.xml
Source0:        http://repo1.maven.org/maven2/org/codehaus/codehaus-parent/%{version}/codehaus-parent-%{version}.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  javapackages-local
BuildRequires:  xmvn-resolve
BuildArch:      noarch

%description
This package contains the parent pom file for codehaus projects.

%prep
%setup -q -c -T
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE
%pom_xpath_remove pom:project/pom:build/pom:plugins

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom

%files -f .mfiles
%license LICENSE

%changelog
