#
# spec file
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


%global saxon_version 10
%global saxon_release 9
%global saxon_compat_version 10
# net.sf.saxon.om.XMLChar is from ASL-licensed Xerces
Name:           saxon%{saxon_version}
Version:        %{saxon_version}.%{saxon_release}
Release:        0
Summary:        The SAXON XSLT Processor from Michael Kay
License:        Apache-2.0 AND MPL-2.0
Group:          Productivity/Publishing/XML
URL:            https://www.saxonica.com/
Source0:        https://github.com/Saxonica/Saxon-HE/raw/main/%{saxon_version}/source/saxon%{saxon_version}-%{saxon_release}source.zip
# %{name}-generate-tarball.sh
Source1:        saxon-resources-%{saxon_version}-cleaned.zip
Source2:        https://repo1.maven.org/maven2/net/sf/saxon/Saxon-HE/%{saxon_version}.%{saxon_release}/Saxon-HE-%{saxon_version}.%{saxon_release}.pom
Source3:        %{name}.build.xml
Source10:       %{name}.saxon.script
Source11:       %{name}.saxonq.script
Source12:       %{name}.gizmo.script
Source20:       %{name}.saxon.pod
Source21:       %{name}.saxonq.pod
Source22:       %{name}.gizmo.pod
# run saxon10-generate-tarball.sh script to remove potential nonfree content from saxon-resources-10.zip.
Source100:      %{name}-generate-tarball.sh
BuildRequires:  ant
BuildRequires:  dom4j
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  icu4j
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  jdom
BuildRequires:  jdom2
BuildRequires:  jetbrains-annotations
BuildRequires:  jline >= 2
BuildRequires:  sed
BuildRequires:  unzip
BuildRequires:  xml-commons-apis
BuildRequires:  xml-commons-resolver
BuildRequires:  xom
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     %{name}-scripts
Provides:       jaxp_transform_impl = %{version}
BuildArch:      noarch

%description
The Saxon package is a collection of tools for processing XML documents. The
main components are:

• An XSLT processor, which can be used from the command line, or invoked from
an application, using a supplied API. Saxon implements the XSLT 3.0
Recommendation. The product can also be used to run XSLT 2.0 stylesheets, or
XSLT 1.0 stylesheets in backwards compatibility mode.

• An XPath processor accessible to applications via a supplied API. This
supports XPath 2.0 and XPath 3.1. It can also be used in
backwards-compatibility mode to evaluate XPath 1.0 expressions.

• An XQuery processor that can be used from the command line, or invoked from
an application by use of a supplied API. This supports XQuery 3.1, which also
allows XQuery 1.0 or 3.0 queries to be executed. With Saxon-EE, you can also
use the XQuery extensions defined in the XQuery Update 1.0 Recommendation, but
later working drafts of XQuery Update are not supported (W3C has abandoned work
on these versions).

• An XML Schema Processor. This supports both XSD 1.0 and XSD 1.1. This can be
used on its own to validate a schema for correctness, or to validate a source
document against the definitions in a schema. It is also used to support the
schema-aware functionality of the XSLT and XQuery processors. Like the other
tools, it can be run from the command line, or invoked from an application.

• On the Java platform, when using XSLT, XPath, XQuery, or XML schema
validation, Saxon offers a choice of APIs. If you need portability across
different vendors' tools, you can use the JAXP API for XSLT, XPath, and XML
Schema processing, and the XQJ interface for XQuery. On the other hand, if you
want a more integrated and complete API offering access to all Saxon's
facilities, the s9api interface is recommended. You can also dive down deeper
into the Saxon internals if you need to: there has been no particular attempt
to make interfaces private, and all public interfaces are documented in the
JavaDoc. Clearly, the deeper you go, the greater the risk of interfaces
changing in future releases.

• On the .NET platform, Saxon offers an API that enables close integration with
other services available from .NET, notably the XML-related classes in the
System.Xml namespace. It isn't possible to use Saxon as a transparent plug-in
replacement for the System.Xml.Xsl processor, because the API for the Microsoft
engine using concrete classes rather than abstract interfaces. However, it is
possible to use it as a functional replacement with minor changes to your
application code.

%package		manual
Summary:        Manual for %{name}
Group:          Productivity/Publishing/XML

%description	manual
Manual for %{name}.

%package		javadoc
Summary:        Javadoc for %{name}
Group:          Productivity/Publishing/XML

%description	javadoc
Javadoc for %{name}.

%package		demo
Summary:        Demos for %{name}
Group:          Productivity/Publishing/XML
Requires:       %{name} = %{version}-%{release}

%description	demo
Demonstrations and samples for %{name}.

%package		scripts
Summary:        Utility scripts for %{name}
Group:          Productivity/Publishing/XML
Requires:       %{name} = %{version}-%{release}
Requires:       javapackages-tools
Requires:       jaxp_parser_impl
Requires:       jline
Requires:       xml-commons-apis
Recommends:     icu4j
Recommends:     jdom
Recommends:     jdom2
Recommends:     xml-commons-resolver
Recommends:     xom

%description	scripts
Utility scripts for %{name}.

