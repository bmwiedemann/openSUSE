#
# spec file for package apache-commons-ognl
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


%global short_name commons-ognl
%global base_version 4.0
%global git_date 20191021
%global git_rev 51cf8f4
Name:           apache-%{short_name}
Version:        %{base_version}~%{git_date}git%{git_rev}
Release:        0
Summary:        Object Graph Navigation Library
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-ognl/
Source0:        %{short_name}-%{git_rev}.tar.xz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(org.javassist:javassist)
BuildArch:      noarch

%description
OGNL is an expression language for getting and setting properties of
Java objects, plus other extras such as list projection and selection
and lambda expressions.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{short_name}-%{git_rev}

%pom_remove_plugin org.apache.maven.plugins:maven-clean-plugin

%{mvn_file} :%{short_name} %{short_name} %{name}

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=6 \
%endif
    -Dmaven.compiler.source=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
