#
# spec file for package jemmy
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2000-2010, JPackage Project
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


%global __jar_repack %{nil}
# Install time macros
%global target_jar build/%{name}.jar
%global target_javadoc build/javadoc/*
Name:           jemmy
Version:        2.3.0.0
Release:        0
Summary:        Java UI testing library
License:        GPL-2.0 OR CDDL-1.0
Group:          Development/Libraries/Java
Url:            https://jemmy.dev.java.net
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#
# svn export https://jemmy.dev.java.net/svn/jemmy/trunk/Jemmy2 jemmy-2.3.0.0 --username <username>
# tar -czvf jemmy-2.3.0.0.tar.gz jemmy-2.3.0.0
#
# where <username> is a name of the user registered here: https://www.dev.java.net/servlets/Join
Source0:        jemmy-2.3.0.0.tar.bz2
Source1:        jemmy-2.3.0.0.pom
Patch0:         jemmy-nosource.patch
BuildRequires:  ant >= 1.6.5
BuildRequires:  fdupes
BuildRequires:  java-devel
# Needed for maven conversions
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
Requires:       java >= 1.6.0
Requires:       javapackages-tools
BuildArch:      noarch

%description
Jemmy is a Java UI testing library. Jemmy represents the most natural way to
test Java UI - perform the testing right from the Java code. Jemmy is a Java
library which provides clear and straightforward API to access Java UI. Tests
are then just java programs, which use the API. Having the tests in Java allows
to use all the flexibility of high level language to capture test logic and
also do any other operations needed to be done from test.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML
Requires:       %{name} = %{version}
Requires:       javapackages-tools

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
find . -type f -name '*.jar' | xargs -t rm
echo "Please, visit https://jemmy.dev.java.net for more info about Jemmy." > README.txt

%build
ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 jar javadoc

%install
# jar
mkdir -p %{buildroot}%{_javadir}
cp -a %{target_jar} %{buildroot}%{_javadir}/%{name}.jar

install -d -m 755 %{buildroot}%{_mavenpomdir}
install -m 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a %{target_javadoc} %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%doc README.txt
%{_javadir}/*.jar
%{_mavenpomdir}/*
%config(noreplace) %{_datadir}/maven-metadata/%{name}.xml*

%files javadoc
%{_javadocdir}/%{name}

%changelog
