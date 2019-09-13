#
# spec file for package jython
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


%global pyver %(python -c 'import sys;print(sys.version[0:3])')
%global cpython_version    %{pyver}
%global pyxml_version      0.8.3
%global svn_tag            Release_2_2_1
%global _python_bytecompile_errors_terminate_build 0
Name:           jython
Version:        2.2.1
Release:        0
Summary:        A Java implementation of the Python language
License:        Python-2.0 AND Apache-2.0
Group:          Development/Languages/Python
URL:            http://www.jython.org/
# Use the included fetch-jython.sh script to generate the source drop
# for jython 2.2.1
# sh fetch-jython.sh \
#   jython https://jython.svn.sourceforge.net/svnroot Release_2_2_1
#
Source0:        %{name}-fetched-src-%{svn_tag}.tar.bz2
Source2:        fetch-%{name}.sh
Patch0:         %{name}-cachedir.patch
# Make javadoc and copy-full tasks not depend upon "full-build"
# Also, copy python's license from source directory and not
# ${python.home}
Patch1:         %{name}-nofullbuildpath.patch
# These address CVE-2013-2027 (http://bugs.jython.org/msg8004)
Patch3:         %{name}-cacheperms.patch
Patch4:         %{name}-makeCompiledFilename.patch
Patch5:         %{name}-cached-classes.patch
Patch6:         %{name}-sourcetarget.patch
Patch7:         %{name}-module.patch
Patch8:         %{name}-compareto.patch
Patch9:         %{name}-dont-validate-pom.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  jakarta-oro
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  jline1
BuildRequires:  libreadline-java >= 0.8.0
BuildRequires:  mysql-connector-java
BuildRequires:  python >= %{cpython_version}
BuildRequires:  pyxml >= %{pyxml_version}
BuildRequires:  servletapi5
Requires:       jakarta-oro
Requires:       java >= 1.8
Requires:       javapackages-local
Requires:       jline1
Requires:       libreadline-java >= 0.8.0
Requires:       python >= %{cpython_version}
Requires:       servletapi5
Recommends:     mysql-connector-java
BuildArch:      noarch

%description
Jython is an implementation of the high-level, dynamic, object-oriented
language Python seamlessly integrated with the Java platform. The
predecessor to Jython, JPython, is certified as 100% Pure Java. Jython
is freely available for both commercial and noncommercial use and is
distributed with source code. Jython is complementary to Java and is
especially suited for the following tasks: Embedded scripting--Java
programmers can add the Jython libraries to their system to allow end
users to write simple or complicated scripts that add functionality to
the application. Interactive experimentation--Jython provides an
interactive interpreter that can be used to interact with Java packages
or with running Java applications. This allows programmers to
experiment and debug any Java system using Jython. Rapid application
development--Python programs are typically 2-10X shorter than the
equivalent Java program. This translates directly to increased
programmer productivity. The seamless interaction between Python and
Java allows developers to freely mix the two languages both during
development and in shipping products.

%package manual
Summary:        Manual for jython
Group:          Development/Libraries/Java

%description manual
This package contains the manual for Jython.

Jython is an implementation of the high-level, dynamic, object-oriented
language Python seamlessly integrated with the Java platform. The
predecessor to Jython, JPython, is certified as 100% Pure Java. Jython
is freely available for both commercial and non-commercial use and is
distributed with source code. Jython is complementary to Java and is
especially suited for the following tasks: Embedded scripting - Java
programmers can add the Jython libraries to their system to allow end
users to write simple or complicated scripts that add functionality to
the application. Interactive experimentation - Jython provides an
interactive interpreter that can be used to interact with Java packages
or with running Java applications. This allows programmers to
experiment and debug any Java system using Jython. Rapid application
development - Python programs are typically 2-10X shorter than the
equivalent Java program. This translates directly to increased
programmer productivity. The seamless interaction between Python and
Java allows developers to freely mix the two languages both during
development and in shipping products.

%package javadoc
Summary:        Javadoc for jython
Group:          Development/Libraries/Java

%description javadoc
This package contains the javadoc documentation for jython.

Jython is an implementation of the high-level, dynamic, object-oriented
language Python seamlessly integrated with the Java platform. The
predecessor to Jython, JPython, is certified as 100% Pure Java. Jython
is freely available for both commercial and non-commercial use and is
distributed with source code. Jython is complementary to Java and is
especially suited for the following tasks: Embedded scripting - Java
programmers can add the Jython libraries to their system to allow end
users to write simple or complicated scripts that add functionality to
the application. Interactive experimentation - Jython provides an
interactive interpreter that can be used to interact with Java packages
or with running Java applications. This allows programmers to
experiment and debug any Java system using Jython. Rapid application
development - Python programs are typically 2-10X shorter than the
equivalent Java program. This translates directly to increased
programmer productivity. The seamless interaction between Python and
Java allows developers to freely mix the two languages both during
development and in shipping products.

%package demo
Summary:        Demonstration and samples for jython
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}

%description demo
This package contains demonstration and sample files for Jython.

