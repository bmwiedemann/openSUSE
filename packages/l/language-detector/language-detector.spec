#
# spec file for package language-detector
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


Name:           language-detector
Version:        0.6
Release:        0
Summary:        Language Detection Library for Java
# Source files without license headers https://github.com/optimaize/language-detector/issues/67
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/optimaize/language-detector
Source0:        https://github.com/optimaize/language-detector/archive/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 8
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava:18.0)
BuildRequires:  mvn(com.intellij:annotations)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildArch:      noarch

%description
A language detector / language guesser library in Java.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin

%pom_remove_dep :jsonic

%{mvn_file} com.optimaize.languagedetector:%{name} %{name}

%build

%{mvn_build} -f -- -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
