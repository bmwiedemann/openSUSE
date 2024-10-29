#
# spec file for package s2-geometry-library-java
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


Name:           s2-geometry-library-java
Version:        2.0.0
Release:        0
Summary:        S2 Geometry Library
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://s2geometry.io/
Source0:        https://github.com/google/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.errorprone:error_prone_annotations)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
This is a package for manipulating geometric shapes. Unlike many geometry
libraries, S2 is primarily designed to work with spherical geometry, i.e.,
shapes drawn on a sphere rather than on a planar 2D map. This makes it
especially suitable for working with geographic data.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q

%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%pom_add_dep com.google.errorprone:error_prone_annotations

%{mvn_file} ':{*}' @1

%build
%{mvn_build} -f -- \
	-Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
