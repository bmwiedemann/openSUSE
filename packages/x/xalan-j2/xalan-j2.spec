#
# spec file for package xalan-j2
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "extras"
%bcond_without extras
%else
%bcond_with extras
%endif
%define cvs_version 2_7_3
%global base_name xalan-j2
Version:        2.7.3
Release:        0
Summary:        Java XSLT processor
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://xalan.apache.org/index.html
Source0:        %{base_name}-%{version}.tar.xz
Source1:        https://repo1.maven.org/maven2/xalan/xalan/%{version}/xalan-%{version}.pom
Source2:        https://repo1.maven.org/maven2/xalan/serializer/%{version}/serializer-%{version}.pom
Source3:        xsltc-%{version}.pom
Source4:        xalan-j2-serializer-MANIFEST.MF
Source5:        xalan-j2-MANIFEST.MF
# OSGi manifests
Patch0:         %{base_name}-noxsltcdeps.patch
Patch1:         %{base_name}-manifest.patch
Patch2:         %{base_name}-crosslink.patch
Patch3:         openjdk-build.patch
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  xml-commons-apis-bootstrap
#!BuildIgnore:  apache-commons-lang3
#!BuildIgnore:  java-cup
#!BuildIgnore:  xml-commons
#!BuildIgnore:  xml-commons-apis
#!BuildIgnore:  xml-commons-jaxp-1.3-apis
#!BuildIgnore:  xml-commons-resolver
Requires:       xerces-j2
BuildArch:      noarch
%if %{with extras}
Name:           %{base_name}-extras
%else
Name:           %{base_name}
%endif
%if %{with extras}
BuildRequires:  bcel
BuildRequires:  dejavu-fonts
BuildRequires:  java-cup-bootstrap
BuildRequires:  jlex
BuildRequires:  regexp
BuildRequires:  servletapi5
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildRequires:  xml-stylebook
%else
#!BuildIgnore:  xerces-j2
%endif

%description
Xalan is an XSLT processor for transforming XML documents into HTML,
text, or other XML document types. It implements the W3C
Recommendations for XSL Transformations (XSLT) and the XML Path
Language (XPath). It can be used from the command line, in an applet or
a servlet, or as a module in other program.

%package        -n %{base_name}-xsltc
Summary:        Java XSLT compiler
Group:          Development/Libraries/Java
Requires:       bcel
Requires:       java_cup
Requires:       jlex
Requires:       regexp
Requires:       xerces-j2

%description    -n %{base_name}-xsltc
The XSLT Compiler is a Java-based tool for compiling XSLT stylesheets
into lightweight and portable Java byte codes called translets.

%package        -n %{base_name}-manual
Summary:        Manual for xalan-j2
Group:          Development/Libraries/Java

%description    -n %{base_name}-manual
Xalan is an XSLT processor for transforming XML documents into HTML,
text, or other XML document types. It implements the W3C
Recommendations for XSL Transformations (XSLT) and the XML Path
Language (XPath). It can be used from the command line, in an applet or
a servlet, or as a module in other program.

This package contains the manual for Xalan.

%package        -n %{base_name}-demo
Summary:        Demonstration and samples for xalan-j2
Group:          Development/Libraries/Java
Requires:       %{base_name} = %{version}-%{release}
Requires:       servlet

%description    -n %{base_name}-demo
Xalan is an XSLT processor for transforming XML documents into HTML,
text, or other XML document types. It implements the W3C
Recommendations for XSL Transformations (XSLT) and the XML Path
Language (XPath). It can be used from the command line, in an applet or
a servlet, or as a module in other program.

This package contains demonstration and sample files for Xalan.

%prep
%setup -q -n %{base_name}-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1

