#
# spec file for package apache-commons-lang
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2000-2009, JPackage Project
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


%define base_name lang
%define short_name commons-%{base_name}
Name:           apache-commons-lang
Version:        2.6
Release:        0
Summary:        Apache Commons Lang Package
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/%{base_name}
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Patch0:         fix_StopWatchTest_for_slow_systems.patch
Patch1:         0002-Fix-FastDateFormat-for-Java-7-behaviour.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  junit
# Java 8 is the last version that can build with source and target level 1.4
BuildConflicts: java-devel >= 1.9
Provides:       %{short_name} = %{version}-%{release}
Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{version}-%{release}
BuildArch:      noarch

%description
The standard Java libraries fail to provide enough methods for
manipulation of its core classes. The Commons Lang Component provides
these extra methods.

The Commons Lang Component provides a host of helper utilities for the
java.lang API, notably String manipulation methods, basic numerical
methods, object reflection, creation and serialization, and System
properties. Additionally it contains an inheritable enum type, an
exception structure that supports multiple types of nested-Exceptions
and a series of utilities dedicated to help with building methods, such
as hashCode, toString and equals.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
%patch0
%patch1 -p1
sed -i 's/\r//' *.txt *.html

%pom_remove_parent .

%build
export OPT_JAR_LIST=`cat %{_sysconfdir}/ant.d/junit`
export CLASSPATH=
ant \
    -Dcompile.source=1.4 -Dcompile.target=1.4 \
    -Djunit.jar=$(build-classpath junit4) \
    -Dfinal.name=%{short_name} \
    -Djdk.javadoc=%{_javadocdir}/java \
    test dist

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p target/%{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
(cd %{buildroot}%{_javadir} && for jar in apache-*; do ln -sf ${jar} `echo $jar| sed "s|apache-||g"`; done)

# pom
mkdir -p %{buildroot}%{_mavenpomdir}
cp -p pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr target/apidocs/* %{buildroot}%{_javadocdir}/%{name}/

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc PROPOSAL.html RELEASE-NOTES.txt
%{_javadir}/%{short_name}.jar

%files javadoc
%license LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%changelog
