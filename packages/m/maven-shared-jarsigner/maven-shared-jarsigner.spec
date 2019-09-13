#
# spec file for package maven-shared-jarsigner
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           maven-shared-jarsigner
Version:        3.0.0
Release:        0
Summary:        Component to assist in signing Java archives
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://maven.apache.org/shared/maven-jarsigner/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/maven-jarsigner/%{version}/maven-jarsigner-%{version}-source-release.zip
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(com.thoughtworks.qdox:qdox) >= 2.0
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils) >= 0.6
BuildRequires:  mvn(org.apache.maven:maven-toolchain)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-annotations)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildArch:      noarch

%description
Apache Maven Jarsigner is a component which provides utilities to sign
and verify Java archive and other files in your Maven MOJOs.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n maven-jarsigner-%{version}
find -name \*.jar -delete

%build
# Tests require bundled JARs, which are removed.
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE
%doc NOTICE README.TXT

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE

%changelog
