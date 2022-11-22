#
# spec file for package testng
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


Name:           testng
Version:        7.4.0
Release:        0
Summary:        Java-based testing framework
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://testng.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        pom.xml
Source2:        %{name}-build.xml
Patch0:         0001-Avoid-accidental-javascript-in-javadoc.patch
Patch1:         0002-Replace-bundled-jquery-with-CDN-link.patch
Patch2:         testng-CVE-2022-4065.patch
BuildRequires:  ant
BuildRequires:  beust-jcommander
BuildRequires:  bsh2
BuildRequires:  fdupes
BuildRequires:  google-guice
BuildRequires:  javapackages-local
BuildRequires:  jsr-305
BuildRequires:  junit
BuildRequires:  snakeyaml
Requires:       mvn(com.beust:jcommander)
Requires:       mvn(org.yaml:snakeyaml)
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

%patch0 -p1
%patch1 -p1
%patch2 -p1

sed 's/@VERSION@/%{version}/' %{SOURCE1} > pom.xml
cp %{SOURCE2} build.xml

# remove any bundled libs, but not test resources
find ! -path "*/test/*" -name *.jar -print -delete
find -name *.class -delete

# these are unnecessary
%pom_remove_plugin :maven-gpg-plugin .
%pom_remove_plugin :maven-source-plugin .
%pom_remove_plugin :maven-javadoc-plugin .

sed -i -e 's/DEV-SNAPSHOT/%{version}/' src/main/java/org/testng/internal/Version.java

cp -p ./src/main/java/*.dtd.html ./src/main/resources/.

# jdk15 classifier is used by some other packages
%{mvn_alias} : :::jdk15:

%build
mkdir -p lib
build-jar-repository -s lib ant/ant beust-jcommander bsh2/bsh google-guice jsr305 junit snakeyaml
%{ant} jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
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