%build
if [ ! -e "$JAVA_HOME" ] ; then export JAVA_HOME="%{java_home}" ; fi
pushd lib
%if %{with extras}
ln -sf $(build-classpath java-cup-runtime) runtime.jar
ln -sf $(build-classpath bcel) bcel-6.7.0.jar
ln -sf $(build-classpath regexp) regexp.jar
pushd endorsed
ln -sf $(build-classpath xerces-j2) xercesImpl.jar
ln -sf $(build-classpath xml-apis) xml-apis.jar
popd
%endif
popd
pushd tools
ln -sf $(build-classpath ant) ant.jar
%if %{with extras}
ln -sf $(build-classpath java-cup) java_cup.jar
ln -sf $(build-classpath jlex) JLex.jar
ln -sf $(build-classpath xml-stylebook) stylebook-1.0-b3_xalan-2.jar
%endif
popd
%if %{with extras}
mkdir -p build
pushd build
ln -sf $(build-classpath %{base_name}) xalan-interpretive.jar
popd
%endif

%{ant} \
  -Dcompiler.source=1.8 -Dcompiler.target=1.8 \
  -Djava.awt.headless=true \
  -Dapi.j2se=%{_javadocdir}/java \
  -Dbuild.xalan-interpretive.jar=build/xalan-interpretive.jar \
%if %{with extras}
  -Dservlet-api.jar=$(build-classpath servletapi5) \
  xsltc.unbundledjar \
  docs \
  xsltc.docs \
  samples \
  servlet
%else
  xalan-interpretive.jar

# inject OSGi manifests
jar \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
    --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
    --update --file=build/serializer.jar --manifest=%{SOURCE4}
jar \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
    --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
    --update --file=build/xalan-interpretive.jar --manifest=%{SOURCE5}

%endif

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
%if %{without extras}
install -p -m 644 build/xalan-interpretive.jar \
  %{buildroot}%{_javadir}/%{base_name}.jar
install -p -m 644 build/serializer.jar \
  %{buildroot}%{_javadir}/%{base_name}-serializer.jar
%else
install -p -m 644 build/xsltc.jar \
  %{buildroot}%{_javadir}/xsltc.jar
%endif

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
%if %{without extras}
%{mvn_install_pom} %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{base_name}.pom
%add_maven_depmap %{base_name}.pom %{base_name}.jar
%{mvn_install_pom} %{SOURCE2} %{buildroot}%{_mavenpomdir}/%{base_name}-serializer.pom
%add_maven_depmap %{base_name}-serializer.pom %{base_name}-serializer.jar

# bnc#485299
install -d -m 0755 %{buildroot}/%{_sysconfdir}/ant.d/
echo xalan-j2-serializer > %{buildroot}/%{_sysconfdir}/ant.d/serializer

%else
%{mvn_install_pom} %{SOURCE3}  %{buildroot}%{_mavenpomdir}/xsltc.pom
%add_maven_depmap xsltc.pom xsltc.jar -f xsltc

# demo
install -d -m 755 %{buildroot}%{_datadir}/%{base_name}
install -p -m 644 build/xalansamples.jar \
  %{buildroot}%{_datadir}/%{base_name}/%{base_name}-samples.jar
install -p -m 644 build/xalanservlet.war \
  %{buildroot}%{_datadir}/%{base_name}/%{base_name}-servlet.war
cp -pr samples %{buildroot}%{_datadir}/%{base_name}
%fdupes -s %{buildroot}%{_datadir}/%{base_name}

# manual
%fdupes -s build/docs
%endif

%if %{without extras}
%files -f .mfiles
%defattr(0644,root,root,0755)
%license LICENSE.txt
%doc KEYS NOTICE.txt
%config %{_sysconfdir}/ant.d/serializer

%else

%files -n %{base_name}-xsltc -f .mfiles-xsltc

%files -n %{base_name}-manual
%defattr(0644,root,root,0755)
%doc build/docs/*

%files -n %{base_name}-demo
%defattr(0644,root,root,0755)
%{_datadir}/%{base_name}

%endif

%changelog
