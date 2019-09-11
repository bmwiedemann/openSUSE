#
# spec file for package kohsuke-pom
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


Name:           kohsuke-pom
Version:        14
Release:        0
Summary:        Kohsuke parent POM
# License is specified in pom file
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/kohsuke/pom
Source0:        https://github.com/kohsuke/pom/archive/pom-%{version}.tar.gz
Source1:        https://raw.github.com/kohsuke/youdebug/youdebug-1.5/LICENSE.txt
BuildRequires:  javapackages-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildArch:      noarch

%description
This package contains Kohsuke parent POM file.

%prep
%setup -q -n pom-pom-%{version}

cp %{SOURCE1} LICENSE

# we don't have these plugins and extensions
%pom_xpath_remove pom:extensions
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :gmaven-plugin

# missing dep org.kohsuke:doxia-module-markdown
%pom_remove_plugin :maven-site-plugin

%pom_remove_plugin :maven-release-plugin

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/pom.pom
%add_maven_depmap %{name}/pom.pom

%files -f .mfiles
%license LICENSE

%changelog
