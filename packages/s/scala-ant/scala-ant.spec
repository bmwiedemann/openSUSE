#
# spec file for package scala-ant
#
# Copyright (c) 2023 SUSE LLC
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


Name:           scala-ant
Version:        2.13.1
Release:        0
Summary:        Scala Ant Support
License:        Apache-2.0
URL:            https://github.com/cigaly/scala-ant
Source0:        %{name}-%{version}.tar.xz
Source1:        scala.ant.d
Patch0:         0001-no-pack200.patch
BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  scala >= %{version}
Requires:       scala >= %{version}
Provides:       ant-scala = %{version}
Obsoletes:      ant-scala < %{version}
BuildArch:      noarch

%description
Ant support from scala, copied from original repository
since it is abandoned in 2.13+

%prep
%setup -q
%patch0 -p1

%build
mkdir -p target/classes

scalac -release 8 -d target/classes -cp $(build-classpath ant scala) \
    $(find src/main -name \*.scala | xargs)
jar -cf target/%{name}-%{version}.jar -C target/classes . -C src/main/resources .

%install
install -d -m 0755 %{buildroot}%{_javadir}/scala
install -p -m 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/scala/%{name}.jar
install -d -m 0755 %{buildroot}%{_sysconfdir}/ant.d
install -p -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/ant.d/scala

%files
%license LICENSE
%{_javadir}/scala/%{name}.jar
%{_sysconfdir}/ant.d/scala

%changelog
