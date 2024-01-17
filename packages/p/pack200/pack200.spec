#
# spec file for package reload4j
#
# Copyright (c) 2023 SUSE LLC
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


Name:           pack200
Version:        14
Release:        0
Summary:        Pack200 compression for JAR files
License:        GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/pack200/pack200
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javamail
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
Pack200 is an optimized compression format for JAR files.
It was introduced in Java 5 and eventually removed in Java 14.
This project is a fork of the Pack200 source code extracted
from OpenJDK just before its removal.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} build.xml

# Test dependency that should not be in compile scope
%pom_remove_dep :junit

%build
%{ant} package javadoc

%install
# jar
install -d -m 0755 %{buildroot}%{_javadir}
install -p -m 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%mvn_install_pom pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE.txt
%doc README.md TODO.md

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}

%changelog
