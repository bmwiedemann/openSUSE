#
# spec file for package clojure-maven-plugin
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global group clojure
Name:           clojure-maven-plugin
Version:        1.9.3
Release:        0
Summary:        Maven plugin for compiling Clojure source files
License:        EPL-1.0
URL:            https://github.com/talios/clojure-maven-plugin
Source0:        https://github.com/talios/clojure-maven-plugin/archive/refs/tags/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildArch:      noarch

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
This package contains the API documentation for %{name}.

%description
clojure-maven-plugin is a Maven plugin that allows compiling Clojure source
files, running Clojure REPLs, and executing Clojure scripts within a Maven
project lifecycle.

%prep
%setup -q -n %{name}-%{name}-%{version}

# Remove pre-built upstream JARs to ensure building from source
find . -type f -name "*.jar" -delete

# Remove unnecessary plugins to simplify offline build
%pom_remove_plugin :cyclonedx-maven-plugin
%pom_remove_plugin :ossindex-maven-plugin
%pom_remove_plugin :googleformatter-maven-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-invoker-plugin
%pom_remove_plugin :maven-enforcer-plugin

%{mvn_file} :{*} %{group}/@1

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license epl-v10.html
%doc README.markdown

%files javadoc -f .mfiles-javadoc
%license epl-v10.html

%changelog
