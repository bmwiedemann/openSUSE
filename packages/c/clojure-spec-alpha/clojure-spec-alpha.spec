#
# spec file for package clojure-spec-alpha
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
%global group clojure
%global fragment spec-alpha
%global artifact_id spec.alpha
Name:           %{group}-%{fragment}%{name_suffix}
Version:        0.6.249
Release:        0
Summary:        Clojure data and function specifications
License:        EPL-1.0
URL:            https://github.com/clojure/spec.alpha
Source0:        https://github.com/%{group}/%{artifact_id}/archive/refs/tags/v%{version}.tar.gz
BuildArch:      noarch
%if "%{flavor}" == "bootstrap"
BuildRequires:  javapackages-local
%else
BuildRequires:  maven-local
BuildRequires:  mvn(com.theoryinpractise:clojure-maven-plugin)
BuildRequires:  mvn(org.clojure:clojure)
BuildRequires:  mvn(org.clojure:pom.contrib:pom:)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
#!BuildRequires: clojure-spec-alpha-bootstrap clojure-bootstrap clojure-core-specs-alpha-bootstrap
Obsoletes:      %{group}-%{fragment}-bootstrap
%endif

%description
This package provides specifications of data and functions for Clojure.

%prep
%setup -q -n %{artifact_id}-%{version}

%{mvn_file} :{*} %{group}/@1

%build
%if "%{flavor}" == "bootstrap"
jar \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
    --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
    --create --file=spec.alpha.jar -C src/main/clojure .
%else
%{mvn_build} -jf
%endif

%install
%if "%{flavor}" == "bootstrap"
install -dm 0755 %{buildroot}%{_javadir}/%{group}
install -pm 0644 %{artifact_id}.jar %{buildroot}%{_javadir}/%{group}
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{group}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{group}/%{artifact_id}.pom
%add_maven_depmap %{group}/%{artifact_id}.pom %{group}/%{artifact_id}.jar
%else
%mvn_install
%endif

%files -f .mfiles
%license epl-v10.html
%doc README.md

%changelog
