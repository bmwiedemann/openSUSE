#
# spec file for package hamcrest
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


%bcond_with tests
Name:           hamcrest
Version:        2.2
Release:        0
Summary:        Library of matchers for building test expressions
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/hamcrest/JavaHamcrest
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.xml
Source2:        https://repo1.maven.org/maven2/org/hamcrest/%{name}/%{version}/%{name}-%{version}.pom
Source3:        https://raw.githubusercontent.com/hamcrest/JavaHamcrest/v2.2/LICENSE.txt
Source4:        https://raw.githubusercontent.com/hamcrest/JavaHamcrest/v2.2/README.md
Patch0:         0001-Fix-build-with-OpenJDK-11.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
Provides:       %{name}-core = %{version}
Obsoletes:      %{name}-core < %{version}
Obsoletes:      %{name}-demo < %{version}
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit
%endif

%description
Provides a library of matcher objects (also known as constraints or
predicates) allowing 'match' rules to be defined declaratively, to be
used in other frameworks. Typical scenarios include testing frameworks,
mocking libraries and UI validation rules.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
cp %{SOURCE1} build.xml
cp %{SOURCE3} %{SOURCE4} .

%patch -P 0 -p2

%build
%{ant} \
%if %{without tests}
    -Dtest.skip=true \
%endif
    jar javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{name}/all.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{name}/core.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{name}/library.jar

# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar -a "org.hamcrest:hamcrest-all,org.hamcrest:hamcrest-core,org.hamcrest:hamcrest-library"

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%{_javadir}/%{name}
%license LICENSE.txt
%doc README.md

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}

%changelog
