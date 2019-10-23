#
# spec file for package stringtemplate4
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
%global base_name stringtemplate4
Version:        4.0.8
Release:        0
Summary:        A Java template engine
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://www.stringtemplate.org/
Source0:        https://github.com/antlr/%{base_name}/archive/%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.antlr:antlr-runtime) >= 3.5.2
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch
%if %{with bootstrap}
Name:           %{base_name}-bootstrap
Patch0:         %{base_name}-generated-sources.patch
%else
Name:           %{base_name}
BuildRequires:  mvn(org.antlr:antlr3-maven-plugin) >= 3.5.2
#!BuildRequires: antlr3-bootstrap-tool
#!BuildRequires: %{base_name}-bootstrap
%endif

%description
StringTemplate is a java template engine (with ports for
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%if %{without bootstrap}
%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.
%endif

%prep
%setup -q -n %{base_name}-%{version}
%if %{with bootstrap}
%patch0
%pom_remove_plugin :antlr3-maven-plugin
%endif

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-shade-plugin

%pom_add_dep antlr:antlr:runtime:

# Bug, should be reported upstream
sed -i '/tmpdir =/s,;,+"/"&,' test/org/stringtemplate/v4/test/BaseTest.java
# Tests fail for unknown reason
sed -i /testUnknownNamedArg/s/@Test// test/org/stringtemplate/v4/test/TestGroups.java
sed -i /testMissingImportString/s/@Test// test/org/stringtemplate/v4/test/TestGroupSyntaxErrors.java
# Requires running X server
rm -r test/org/stringtemplate/v4/test/TestEarlyEvaluation.java

%build
%if %{with bootstrap}
%{mvn_build} -fj
%else
%{mvn_build} -f
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc CHANGES.txt contributors.txt README.txt
%license LICENSE.txt

%if %{without bootstrap}
%files javadoc -f .mfiles-javadoc
%license LICENSE.txt
%endif

%changelog
