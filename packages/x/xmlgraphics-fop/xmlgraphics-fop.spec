#
# spec file for package xmlgraphics-fop
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2000-2008, JPackage Project
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


%define bname fop
Name:           xmlgraphics-fop
Version:        2.1
Release:        0
Summary:        Formatter for Printing XSLT Processed XML Files
License:        Apache-2.0
Group:          Productivity/Publishing/XML
URL:            https://xmlgraphics.apache.org/fop/
Source0:        https://ftp.halifax.rwth-aachen.de/apache/xmlgraphics/fop/source/fop-%{version}-src.tar.gz
Source1:        https://repo.maven.apache.org/maven2/org/apache/xmlgraphics/fop/%{version}/fop-%{version}.pom
#FIX-OPENSUSE: add xmlgraphics-commons to classpath
Source2:        %{name}.script
Source3:        %{name}-fontmetrics.script
Source4:        %{name}-fontlist.script
Source5:        https://download.sourceforge.net/project/offo/offo-hyphenation/2.2/offo-hyphenation.zip
# Manpage(s)
Source10:       %{name}.xml
Source11:       %{name}-fontmetrics.xml
Source12:       %{name}-fontlist.xml
Patch1:         xmlgraphics-fop-cli.patch
Patch2:         hyphenation-more-stack.patch
Patch3:         fix-javadoc-java8.patch
Patch4:         java8-compatibility.patch
# PATCH-FEATURE-OPENSUSE reproducible-build-manifest.patch -- boo#1110024
Patch5:         reproducible-build-manifest.patch
Patch6:         fop-2.1-QDox-2.0.patch
Patch7:         fop-2.1-batik-xmlconstants.patch
BuildRequires:  ant >= 1.6.5
BuildRequires:  apache-pdfbox
BuildRequires:  avalon-framework >= 4.3
BuildRequires:  commons-io >= 2.4
BuildRequires:  commons-logging
BuildRequires:  docbook-xsl-stylesheets
# Needed for maven conversions
BuildRequires:  glassfish-servlet-api
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  libxslt
BuildRequires:  qdox >= 2.0
BuildRequires:  unzip
BuildRequires:  xml-commons-apis >= 1.3
BuildRequires:  xmlgraphics-batik >= 1.8
BuildRequires:  xmlgraphics-commons >= 2.1
#!BuildIgnore:  saxon
Requires:       apache-pdfbox
Requires:       avalon-framework >= 4.3
Requires:       commons-io >= 2.4
Requires:       commons-logging
Requires:       java >= 1.8
Requires:       xml-commons-apis >= 1.3
Requires:       xmlgraphics-commons >= 2.1
%requires_ge    xmlgraphics-batik
Provides:       %{bname} = %{version}-%{release}
Obsoletes:      %{bname} < %{version}-%{release}
Provides:       fo-formatter = %{version}-%{release}
BuildArch:      noarch

%description
FOP (Formatting Objects Processor) is driven by XSL formatting objects
(XSL-FO). It is a Java application that reads a formatting object (FO)
tree and renders the resulting pages to one of the following output
formats: PDF (primary output target), PCL, PS, SVG, XML (area tree
representation), Print, AWT, MIF, and TXT.

%prep
%setup -q -n %{bname}-%{version} -a5
ln -thyph offo-hyphenation/hyph/*.xml
find -name "*.jar" | xargs -t rm
# Remove this file. It needs jai and we don't compile it.
# Just javadoc chokes on it.
rm src/java/org/apache/fop/util/bitmap/JAIMonochromeBitmapConverter.java
%patch1 -p1 -b .cli
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
# Batik 1.11 moved XMLConstants from org.apache.batik.util to org.apache.batik.constants
%patch6 -p1
%if %{?pkg_vcmp:%pkg_vcmp xmlgraphics-batik >= 1.11}%{!?pkg_vcmp:0}
%patch7 -p1
%endif

# Replace keyword "VERSION" in XML files with the real one:
for x in %{SOURCE10} %{SOURCE11} %{SOURCE12}; do
 sed -i "s=@VERSION@=%{version}=" $x
done

%build
build-jar-repository -s lib \
        avalon-framework-api \
        avalon-framework-impl \
        commons-io \
        commons-logging \
        fontbox \
        glassfish-servlet-api \
        xml-commons-apis \
        xml-commons-apis-ext \
        batik-all \
        xmlgraphics-commons \
        qdox

export CLASSPATH= LANG=en_US.UTF-8
%{ant} \
    -Djavac.source=1.8 -Djavac.target=1.8 \
	package

# Build the manpage(s) and HTML
DB=%{_datadir}/xml/docbook/stylesheet/nwalsh/current
for m in %{SOURCE10} %{SOURCE11} %{SOURCE12}; do
 xsltproc $DB/manpages/docbook.xsl $m
# Only filename for HTML is needed, remove anything before /
 xml=${m##*/}
 xsltproc --output ${xml%%.xml}.html $DB/html/docbook.xsl $m
done

%install
# jars
mkdir -p %{buildroot}%{_javadir}
install -m 644 build/%{bname}.jar %{buildroot}%{_javadir}/%{name}.jar
install -m 644 build/%{bname}-hyph.jar %{buildroot}%{_javadir}/%{name}-hyph.jar
install -m 644 build/%{bname}-sandbox.jar %{buildroot}%{_javadir}/%{name}-sandbox.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

# script
mkdir -p %{buildroot}%{_bindir}
cp -p %{SOURCE2}  %{buildroot}%{_bindir}/%{name}
cp -p %{SOURCE3}  %{buildroot}%{_bindir}/%{name}-fontmetrics
cp -p %{SOURCE4}  %{buildroot}%{_bindir}/%{name}-fontlist
# compat symlink
ln -s %{name}             %{buildroot}%{_bindir}/%{bname}
ln -s %{name}-fontmetrics %{buildroot}%{_bindir}/%{bname}-fontmetrics
ln -s %{name}-fontlist    %{buildroot}%{_bindir}/%{bname}-fontlist

# data
install -D -m 644 conf/fop.xconf %{buildroot}%{_sysconfdir}/fop.xconf

# Manpages
mkdir -p %{buildroot}%{_mandir}/man1
for m in *.1; do
  gzip $m
done
cp -vi *.1.gz %{buildroot}%{_mandir}/man1

# Remove prefix xmlgraphics to make also the linked manpage version available
pushd %{buildroot}%{_mandir}/man1
for m in *.1.gz; do
  ln -s $m ${m#*-}
done
popd

%files -f .mfiles
%{_javadir}/%{name}-hyph.jar
%{_javadir}/%{name}-sandbox.jar
%license LICENSE
%doc NOTICE README known-issues.xml
%doc *.html
%attr(0755,root,root) %{_bindir}/%{name}
%{_bindir}/%{bname}
%attr(0755,root,root) %{_bindir}/%{name}-fontmetrics
%{_bindir}/%{bname}-fontmetrics
%attr(0755,root,root) %{_bindir}/%{name}-fontlist
%{_bindir}/%{bname}-fontlist
%{_mandir}/man1/*
%config(noreplace) %{_sysconfdir}/fop.xconf

%changelog
