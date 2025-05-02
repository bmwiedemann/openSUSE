#
# spec file for package jspecify
#
# Copyright (c) 2025 SUSE LLC
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


Name:           jspecify
Version:        1.0.0
Release:        0
Summary:        An artifact of fully-specified annotations to power static-analysis checks
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://jspecify.org/
Source0:        https://github.com/jspecify/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-build.xml
Source2:        https://repo1.maven.org/maven2/org/jspecify/%{name}/%{version}/%{name}-%{version}.pom
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
An artifact of well-specified annotations to power static analysis checks and
JVM language interop. Developed by consensus of the partner organizations
listed at our main web site, jspecify.org.

Our current focus is on annotations for nullness analysis.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} build.xml

%build
ant jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}
cp -rp target/site/apidocs %{buildroot}%{_javadocdir}/%{name}
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE
%doc AUTHORS README.md

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