Jython is an implementation of the high-level, dynamic, object-oriented
language Python seamlessly integrated with the Java platform. The
predecessor to Jython, JPython, is certified as 100% Pure Java. Jython
is freely available for both commercial and non-commercial use and is
distributed with source code. Jython is complementary to Java and is
especially suited for the following tasks: Embedded scripting - Java
programmers can add the Jython libraries to their system to allow end
users to write simple or complicated scripts that add functionality to
the application. Interactive experimentation - Jython provides an
interactive interpreter that can be used to interact with Java packages
or with running Java applications. This allows programmers to
experiment and debug any Java system using Jython. Rapid application
development - Python programs are typically 2-10X shorter than the
equivalent Java program. This translates directly to increased
programmer productivity. The seamless interaction between Python and
Java allows developers to freely mix the two languages both during
development and in shipping products.

%prep
%setup -q -n %{name}-svn-%{svn_tag}
%patch0 -p1
%patch1 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
export CLASSPATH=$(build-classpath mysql-connector-java oro servlet jline1)
# FIXME: fix jpackage-utils to handle multilib correctly
export CLASSPATH=$CLASSPATH:%{_libdir}/libreadline-java/libreadline-java.jar

rm -rf org/apache
perl -p -i -e 's|execon|apply|g' build.xml

ant \
  -Dpython.home=%{_bindir} \
  -Dht2html.dir=%{_datadir}/ht2html \
  -Dpython.lib=./CPythonLib \
  -Dpython.exe=%{_bindir}/python \
  -DPyXmlHome=%{_libdir}/python%{pyver} \
  -Dtargetver=1.3 \
  copy-dist

# remove #! from python files
pushd dist
  for f in `find . -name '*.py'`
  do
    sed --in-place  "s:#!\s*/usr.*::" $f
  done
popd

pushd maven
# generate maven pom
ant -Dproject.version=%{version} install
popd

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/%{name}.jar \
  %{buildroot}%{_javadir}/%{name}.jar
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -m 644 build/maven/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a org.python:jython-standalone,jython:jython

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/Doc/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# data
install -d -m 755 %{buildroot}%{_datadir}/%{name}
# these are not supposed to be distributed
find dist/Lib -type d -name test | xargs rm -rf

cp -pr dist/Lib %{buildroot}%{_datadir}/%{name}
cp -pr dist/Tools %{buildroot}%{_datadir}/%{name}
# demo
cp -pr dist/Demo %{buildroot}%{_datadir}/%{name}
fdupes -s %{buildroot}%{_datadir}/%{name}/Demo
fdupes -s %{buildroot}%{_datadir}/%{name}/{Lib,Tools}
# manual
rm -rf dist/Doc/javadoc
mv dist/Doc %{name}-manual-%{version}
%fdupes -s %{name}-manual-%{version}

# registry
install -m 644 registry %{buildroot}%{_datadir}/%{name}
# scripts
install -d %{buildroot}%{_bindir}

cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
#
# %{name} script
# JPackage Project (http://jpackage.sourceforge.net)
#
# Source functions library
. %{_datadir}/java-utils/java-functions

# Source system prefs
if [ -f %{_sysconfdir}/%{name}.conf ] ; then
  . %{_sysconfdir}/%{name}.conf
fi

# Source user prefs
if [ -f \$HOME/.%{name}rc ] ; then
  . \$HOME/.%{name}rc
fi

# Arch-specific location of dependency
case \$(uname -m) in
   x86_64 | ia64 | s390x | ppc64 | sparc64 )
      JYTHONLIBDIR="%{_libdir}" ;;
   * )
      JYTHONLIBDIR="%{_prefix}/lib" ;;
esac

# Configuration
MAIN_CLASS=org.python.util.%{name}
BASE_FLAGS=-Dpython.home=%{_datadir}/%{name}
BASE_JARS="%{name} oro servlet mysql-connector-java"

BASE_FLAGS="\$BASE_FLAGS -Dpython.console=org.python.util.ReadlineConsole"
BASE_FLAGS="\$BASE_FLAGS -Djava.library.path=\$JYTHONLIBDIR/libreadline-java"
BASE_FLAGS="\$BASE_FLAGS -Dpython.console.readlinelib=Editline"

# Set parameters
set_jvm
CLASSPATH=$CLASSPATH:\$JYTHONLIBDIR/libreadline-java/libreadline-java.jar
set_classpath \$BASE_JARS
set_flags \$BASE_FLAGS
set_options \$BASE_OPTIONS

# Let's start
run "\$@"
EOF

cat > %{buildroot}%{_bindir}/%{name}c << EOF
#!/bin/sh
#
# %{name}c script
# JPackage Project (http://jpackage.sourceforge.net)

%{_bindir}/%{name} %{_datadir}/%{name}/Tools/%{name}c/%{name}c.py "\$@"
EOF

%files
%license LICENSE.txt
%doc ACKNOWLEDGMENTS NEWS README.txt
%attr(0755,root,root) %{_bindir}/%{name}
%attr(0755,root,root) %{_bindir}/%{name}c
%{_javadir}/*
%{_mavenpomdir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/Lib
%{_datadir}/%{name}/Tools
%{_datadir}/%{name}/registry
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml*
%endif

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}

%files manual
%license LICENSE.txt
%doc README.txt
%doc %{name}-manual-%{version}

%files demo
%license LICENSE.txt
%doc ACKNOWLEDGMENTS NEWS README.txt
%{_datadir}/%{name}/Demo

%changelog
