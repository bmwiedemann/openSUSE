#
# spec file for package spatial4j
#
# Copyright (c) 2023 SUSE LLC
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


Name:           spatial4j
Version:        0.8
Release:        0
Summary:        A Geospatial Library for Java
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://projects.eclipse.org/projects/locationtech.%{name}
Source0:        https://github.com/locationtech/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
Patch0:         00-jts-1.18.1.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.google.code.maven-replacer-plugin:replacer)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.locationtech.jts:jts-core)
BuildRequires:  mvn(org.noggit:noggit)
BuildArch:      noarch

%description
Spatial4j is a general purpose spatial / geospatial ASL licensed open-source
Java library. It’s core capabilities are 3-fold: to provide common shapes that
can work in Euclidean and geodesic (surface of sphere) world models, to provide
distance calculations and other math, and to read & write shapes from formats
like WKT and GeoJSON. Spatial4j is a project of the LocationTech Industry
Working Group of the Eclipse Foundation.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch -P 0 -p1

%pom_remove_plugin de.thetaphi:forbiddenapis
%pom_remove_plugin org.jacoco:jacoco-maven-plugin

%build
%{mvn_build} -f -- \
	-Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license asl-v20.txt
%doc {notice,README}.md

%files javadoc -f .mfiles-javadoc
%license asl-v20.txt

%changelog
