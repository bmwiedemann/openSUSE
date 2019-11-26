#
# spec file for package kryo
#
# Copyright (c) 2019 SUSE LLC
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


Name:           kryo
Version:        4.0.2
Release:        0
Summary:        Object graph serialization framework for Java
License:        Apache-2.0 AND BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/EsotericSoftware/kryo
Source0:        %{name}-%{version}.tar.xz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
Patch0:         kryo-4.0.2-unsafe.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.esotericsoftware:minlog)
BuildRequires:  mvn(com.esotericsoftware:reflectasm)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
Kryo is a fast and efficient object graph serialization framework for Java.
The goals of the project are speed, efficiency, and an easy to use API.
The project is useful any time objects need to be persisted, whether to a
file, database, or over the network.

Kryo can also perform automatic deep and shallow copying/cloning.
This is direct copying from object to object, not object->bytes->object.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p1 -E

# Do not use shaded reflectasm
%pom_disable_module pom-shaded.xml

%pom_remove_plugin :maven-assembly-plugin pom-main.xml
%pom_remove_plugin :clirr-maven-plugin pom-main.xml

%pom_remove_plugin :maven-bundle-plugin pom-main.xml
%pom_add_plugin org.apache.felix:maven-bundle-plugin pom-main.xml "
<extensions>true</extensions>
<configuration>
  <instructions>
    <Import-Package>sun.reflect;resolution:=optional,*</Import-Package>
    <Export-Package>com.esotericsoftware.kryo.*</Export-Package>
  </instructions>
</configuration>"

cp -p %{SOURCE1} .
sed -i 's/\r//' license.txt LICENSE-2.0.txt

%{mvn_file} :%{name} %{name}
%{mvn_alias} :%{name} "com.esotericsoftware.%{name}:%{name}"

%mvn_package :%{name}-parent __noinstall

%build

%{mvn_build} -f -- -f pom-main.xml \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc CHANGES.md README.md
%license license.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%license license.txt LICENSE-2.0.txt

%changelog
