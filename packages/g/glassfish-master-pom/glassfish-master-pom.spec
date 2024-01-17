#
# spec file for package glassfish-master-pom
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


%global oname pom
Name:           glassfish-master-pom
Version:        8
Release:        0
Summary:        Master POM for Glassfish Maven projects
License:        CDDL-1.0 OR GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            http://glassfish.java.net/
Source0:        http://central.maven.org/maven2/org/glassfish/%{oname}/%{version}/%{oname}-%{version}.pom
Source1:        https://raw.githubusercontent.com/javaee/glassfish/5.0.1/LICENSE
BuildRequires:  javapackages-local
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildArch:      noarch

%description
This is a shared POM parent for Glassfish Maven projects.

%prep
%setup -q -c -T
cp %{SOURCE0} pom.xml
# remove wagon-webdav
%pom_xpath_remove pom:build/pom:extensions
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-compiler-plugin']" "<groupId>org.apache.maven.plugins</groupId><version>2.5.1</version>"
cp -p %{SOURCE1} LICENSE

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{oname}.pom
%add_maven_depmap %{name}/%{oname}.pom

%files -f .mfiles
%license LICENSE

%changelog
