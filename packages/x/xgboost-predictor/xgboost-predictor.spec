#
# spec file for package xgboost-predictor
#
# Copyright (c) 2020 SUSE LLC
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
Version:        0.3.3
Release:        0
Summary:        Pure Java implementation of Xgboost predictor for online prediction tasks
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/h2oai/%{name}
Source0:        https://github.com/h2oai/%{name}/archive/v%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/ai/h2o/%{name}/%{version}/%{name}-%{version}.pom
BuildRequires:  fdupes
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
%setup -q -n %{name}-%{version}/%{name}

cp %{SOURCE1} pom.xml

%{mvn_alias} : biz.k11i:

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=7 \
%endif
	-Dmaven.compiler.source=7 -Dmaven.compiler.target=7 -Dsource=7

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license ../LICENSE

%files javadoc -f .mfiles-javadoc
%license ../LICENSE

%changelog
