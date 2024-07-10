#
# spec file for package felix-parent
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


Name:           felix-parent
Version:        8
Release:        0
Summary:        Parent POM file for Apache Felix Specs
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://felix.apache.org/
Source0:        https://repo1.maven.org/maven2/org/apache/felix/felix-parent/%{version}/%{name}-%{version}-source-release.tar.gz
BuildRequires:  javapackages-local >= 6
BuildRequires:  mvn(org.apache:apache:pom:)
Requires:       mvn(org.apache:apache:pom:)
BuildArch:      noarch

%description
Parent POM file for Apache Felix Specs.

%prep
%setup -q -n felix-parent-%{version}
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :tools-maven-plugin

# wagon ssh dependency unneeded
%pom_xpath_remove pom:extensions
%pom_xpath_remove pom:project/pom:parent/pom:relativePath

%build

%install
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom -a org.apache.felix:felix

%files -f .mfiles
%license LICENSE
%doc NOTICE

%changelog
