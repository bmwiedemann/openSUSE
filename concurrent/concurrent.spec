#
# spec file for package concurrent
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


Name:           concurrent
Version:        1.3.4
Release:        0
Summary:        Utility Classes for Concurrent Java Programming
License:        SUSE-Public-Domain
Group:          Development/Libraries/Java
Url:            http://gee.cs.oswego.edu/dl/classes/EDU/oswego/cs/dl/util/concurrent/
Source0:        http://gee.cs.oswego.edu/dl/classes/EDU/oswego/cs/dl/current/concurrent.tar.gz
Source1:        %{name}-%{version}.build.xml
Patch0:         concurrent-jdk8.patch
BuildRequires:  ant
BuildRequires:  java-devel >= 1.8
Obsoletes:      %{name}-javadoc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package provides standardized, efficient versions of utility
classes commonly encountered in concurrent Java programming. This code
consists of implementations of ideas that have been around for ages and
is merely intended to save you the trouble of coding them. Discussions
of the rationale and application of several of these classes can be
found in the second edition of Concurrent Programming in Java.

%prep
%setup -q -c
%patch0 -p0
mkdir -p src/EDU/oswego/cs/dl/util
mv concurrent src/EDU/oswego/cs/dl/util
cp %{SOURCE1} build.xml

%build
ant \
  -Dversion=%{version} \
  -Dj2se.apiurl=%{_javadocdir}/java \
  jar

%install
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 %{name}-%{version}.jar %{buildroot}%{_javadir}/
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

%files
%defattr(0644,root,root,0755)
%{_javadir}/*.jar

%changelog
