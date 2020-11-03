#
# spec file for package apache-commons-parent
#
# Copyright (c) 2020 SUSE LLC
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


%define base_name       parent
%define short_name      commons-%{base_name}
Name:           apache-%{short_name}
Version:        52
Release:        0
Summary:        Apache Commons Parent Pom
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/commons-parent-pom.html
Source0:        https://archive.apache.org/dist/commons/%{short_name}/%{short_name}-%{version}-src.tar.gz
BuildRequires:  javapackages-local
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:  mvn(org.apache:apache:pom:)
# Not generated automatically
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
Requires:       mvn(org.apache:apache:pom:)
Requires:       mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildArch:      noarch

%description
The Project Object Model files for the apache-commons packages.

%prep
%setup -q -n %{short_name}-%{version}-src

# Plugin is not in suse
%pom_remove_plugin org.apache.commons:commons-build-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin

# Plugins useless in package builds
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin

# Remove profiles for plugins that are useless in package builds
for profile in animal-sniffer japicmp jacoco cobertura clirr; do
    %pom_xpath_remove "pom:profile[pom:id='$profile']"
done

%build

%install
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{short_name}.pom
%add_maven_depmap %{name}/%{short_name}.pom

%files -f .mfiles
%doc RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%changelog
