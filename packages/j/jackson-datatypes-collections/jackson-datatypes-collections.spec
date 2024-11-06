#
# spec file for package jackson-datatypes-collections
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


Name:           jackson-datatypes-collections
Version:        2.17.3
Release:        0
Summary:        Jackson datatypes: collections
License:        Apache-2.0
URL:            https://github.com/FasterXML/%{name}
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(com.carrotsearch:hppc)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-core) >= 2.16
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind) >= 2.16
BuildRequires:  mvn(com.fasterxml.jackson:jackson-base:pom:) >= 2.16
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.eclipse.collections:eclipse-collections)
BuildRequires:  mvn(org.pcollections:pcollections)
BuildArch:      noarch

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

%package -n jackson-datatype-hppc
Summary:        Add-on module for Jackson to support HPPC data-types

%description -n jackson-datatype-hppc
Jackson data-type module to support JSON serialization and
deserialization of High-Performance Primitive Collections
data-types.

%package -n jackson-datatype-eclipse-collections
Summary:        Add-on module for Jackson to support Eclipse Collections data-types

%description -n jackson-datatype-eclipse-collections
Jackson data-type module to support JSON serialization and deserialization of
Eclipse Collections data types.

%package -n jackson-datatype-pcollections
Summary:        Add-on module for Jackson to support PCollections data-types

%description -n jackson-datatype-pcollections
Jackson data-type module to support JSON serialization and deserialization of
PCollections data types.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

sed -i 's/\r//' hppc/src/main/resources/META-INF/LICENSE
cp -p hppc/src/main/resources/META-INF/LICENSE .

%pom_remove_plugin -r :moditect-maven-plugin
%pom_remove_plugin -r :gradle-module-metadata-maven-plugin

%build
%{mvn_build} -f -s -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
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

%files -n jackson-datatype-hppc -f .mfiles-jackson-datatype-hppc
%doc hppc/README.md hppc/release-notes
%license LICENSE

%files -n jackson-datatype-eclipse-collections -f .mfiles-jackson-datatype-eclipse-collections
%doc eclipse-collections/README.md
%license LICENSE

%files -n jackson-datatype-pcollections -f .mfiles-jackson-datatype-pcollections
%doc pcollections/README.md pcollections/release-notes
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
