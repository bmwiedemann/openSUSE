#
# spec file for package jwnl
#
# Copyright (c) 2022 SUSE LLC
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


%global reltag rc3
%global base_version 1.4
%global namedversion %{version}%{namedreltag}
Name:           jwnl
Version:        %{base_version}~%{reltag}
Release:        0
Summary:        Java API for accessing the WordNet relational dictionary
License:        BSD-3-Clause
URL:            https://sourceforge.net/projects/jwordnet/
# Source0:       http://downloads.sourceforge.net/jwordnet/jwnl14-rc2.zip
# svn checkout svn://svn.code.sf.net/p/jwordnet/code/trunk/jwnl/  jwnl-1.4-rc3
# tar cJf jwnl-1.4-rc3.tar.xz jwnl-1.4-rc3
Source0:        %{name}-%{base_version}-%{reltag}.tar.xz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(commons-logging:commons-logging)
BuildArch:      noarch

%description
JWNL is a Java API for accessing the WordNet relational dictionary.
WordNet is widely used for developing NLP applications, and a Java
API such as JWNL will allow developers to more easily use Java for
building NLP applications.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{base_version}-%{reltag}

%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

%pom_change_dep junit:junit:: :::test

sed -i 's/\r//' changes.txt doc/*

%{mvn_file} :%{name} %{name}
%{mvn_alias} %{name}: net.sf.jwordnet:

%build

%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8 \
%endif
	-Dsource=8 -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc changes.txt doc/*
%license license.txt

%files javadoc -f .mfiles-javadoc
%license license.txt

%changelog
