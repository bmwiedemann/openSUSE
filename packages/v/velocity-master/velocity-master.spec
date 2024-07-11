#
# spec file for package velocity-master
#
# Copyright (c) 2021 SUSE LLC
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


Name:           velocity-master
Version:        4
Release:        0
Summary:        Velocity - Master POM
License:        Apache-2.0
Group:          Development/Libraries/Java
Source0:        https://repo1.maven.org/maven2/org/apache/velocity/%{name}/%{version}/%{name}-%{version}.pom
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  javapackages-local
%if 0%{?rhel} >= 9
BuildRequires:  xmvn-tools
%else
BuildRequires:  xmvn-resolve
%endif
BuildRequires:  mvn(org.apache:apache:pom:)
BuildArch:      noarch

%description
Master POM for Velocity.

%prep
%setup -q -c -T
cp %{SOURCE0} pom.xml
cp %{SOURCE1} LICENSE
%if 0%{?rhel}
%mvn_artifact pom.xml
%endif

%build

%install
%if 0%{?rhel}
%mvn_install
%else
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom
%endif

%files -f .mfiles
%license LICENSE

%changelog
