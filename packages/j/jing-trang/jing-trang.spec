#
# spec file for package jing-trang
#
# Copyright (c) 2023 SUSE LLC
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


Name:           jing-trang
Version:        20220510
Release:        0
Summary:        Schema validation and conversion based on RELAX NG
License:        BSD-3-Clause
Group:          Productivity/Text/Utilities
URL:            https://github.com/relaxng/%{name}
Source0:        %{name}-%{version}.tar.xz
Source1:        https://repo1.maven.org/maven2/org/relaxng/jing/%{version}/jing-%{version}.pom
Source2:        https://repo1.maven.org/maven2/org/relaxng/trang/%{version}/trang-%{version}.pom
Source10:       dtdinst.1
#
Patch0:         0000-Various-build-fixes.patch
Patch2:         no-tests.patch
Patch3:         old-saxon.patch
BuildRequires:  ant >= 1.8.2
#
BuildRequires:  bsh2
BuildRequires:  fdupes
BuildRequires:  isorelax
BuildRequires:  java-devel >= 1.8
BuildRequires:  javacc
BuildRequires:  javapackages-local
BuildRequires:  qdox
BuildRequires:  relaxngDatatype >= 2011.1
BuildRequires:  saxon9
BuildRequires:  unzip
BuildRequires:  xalan-j2
BuildRequires:  xml-commons-apis
BuildRequires:  xml-commons-resolver
#
BuildArch:      noarch

%description
%{summary}:

jing:  Schema validator
trang: Multi-format schema converter

%package     -n jing
Summary:        RELAX NG validator in Java
Group:          Productivity/Text/Utilities
Requires:       java-headless
Requires:       jpackage-utils
Requires:       mvn(com.github.relaxng:relaxngDatatype) >= 2011.1
Requires:       mvn(xml-resolver:xml-resolver)
Provides:       mvn(com.thaiopensource:jing)
Provides:       mvn(org.relaxng:jing) = %{version}

%description -n jing
jing is an XML validator implemented in Java. It validates against the
RELAX NG schema language and implements the following specifications:

* RELAX NG 1.0 Specification
* RELAX NG Compact Syntax
* Parts of RELAX NG DTD Compatibility (checking of ID/IDREF/IDREFS)

It also comes with experimental support for schema languages other than
RELAX NG:

* W3C XML Schema (based on Xerces-J)
* Schematron 1.5
* Namespace Routing Language

%package     -n jing-javadoc
Summary:        Javadoc API documentation for Jing
Group:          Documentation/HTML

%description -n jing-javadoc
Javadoc API documentation for Jing.

%package     -n trang
Summary:        Multi-format schema converter based on RELAX NG
Group:          Productivity/Text/Utilities
Requires:       java-headless
Requires:       jpackage-utils
Requires:       mvn(com.github.relaxng:relaxngDatatype) >= 2011.1
Requires:       mvn(xerces:xercesImpl)
Requires:       mvn(xml-resolver:xml-resolver)
Provides:       mvn(com.thaiopensource:trang)
Provides:       mvn(org.relaxng:trang) = %{version}

%description -n trang
Trang converts between different schema languages for XML.  It supports the
following languages: RELAX NG (both XML and compact syntax), XML 1.0 DTDs, W3C
XML Schema.  A schema written in any of the supported schema languages can be
converted into any of the other supported schema languages, except that W3C XML
Schema is supported for output only, not for input.

%package     -n dtdinst
Summary:        XML DTD to XML instance format converter
Group:          Productivity/Text/Utilities
Requires:       java-headless
Requires:       jpackage-utils

%description -n dtdinst
DTDinst is a program for converting XML DTDs into an XML instance format.

%prep
%setup -q

cp %{SOURCE1} jing.pom
cp %{SOURCE2} trang.pom
cp %{SOURCE10} .
mv gcj/{trang,jing}.1 .

%patch0 -p1
%patch2 -p1
%patch3 -p1
rm -f \
  mod/schematron/src/main/com/thaiopensource/validate/schematron/OldSaxonSchemaReaderFactory.java
sed -i -e 's/\r//g' lib/isorelax.copying.txt
sed -i -e 's|"\(copying\.txt\)"|"%{_licensedir}/dtdinst/\1"|' \
    dtdinst/index.html
