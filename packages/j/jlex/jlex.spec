#
# spec file for package jlex
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define section		free
Name:           jlex
Version:        1.2.6
Release:        0
Summary:        A Lexical Analyzer Generator for Java
License:        BSD-3-Clause
Group:          Development/Libraries/Java
Url:            http://www.cs.princeton.edu/~appel/modern/java/JLex/
Source0:        http://www.cs.princeton.edu/~appel/modern/java/JLex/Archive/1.2.5/Main.java
Source1:        %{name}-%{version}.build.xml
Patch0:         %{name}-%{version}.static.patch
BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  xml-commons-apis-bootstrap
#!BuildIgnore:  xerces-j2
#!BuildIgnore:  xml-commons
#!BuildIgnore:  xml-commons-apis
#!BuildIgnore:  xml-commons-jaxp-1.3-apis
#!BuildIgnore:  xml-commons-resolver
#!BuildIgnore:  xml-commons-resolver12
BuildArch:      noarch

%description
JLex is a lexical analyzer generator for Java.

%prep
%setup -q -c -T
cp %{SOURCE0} .
%patch0
cp %{SOURCE1} build.xml

%build
unset CLASSPATH
ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

%files
%{_javadir}/*

%changelog
