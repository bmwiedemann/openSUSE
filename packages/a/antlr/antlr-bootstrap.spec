#
# spec file for package antlr-bootstrap
#
# Copyright (c) 2020 SUSE LLC
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


%define gccbinsuffix %(rpm -q --qf "-%%{VERSION}" gcc-java)
%define real_name antlr
Name:           antlr-bootstrap
Version:        2.7.7
Release:        0
Summary:        Antlr for bootstrapping purposes
License:        BSD-3-Clause AND SUSE-Public-Domain
Group:          Development/Libraries/Java
URL:            https://www.antlr.org
Source0:        antlr-%{version}.tar.bz2
Source1:        manifest.antlr
BuildRequires:  java-devel >= 1.8
BuildArch:      noarch

%description
This antlr package is used for bootstrapping purposes only.

%prep
%setup -q -n %{real_name}-%{version}
find | grep "\(ShowString.java$\|StreamConverter.java$\)" && exit 42 || :

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
#>>> some useful functions ... used throughout bootstrap packages
# variables:
TARGET_DIR=`pwd`
CLASSPATH_ORIG="$CLASSPATH"
#>>> delete binary file and files not needed
function delBinaryFiles() {
  set +x
  echo deleting binary files ...
  find . -name "*.class" -o -name "*.jar" -o -name "*DELETED-BY-PACKAGER*" -delete
  set -x
}
#>>> make %{?_smp_mflags} a string with all jar files found in target folder that can be used for a classpath string
# string is saved in JAR_CLASSPATH
function mkTargetClasspath() {
  set +x
  JAR_CLASSPATH=""
  for file in `find %{_javadir} -name "*.jar"`
  do
    JAR_CLASSPATH=$file:$JAR_CLASSPATH
  done
  set -x
}
#>>> compiles all *.java file in the current directory tree
# uses mkTargetClasspath for CLASSPATH  variable
function compileFiles() {
  mkTargetClasspath
  set +x
  COMPILE_CLASSPATH_PATH=.:${JAR_CLASSPATH}
  echo -e "$COMPILER_COMMAND $COMPILE_CLASSPATH_PATH $(find . -name "*.java" | xargs)"
  $COMPILER_COMMAND $COMPILE_CLASSPATH_PATH $(find . -name "*.java" | xargs)
  # check for errors
  if [ $? != 0 ]
  then
    echo ERROR
    exit 1;
  fi
  echo done
  set -x
}
#>>> make %{?_smp_mflags} jar archive
# PARAM#1: name of jar archive (without .jar suffix)
# uses $TARGET_DIR to move created jar to
function mkJar() {
  find  -name "version.txt" -or -name "*.class" -or -name "*.properties" -or -name "*.rsc" -or -name "*manifest*" |\
    xargs jar cfm ${1}.jar manifest.* ;
  mv ${1}.jar $TARGET_DIR
}
COMPILER_COMMAND="javac -source 8 -target 8 -cp  "
delBinaryFiles
mkdir src
mv antlr src
cd src
cp %{SOURCE1} .
compileFiles
mkJar %{name}
delBinaryFiles

%install
install -d -m 0755 %{buildroot}%{_javadir}
install -m 0644 %{name}.jar %{buildroot}%{_javadir}/
ln -s -f %{_javadir}/%{name}.jar %{buildroot}/%{_javadir}/%{name}-%{version}.jar

%files
%{_javadir}/%{name}*.jar

%changelog
