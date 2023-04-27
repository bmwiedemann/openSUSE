#
# spec file
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


%global cluster jnr
Name:           %{cluster}-enxio
Version:        0.32.14
Release:        0
Summary:        Native I/O access for java
# src/main/java/jnr/enxio/channels/PollSelectionKey.java is LGPLv3
# rest of the source code is ASL 2.0
License:        Apache-2.0 AND LGPL-3.0-only
Group:          Development/Libraries/Java
URL:            https://github.com/%{cluster}/%{name}/
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
# Avoid split-package situation, this patch submitted upstream here: https://github.com/jnr/jnr-enxio/pull/26
#Patch0:         0001-Add-enxio-classes-from-jnr-unixsocket.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.github.jnr:jnr-constants)
BuildRequires:  mvn(com.github.jnr:jnr-ffi)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
Java Native Runtime Enhanced X-platform I/O

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%{mvn_file} : %{cluster}/%{name}

# Unnecessary for RPM builds
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
