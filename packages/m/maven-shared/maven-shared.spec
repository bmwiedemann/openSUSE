#
# spec file for package maven-shared
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           maven-shared
Version:        22
Release:        0
Summary:        Maven Shared Components
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://maven.apache.org/shared/
Source0:        https://github.com/apache/%{name}/archive/%{name}-components-%{version}.tar.gz
BuildRequires:  javapackages-local
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
Requires:       mvn(org.apache.maven:maven-parent:pom:)
BuildArch:      noarch

%description
Maven Shared Components

%prep
%setup -q -n %{name}-%{name}-components-%{version}
chmod -R go=u-w *

# Maven-scm-publish-plugin is not in Fedora
%pom_remove_plugin org.apache.maven.plugins:maven-scm-publish-plugin

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-components.pom
%add_maven_depmap %{name}/%{name}-components.pom

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%changelog
