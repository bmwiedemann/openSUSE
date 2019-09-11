#
# spec file for package saxon8
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
Name:           saxon8
Version:        B.8.8
Release:        0
Summary:        Java Basic XPath 2.0, XSLT 2.0, and XQuery 1.0 implementation
License:        MPL-1.1
Group:          Development/Languages/Other
Url:            http://saxon.sourceforge.net/
Source0:        http://download.sf.net/saxon/saxon-resources8-8.tar.bz2
Source1:        %{name}.saxon.script
Source2:        %{name}.saxonq.script
Source3:        %{name}.build.script
Source4:        %{name}.1
Source5:        %{name}q.1
BuildRequires:  ant
BuildRequires:  bea-stax-api
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  jdom >= 1.0-0.b7
BuildRequires:  unzip
BuildRequires:  xml-commons-apis
BuildRequires:  xom
Requires:       %{_sbindir}/update-alternatives
Requires:       bea-stax
Requires:       bea-stax-api
Requires:       jaxp_parser_impl
Provides:       jaxp_transform_impl
BuildArch:      noarch

%description
Release 8.6 represents an important milestone in Saxonica's progressive
implementation of the XPath 2.0, XSLT 2.0, and XQuery 1.0
specifications. Saxon 8.6 is aligned with the W3C Candidate
Recommendation published on 3 November 2005. It is a complete and
conformant implementation, providing all the mandatory features of
those specifications and nearly all the optional features. Saxon is
available in two versions. Saxon-B is a non-schema-aware processor, and
is available as an open-source product, free of charge, from
SourceForge. It is designed to conform to the basic conformance level
of XSLT 2.0, and the equivalent level of functionality in XQuery 1.0.
Saxon-SA is the schema-aware version of the package, and is available
as a commercially supported product from Saxonica Limited.

This package provides the Basic XSLT 2.0 and XQuery 1.0 processor.
Includes the command line interfaces and the JAVA APIs; also includes a
standalone XPath API that doesn't depend on JAXP 1.3.

%package        manual
Summary:        Manual for saxon8
Group:          Development/Languages/Other

%description    manual
Manual for saxon8.

%package        javadoc
Summary:        Javadoc for saxon8
Group:          Development/Languages/Other

%description    javadoc
Javadoc for saxon8.

%package        demo
Summary:        Demos for saxon8
Group:          Development/Languages/Other
Requires:       %{name} = %{version}-%{release}

%description    demo
Demonstrations and samples for saxon8.

%package        sql
Summary:        SQL support for saxon8
Group:          Development/Languages/Other
Requires:       %{name} = %{version}-%{release}

%description    sql
Supports XSLT extensions for accessing and updating a relational
database from within a stylesheet.

%package        jdom
Summary:        JDOM support for saxon8
Group:          Development/Languages/Other
Requires:       %{name} = %{version}-%{release}
Requires:       jdom >= 1.0-0.b7

%description    jdom
Provides additional classes enabling Saxon to be used with JDOM trees.
Supports using a JDOM document as the input or output of
transformations and queries. Requires jdom.jar on the classpath.

%package        dom
Summary:        DOM support for saxon8
Group:          Development/Languages/Other
Requires:       %{name} = %{version}-%{release}
#Requires:       jdom >= 0:1.0-0.b7

%description    dom
Provides additional classes enabling Saxon to be used with the DOM
Document Object Model. Supports using a DOM as the input or output of
transformations and queries, and calling extension functions that use
DOM interfaces to access a Saxon tree structure. Requires DOM level 3
(dom.jar, part of JAXP 1.3) to be on the classpath, if not running
under JDK 1.5.

%package        xom
Summary:        XOM support for saxon8
Group:          Development/Languages/Other
Requires:       %{name} = %{version}-%{release}
Requires:       xom

%description    xom
Provides additional classes enabling Saxon to be used with XOM trees.
Supports using a XOM document as the input or output of transformations
and queries. Requires xom.jar on the classpath.

%package        xpath
Summary:        XPATH support for saxon8
Group:          Development/Languages/Other
Requires:       %{name} = %{version}-%{release}

%description    xpath
Provides support for the JAXP 1.3 XPath API. Requires the JAXP 1.3
version of jaxp-api.jar on the classpath, if not running under JDK 1.5.

%package        scripts
Summary:        Utility scripts for saxon8
Group:          Development/Languages/Other
Requires:       %{name} = %{version}-%{release}

%description    scripts
Utility scripts for saxon8.

%prep
%setup -q -c
mkdir src
(cd src
unzip -q ../source.zip
find . -name CVS -exec rm -rf {} \;
# Clean up .NET classes
rm -rf net/sf/saxon/dotnet/)
cp -p %{SOURCE3} ./build.xml
# cleanup unnecessary stuff we'll build ourselves
rm -rf docs/api
#find . -name "*.jar" -exec rm {} \;
for j in $(find . -name "*.jar"); do
	mv $j $j.no
done
#remove a crap
# rm samples/query/tour.xq.bak
# rm samples/styles/play.xsl.bak

%build
export CLASSPATH=%(build-classpath xml-commons-apis jdom xom bea-stax-api)
ant \
  -Dj2se.javadoc=%{_javadocdir}/java \
  -Djdom.javadoc=%{_javadocdir}/jdom \
  -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p build/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
cp -p build/lib/%{name}-xpath.jar %{buildroot}%{_javadir}/%{name}-xpath-%{version}.jar
cp -p build/lib/%{name}-xom.jar %{buildroot}%{_javadir}/%{name}-xom-%{version}.jar
cp -p build/lib/%{name}-sql.jar %{buildroot}%{_javadir}/%{name}-sql-%{version}.jar
cp -p build/lib/%{name}-jdom.jar %{buildroot}%{_javadir}/%{name}-jdom-%{version}.jar
cp -p build/lib/%{name}-dom.jar %{buildroot}%{_javadir}/%{name}-dom-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}
# demo
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr samples/* %{buildroot}%{_datadir}/%{name}
%fdupes -s %{buildroot}%{_datadir}/%{name}
# scripts
mkdir -p %{buildroot}%{_bindir}
sed 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE1} \
  > %{buildroot}%{_bindir}/%{name}
sed 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE2} \
  > %{buildroot}%{_bindir}/%{name}q
mkdir -p %{buildroot}%{_mandir}/man1
sed 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE4} \
  > %{buildroot}%{_mandir}/man1/%{name}.1
sed 's,__RESOLVERDIR__,%{resolverdir},' < %{SOURCE5} \
  > %{buildroot}%{_mandir}/man1/%{name}q.1
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
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/jaxp_transform_impl.jar
%ghost %{_sysconfdir}/alternatives/jaxp_transform_impl.jar

%files xpath
%{_javadir}/%{name}-xpath*

%files xom
%{_javadir}/%{name}-xom*

%files sql
%{_javadir}/%{name}-sql*

%files jdom
%{_javadir}/%{name}-jdom*

%files dom
%{_javadir}/%{name}-dom*

%files manual
%doc doc/*.html

%files javadoc
%doc %{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%files scripts
%defattr(0755,root,root,0755)
%{_bindir}/%{name}
%{_bindir}/%{name}q
%attr(0644,root,root) %{_mandir}/man1/%{name}.1*
%attr(0644,root,root) %{_mandir}/man1/%{name}q.1*

%changelog
