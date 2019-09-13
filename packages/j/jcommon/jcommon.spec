#
# spec file for package jcommon
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


%define section free
Name:           jcommon
Version:        1.0.9
Release:        0
Summary:        Common library
License:        LGPL-2.1
Group:          Development/Languages/Java
Url:            http://www.jfree.org/jcommon/index.php
Source0:        http://download.sourceforge.net/jfreechart/jcommon-%{version}.tar.bz2
BuildRequires:  ant >= 1.6.5
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildArch:      noarch

%description
Collection of classes used by Object Refinery Projects, for example
jfreechart

%package test
Summary:        Common library
Group:          Development/Languages/Java
Requires:       %{name} = %{version}-%{release}
Requires:       junit

%description test
Collection of classes used by Object Refinery Projects, for example
jfreechart

%package javadoc
Summary:        Common library
Group:          Development/Languages/Java

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

%build
export CLASSPATH=%(build-classpath junit)
ant \
    -f ant/build.xml \
    -Dbuildstable=true -Dproject.outdir=. -Dbasedir=. \
    -Dbuild.source=1.6 -Dbuild.target=1.6 \
    compile compile-junit-tests javadoc

%install
install -d -m 755 %{buildroot}%{_javadir}/%{name}
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 %{name}-%{version}.jar %{buildroot}%{_javadir}
install -m 644 lib/%{name}-%{version}-junit.jar %{buildroot}%{_javadir}/%{name}-junit-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}-%{version}

ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}

%files
%doc licence-LGPL.txt README.txt
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-%{version}.jar
%dir %{_javadir}/%{name}

%files test
%{_javadir}/%{name}-junit-%{version}.jar
%{_javadir}/%{name}-junit.jar

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%changelog
