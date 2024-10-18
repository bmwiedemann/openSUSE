#
# spec file for package jcodings
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


%global cluster jruby
Name:           jcodings
Version:        1.0.58
Release:        0
Summary:        Java-based codings helper classes for Joni and JRuby
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/%{cluster}/%{name}
Source0:        %{url}/archive/refs/tags/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Requires:       java >= 1.8
Requires:       javapackages-tools
BuildArch:      noarch

%description
%{name}: java-based codings helper classes for Joni and JRuby.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%autosetup -n %{name}-%{name}-%{version}

%pom_xpath_remove pom:extensions
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%{mvn_file} : %{name}

%build
%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
	-Dsource=8

%install
%mvn_install
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
