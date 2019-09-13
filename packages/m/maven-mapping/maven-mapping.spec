#
# spec file for package maven-mapping
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           maven-mapping
Version:        3.0.0
Release:        0
Summary:        Apache Maven Mapping
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://maven.apache.org/shared/%{name}/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.codehaus.plexus:plexus-interpolation)
BuildRequires:  unzip
BuildArch:      noarch

%description
Maven shared component that implements file name mapping.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
