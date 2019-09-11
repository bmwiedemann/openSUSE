#
# spec file for package xalan-j2
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define cvs_version 2_7_2
Name:           xalan-j2
Version:        2.7.2
Release:        0
Summary:        Java XSLT processor
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://xalan.apache.org/index.html
Source0:        http://www.apache.org/dist/xalan/xalan-j/source/xalan-j_%{cvs_version}-src.tar.gz
Source1:        http://repo1.maven.org/maven2/xalan/xalan/%{version}/xalan-%{version}.pom
Source2:        http://repo1.maven.org/maven2/xalan/serializer/%{version}/serializer-%{version}.pom
Source3:        xsltc-%{version}.pom
Source4:        xalan-j2-serializer-MANIFEST.MF
Source5:        xalan-j2-MANIFEST.MF
# OSGi manifests
Patch0:         %{name}-noxsltcdeps.patch
Patch1:         %{name}-manifest.patch
Patch2:         %{name}-crosslink.patch
Patch3:         openjdk-build.patch
BuildRequires:  ant
BuildRequires:  bcel
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  java-cup-bootstrap
BuildRequires:  java-devel >= 1.6
BuildRequires:  javapackages-local
BuildRequires:  jlex
BuildRequires:  servletapi5
BuildRequires:  xml-commons-apis-bootstrap
Requires:       jaxp_parser_impl
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       jaxp_transform_impl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
#!BuildIgnore:  xerces-j2 xml-commons xml-commons-resolver xml-commons-apis java-cup
#!BuildIgnore:  xml-commons-jaxp-1.3-apis

%description
Xalan is an XSLT processor for transforming XML documents into HTML,
text, or other XML document types. It implements the W3C
Recommendations for XSL Transformations (XSLT) and the XML Path
Language (XPath). It can be used from the command line, in an applet or
a servlet, or as a module in other program.

%package        xsltc
Summary:        Java XSLT compiler
Group:          Development/Libraries/Java
Requires:       bcel
Requires:       java_cup
Requires:       jaxp_parser_impl
Requires:       jlex
Requires:       regexp

%description    xsltc
The XSLT Compiler is a Java-based tool for compiling XSLT stylesheets
into lightweight and portable Java byte codes called translets.

%package        manual
Summary:        Manual for xalan-j2
Group:          Development/Libraries/Java

%description    manual
Xalan is an XSLT processor for transforming XML documents into HTML,
text, or other XML document types. It implements the W3C
Recommendations for XSL Transformations (XSLT) and the XML Path
Language (XPath). It can be used from the command line, in an applet or
a servlet, or as a module in other program.

This package contains the manual for Xalan.

%package        demo
Summary:        Demonstration and samples for xalan-j2
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}
Requires:       servlet

%description    demo
Xalan is an XSLT processor for transforming XML documents into HTML,
text, or other XML document types. It implements the W3C
Recommendations for XSL Transformations (XSLT) and the XML Path
Language (XPath). It can be used from the command line, in an applet or
a servlet, or as a module in other program.

This package contains demonstration and sample files for Xalan.

