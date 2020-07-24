#
# spec file for package jnr-enxio
#
# Copyright (c) 2020 SUSE LLC
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


Name:           jnr-enxio
Version:        0.19
Release:        0
Summary:        Unix sockets for Java
# src/main/java/jnr/enxio/channels/PollSelectionKey.java is LGPLv3
# rest of the source code is ASL 2.0
License:        Apache-2.0 AND LGPL-3.0-only
URL:            https://github.com/jnr/%{name}/
Source0:        https://github.com/jnr/%{name}/archive/%{name}-%{version}.tar.gz
# Avoid split-package situation, this patch submitted upstream here: https://github.com/jnr/jnr-enxio/pull/26
Patch0:         0001-Add-enxio-classes-from-jnr-unixsocket.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jnr-constants)
BuildRequires:  mvn(com.github.jnr:jnr-ffi)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
Unix sockets for Java.

%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1

find ./ -name '*.jar' -delete
find ./ -name '*.class' -delete

# Unnecessary for RPM builds
%pom_remove_plugin ":maven-javadoc-plugin"
%pom_remove_plugin ":maven-source-plugin"

%build
%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=7 \
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
