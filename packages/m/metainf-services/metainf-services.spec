#
# spec file for package metainf-services
#
# Copyright (c) 2022 SUSE LLC
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


Name:           metainf-services
Version:        1.9
Release:        0
Summary:        Small java library for generating META-INF/services files
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/kohsuke/metainf-services
Source0:        https://github.com/kohsuke/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        https://raw.github.com/kohsuke/youdebug/youdebug-1.5/LICENSE.txt
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(org.kohsuke:pom:pom:)
BuildArch:      noarch

%description
This package contains small Java library which can be used
for automatic generation of META-INF/services files.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description    javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

cp %{SOURCE1} LICENSE

%pom_remove_plugin :animal-sniffer-maven-plugin

%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:source" "1.8"
%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:target" "1.8"

%build
%{mvn_build} -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
