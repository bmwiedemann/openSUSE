#
# spec file for package jboss-vfs
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


Name:           jboss-vfs
Version:        3.3.2
Release:        0
Summary:        JBoss VFS
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://www.jboss.org/
Source0:        https://github.com/jbossas/%{name}/archive/refs/tags/%{version}.Final.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.jboss.logging:jboss-logging)
BuildRequires:  mvn(org.jboss.logging:jboss-logging-annotations)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
BuildArch:      noarch

%description
JBoss VFS provides an API to represent a deployment as a read-only hierarchical
file system regardless of whether it is packaged or not. It also allows
deployments to be accessed both locally and remotely using a pluggable design
so that new protocols can easily be added to those supplied by default (file,
jar, memory).

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}.Final

%pom_remove_plugin :maven-checkstyle-plugin

%{mvn_file} : %{name}

%build
%{mvn_build} -f -- \
	-Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
