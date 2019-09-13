#
# spec file for package geronimo-specs-pom
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


Name:           geronimo-specs-pom
Version:        1.6
Release:        0
Summary:        Parent POM files for geronimo-specs
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://geronimo.apache.org/
# Following the parent chain all the way up ...
Source0:        http://svn.apache.org/repos/asf/geronimo/specs/tags/specs-parent-%{version}/pom.xml
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  javapackages-local
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
Obsoletes:      geronimo-specs-poms
BuildArch:      noarch

%description
The Project Object Model files for the geronimo-specs modules.

%prep
%setup -q -c -T
cp -p %{SOURCE0} .
cp -p %{SOURCE1} LICENSE
%pom_remove_parent
# not really useful for rpm build
%pom_remove_plugin :maven-idea-plugin

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-geronimo-specs.pom
%add_maven_depmap JPP-geronimo-specs.pom -a org.apache.geronimo.specs:specs

%files -f .mfiles
%license LICENSE

%changelog
