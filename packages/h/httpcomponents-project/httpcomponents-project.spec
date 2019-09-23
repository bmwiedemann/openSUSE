#
# spec file for package httpcomponents-project
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


Name:           httpcomponents-project
Version:        9
Release:        0
Summary:        Common POM file for HttpComponents
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://hc.apache.org/
Source0:        http://archive.apache.org/dist/httpcomponents/httpcomponents-parent/9/httpcomponents-parent-9.pom
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  javapackages-local
BuildRequires:  mvn(org.apache:apache:pom:)
Requires:       mvn(org.apache:apache:pom:)
BuildArch:      noarch

%description
Common Maven POM  file for HttpComponents. This project should be
required only for building dependent packages with Maven. Please don't
use it as runtime requirement.

%prep
%setup -q -T -c %{name}

cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} .

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :clirr-maven-plugin
%pom_remove_plugin :docbkx-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :apache-rat-plugin
%pom_remove_plugin :maven-jar-plugin

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom -a org.apache.httpcomponents:project

%files -f .mfiles
%doc LICENSE-2.0.txt

%changelog
