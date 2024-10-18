#
# spec file for package fusesource-pom
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


Name:           fusesource-pom
Version:        1.12
Release:        0
Summary:        Parent POM for FuseSource Maven projects
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://fusesource.com/
Source0:        https://repo1.maven.org/maven2/org/fusesource/fusesource-pom/%{version}/fusesource-pom-%{version}.pom
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
This is a shared POM parent for FuseSource Maven projects

%prep
%setup -q -c -T
cp %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE

# Our default java source/target level
%pom_xpath_set "pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" 1.8
%pom_xpath_set "pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" 1.8

%pom_remove_plugin :maven-scm-plugin
%pom_xpath_remove "pom:extension[pom:artifactId[text()='wagon-webdav-jackrabbit']]"

%build

%install
install -dm 755 %{buildroot}%{_mavenpomdir}
install -m 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom

%files -f .mfiles
%license LICENSE

%changelog
