#
# spec file for package segment
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


Name:           segment
Version:        2.0.1
Release:        0
Summary:        Split text into segments
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/loomchild/segment
Source0:        https://github.com/loomchild/segment/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(org.jvnet.jaxb2.maven2:maven-jaxb2-plugin)
BuildArch:      noarch

%description
Segment program is used to split text into segments, for example sentences.
Splitting rules are read from SRX file, which is standard format for this task.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
%pom_remove_parent
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-jar-plugin

%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8 \
%endif
	-Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license ../LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license ../LICENSE.txt

%changelog
