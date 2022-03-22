#
# spec file for package codemodel
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


Name:           codemodel
Version:        2.6
Release:        0
Summary:        Java library for code generators
License:        CDDL-1.1 OR GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            https://codemodel.java.net
Source0:        https://github.com/javaee/jaxb-codemodel/archive/%{name}-project-%{version}.tar.gz
# Remove the dependency on istack-commons (otherwise it will be a
# recursive dependency with the upcoming changes to that package):
Patch0:         %{name}-remove-istack-commons-dependency.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.ant:ant)
BuildArch:      noarch

%description
CodeModel is a Java library for code generators; it provides a way to
generate Java programs in a way much nicer than PrintStream.println().
This project is a spin-off from the JAXB RI for its schema compiler
to generate Java source files.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep

# Unpack and patch the original source:
%setup -q -n jaxb-%{name}-%{name}-project-2.6
%patch0 -p1

%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" 1.8
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" 1.8

# Remove bundled jar files:
find . -name '*.jar' -print -delete
find . -name '*.class' -print -delete

%{mvn_file} :%{name} %{name}
%{mvn_file} :%{name}-annotation-compiler %{name}-annotation-compiler

%build

%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.html

%files javadoc -f .mfiles-javadoc
%license LICENSE.html

%changelog
