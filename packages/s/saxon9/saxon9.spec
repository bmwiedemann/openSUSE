#
# spec file for package saxon9
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


# net.sf.saxon.om.XMLChar is from ASL-licensed Xerces
Name:           saxon9
Version:        9.4.0.7
Release:        0
Summary:        The SAXON XSLT Processor from Michael Kay
License:        MPL-1.0 AND Apache-2.0
Group:          Productivity/Publishing/XML
Url:            http://saxon.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/saxon/Saxon-HE/9.4/saxon9-4-0-7source.zip
Source1:        %{name}.saxon.script
Source2:        %{name}.saxonq.script
Source3:        %{name}.build.script
Source4:        %{name}.1
Source5:        %{name}q.1
Source6:        https://downloads.sourceforge.net/project/saxon/Saxon-HE/9.4/saxon-resources9-4.zip
#Made from original pom file
#Source7:        http://irrational.googlecode.com/svn/trunk/maven-repo/net/sf/saxon/saxon-he/9.3.0.7/saxon-he-9.3.0.7.pom
Source7:        saxon-he-9.4.0.7.pom
BuildRequires:  ant
BuildRequires:  bea-stax-api
BuildRequires:  dom4j
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  jdom
BuildRequires:  unzip
BuildRequires:  xml-commons-apis
BuildRequires:  xml-commons-resolver
BuildRequires:  xom
Requires:       bea-stax
Requires:       bea-stax-api
Recommends:     %{name}-scripts
Recommends:     xml-commons-resolver
Provides:       jaxp_transform_impl = %{version}
# Older versions were split into multile packages
Obsoletes:      %{name}-dom < %{version}
Provides:       %{name}-dom = %{version}
Obsoletes:      %{name}-jdom < %{version}
Provides:       %{name}-jdom = %{version}
Obsoletes:      %{name}-sql < %{version}
Provides:       %{name}-sql = %{version}
Obsoletes:      %{name}-xom < %{version}
Provides:       %{name}-xom = %{version}
Obsoletes:      %{name}-xpath < %{version}
Provides:       %{name}-xpath = %{version}
BuildArch:      noarch

%description
The most recent version of the open-source implementation of XSLT 2.0 and XPath
2.0, and XQuery 1.0. This provides the "basic" conformance level of these
languages: in effect, this provides all the features of the languages except
schema-aware processing. This version reflects the syntax of the final XSLT
2.0, XQuery 1.0, and XPath 2.0 Recommendations of 23 January 2007 as amended in
the second editions of those specifications where appropriate.

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

%package        scripts
Summary:        Utility scripts for %{name}
Group:          Productivity/Publishing/XML
Requires:       %{name} = %{version}-%{release}
Requires:       jaxp_parser_impl
Requires:       xml-commons-apis

%description    scripts
Utility scripts for %{name}.

%prep
%setup -q -c

unzip -q %{SOURCE6}
cp -p %{SOURCE3} ./build.xml

# deadNET
rm -rf net/sf/saxon/dotnet

# Depends on XQJ (javax.xml.xquery)
rm -rf net/sf/saxon/xqj

# This requires a EE edition feature (com.saxonica.xsltextn)
rm -rf net/sf/saxon/option/sql/SQLElementFactory.java

# cleanup unnecessary stuff we'll build ourselves
rm -rf docs/api
find . \( -name "*.jar" -name "*.pyc" \) -delete

%build
mkdir -p build/classes
cat >build/classes/edition.properties <<EOF
config=net.sf.saxon.Configuration
platform=net.sf.saxon.java.JavaPlatform
EOF

export CLASSPATH=%(build-classpath xml-commons-apis jdom xom bea-stax-api dom4j xml-commons-resolver)
ant \
  -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
  -Dant.build.javadoc.source=1.6 \
  -Dj2se.javadoc=%{_javadocdir}/java \
  -Djdom.javadoc=%{_javadocdir}/jdom

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p build/lib/saxon.jar %{buildroot}%{_javadir}/%{name}.jar

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
install -p -m755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}
install -p -m755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}q
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m644 %{SOURCE4} %{buildroot}%{_mandir}/man1/%{name}.1
install -p -m644 %{SOURCE5} %{buildroot}%{_mandir}/man1/%{name}q.1

# jaxp_transform_impl ghost symlink
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
ln -sf %{_sysconfdir}/alternatives/jaxp_transform_impl.jar %{buildroot}%{_javadir}/jaxp_transform_impl.jar

# a simple POM
install -dm 755 %{buildroot}%{_mavenpomdir}
install -m 644 %{SOURCE7} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
sed -i -e 's/saxon-he/saxon/' %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

%post
update-alternatives --install %{_javadir}/jaxp_transform_impl.jar \
  jaxp_transform_impl %{_javadir}/%{name}.jar 25

%postun
if [ $1 -eq 0 ] ; then
  update-alternatives --remove jaxp_transform_impl %{_javadir}/%{name}.jar
fi

%files
%{_javadir}/%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_datadir}/maven-metadata/%{name}.xml
%{_javadir}/jaxp_transform_impl.jar
%ghost %{_sysconfdir}/alternatives/jaxp_transform_impl.jar

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
