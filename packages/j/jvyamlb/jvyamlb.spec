#
# spec file for package jvyamlb
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


%global git_commit e0fdedc
%global cluster olabini

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

Name:           jvyamlb
Version:        0.2.5
Release:        0
Summary:        YAML processor for JRuby
License:        MIT
Group:          Development/Libraries/Java

Url:            http://github.com/%{cluster}/%{name}
Source0:        %{url}/tarball/%{version}/%{cluster}-%{name}-%{git_commit}.tar.gz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  bytelist
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  jcodings
BuildRequires:  joda-time
BuildRequires:  junit

Requires:       bytelist
Requires:       java
Requires:       javapackages-tools
Requires:       jcodings
Requires:       joda-time

%description
YAML processor extracted from JRuby.


%prep
%setup -q -n %{cluster}-%{name}-%{git_commit}

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

build-jar-repository -s -p lib joda-time bytelist jcodings

%build
%ant -Djavac.version=1.6

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_javadir}

%__cp -p lib/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
pushd %{buildroot}%{_javadir}/
  %__ln_s %{name}-%{version}.jar %{name}.jar
popd

%check
%ant test

%clean
%__rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_javadir}/*
%doc LICENSE README CREDITS

%changelog
