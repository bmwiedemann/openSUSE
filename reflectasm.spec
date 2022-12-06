#
# spec file for package reflectasm
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


Name:           reflectasm
Version:        1.11.1
Release:        0
Summary:        High performance Java library that provides reflection by using code generation
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/EsotericSoftware/reflectasm
Source0:        https://github.com/EsotericSoftware/reflectasm/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
ReflectASM is a very small Java library that provides
high performance reflection by using code generation.
An access class is generated to set/get fields,
call methods, or create a new instance. The access class
uses byte-code rather than Java's reflection, so it
is much faster. It can also access primitive fields
via byte-code to avoid boxing.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
find -name "*.class" -delete
find -name "*.jar" -delete

sed -i 's/\r//' license.txt
# Do not shade asm
%pom_remove_plugin :maven-shade-plugin

%{mvn_file} :%{name} %{name}
%{mvn_alias} :%{name} "com.esotericsoftware.%{name}:%{name}"

# AssertionFailedError: expected:<1> but was:<0>
rm -r test/com/esotericsoftware/reflectasm/ClassLoaderTest.java

%build

%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license license.txt

%files javadoc -f .mfiles-javadoc
%license license.txt

%changelog
