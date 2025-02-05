#
# spec file for package languagetool-tools
#
# Copyright (c) 2025 SUSE LLC
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


%global base_name languagetool
Name:           %{base_name}-tools
Version:        4.8
Release:        0
Summary:        Style and Grammar Checker for 25+ Languages - Tools package
License:        LGPL-2.1-or-later
URL:            https://languagetool.org
Source0:        https://github.com/languagetool-org/%{base_name}/archive/v%{version}.tar.gz
# Newer mavens
Patch0:         languagetool-descriptor.patch
Patch1:         languagetool-xgboost-predictor.patch
Patch2:         languagetool-hunspell.patch
Patch3:         languagetool-4.8-lucene-8.patch
Patch4:         languagetool-test-resource.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.carrot2:morfologik-tools)
BuildRequires:  mvn(org.languagetool:languagetool-core)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
LanguageTool is a free and open-source grammar checker.
This package contains the tools for dictionary developers

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{base_name}-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%if %{?pkg_vcmp:%pkg_vcmp lucene-core >= 8}%{!?pkg_vcmp:0}
%patch -P 3 -p1
%endif
%patch -P 4 -p1

pushd %{name}
%{mvn_file} :{*} %{base_name}/@1
popd

%build
# Remove unneeded dependencies
%pom_xpath_remove pom:project/pom:build/pom:extensions

pushd %{name}
%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dsource=8
popd

%install
pushd %{name}
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f %{name}/.mfiles
%license COPYING.txt

%files javadoc -f %{name}/.mfiles-javadoc
%license COPYING.txt

%changelog
