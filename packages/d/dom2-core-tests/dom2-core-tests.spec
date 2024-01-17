#
# spec file for package dom2-core-tests
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define section         free
Name:           dom2-core-tests
Version:        0.0.1
Release:        0
Summary:        DOM Conformance Test Suite
License:        W3C
Group:          Development/Libraries/Java
Url:            http://www.w3.org/DOM/Test/
Source0:        http://www.w3.org/2004/04/dom2-core-tests-20040405.jar
Source1:        LICENSE.html
Patch0:         dom2-core-tests-build_xml.patch
BuildRequires:  ant
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  unzip
BuildArch:      noarch

%description
The DOM Test Suites (DOM TS) will consist of a number of tests for each
level of the DOM specification. The tests will be represented in an XML
grammar which ensures that tests can easily be ported from the
description format to a number of specific language bindings. This
grammar will be specified in XML Schema and DTD form. The grammar will
be automatically generated from the DOM specifications themselves, to
ensure stability and correctness.

%prep
%setup -q -c
rm -rf junit
find . -name "*.class" -exec rm {} \;
%patch0 -b .orig
cp %{SOURCE1} .
# not compatible with junit 4
rm -rf org/w3c/domts/JUnitRunner.java

%build
export CLASSPATH=$(build-classpath junit)
ant -Dant.build.javac.source=8 -Dant.build.javac.target=8 dist

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
vjar=$(echo %{name}.jar | sed s+.jar+-%{version}.jar+g)
install -m 644 %{name}-%{version}/%{name}.jar %{buildroot}%{_javadir}/$vjar
pushd %{buildroot}%{_javadir}
   ln -fs $vjar %{name}.jar
popd

%files
%doc LICENSE.html
%{_javadir}/*

%changelog
