#
# spec file
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


%global short_name logging-parent
Name:           apache-%{short_name}
Version:        5
Release:        0
Summary:        Parent pom for Apache Logging Services projects
License:        Apache-2.0
URL:            https://logging.apache.org/
Source0:        https://repo1.maven.org/maven2/org/apache/logging/%{short_name}/%{version}/%{short_name}-%{version}-source-release.zip
BuildRequires:  javapackages-local
BuildRequires:  unzip
BuildRequires:  mvn(org.apache:apache:pom:)
Requires:       mvn(org.apache:apache:pom:)
BuildArch:      noarch

%description
Parent pom for Apache Logging Services projects.

%prep
%setup -q -n %{short_name}-%{version}

%build

%install
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{name}
install -m 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{short_name}.pom
%add_maven_depmap %{name}/%{short_name}.pom

%files -f .mfiles
%license LICENSE NOTICE

%changelog
