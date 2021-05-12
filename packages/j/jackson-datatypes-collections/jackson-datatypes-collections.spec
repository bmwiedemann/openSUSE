#
# spec file for package jackson-datatypes-collections
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


%bcond_with jp_minimal
Name:           jackson-datatypes-collections
Version:        2.10.3
Release:        0
Summary:        Jackson datatypes: collections
License:        Apache-2.0
URL:            https://github.com/FasterXML/jackson-datatypes-collections
Source0:        https://github.com/FasterXML/jackson-datatypes-collections/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= %{version}
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= %{version}
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildArch:      noarch
%if %{without jp_minimal}
BuildRequires:  mvn(com.carrotsearch:hppc)
%endif

%description
This is a multi-module umbrella project for various Jackson
Data-type modules to support 3rd party Collection libraries.

Currently included are:
* Guava data-type
* HPPC data-type
* PCollections data-type

%package -n jackson-datatype-guava
Summary:        Add-on module for Jackson which handles Guava data-types

%description -n jackson-datatype-guava
Add-on datatype-support module for Jackson that handles
Guava types (currently mostly just collection ones).

%if %{without jp_minimal}
%package -n jackson-datatype-hppc
Summary:        Add-on module for Jackson to support HPPC data-types

%description -n jackson-datatype-hppc
Jackson data-type module to support JSON serialization and
deserialization of High-Performance Primitive Collections
data-types.
%endif

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

sed -i 's/\r//' hppc/src/main/resources/META-INF/LICENSE
cp -p hppc/src/main/resources/META-INF/LICENSE .

%if %{with jp_minimal}
# Disable modules with additional deps
%pom_disable_module hppc
%endif

# Deps are missing from Fedora for these modules:
%pom_disable_module eclipse-collections
%pom_disable_module pcollections

%pom_remove_plugin :moditect-maven-plugin guava
%pom_remove_plugin :moditect-maven-plugin hppc

%build
%{mvn_build} -f -s -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8 \
%endif
	-Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-jackson-datatypes-collections
%doc README.md release-notes
%license LICENSE

%files -n jackson-datatype-guava -f .mfiles-jackson-datatype-guava
%doc guava/README.md guava/release-notes
%license LICENSE

%if %{without jp_minimal}
%files -n jackson-datatype-hppc -f .mfiles-jackson-datatype-hppc
%doc hppc/README.md hppc/release-notes
%license LICENSE
%endif

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
