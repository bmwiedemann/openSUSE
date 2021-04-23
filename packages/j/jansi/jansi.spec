#
# spec file for package jansi
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           jansi
Version:        1.17.1
Release:        0
Summary:        Java library for generating and interpreting ANSI escape sequences
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://fusesource.github.io/jansi/
Source0:        https://github.com/fusesource/jansi/archive/jansi-project-%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  hawtjni-runtime
BuildRequires:  jansi-native
BuildRequires:  javapackages-local
%if %{with tests}
BuildRequires:  ant-junit
%endif
Requires:       mvn(org.fusesource.hawtjni:hawtjni-runtime)
Requires:       mvn(org.fusesource.jansi:jansi-native)
BuildArch:      noarch

%description
Jansi is a java library that allows you to use ANSI escape sequences
in your Java console applications. It implements ANSI support on platforms
which don't support it, like Windows, and provides graceful degradation for
when output is being sent to output devices which cannot support ANSI sequences.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jansi-jansi-project-%{version}
cp %{SOURCE1} .

%pom_disable_module example
%pom_xpath_remove "pom:build/pom:extensions"

%pom_remove_plugin -r :maven-site-plugin

# No maven-uberize-plugin
%pom_remove_plugin -r :maven-uberize-plugin

# Remove unnecessary deps for jansi-native builds
pushd jansi
%pom_remove_dep :jansi-windows32
%pom_remove_dep :jansi-windows64
%pom_remove_dep :jansi-osx
%pom_remove_dep :jansi-freebsd32
%pom_remove_dep :jansi-freebsd64
# it's there only to be bundled in uberjar and we disable uberjar generation
%pom_remove_dep :jansi-linux32
%pom_remove_dep :jansi-linux64
popd

%pom_remove_parent jansi
%pom_xpath_inject pom:project "
  <groupId>org.fusesource.jansi</groupId>
  <version>%{version}</version>" jansi
%pom_change_dep ::\${jansi-native-version} ::1.8 jansi

%build
mkdir -p jansi/lib
build-jar-repository -s jansi/lib \
	hawtjni/hawtjni-runtime jansi-native/jansi-native 
%{ant} -f %{name}-build.xml \
%if %{without tests}
	-Dtest.skip=true \
%endif
	jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 jansi/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 jansi/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
%fdupes -s %{buildroot}%{_javadocdir}
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr jansi/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license license.txt
%doc readme.md changelog.md

%files javadoc
%{_javadocdir}/%{name}

%changelog
