#
# spec file for package testng
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


Name:           testng
Version:        7.10.1
Release:        0
Summary:        Java-based testing framework
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://testng.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        https://repo1.maven.org/maven2/org/testng/testng/%{version}/testng-%{version}.pom
Source2:        %{name}-build.xml
Patch0:         0001-Avoid-accidental-javascript-in-javadoc.patch
Patch1:         0002-Replace-bundled-jquery-with-CDN-link.patch
Patch2:         0003-Preserve-Java-8-compatibility.patch
BuildRequires:  ant
BuildRequires:  beust-jcommander
BuildRequires:  fdupes
BuildRequires:  google-guice
BuildRequires:  javapackages-local >= 6
BuildRequires:  jsr-305
BuildRequires:  slf4j
BuildRequires:  snakeyaml >= 2.0
BuildArch:      noarch

%description
TestNG is a testing framework inspired from JUnit and NUnit but introducing
some new functionality, including flexible test configuration, and
distributed test running.  It is designed to cover unit tests as well as
functional, end-to-end, integration, etc.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} pom.xml
cp %{SOURCE2} build.xml
cp -p testng-core/src/main/java/*.dtd.html testng-core/src/main/resources/

%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1

%pom_remove_dep org.webjars:jquery

%build
mkdir -p lib
build-jar-repository -s lib beust-jcommander guice/google-guice jsr-305 slf4j/api snakeyaml
%{ant} jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a org.testng:testng::jdk15:

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc CHANGES.txt README.md
%license LICENSE.txt

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt

%changelog
