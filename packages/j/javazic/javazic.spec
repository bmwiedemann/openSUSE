#
# spec file for package javazic
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


Name:           javazic
# javazic source codes comes from jdk7u/jdk mercurial
Version:        1.7.0
Release:        0
Summary:        A time zone compiler for Java
License:        GPL-2.0-with-classpath-exception
Group:          Development/Libraries/Java
URL:            https://icedtea.classpath.org
Source0:        javazic.tar.gz
BuildRequires:  java-devel >= 1.7
BuildArch:      noarch

%description
This is a time zone compiler for opensource Java Virtual Machine
derived from openjdk6 source code.

%prep
%setup -q -c %{name}-%{version}

%build
javac -source 7 -target 7 $(find build/ -iname '*.java')
echo "Main-Class: build.tools.javazic.Main" > manifest.txt
jar -cfm %{name}-%{version}.jar manifest.txt $(find . -iname '*.class')

%install
install -d -m 0755 %{buildroot}/%{_javadir}
install -m 0644 %{name}-%{version}.jar %{buildroot}/%{_javadir}/
# jars
(cd %{buildroot}%{_javadir}/ && for jar in *-%{version}*; do ln -sf ${jar} ${jar/-%{version}/}; done)
install -d -m 0755 %{buildroot}/%{_datadir}/%{name}
cp -rp tzdata_jdk %{buildroot}/%{_datadir}/%{name}/

%files
%{_javadir}/%{name}*.jar
%{_datadir}/%{name}

%changelog
