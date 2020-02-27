#
# spec file for package hawtbuf
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


Name:           hawtbuf
Version:        1.11
Release:        0
Summary:        A rich byte buffer library
License:        Apache-2.0
URL:            https://github.com/fusesource/hawtbuf/
Source0:        https://github.com/fusesource/hawtbuf/archive/%{name}-project-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
BuildRequires:  mvn(org.fusesource:fusesource-pom:pom:)
BuildArch:      noarch

%description
This library implements a simple interface with working with
byte arrays. It is a shame that the Java SDK did not come with
a built in class that was just simply a byte[], int offset,
int length class which provided a rich interface similar to
what the String class does for char arrays. This library
fills in that void by providing a Buffer class which does provide
that rich interface.

%package proto
Summary:        A protobuf library

%description proto
HawtBuf Proto: A protobuf library.

%package protoc
Summary:        A protobuf compiler as a maven plugin

%description protoc
HawtBuf Protoc: A protobuf compiler as a maven plugin.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-project-%{version}

%pom_remove_plugin :maven-assembly-plugin

%pom_xpath_set "pom:properties/pom:log4j-version" 1.2.17
%pom_xpath_remove pom:Private-Package

%{mvn_package} ":%{name}-project" %{name}

for i in . %{name}-proto %{name}-protoc; do
  %pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" 1.6 ${i}
  %pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" 1.6 ${i}
done

%build

%{mvn_build} -s -f -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-%{name}
%doc readme.md
%license license.txt notice.md

%files proto -f .mfiles-%{name}-proto
%doc %{name}-proto/readme.md
%license license.txt notice.md

%files protoc -f .mfiles-%{name}-protoc
%doc %{name}-protoc/readme.md
%license license.txt notice.md

%files javadoc -f .mfiles-javadoc
%license license.txt notice.md

%changelog
