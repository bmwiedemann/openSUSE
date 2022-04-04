#
# spec file for package ee4j
#
# Copyright (c) 2022 SUSE LLC
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


Name:           ee4j
Version:        1.0.7
Release:        0
Summary:        EE4J Project
License:        EPL-2.0 AND GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://projects.eclipse.org/projects/ee4j
Source0:        https://github.com/eclipse-ee4j/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
Eclipse Enterprise for Java (EE4J) is an open source initiative to create standard
APIs, implementations of those APIs, and technology compatibility kits for Java
runtimes that enable development, deployment, and management of server-side and
cloud-native applications.

EE4J is based on the Java(TM) Platform, Enterprise Edition (Java EE) standards,
and uses Java EE 8 as the baseline for creating new standards.

%prep
%setup -q

%build

%install
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 parent/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/project.pom
%add_maven_depmap %{name}/project.pom

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%changelog