%prep
%setup -q -n xalan-j_%{cvs_version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
# Remove all binary libs, except ones needed to build docs and N/A elsewhere.
for j in $(find . -name "*.jar"); do
        mv $j $j.no
done
mv tools/xalan2jdoc.jar.no tools/xalan2jdoc.jar
mv tools/xalan2jtaglet.jar.no tools/xalan2jtaglet.jar
dos2unix KEYS LICENSE.txt NOTICE.txt xdocs/sources/xsltc/README.xsltc xdocs/sources/xsltc/README.xslt

%build
if [ ! -e "$JAVA_HOME" ] ; then export JAVA_HOME="%{java_home}" ; fi
pushd lib
ln -sf $(build-classpath java_cup-runtime) runtime.jar
ln -sf $(build-classpath bcel) BCEL.jar
ln -sf $(build-classpath regexp) regexp.jar
ln -sf $(build-classpath xerces-j2) xercesImpl.jar
ln -sf $(build-classpath xml-commons-apis) xml-apis.jar
popd
pushd tools
ln -sf $(build-classpath java_cup) java_cup.jar
ln -sf $(build-classpath ant) ant.jar
ln -sf $(build-classpath jlex) JLex.jar
ln -sf $(build-classpath stylebook) stylebook-1.0-b3_xalan-2.jar
popd
ant \
  -Dservlet-api.jar=$(build-classpath servletapi5) \
  -Dcompiler.source=1.6 -Dcompiler.target=1.6 \
  -Djava.awt.headless=true \
  -Dapi.j2se=%{_javadocdir}/java \
  -Dbuild.xalan-interpretive.jar=build/xalan-interpretive.jar \
  xalan-interpretive.jar\
  xsltc.unbundledjar \
  docs \
  xsltc.docs \
  samples \
  servlet

# inject OSGi manifests
jar ufm build/serializer.jar %{SOURCE4}
jar ufm build/xalan-interpretive.jar %{SOURCE5}

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 build/xalan-interpretive.jar \
  %{buildroot}%{_javadir}/%{name}-%{version}.jar
install -p -m 644 build/xsltc.jar \
  %{buildroot}%{_javadir}/xsltc-%{version}.jar
install -p -m 644 build/serializer.jar \
  %{buildroot}%{_javadir}/%{name}-serializer-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}-%{version}.pom
%add_maven_depmap %{name}-%{version}.pom %{name}-%{version}.jar
install -p -m 644 %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{name}-serializer-%{version}.pom
%add_maven_depmap %{name}-serializer-%{version}.pom %{name}-serializer-%{version}.jar
install -p -m 644 %{SOURCE3}  %{buildroot}%{_mavenpomdir}/xsltc-%{version}.pom
%add_maven_depmap xsltc-%{version}.pom xsltc-%{version}.jar -f xsltc

# demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -p -m 644 build/xalansamples.jar \
  %{buildroot}%{_datadir}/%{name}/%{name}-samples.jar
install -p -m 644 build/xalanservlet.war \
  %{buildroot}%{_datadir}/%{name}/%{name}-servlet.war
cp -pr samples %{buildroot}%{_datadir}/%{name}
%fdupes -s %{buildroot}%{_datadir}/%{name}

# alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -sf %{_sysconfdir}/alternatives/jaxp_transform_impl.jar %{buildroot}%{_javadir}/jaxp_transform_impl.jar

# bnc#485299
install -d -m 0755 %{buildroot}/%{_sysconfdir}/ant.d/
echo xalan-j2-serializer > %{buildroot}/%{_sysconfdir}/ant.d/serializer

%post
update-alternatives --install %{_javadir}/jaxp_transform_impl.jar \
  jaxp_transform_impl %{_javadir}/%{name}.jar 30

%preun
{
  [ $1 = 0 ] || exit 0
  update-alternatives --remove jaxp_transform_impl %{_javadir}/%{name}.jar
} >/dev/null 2>&1 || :

%files
%defattr(0644,root,root,0755)
%doc KEYS LICENSE.txt NOTICE.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-serializer-%{version}.jar
%{_javadir}/%{name}-serializer.jar
%config %{_sysconfdir}/ant.d/serializer
%ghost %{_sysconfdir}/alternatives/jaxp_transform_impl.jar
%{_javadir}/jaxp_transform_impl.jar
%{_mavenpomdir}/%{name}*
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml*
%endif

%files xsltc
%defattr(0644,root,root,0755)
%{_javadir}/xsltc-%{version}.jar
%{_javadir}/xsltc.jar
%{_mavenpomdir}/xsltc*
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}-xsltc
%else
%{_datadir}/maven-metadata/%{name}-xsltc.xml*
%endif

%files manual
%defattr(0644,root,root,0755)
%doc build/docs/*

%files demo
%defattr(0644,root,root,0755)
%{_datadir}/%{name}

%changelog
