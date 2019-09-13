#
# spec file for package felix-gogo-parent
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


Name:           felix-gogo-parent
Version:        4
Release:        0
Summary:        Parent pom for Apache Felix Gogo
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://felix.apache.org/documentation/subprojects/apache-felix-gogo.html
Source0:        http://archive.apache.org/dist/felix/gogo-parent-%{version}-source-release.tar.gz
BuildRequires:  javapackages-local
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.felix:felix-parent:pom:)
BuildArch:      noarch

%description
Apache Felix Gogo is a subproject of Apache Felix implementing a command
line shell for OSGi. It is used in many OSGi runtimes and servers.

%prep
%setup -q -n gogo-parent-%{version}

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/gogo-parent.pom
%add_maven_depmap %{name}/gogo-parent.pom

%files -f .mfiles
%license LICENSE NOTICE

%changelog
