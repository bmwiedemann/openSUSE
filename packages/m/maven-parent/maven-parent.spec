#
# spec file for package maven-parent
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           maven-parent
Version:        45
Release:        0
Summary:        Apache Maven parent POM
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org
Source0:        https://repo1.maven.org/maven2/org/apache/maven/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildRequires:  apache-parent
BuildRequires:  javapackages-local >= 6
BuildRequires:  unzip
Requires:       apache-parent
Obsoletes:      maven-plugins-pom < %{version}-%{release}
Provides:       maven-plugins-pom = %{version}-%{release}
Obsoletes:      maven-shared < %{version}-%{release}
Provides:       maven-shared = %{version}-%{release}
BuildArch:      noarch

%description
Apache Maven parent POM file used by other Maven projects.

%prep
%setup -q
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :spotless-maven-plugin
%pom_remove_plugin -r :maven-scm-publish-plugin
%pom_remove_plugin -r :maven-dependency-plugin

%pom_remove_dep :junit-bom

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom

for i in doxia-tools maven-extensions maven-plugins maven-shared-components maven-skins; do
    %{mvn_install_pom} ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
    %add_maven_depmap %{name}/${i}.pom
done

%files -f .mfiles
%license LICENSE
%doc NOTICE

%changelog
