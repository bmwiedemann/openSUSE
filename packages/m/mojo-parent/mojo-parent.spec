#
# spec file for package mojo-parent
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


Name:           mojo-parent
Version:        82
Release:        0
Summary:        Codehaus MOJO parent project pom file
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://www.mojohaus.org/mojo-parent/
Source0:        https://github.com/mojohaus/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  javapackages-local
Requires:       mvn(org.junit:junit-bom:pom:)
BuildArch:      noarch

%description
Codehaus MOJO parent project pom file

%prep
%setup -q
# Not needed
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-checkstyle-plugin
%pom_remove_plugin :spotless-maven-plugin

cp %{SOURCE1} .

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom -a org.codehaus.mojo:mojo

%files -f .mfiles
%license LICENSE-2.0.txt

%changelog
