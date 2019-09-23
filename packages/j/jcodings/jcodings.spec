#
# spec file for package jcodings
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


%global cluster jruby
Name:           jcodings
Version:        1.0.12
Release:        0
Summary:        Java-based codings helper classes for Joni and JRuby
License:        MIT
Group:          Development/Libraries/Java
Url:            https://github.com/jruby/jcodings
Source0:        https://github.com/jruby/jcodings/archive/%{version}.tar.gz
BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
Requires:       java
Requires:       javapackages-tools
BuildArch:      noarch

%description
%{name}: java-based codings helper classes for Joni and JRuby.

%prep
%setup -q

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%build
echo "See %{url} for more info about the %{name} project." > README.txt

ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6

%install
mkdir -p %{buildroot}%{_javadir}

cp -p target/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
pushd %{buildroot}%{_javadir}/
  ln -s %{name}-%{version}.jar %{name}.jar
popd

%files
%{_javadir}/*
%doc README.txt

%changelog
