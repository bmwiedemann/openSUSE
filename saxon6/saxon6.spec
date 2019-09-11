#
# spec file for package saxon6
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


%define resolverdir %{_sysconfdir}/java/resolver
Name:           saxon6
Version:        6.5.5
Release:        0
Summary:        The SAXON XSLT Processor from Michael Kay
License:        MPL-1.0
Group:          Productivity/Publishing/XML
Url:            http://saxon.sourceforge.net/
Source0:        http://download.sf.net/saxon/saxon6-5-5.zip
Source1:        %{name}.saxon.script
Source2:        %{name}.build.script
Source3:        %{name}.1
Source4:        http://www.xml.com/2000/08/09/xslt/StructXmlParser.java
# implementes batch based interface to saxon6, SUSE specific
Source5:        saxon6.saxon-batch.script
Patch2:         %{name}-cmdlinefix.patch
#PATCH-FIX-OPENSUSE: jdk7+ assumes ASCII as default encoding, so iso-8859-1 does not work by default
Patch3:         saxon-javac-encoding.patch
#PATCH-FIX-OPENSUSE: bnc#739498 - backport changes from com/icl/saxon/aelfred/XmlParser.java
# to older version released under more permissive license
Patch4:         saxon-add-fixes-from-com-isl-saxon-aelfred.patch
#PATCH-FIX-OPENSUSE: implements batch mode in which saxon is capable to proceed more files per one JVM launch
Patch5:         saxon6-batch.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  fop >= 0.20.1
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  jdom >= 1.0
BuildRequires:  unzip
BuildRequires:  xml-commons-apis
Requires:       %{_sbindir}/update-alternatives
Requires:       jaxp_parser_impl
Provides:       jaxp_transform_impl = %{name}-%{version}
Provides:       saxon
BuildArch:      noarch

%description
The SAXON package is a collection of tools for processing XML
documents. The main components are:

* An XSLT processor, which implements the Version 1.0 XSLT and XPath
   Recommendations from the World Wide Web Consortium, found at
   http://www.w3.org/TR/1999/REC-xslt-19991116 and
   http://www.w3.org/TR/1999/REC-xpath-19991116 with a number of
   powerful extensions. This version of Saxon also includes many of
   the new features defined in the XSLT 1.1 working draft, but for
   conformance and portability reasons these are not available if
   the stylesheet header specifies version="1.0".

* A Java library, which supports a similar processing model to XSL,
   but allows full programming capability, which you need if you
   want to perform complex processing of the data or to access
   external services such as a relational database

* A slightly improved version of the Aelfred parser from Microstar.
   (But you can use SAXON with any SAX-compliant XML parser if you
   prefer).

So you can use SAXON by writing XSLT stylesheets, by writing Java
applications, or by any combination of the two.

%package        aelfred
Summary:        Java XML parser
Group:          Productivity/Publishing/XML
Requires:       xml-commons-apis
Provides:       saxon-aelfred

%description    aelfred
A slightly improved version of the AElfred Java XML parser from
Microstar.

%package        manual
Summary:        Manual for %{name}
Group:          Productivity/Publishing/XML

%description    manual
Manual for %{name}.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Productivity/Publishing/XML

%description    javadoc
Javadoc for %{name}.

%package        demo
Summary:        Demos for %{name}
Group:          Productivity/Publishing/XML
Requires:       %{name} = %{version}-%{release}

%description    demo
Demonstrations and samples for %{name}.

%package        fop
Summary:        FOP support for %{name}
Group:          Productivity/Publishing/XML
Requires:       %{name} = %{version}-%{release}
Requires:       fop >= 0.20.1
Provides:       saxon-fop

%description    fop
FOP support for %{name}.

%package        jdom
Summary:        JDOM support for %{name}
Group:          Productivity/Publishing/XML
Requires:       %{name} = %{version}-%{release}
Requires:       jdom >= 1.0
Provides:       saxon-jdom

%description    jdom
JDOM support for %{name}.

%package        scripts
Summary:        Utility scripts for %{name}
Group:          Productivity/Publishing/XML
Requires:       %{name} = %{version}-%{release}
Provides:       saxon-scripts

%description    scripts
Utility scripts for %{name}.

%prep
%setup -q -c
unzip -q source.zip
cp -p %{SOURCE2} ./build.xml
cp -p %{SOURCE4} XmlParser.java
%patch2
%patch3 -p1
%patch4
%patch5 -p1
cp XmlParser.java com/icl/saxon/aelfred/XmlParser.java
# cleanup unnecessary stuff we'll build ourselves
rm -rf *.jar docs/api

%build
# fixes the javadoc fail
export LC_ALL=en_US.ISO-8859-2
export CLASSPATH=%(build-classpath xml-commons-apis xmlgraphics-fop jdom)
ant \
  -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
  -Dj2se.javadoc=%{_javadocdir}/java \
  -Dfop.javadoc=%{_javadocdir}/fop \
  -Djdom.javadoc=%{_javadocdir}/jdom

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p build/lib/saxon.jar %{buildroot}%{_javadir}/%{name}.jar
cp -p build/lib/saxon-aelfred.jar %{buildroot}%{_javadir}/%{name}-aelfred.jar
cp -p build/lib/saxon-fop.jar %{buildroot}%{_javadir}/%{name}-fop.jar
cp -p build/lib/saxon-jdom.jar %{buildroot}%{_javadir}/%{name}-jdom.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# demo
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr samples/* %{buildroot}%{_datadir}/%{name}
# scripts
mkdir -p %{buildroot}%{_bindir}
sed 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE1} \
  > %{buildroot}%{_bindir}/%{name}
ln -s %{name} %{buildroot}%{_bindir}/saxon
sed 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE5} \
  > %{buildroot}%{_bindir}/%{name}-batch

mkdir -p %{buildroot}%{_mandir}/man1
sed 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE3} \
  > %{buildroot}%{_mandir}/man1/%{name}.1

# jaxp_transform_impl ghost symlink
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
ln -sf %{_sysconfdir}/alternatives/jaxp_transform_impl.jar %{buildroot}%{_javadir}/jaxp_transform_impl.jar

%post
update-alternatives --install %{_javadir}/jaxp_transform_impl.jar \
  jaxp_transform_impl %{_javadir}/%{name}.jar 25

%postun
if [ $1 -eq 0 ] ; then
  update-alternatives --remove jaxp_transform_impl %{_javadir}/%{name}.jar
fi

%files
%{_javadir}/%{name}.jar
%{_javadir}/%{name}.jar
%{_javadir}/jaxp_transform_impl.jar
%ghost %{_sysconfdir}/alternatives/jaxp_transform_impl.jar

%files aelfred
%{_javadir}/%{name}-aelfred*

%files fop
%{_javadir}/%{name}-fop*

%files jdom
%{_javadir}/%{name}-jdom*

%files manual
%doc doc/*.html

%files javadoc
%doc %{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%files scripts
%defattr(0755,root,root,0755)
%{_bindir}/%{name}
%{_bindir}/%{name}-batch
%{_bindir}/saxon
%attr(0644,root,root) %{_mandir}/man1/%{name}.1*

%changelog
