#
# spec file for package swingx
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


%global real_version 1.6.5-1
Name:           swingx
Version:        1.6.5.1
Release:        0
Summary:        A collection of Swing components
License:        LGPL-2.0-only
Group:          Development/Libraries/Java
URL:            https://swingx.java.net/
Source0:        https://github.com/ebourg/swingx/archive/refs/tags/%{real_version}.tar.gz
Patch0:         swingx-remove-jhlabs-filters.patch
Patch1:         swingx-java7-swing-painter-compat.patch
Patch2:         swingx-java7-treepath-compat.patch
Patch3:         swingx-uititlelabel-test-failure.patch
Patch4:         swingx-java8-compat.patch
Patch5:         jdk17.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.kohsuke.metainf-services:metainf-services)
BuildArch:      noarch

%description
SwingX contains a collection of powerful, useful, and just plain fun Swing
components. Each of the Swing components have been extended, providing
data-aware functionality out of the box. New useful components have been
created like the JXDatePicker, JXTaskPane, and JXImagePanel.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{real_version}
%patch -P 0 -p1
%patch -P 1
%patch -P 2
%patch -P 3
%patch -P 4
%patch -P 5 -p1

%pom_disable_module %{name}-testsupport

%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:source" "1.8"
%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:target" "1.8"

%{mvn_file} :%{name}-all %{name} %{name}/%{name}-all

# Remove all binaries
find . -name "*.jar" -print -delete
find . -name "*.class" -print -delete
find . -name "*.so" -print -delete
find . -name "*.dll" -print -delete

%build
%{mvn_build} -f -- -Pjvnet-release -Dmaven.compiler.proc=full

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license COPYING

%files javadoc -f .mfiles-javadoc
%license COPYING

%changelog
