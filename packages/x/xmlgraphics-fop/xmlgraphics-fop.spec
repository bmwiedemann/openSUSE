#
# spec file for package xmlgraphics-fop
#
# Copyright (c) 2023 SUSE LLC
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
Version:        2.8
Release:        0
Summary:        Formatter for Printing XSLT Processed XML Files
License:        Apache-2.0
Group:          Productivity/Publishing/XML
URL:            https://xmlgraphics.apache.org/fop/
Source0:        https://dlcdn.apache.org/xmlgraphics/fop/source/fop-%{version}-src.tar.gz
Source1:        https://download.sourceforge.net/project/offo/offo-hyphenation/2.2/offo-hyphenation.zip
#FIX-OPENSUSE: add xmlgraphics-commons to classpath
Source2:        %{name}.script
Source3:        %{name}-fontmetrics.script
Source4:        %{name}-fontlist.script
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
Patch6:         fop-2.5-QDox-2.0.patch
Patch7:         reproducible.patch
BuildRequires:  ant >= 1.9.15
BuildRequires:  apache-pdfbox >= 2.0.23
BuildRequires:  commons-io >= 2.4
BuildRequires:  commons-logging
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  glassfish-servlet-api
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  libxslt
BuildRequires:  qdox >= 2.0
BuildRequires:  unzip
BuildRequires:  xml-commons-apis
BuildRequires:  xmlgraphics-batik >= 1.14
BuildRequires:  xmlgraphics-commons >= 2.6
#!BuildIgnore:  saxon
Requires:       java >= 1.8
Requires:       xml-commons-apis
Requires:       mvn(com.thoughtworks.qdox:qdox) >= 2.0
Requires:       mvn(commons-io:commons-io)
Requires:       mvn(commons-logging:commons-logging)
Requires:       mvn(javax.servlet:servlet-api)
Requires:       mvn(org.apache.pdfbox:fontbox) >= 2.0.0
Requires:       mvn(org.apache.xmlgraphics:batik-anim) >= 1.14
Requires:       mvn(org.apache.xmlgraphics:batik-awt-util) >= 1.14
Requires:       mvn(org.apache.xmlgraphics:batik-bridge) >= 1.14
Requires:       mvn(org.apache.xmlgraphics:batik-extension) >= 1.14
Requires:       mvn(org.apache.xmlgraphics:batik-gvt) >= 1.14
Requires:       mvn(org.apache.xmlgraphics:batik-transcoder) >= 1.14
Requires:       mvn(org.apache.xmlgraphics:xmlgraphics-commons)
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
%setup -q -n %{bname}-%{version} -a1
ln -t fop/hyph offo-hyphenation/hyph/*.xml
find -name "*.jar" | xargs -t rm
%patch1 -p1 -b .cli
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

# Replace keyword "VERSION" in XML files with the real one:
for x in %{SOURCE10} %{SOURCE11} %{SOURCE12}; do
 sed -i "s=@VERSION@=%{version}=" $x
done

# Building with ant, so the parent is pointless
%pom_remove_parent fop
%pom_xpath_inject pom:project "<version>%{version}</version>" fop

# When building with ant, the fop.jar is an all-in jar,
# so adapt the dependencies accordingly

# Remove dependencies on fop modules included in the jar
%pom_remove_dep :fop-events fop
%pom_remove_dep :fop-util fop
%pom_remove_dep :fop-core fop

# Add dependencies of fop modules included in the jar
%pom_add_dep com.thoughtworks.qdox:qdox:2 fop
%pom_add_dep commons-io:commons-io:1.3.1 fop
%pom_add_dep commons-logging:commons-logging:1.0.4 fop
%pom_add_dep javax.servlet:servlet-api:2.2 fop
%pom_add_dep org.apache.pdfbox:fontbox:2.0 fop
%pom_add_dep org.apache.xmlgraphics:batik-anim:1.14 fop
%pom_add_dep org.apache.xmlgraphics:batik-awt-util:1.14 fop
%pom_add_dep org.apache.xmlgraphics:batik-bridge:1.14 fop
%pom_add_dep org.apache.xmlgraphics:batik-extension:1.14 fop
%pom_add_dep org.apache.xmlgraphics:batik-gvt:1.14 fop
%pom_add_dep org.apache.xmlgraphics:batik-transcoder:1.14 fop
%pom_add_dep org.apache.xmlgraphics:xmlgraphics-commons:2.6 fop

%build
build-jar-repository -s fop/lib \
        commons-io \
        commons-logging \
        fontbox \
        glassfish-servlet-api \
        batik-all \
        xml-commons-apis \
        xml-commons-apis-ext \
        xmlgraphics-commons \
        qdox

export CLASSPATH= LANG=en_US.UTF-8
%{ant} -f fop/build.xml \
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
install -m 644 fop/build/%{bname}.jar %{buildroot}%{_javadir}/%{name}.jar
install -m 644 fop/build/%{bname}-hyph.jar %{buildroot}%{_javadir}/%{name}-hyph.jar
install -m 644 fop/build/%{bname}-sandbox.jar %{buildroot}%{_javadir}/%{name}-sandbox.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 fop/pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
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
install -D -m 644 fop/conf/fop.xconf %{buildroot}%{_sysconfdir}/fop.xconf

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
%doc NOTICE README fop/known-issues.xml
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
