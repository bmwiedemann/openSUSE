#
# spec file for package xz-java
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2013 Peter Conrad
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


Name:           xz-java
Version:        1.11
Release:        0
Summary:        Pure Java implementation of XZ compression
License:        0BSD
Group:          Development/Libraries/Java
URL:            https://tukaani.org/xz/java.html
Source0:        https://tukaani.org/xz/xz-java-%{version}.zip
Patch0:         xz-java-module-info.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  unzip
Provides:       java-xz
Obsoletes:      java-xz
BuildArch:      noarch

%description
This is an implementation of XZ data compression in pure Java.
Single-threaded streamed compression and decompression and random access
decompression have been implemented.

%package javadoc
Summary:        API documentation of Java XZ compression library
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation of xz-java.

%prep
%setup -q -c -n %{name}
%patch -P 0 -p1

%build
ant -Dant.build.javac.{source,target}=8 clean jar doc maven

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 build/maven/xz-%{version}.jar  %{buildroot}%{_javadir}/%{name}.jar
(cd %{buildroot}%{_javadir} && ln -s %{name}.jar xz.jar)
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} build/maven/xz-%{version}.pom %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/doc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license COPYING
%doc {NEWS,README,THANKS}.md
%{_javadir}/xz.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
