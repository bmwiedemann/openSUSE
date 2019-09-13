#
# spec file for package werken-xpath
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


%define dotname werken.xpath
Name:           werken-xpath
Version:        0.9.4
Release:        0
Summary:        XPath implementation using JDOM
License:        Apache-1.1
Group:          Development/Libraries/Java
Url:            http://sourceforge.net/projects/werken-xpath/
Source0:        %{dotname}-%{version}-beta-src.tar.bz2
Source1:        %{name}-%{version}.pom
Patch0:         %{name}-ElementNamespaceContext.patch
Patch1:         %{name}-Partition.patch
Patch2:         %{name}-ParentStep.patch
Patch3:         %{name}-NodeTypeStep.patch
Patch4:         %{name}-UnAbbrStep.patch
Patch5:         %{name}-StringFunction.patch
Patch6:         %{name}-Test.patch
Patch7:         %{name}-Driver.patch
Patch8:         %{name}-runtests_sh.patch
BuildRequires:  ant >= 1.6
BuildRequires:  antlr
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  jdom
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis
Requires:       jdom
Provides:       werken.xpath = %{version}-%{release}
Obsoletes:      werken.xpath < 0.9.4
BuildArch:      noarch

%description
werken.xpath is an implementation of the W3C XPath Recommendation, on
top of the JDOM library.  It takes as input a XPath expression, and a
JDOM tree, and returns a NodeSet (java.util.List) of selected
elements.  Is is being used in the development of the
as-yet-unreleased werken.xslt (eXtensible Stylesheet Language) and the
werken.canonical (XML canonicalization) packages.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
Provides:       werken.xpath-javadoc = %{version}-%{release}
Obsoletes:      werken.xpath-javadoc < 0.9.4

%description    javadoc
werken.xpath is an implementation of the W3C XPath Recommendation, on
top of the JDOM library.  It takes as input a XPath expression, and a
JDOM tree, and returns a NodeSet (java.util.List) of selected
elements.  Is is being used in the development of the
as-yet-unreleased werken.xslt (eXtensible Stylesheet Language) and the
werken.canonical (XML canonicalization) packages.

%prep
%setup -q -n %{dotname}
%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -b .sav
%patch4 -b .sav
%patch5 -b .sav
%patch6 -b .sav
%patch7 -b .sav
%patch8 -b .sav
# remove all binary libs
for j in $(find . -name "*.jar"); do
	mv $j $j.no
done

%build
export CLASSPATH=$(build-classpath jdom antlr xerces-j2 xml-commons-apis)
ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 -Dbuild.compiler=modern package javadoc compile-test
# Note that you'll have to java in PATH for this to work, it is by default
# when using a JPackage JVM.
CLASSPATH=$CLASSPATH:build/werken.xpath.jar:build/test/classes
sh runtests.sh

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p build/%{dotname}.jar %{buildroot}%{_javadir}/%{dotname}.jar
(cd %{buildroot}%{_javadir}; ln -sf %{dotname}.jar %{name}.jar)
# pom
mkdir -p %{buildroot}%{_mavenpomdir}
cp %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-werken-xpath.pom
%add_maven_depmap

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%doc LICENSE LIMITATIONS README TODO
%{_javadir}/*
%{_mavenpomdir}/*
%{_datadir}/maven-metadata/%{name}.xml*

%files javadoc
%{_javadocdir}/%{name}

%changelog
