#
# spec file for package IPAddress
#
# Copyright (c) 2024 SUSE LLC
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


Name:           IPAddress
Version:        5.5.1
Release:        0
Summary:        Library for handling IP addresses and subnets, both IPv4 and IPv6
License:        Apache-2.0
URL:            https://github.com/seancfoley/IPAddress
Source0:        https://github.com/seancfoley/IPAddress/archive/v%{version}.tar.gz
Patch0:         IPAddress-encoding.patch
Patch1:         IPAddress-doclet.patch
BuildRequires:  ant
BuildRequires:  aqute-bnd
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
Library for handling IP addresses and subnets, both IPv4 and IPv6

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description    javadoc
This package provides API documentation for xbean.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
find -name \*.jar -delete
find -name \*.class -delete

echo "-reproducible: true" >> IPAddress/ipaddress.bnd
echo "-noextraheaders: true" >> IPAddress/ipaddress.bnd
echo "-snapshot: SNAPSHOT" >> IPAddress/ipaddress.bnd

%build
pushd IPAddress
mkdir bin
%{ant} "create dist jar" "create javadoc" "create pom"

%install
# jar
install -dm 755 %{buildroot}%{_javadir}
install -m 0644 IPAddress/dist/IPAddress*.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} IPAddress/dist/mavenlib/pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -dm 755 %{buildroot}/%{_javadocdir}/%{name}
cp -a IPAddress/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc
%{_javadocdir}/%{name}

%changelog
