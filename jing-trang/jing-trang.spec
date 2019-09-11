#
# spec file for package jing-trang
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        20151127
Release:        0
Summary:        Schema validation and conversion based on RELAX NG
License:        BSD-3-Clause
Group:          Productivity/Text/Utilities
Url:            https://github.com/relaxng/jing-trang
Source0:        https://github.com/relaxng/jing-trang/archive/V%{version}.tar.gz
Source1:        dtdinst.1
#
Patch0:         0001-Various-build-fixes.patch
Patch1:         0002-Use-Xalan-instead-of-Saxon-for-the-build-655601.patch
Patch2:         %{name}-20091111-datatype-sample.patch
Patch3:         %{name}-%{version}-notestng.patch
BuildRequires:  ant >= 1.8.2
#
BuildRequires:  bsh2
BuildRequires:  fdupes
BuildRequires:  isorelax
BuildRequires:  java-devel >= 1.6
BuildRequires:  javacc
BuildRequires:  jpackage-utils
BuildRequires:  qdox
BuildRequires:  relaxngDatatype >= 2011.1
BuildRequires:  saxon9
BuildRequires:  unzip
BuildRequires:  xalan-j2
BuildRequires:  xml-commons-apis
BuildRequires:  xml-commons-resolver
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
Requires:       relaxngDatatype
Requires:       xerces-j2
Requires:       xml-commons-resolver
Recommends:     saxon9

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
Requires:       relaxngDatatype
Requires:       xerces-j2
Requires:       xml-commons-resolver

%description -n trang
Trang converts between different schema languages for XML.  It
supports the following languages: RELAX NG (both XML and compact
syntax), XML 1.0 DTDs, W3C XML Schema.  A schema written in any of the
supported schema languages can be converted into any of the other
supported schema languages, except that W3C XML Schema is supported
for output only, not for input.

%package     -n dtdinst
Summary:        XML DTD to XML instance format converter
Group:          Productivity/Text/Utilities
Requires:       java-headless >= 1.5.0
Requires:       jpackage-utils

%description -n dtdinst
DTDinst is a program for converting XML DTDs into an XML instance
format.

%prep
%setup -q

cp %{SOURCE1} .
mv gcj/{trang,jing}.1 .

rm -r gcj mod/datatype/src/main/org $(find . -name "*.jar")
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
sed -i -e 's/\r//g' lib/isorelax.copying.txt
find . -name "OldSaxon*.java" -delete # No "old" saxon available in SUSE
sed -i -e 's|"\(copying\.txt\)"|"%{_licensedir}/dtdinst/\1"|' \
    dtdinst/index.html
sed -i -e 's|"\(copying\.txt\)"|"%{_licensedir}/trang/\1"|' \
    trang/doc/trang.html trang/doc/trang-manual.html

%build
CLASSPATH=$(build-classpath \
    xalan-j2 xalan-j2-serializer xerces-j2 xml-commons-apis saxon9 relaxngDatatype) \
%{ant} \
	-Dlib.dir=%{_javadir} -Dbuild.sysclasspath=last \
	-Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
	dist

%install
rm -rf %{buildroot} *-%{version}

install -dm 755 $RPM_BUILD_ROOT{%{_javadir},%{_javadocdir},%{_mandir}/man1}

unzip build/dist/jing-%{version}.zip
install -Dpm 644 jing-%{version}/bin/jing.jar %{buildroot}%{_javadir}
mv jing-%{version}/doc/api %{buildroot}%{_javadocdir}/jing
rm -f jing-%{version}/sample/datatype/datatype-sample.jar

# We need to redefine name here to make jpackage_script aware of
# the correct name, otherwise it would use "jing-trang" in configuration names etc.
%define name jing
%jpackage_script com.thaiopensource.relaxng.util.Driver "" "" jing:relaxngDatatype:xml-commons-resolver:xerces-j2 jing true
mkdir -p jing-%{version}/_licenses
mv jing-%{version}/doc/*copying.* jing-%{version}/_licenses

unzip build/dist/trang-%{version}.zip
install -pm 644 trang-%{version}/trang.jar %{buildroot}%{_javadir}
%define name trang
%jpackage_script com.thaiopensource.relaxng.translate.Driver "" "" trang:relaxngDatatype:xml-commons-resolver:xerces-j2 trang true

unzip build/dist/dtdinst-%{version}.zip
install -pm 644 dtdinst-%{version}/dtdinst.jar %{buildroot}%{_javadir}
%define name dtdinst
%jpackage_script com.thaiopensource.xml.dtd.app.Driver "" "" dtdinst dtdinst true

# Install manpages and replace @VERSION@
install -D -m 0644 {dtdinst,jing,trang}.1 %{buildroot}%{_mandir}/man1/
sed -i 's/@VERSION@/%{version}/g' %{buildroot}%{_mandir}/man1/*.1

%fdupes %{buildroot}%{_javadocdir}

%files -n jing
%license jing-%{version}/_licenses/*
%doc jing-%{version}/{readme.html,doc,sample}
%{_mandir}/man1/jing.1%{ext_man}
%{_bindir}/jing
%{_javadir}/jing.jar

%files -n jing-javadoc
%license jing-%{version}/_licenses/*
%{_javadocdir}/jing/

%files -n trang
%license trang-%{version}/copying.txt
%doc trang-%{version}/*.html
%{_bindir}/trang
%{_javadir}/trang.jar
%{_mandir}/man1/trang.1%{ext_man}

%files -n dtdinst
%license dtdinst-%{version}/copying.txt
%doc dtdinst-%{version}/*.{html,rng,xsl}
%doc dtdinst-%{version}/{dtdinst.rnc.txt,teixml.dtd.txt,example}
%{_bindir}/dtdinst
%{_javadir}/dtdinst.jar
%{_mandir}/man1/dtdinst.1%{ext_man}

%changelog
