#
# spec file for package tzdb
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


Name:           tzdb
Version:        1.8
Release:        0
Summary:        Time zone rules compiler Java
License:        GPL-2.0-with-classpath-exception
Group:          Development/Libraries/Java
Url:            http://icedtea.classpath.org
Source0:        tzdb-%{version}-37392f2f5d59.tar.xz
BuildRequires:  java-devel >= 1.7
BuildRequires:  xz
BuildArch:      noarch

%description
This is a time zone rules compiler for opensource Java Virtual Machine
derived from openjdk8 source code.

%prep
%setup -q %{name}-%{version}

%build
javac -source 7 -target 7 -classpath . $(find build/ -iname '*.java')
echo "Main-Class: build.tools.tzdb.TzdbZoneRulesCompiler" > manifest.txt
jar -cfm %{name}-%{version}.jar manifest.txt $(find . -iname '*.class')

%install
# skip /usr/lib/rpm/brp-check-bytecode-version:
export NO_BRP_CHECK_BYTECODE_VERSION=true
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
