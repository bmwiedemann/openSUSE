#
# spec file for package jcommon
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define section free
Name:           jcommon
Version:        1.0.23
Release:        0
Summary:        Common library
License:        LGPL-2.1-only
URL:            http://www.jfree.org/jcommon/index.php
Source0:        jcommon-%{version}.tar.xz
BuildRequires:  ant >= 1.6.5
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
Obsoletes:      %{name}-test
BuildArch:      noarch

%description
Collection of classes used by Object Refinery Projects, for example
jfreechart

%package javadoc
Summary:        Common library

%description javadoc
Collection of classes used by Object Refinery Projects, for example
jfreechart

%description javadoc -l fr
Collection of classes used by Object Refinery Projects, for example
jfreechart

%prep
%setup -q
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%{pom_remove_parent}

%build
export CLASSPATH=%(build-classpath junit)
ant \
    -f ant/build.xml \
    -Dbuildstable=true -Dproject.outdir=. -Dbasedir=. \
    -Dbuild.source=1.6 -Dbuild.target=1.6 \
    compile javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc
%{_javadocdir}/%{name}

%changelog
