#
# spec file for package xgboost-predictor
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           xgboost-predictor
Version:        0.3.20
Release:        0
Summary:        Pure Java implementation of Xgboost predictor for online prediction tasks
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/h2oai/%{name}
Source0:        %{name}-%{version}.tar.xz
Source1:        https://repo1.maven.org/maven2/ai/h2o/%{name}/%{version}/%{name}-%{version}.pom
Source2:        https://repo1.maven.org/maven2/ai/h2o/h2o-tree-api/%{version}/h2o-tree-api-%{version}.pom
Source100:      aggregator.pom
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(net.jafama:jafama)
BuildArch:      noarch

%description
Pure Java implementation of XGBoost predictor for online prediction tasks.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
%{summary}

%prep
%setup -q

cp %{SOURCE100} pom.xml
cp %{SOURCE1} %{name}/pom.xml
cp %{SOURCE2} h2o-tree-api/pom.xml

%mvn_package :aggregator __noinstall

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8 \
%endif
	-Dmaven.compiler.source=8 -Dmaven.compiler.target=8 -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
