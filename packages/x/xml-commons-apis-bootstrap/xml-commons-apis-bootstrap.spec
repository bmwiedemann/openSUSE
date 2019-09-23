# vim:fdm=marker:foldmarker=#>>>,#<<<:foldcolumn=6:
#
# spec file for package xml-commons-apis-bootstrap
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


%define       xml_commons_version 1.0.b2
%define       real_name xml-commons
%define       apis_jar %{real_name}-apis-bootstrap
%define       which_jar %{real_name}-which-bootstrap
%define       resolver_jar %{real_name}-resolver-bootstrap
Name:           xml-commons-apis-bootstrap
Version:        1.4.01
Release:        0
Summary:        Common code for XML projects - bootstrapping package
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://xml.apache.org/commons/
# svn export http://svn.apache.org/repos/asf/xml/commons/tags/xml-commons-1_0_b2/
Source0:        xml-commons-1.0.b2.tar.bz2
# svn export http://svn.apache.org/repos/asf/xml/commons/tags/xml-commons-resolver-1_1_b1/
Source3:        xml-commons-resolver-1.1.b1.tar.bz2
Patch1:         %{real_name}-resolver-crosslink.patch
Patch2:         %{real_name}-resolver-1.1-build_xml.patch
Patch3:         %{real_name}-enum.patch
BuildRequires:  antlr-bootstrap
BuildRequires:  java-devel >= 1.6
# Needed for maven conversions
BuildRequires:  javapackages-tools
#!BuildIgnore:  antlr
#!BuildIgnore:  antlr-java
Provides:       xml-apis
BuildArch:      noarch

%description
This is xml-apis from the java-bootrapping-tools package. DO NOT
INSTALL ... THIS IS JUST FOR PACKAGING & BOOTSTRAPPING JAVA PURPOSES!!

%package -n xml-commons-which-bootstrap
Summary:        Which subproject of xml-commons
Group:          Development/Libraries/Java
URL:            http://xml.apache.org/commons/

%description -n xml-commons-which-bootstrap
This is xml-which from the java-bootrapping-tools package. DO NOT
INSTALL ... THIS IS JUST FOR PACKAGING & BOOTSTRAPPING JAVA PURPOSES!!

%package -n xml-commons-resolver-bootstrap
Summary:        Resolver subproject of xml-commons
Group:          Development/Libraries/Java
URL:            http://xml.apache.org/commons/
Provides:       xml-resolver

%description -n xml-commons-resolver-bootstrap
This is xml-resolver from the java-bootrapping-tools package. DO NOT
INSTALL ... THIS IS JUST FOR PACKAGING & BOOTSTRAPPING JAVA PURPOSES!!

%prep
# To make patches unchanged
%setup -q -T -c
%setup -q -T -D -a 0
%setup -q -T -D -a 3

%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav

%build
#>>> some useful functions ... used throughout bootstrap packages

#>>> delete binary file and files not needed
function delBinaryFiles() {
  set +x
  echo deleting binary files ...
  find . -name "*.class" -o -name "*.jar" -o -name "*DELETED-BY-PACKAGER*" -delete
  set -x
}
#<<<

#>>> make a string with all jar files found in target folder that can be used for a classpath string
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
#<<<

#>>> compiles all *.java file in the current directory tree
# uses mkTargetClasspath for CLASSPATH  variable
# uses LIB_GCJ for CLASSPATH
function compileFiles() {
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
}
#<<<

#>>> make jar archive
# PARAM#1: name of jar archive (without .jar suffix)
# uses $TARGET_DIR to move created jar to
function mkJar() {
  find  -name "version.txt" -or -name "*.class" -or -name "*.properties" -or -name "*.rsc" |\
    xargs jar cfm ${1}.jar manifest.* ;
  mv ${1}.jar $TARGET_DIR
}
#<<<

#<<< end functions

# variables:
COMPILER_COMMAND="javac -source 1.6 -target 1.6 -classpath "
TARGET_DIR=`pwd`
CLASSPATH_ORIG="$CLASSPATH"

delBinaryFiles
#>>> xml-apis and xml-which
# compile external files

pushd xml-commons-1_0_b2
cd java/external/src
# These are java internal
# classes since 1.6
rm -rf javax/xml
mkTargetClasspath
compileFiles
mkJar %{apis_jar}
delBinaryFiles

# compile the rest
cd ../../src/
# remove resolver
rm -rf org/apache/xml/
mkTargetClasspath
compileFiles
mkJar %{which_jar}
delBinaryFiles
popd

pushd xml-commons-resolver-1_1_b1
mkTargetClasspath
export JAR_CLASSPATH=$JAR_CLASSPATH:${TARGET_DIR}/%{apis_jar}.jar:${TARGET_DIR}/%{which_jar}.jar
#compileFiles
pushd java/src/
$COMPILER_COMMAND $JAR_CLASSPATH `find . -name *.java`
rm manifest.which
mkJar %{resolver_jar}
delBinaryFiles
#<<< xml-commons end
popd
popd
#<<< build end

%install
#>>> % install
mkdir -p %{buildroot}%{_javadir}
cp %{apis_jar}.jar %{buildroot}%{_javadir}
ln -sf %{apis_jar}.jar %{buildroot}%{_javadir}/xml-apis.jar
cp %{which_jar}.jar %{buildroot}%{_javadir}
cp %{resolver_jar}.jar %{buildroot}%{_javadir}
ln -sf %{resolver_jar}.jar %{buildroot}%{_javadir}/xml-resolver.jar
#<<< install end

%files
%license xml-commons-1_0_b2/LICENSE.txt
%{_javadir}/%{apis_jar}.jar
%{_javadir}/xml-apis.jar

%files -n xml-commons-which-bootstrap
%license xml-commons-1_0_b2/LICENSE.txt
%{_javadir}/%{which_jar}.jar

%files -n xml-commons-resolver-bootstrap
%license xml-commons-1_0_b2/LICENSE.txt
%{_javadir}/%{resolver_jar}.jar
%{_javadir}/xml-resolver.jar
#<<<

%changelog
