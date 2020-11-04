#
# spec file for package itext-parent
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


Name:           itext-parent
Version:        1.0.0
Release:        0
Summary:        iText Parent POM
License:        AGPL-3.0-only
Group:          Development/Libraries/Java
URL:            http://codehaus.org/
Source0:        https://repo1.maven.org/maven2/com/itextpdf/%{name}/%{version}/%{name}-%{version}.pom
Source1:        http://www.gnu.org/licenses/agpl-3.0.txt
BuildRequires:  javapackages-local
BuildRequires:  xmvn-resolve
BuildArch:      noarch

%description
The Parent POM for iText Projects.

%prep
%setup -q -c -T
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE
%pom_remove_plugin : 

%build

%install
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom

%files -f .mfiles
%license LICENSE

%changelog
