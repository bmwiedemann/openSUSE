#
# spec file for package methanol
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


Name:           methanol
Version:        1.9.0
Release:        0
Summary:        Lightweight HTTP extensions for Java
License:        MIT
Group:          Development/Libraries/Java
URL:            https://mizosoft.github.io/methanol/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.xml
Source2:        https://repo1.maven.org/maven2/com/github/mizosoft/methanol/%{name}/%{version}/%{name}-%{version}.pom
Source3:        https://raw.githubusercontent.com/mizosoft/methanol/refs/heads/master/LICENSE
BuildRequires:  ant
BuildRequires:  checker-qual
BuildRequires:  fdupes
BuildRequires:  google-errorprone-annotations
BuildRequires:  java-devel >= 11
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
Methanol is a library designed to extend the functionality of Java's
built-in HTTP client (java.net.http). While it acts as a wrapper
around the HTTP client, it provides additionalfeatures such as
multipart uploads, caching, and response decompression.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} build.xml
cp %{SOURCE2} pom.xml
cp %{SOURCE3} .

%pom_add_dep org.checkerframework:checker-qual:3.49.5:provided
%pom_add_dep com.google.errorprone:error_prone_annotations:2.41.0:provided

%build
mkdir -p lib
build-jar-repository -s lib checker-qual google-errorprone/annotations
ant jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}
cp -rp target/site/apidocs %{buildroot}%{_javadocdir}/%{name}
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
