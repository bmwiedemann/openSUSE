#
# spec file for package jatl
#
# Copyright (c) 2019 SUSE LLC
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


Name:           jatl
Version:        0.2.2
Release:        0
Summary:        Java Anti-Template Language
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/chris-martin/jatl
Source0:        https://github.com/chris-martin/jatl/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(commons-lang:commons-lang)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
Is an extremely lightweight efficient Java library to
generate XHTML or XML in a micro DSL builder/fluent style.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

# Unwanted
%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_plugin :maven-license-plugin
# Unwanted build source jar
%pom_remove_plugin :maven-source-plugin
# Unwanted build javadoc jar
%pom_remove_plugin :maven-javadoc-plugin
# Unavailable
%pom_remove_plugin com.googlecode.maven-gcu-plugin:maven-gcu-plugin

%pom_remove_plugin org.apache.maven.plugins:maven-enforcer-plugin

%{mvn_file} :%{name} %{name}

%build

%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license COPYING

%files javadoc -f .mfiles-javadoc
%license COPYING

%changelog
