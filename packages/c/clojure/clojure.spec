#
# spec file for package clojure
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "bootstrap"
%define name_suffix -bootstrap
%else
%define name_suffix %{nil}
%endif
%define group clojure
%define base_name clojure
Name:           %{base_name}%{name_suffix}
Version:        1.12.6
Release:        0
Summary:        Clojure core environment and runtime library
License:        EPL-1.0
URL:            https://clojure.org/
Source0:        https://github.com/clojure/clojure/archive/refs/tags/%{base_name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildArch:      noarch
%if "%{flavor}" == "bootstrap"
BuildRequires:  ant
BuildRequires:  clojure-core-specs-alpha-bootstrap
BuildRequires:  clojure-spec-alpha-bootstrap
%else
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.clojure:core.specs.alpha)
BuildRequires:  mvn(org.clojure:spec.alpha)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
Requires:       clojure-core-specs-alpha
Requires:       clojure-spec-alpha
Requires:       javapackages-tools
Obsoletes:      %{base_name}-bootstrap
#!BuildRequires: clojure-bootstrap clojure-core-specs-alpha clojure-spec-alpha
%endif

%description
Clojure is a dynamic programming language that targets the Java Virtual
Machine. It is designed to be a general-purpose language, combining the
approachability and interactive development of a scripting language with an
efficient and robust infrastructure for multithreaded programming.

%prep
%setup -q -n %{base_name}-%{base_name}-%{version}

%pom_remove_plugin :central-publishing-maven-plugin

%build
%if "%{flavor}" == "bootstrap"
ant -Dmaven.compile.classpath=$(build-classpath clojure/spec.alpha clojure/core.specs.alpha) jar
%else
%{mvn_build} -jf
%endif

%install

%if "%{flavor}" == "bootstrap"
install -dm 0755 %{buildroot}%{_javadir}/%{group}
install -pm 0644 %{base_name}.jar %{buildroot}%{_javadir}/%{group}/%{base_name}.jar
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{group}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{group}/%{base_name}.pom
%add_maven_depmap %{group}/%{base_name}.pom %{group}/%{base_name}.jar
%else
%mvn_install
%jpackage_script clojure.main "" "" %{group}/%{base_name}:%{group}/core.specs.alpha:%{group}/spec.alpha %{base_name}
%endif

%fdupes -s %{buildroot}%{_javadir}

%files -f .mfiles
%license epl-v10.html
%doc readme.txt changes.md
%if "%{flavor}" != "bootstrap"
%{_bindir}/%{base_name}
%endif

%changelog
