#
# spec file for package werken-xpath
#
# Copyright (c) 2024 SUSE LLC
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


%define dotname werken.xpath
Name:           werken-xpath
Version:        0.9.4
Release:        0
Summary:        XPath implementation using JDOM
License:        Apache-1.1
Group:          Development/Libraries/Java
URL:            https://sourceforge.net/projects/werken-xpath/
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
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  jdom
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis
Requires:       jdom
Provides:       %{dotname} = %{version}-%{release}
Obsoletes:      %{dotname} < %{version}
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
Provides:       %{dotname}-javadoc = %{version}-%{release}
Obsoletes:      %{dotname}-javadoc < %{version}

%description    javadoc
werken.xpath is an implementation of the W3C XPath Recommendation, on
top of the JDOM library.  It takes as input a XPath expression, and a
JDOM tree, and returns a NodeSet (java.util.List) of selected
elements.  Is is being used in the development of the
as-yet-unreleased werken.xslt (eXtensible Stylesheet Language) and the
werken.canonical (XML canonicalization) packages.

%prep
%setup -q -n %{dotname}
%patch -P 0 -b .sav
%patch -P 1 -b .sav
%patch -P 2 -b .sav
%patch -P 3 -b .sav
%patch -P 4 -b .sav
%patch -P 5 -b .sav
%patch -P 6 -b .sav
%patch -P 7 -b .sav
%patch -P 8 -b .sav
# remove all binary libs
for j in $(find . -name "*.jar"); do
	mv $j $j.no
done

%build
export CLASSPATH=$(build-classpath jdom antlr xerces-j2 xml-commons-apis)
%{ant} -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 package javadoc compile-test
# Note that you'll have to java in PATH for this to work, it is by default
# when using a JPackage JVM.
CLASSPATH=$CLASSPATH:build/werken.xpath.jar:build/test/classes
sh runtests.sh

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p build/%{dotname}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -sf %{name}.jar %{buildroot}%{_javadir}/%{dotname}.jar
# pom
mkdir -p %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%{_javadir}/%{dotname}.jar
%license LICENSE
%doc LIMITATIONS README TODO

%files javadoc
%{_javadocdir}/%{name}

%changelog
