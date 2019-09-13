#
# spec file for package bytelist
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


Name:           bytelist
Version:        1.0.14
Release:        0
Summary:        A java library for lists of bytes
License:        CPL-1.0 OR GPL-2.0-or-later OR LGPL-2.1-or-later
Group:          Development/Libraries/Java
Url:            https://github.com/jruby/bytelist
Source0:        https://github.com/jruby/bytelist/archive/%{name}-%{version}.tar.gz
Patch0:         %{name}-sourcetarget.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  jcodings
BuildRequires:  junit
Requires:       java
Requires:       javapackages-tools
Requires:       jcodings
BuildArch:      noarch

%description
A small java library for manipulating lists of bytes.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0 -p1

find -name '*.class' -delete
find -name '*.jar' -delete

%build
echo "See %{url} for more info about the %{name} project." > README.txt

export CLASSPATH=$(build-classpath junit jcodings)
mkdir -p lib
ant

%install
mkdir -p %{buildroot}%{_javadir}

cp -p lib/%{name}-1.0.2.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
pushd %{buildroot}%{_javadir}/
  ln -s %{name}-%{version}.jar %{name}.jar
popd

%check
export CLASSPATH=$(build-classpath junit jcodings)
ant test

%files
%{_javadir}/*
%doc README.txt

%changelog
