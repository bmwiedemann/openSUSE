#
# spec file for package morfologik-stemming
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


Name:           morfologik-stemming
Version:        2.1.9
Release:        0
Summary:        Morfologik stemming library
License:        BSD-3-Clause
URL:            https://morfologik.blogspot.com/
Source0:        https://github.com/morfologik/morfologik-stemming/archive/%{version}.tar.gz
Patch0:         morfologik-stemming-binaryinput.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(com.carrotsearch:hppc)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildArch:      noarch

%description
Morfologik provides high quality lemmatisation for the Polish language,
along with tools for building and using byte-based finite state automata.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch0 -p1
find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

chmod 644 README.txt
# Convert from dos to unix line ending
for file in CHANGES.txt CONTRIBUTING.txt README.txt LICENSE.txt; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

%pom_add_dep org.hamcrest:hamcrest-core::test morfologik-tools
%pom_remove_plugin com.carrotsearch.randomizedtesting:junit4-maven-plugin
%pom_remove_plugin de.thetaphi:forbiddenapis
%pom_remove_plugin :maven-javadoc-plugin

# Remove classpath from manifest file
%pom_xpath_set pom:addClasspath false morfologik-tools
# Unwanted task
%pom_remove_plugin :maven-assembly-plugin morfologik-tools

%build
# Test skipped for unavailable test deps
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8 \
%endif
    -Dsource=8 \
	-Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc CHANGES.txt CONTRIBUTING.txt README.txt
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