sed -i -e 's|"\(copying\.txt\)"|"%{_licensedir}/trang/\1"|' \
    trang/doc/trang.html trang/doc/trang-manual.html

# The saxon9 package provides mvn(net.sf.saxon:saxon)
# instead of mvn(net.sf.saxon:Saxon-HE)
%pom_remove_dep net.sf.saxon:Saxon-HE jing.pom
%pom_add_dep net.sf.saxon:saxon jing.pom

%build
CLASSPATH=$(build-classpath \
    xalan-j2 xalan-j2-serializer xerces-j2 xml-commons-apis \
	saxon9 relaxngDatatype) \
%{ant} \
	-Dlib.dir=%{_javadir} -Dbuild.sysclasspath=last \
	-Dant.build.javac.source=8 -Dant.build.javac.target=8 \
	dist

%install
install -dm 0755 %{buildroot}{%{_mandir}/man1,%{_javadocdir}}

unzip build/dist/jing-%{version}.zip
unzip build/dist/trang-%{version}.zip
unzip build/dist/dtdinst-%{version}.zip
rm -f jing-%{version}/sample/datatype/datatype-sample.jar

# JAR artifacts
install -dm 0755 %{buildroot}%{_javadir}
install -dm 0755 %{buildroot}%{_mavenpomdir}

install -pm 0644 jing-%{version}/bin/jing.jar %{buildroot}%{_javadir}/jing.jar
install -pm 0644 jing.pom %{buildroot}%{_mavenpomdir}/jing.pom
%add_maven_depmap jing.pom jing.jar -f jing

install -pm 0644 trang-%{version}/trang.jar %{buildroot}%{_javadir}/trang.jar
install -pm 0644 trang.pom  %{buildroot}%{_mavenpomdir}/trang.pom
%add_maven_depmap trang.pom trang.jar -f trang

install -pm 0644 dtdinst-%{version}/dtdinst.jar %{buildroot}%{_javadir}/dtdinst.jar
%add_maven_depmap org.relaxng:dtdinst:%{version} dtdinst.jar -f dtdinst

# API cocumentation
mv jing-%{version}/doc/api %{buildroot}%{_javadocdir}/jing
%fdupes %{buildroot}%{_javadocdir}

# We need to redefine name here to make jpackage_script aware of
# the correct name, otherwise it would use "jing-trang" in configuration names etc.
%define name jing
%jpackage_script com.thaiopensource.relaxng.util.Driver "" "" jing:relaxngDatatype:xml-commons-resolver:xerces-j2 jing true
mkdir -p jing-%{version}/_licenses
mv jing-%{version}/doc/*copying.* jing-%{version}/_licenses

%define name trang
%jpackage_script com.thaiopensource.relaxng.translate.Driver "" "" trang:relaxngDatatype:xml-commons-resolver:xerces-j2 trang true

%define name dtdinst
%jpackage_script com.thaiopensource.xml.dtd.app.Driver "" "" dtdinst dtdinst true

# Install manpages and replace @VERSION@
install -Dm0644 {dtdinst,jing,trang}.1 %{buildroot}%{_mandir}/man1/
sed -i 's/@VERSION@/%{version}/g' %{buildroot}%{_mandir}/man1/*.1

%files -n jing -f .mfiles-jing
%license jing-%{version}/_licenses/*
%doc jing-%{version}/{readme.html,doc,sample}
%{_mandir}/man1/jing.1%{?ext_man}
%{_bindir}/jing

%files -n jing-javadoc
%{_javadocdir}/jing
%license jing-%{version}/_licenses/*

%files -n trang -f .mfiles-trang
%license trang-%{version}/copying.txt
%doc trang-%{version}/*.html
%{_bindir}/trang
%{_mandir}/man1/trang.1%{?ext_man}

%files -n dtdinst -f .mfiles-dtdinst
%license dtdinst-%{version}/copying.txt
%doc dtdinst-%{version}/*.{html,rng,xsl}
%doc dtdinst-%{version}/{dtdinst.rnc.txt,teixml.dtd.txt,example}
%{_bindir}/dtdinst
%{_mandir}/man1/dtdinst.1%{?ext_man}

%changelog