%prep
%setup -q -c
unzip -q %{SOURCE1}
cp -p %{SOURCE3} ./build.xml

# purge EE imports
find -name \*.java |xargs sed -i -e 's/\(^import com\.saxonica\..*\)/\/\/\1/'

# deadNET
rm -rf net/sf/saxon/dotnet

# This requires a EE edition feature (com.saxonica.xsltextn)
rm -rf net/sf/saxon/option/sql/SQLElementFactory.java

# cleanup unnecessary stuff we'll build ourselves
rm -rf docs/api
find . \( -name "*.jar" -name "*.pyc" \) -delete

mkdir -p build/classes
cat >build/classes/edition.properties <<__PROPERTIES__
config=net.sf.saxon.Configuration
platform=net.sf.saxon.java.JavaPlatform
__PROPERTIES__

%build
export CLASSPATH=$(build-classpath xml-commons-apis jdom jdom2 xom dom4j icu4j xml-commons-resolver jline jetbrains-annotations)
ant \
	-Dj2se.javadoc=%{_javadocdir}/java \
	-Djdom.javadoc=%{_javadocdir}/jdom \
	-Ddom4j.javadoc=%{_javadocdir}/dom4j

pod2man --release='%{name} %{version}' --section=1 --center='User Commands' --quotes=none %{SOURCE20} %{name}.1
pod2man --release='%{name} %{version}' --section=1 --center='User Commands' --quotes=none %{SOURCE21} %{name}q.1
pod2man --release='%{name} %{version}' --section=1 --center='User Commands' --quotes=none %{SOURCE22} gizmo%{saxon_version}.1

%install

# JARs, POM, API documentation
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 build/lib/saxon.jar %{buildroot}%{_javadir}/%{name}.jar

install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r build/api %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# Demo
install -dm0755 %{buildroot}%{_defaultdocdir}/%{name}
cp -rf use-cases samples drivers %{buildroot}%{_defaultdocdir}/%{name}

# Scripts
install -dm0755 %{buildroot}%{_bindir}
install -m0755 %{SOURCE10} %{buildroot}%{_bindir}/%{name}
install -m0755 %{SOURCE11} %{buildroot}%{_bindir}/%{name}q
install -m0755 %{SOURCE12} %{buildroot}%{_bindir}/gizmo%{saxon_version}

# Manual pages
install -dm0755 %{buildroot}%{_mandir}/man1
install -Dm0644 {%{name}{,q},gizmo%{saxon_version}}.1 %{buildroot}%{_mandir}/man1/

# jaxp_transform_impl ghost symlink
install -dm0755 %{buildroot}%{_sysconfdir}/alternatives/
ln -sf %{_sysconfdir}/alternatives/jaxp_transform_impl.jar %{buildroot}%{_javadir}/jaxp_transform_impl.jar

# Manual
install -dm0755 %{buildroot}%{_defaultdocdir}/%{name}/{doc,source-userdoc}
cp -rf doc/{index.html,img} %{buildroot}%{_defaultdocdir}/%{name}/doc
unzip -qq -d %{buildroot}%{_defaultdocdir}/%{name}/source-userdoc source-userdoc.zip
ln -s %{_javadocdir}/%{name} %{buildroot}%{_defaultdocdir}/%{name}/javadoc
find %{buildroot}%{_defaultdocdir}/%{name} \
	-name \*.class -delete -or -name \*.exe -delete
find %{buildroot}%{_defaultdocdir}/%{name} \
	\( -name \*.cs \
	-or -name \*.xml \
	-or -name \*.xsl \
	-or -name \*.xq \
	-or -name \*.xqlib \
	-or -name \*.dtd \
	-or -name \*.xsd \
	-or -name \*.resx \
	-or -name \*.out \
	-or -name \*.cmd \
	\) -print0 \
	|xargs -0 dos2unix
%fdupes %{buildroot}%{_defaultdocdir}/%{name}

%post
update-alternatives --install %{_javadir}/jaxp_transform_impl.jar \
	jaxp_transform_impl %{_javadir}/%{name}.jar 25

%postun
if [ $1 -eq 0 ] ; then
	update-alternatives --remove jaxp_transform_impl %{_javadir}/%{name}.jar
fi

%files -f .mfiles
%{_javadir}/jaxp_transform_impl.jar
%ghost %{_sysconfdir}/alternatives/jaxp_transform_impl.jar
%license notices/{ASM,ICU-J,JAMESCLARK,JLINE2,LICENSE,THAI,UNICODE}.txt

%files manual
%{_defaultdocdir}/%{name}
%exclude %{_defaultdocdir}/%{name}/drivers
%exclude %{_defaultdocdir}/%{name}/samples
%exclude %{_defaultdocdir}/%{name}/use-cases

%files javadoc
%{_javadocdir}/%{name}

%files demo
%{_defaultdocdir}/%{name}/drivers
%{_defaultdocdir}/%{name}/samples
%{_defaultdocdir}/%{name}/use-cases

%files scripts
%defattr(0755,root,root,0755)
%{_bindir}/*
%attr(0644,root,root) %{_mandir}/man1/*.1%{?ext_man}

%changelog
