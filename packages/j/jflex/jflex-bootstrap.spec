#
# spec file for package jflex-bootstrap
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


%define with()          %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()       %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
%define bcond_with()    %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
##### WARNING: please do not edit this auto generated spec file. Use the jflex.spec! #####
%define with_bootstrap 1
%define section            free
Name:           jflex-bootstrap
# This line is not a comment, please do not remove it!
#%(sh %{_sourcedir}/jpackage-bootstrap-prepare.sh %{_sourcedir} %{name})
Version:        1.4.3
Release:        0
Summary:        Lexical Analyzer Generator for Java
License:        GPL-2.0+
Group:          Development/Libraries/Java
Url:            http://www.jflex.de/
Source0:        http://www.jflex.de/jflex-%{version}.tar.bz2
Source1:        jflex.script
Source100:      jpackage-bootstrap-prepare.sh
Patch0:         jflex-javac-no-target.patch
Patch1:         jflex-no-cup-no-jflex.patch
Patch2:         jflex-classpath.patch
Patch4:         jflex-byaccj-utl.patch
#PATCH-FIX-OPENSUSE: make AllTests.main empty, code was not compatible with junit 4
Patch5:         jflex-junit4.patch
BuildRequires:  ant
BuildRequires:  java-cup-bootstrap
BuildRequires:  java-devel
Requires:       java_cup
Requires:       javapackages-tools
BuildArch:      noarch
%if %without bootstrap
BuildRequires:  jflex-bootstrap
BuildRequires:  junit
Conflicts:      jflex-bootstrap
%else
Conflicts:      jflex
%endif

%description
JFlex is a lexical analyzer generator for Java written in Java. It is
also a rewrite of the very useful tool JLex which was developed by
Elliot Berk at Princeton University. As Vern Paxson states for his C/C++
tool flex: they do not share any code though.

Design goals The main design goals of JFlex are:

    * Full unicode support
    * Fast generated scanners
    * Fast scanner generation
    * Convenient specification syntax
    * Platform independence
    * JLex compatibility

%if %without bootstrap
%package doc
Summary:        Documentation and examples for %{name}
Group:          Development/Libraries/Java

%description doc
JFlex is a lexical analyzer generator for Java written in Java. It is
also a rewrite of the very useful tool JLex which was developed by
Elliot Berk at Princeton University. As Vern Paxson states for his C/C++
tool flex: they do not share any code though.

Design goals The main design goals of JFlex are:

    * Full unicode support
    * Fast generated scanners
    * Fast scanner generation
    * Convenient specification syntax
    * Platform independence
    * JLex compatibility

This package contains documentation and examples for %{name}
%endif

%prep
%setup -q -n jflex-%{version}
perl -pi -e 's/\r$//g' examples/standalone/sample.inp
rm -rf src/java_cup
find . -name '*.jar' | xargs -t rm
%if %without bootstrap
export CLASSPATH=$(build-classpath java-cup java-cup-runtime junit jflex)
export OPT_JAR_LIST=:
pushd src
%{ant} realclean
%{ant} -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 jflex
popd
%endif
%patch0 -p1

%if %with bootstrap
%patch1 -p1

echo `pwd`
rm -rf src/JFlex/tests
%else # with bootstrap
# You must use Re jflex.spec and have a java-cup and jflex installed
%patch2 -p1
%patch4 -p1
%patch5 -p1
%endif

%build
pushd src
%if %without bootstrap
export CLASSPATH=$(build-classpath java-cup java-cup-runtime junit jflex antlr-bootstrap)
%else
export CLASSPATH=$(build-classpath java-cup java-cup-runtime junit antlr-bootstrap)
%endif
export OPT_JAR_LIST=:
echo `pwd`
%{ant} -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 jar
popd

%install
# jar
mkdir -p %{buildroot}%{_javadir}
cp -a lib/JFlex.jar %{buildroot}%{_javadir}/jflex-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -s ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# compatibility symlink
(cd %{buildroot}%{_javadir} && ln -s jflex.jar JFlex.jar)

mkdir -p %{buildroot}%{_bindir}
install -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/jflex

%files
%doc COPYRIGHT src/README src/changelog
%attr(0755,root,root) %{_bindir}/jflex
%{_javadir}/jflex.jar
%{_javadir}/jflex-%{version}.jar
%{_javadir}/JFlex.jar

%if %without bootstrap
%files doc
%doc examples doc
%endif

%changelog
