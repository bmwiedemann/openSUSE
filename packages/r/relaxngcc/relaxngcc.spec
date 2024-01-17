#
# spec file for package relaxngcc
#
# Copyright (c) 2021 SUSE LLC
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


Name:           relaxngcc
Version:        1.12
Release:        0
Summary:        RELAX NG Compiler Compiler
License:        Apache-1.1
Group:          Development/Libraries/Java
URL:            http://relaxngcc.sourceforge.net/en/index.htm
# generate-tarball.sh
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.xml
Source100:      generate-tarball.sh
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  icu
BuildRequires:  isorelax
BuildRequires:  java-devel
BuildRequires:  javacc
BuildRequires:  jpackage-utils
BuildRequires:  msv-msv
BuildRequires:  msv-xsdlib
BuildRequires:  relaxngDatatype
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis
Requires:       isorelax
Requires:       msv-msv
Requires:       msv-xsdlib
Requires:       relaxngDatatype
Requires:       xerces-j2
Requires:       xml-commons-apis
BuildArch:      noarch

%description
RelaxNGCC is a tool for generating Java source code from a given RELAX NG
grammar. By embedding code fragments in the grammar like yacc or JavaCC, you can
take appropriate actions while parsing valid XML documents against the grammar.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep

# Prepare the original sources:
%setup -q

# Remove to avoid dependency on commons-jelly:
rm src/relaxngcc/maven/ChildAntProjectTag.java

# Some of the sources don't use the correct end of line encoding, so to be
# conservative fix all of them:
find . -type f -exec dos2unix {} \;

# Some of the source files contain characters outside of the ASCII set that
# cause problems when compiling, so make sure that they are translated to
# ASCCI:
sources='
src/relaxngcc/builder/SwitchBlockInfo.java
'
for source in ${sources}
do
  uconv -f UTF-8 -i -t ASCII --to-callback escape-java -o tmp.tmp ${source} && mv tmp.tmp ${source}
done

%build

# Populate the lib directory with references to the jar files required for the
# build:
mkdir lib
build-jar-repository -s -p lib \
  msv-msv msv-xsdlib relaxngDatatype isorelax javacc ant

# Put the ant build files in place:
cp %{SOURCE1} build.xml

# Run the ant build:
ant jar javadoc

%install

# Jar files:
mkdir -p %{buildroot}%{_javadir}
install -pm 644 relaxngcc.jar %{buildroot}%{_javadir}/%{name}.jar

# Javadoc files:
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr javadoc/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%fdupes -s doc/

%files
%{_javadir}/*
%license LICENSE.txt
%doc src/HOWTO-readAutomata.txt readme.txt
%doc doc/*

%files javadoc
%{_javadocdir}/*
%license LICENSE.txt

%changelog
