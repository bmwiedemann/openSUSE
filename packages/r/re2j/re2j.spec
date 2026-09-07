#
# spec file for package re2j
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


%bcond_with tests
Name:           re2j
Version:        1.8
Release:        0
Summary:        Linear time regular expression matching in Java
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/google/re2j
Source0:        https://github.com/google/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/com/google/re2j/%{name}/%{version}/%{name}-%{version}.pom
Source2:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
RE2 is a regular expression engine that runs in time linear
in the size of the input. RE2/J is a port of C++ library RE2
to pure Java.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE2} build.xml

%build
ant package javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

#pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -a target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc
%{_javadocdir}/%{name}

%changelog
