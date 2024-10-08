#
# spec file for package javapackages-meta
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


Name:           javapackages-meta
# Sync the version with javapackages-tools package
Version:        6.2.0
Release:        0
Summary:        Meta-packages for different local modes of Java builds
License:        BSD-3-Clause
Group:          Development/Languages/Java
URL:            https://github.com/fedora-java/javapackages
Source100:      %{name}-rpmlintrc
BuildArch:      noarch

%description
This package provides a set of meta-packages needed by local
modes for Ivy and Maven. These local modes allow artifact
resolution using XMvn resolver.

%package -n ivy-local
Summary:        Local mode for Apache Ivy
Group:          Development/Languages/Java
Requires:       ant
Requires:       apache-ivy >= 2.3.0
Requires:       javapackages-ivy >= %{version}
Requires:       xmvn-connector-ivy
Requires:       xmvn-install
Requires:       xmvn-resolve

%description -n ivy-local
This meta-package pulls in macros, scripts and dependencies
implementing local mode for Apache Ivy, which allows
artifact resolution using XMvn resolver.

%package -n maven-local
Summary:        Local mode for Maven
Group:          Development/Languages/Java
Requires:       javapackages-local >= %{version}
Requires:       javapackages-tools >= %{version}
Requires:       xmvn-connector
Requires:       xmvn-install
Requires:       xmvn-minimal
Requires:       xmvn-mojo
Requires:       xmvn-resolve
Requires:       mvn(org.apache.maven.plugins:maven-compiler-plugin)
Requires:       mvn(org.apache.maven.plugins:maven-jar-plugin)
Requires:       mvn(org.apache.maven.plugins:maven-resources-plugin)
Requires:       mvn(org.apache.maven.plugins:maven-surefire-plugin)

%description -n maven-local
This meta-package pulls in macros, scripts and dependencies
implementing local mode for Maven, which allows artifact
resolution using XMvn resolver.

%prep

%build

%install

%files -n ivy-local

%files -n maven-local

%changelog
