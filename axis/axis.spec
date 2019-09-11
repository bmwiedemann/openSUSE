#
# spec file for package axis
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


Name:           axis
Version:        1.4
Release:        0
Summary:        Apache implementation of the SOAP
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://axis.apache.org/axis/
Source0:        axis-src-1_4.tar.bz2
# svn export http://svn.apache.org/repos/asf/webservices/axis/branches/AXIS_1_4_FINAL/
# Build only
# cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/tools export -r v1_1_0 org.eclipse.orbit/javax.xml.rpc/META-INF/MANIFEST.MF
# mv org.eclipse.orbit/javax.xml.rpc/META-INF/MANIFEST.MF xmlrpc-MANIFEST.MF
Source1:        xmlrpc-MANIFEST.MF
# cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/tools export -r v1_4_0 org.eclipse.orbit/org.apache.axis/META-INF/MANIFEST.MF
# mv org.eclipse.orbit/org.apache.axis/META-INF/MANIFEST.MF axis-MANIFEST.MF
Source2:        axis-MANIFEST.MF
# cvs -d :pserver:anonymous@dev.eclipse.org:/cvsroot/tools export -r v1_3_0 org.eclipse.orbit/javax.xml.soap/META-INF/MANIFEST.MF
# mv org.eclipse.orbit/javax.xml.soap/META-INF/MANIFEST.MF saaj-MANIFEST.MF
Source3:        saaj-MANIFEST.MF
Source4:        http://repo1.maven.org/maven2/axis/axis/1.4/axis-1.4.pom
Source5:        http://repo1.maven.org/maven2/axis/axis-ant/1.4/axis-ant-1.4.pom
Source6:        http://repo1.maven.org/maven2/axis/axis-jaxrpc/1.4/axis-jaxrpc-1.4.pom
Source7:        http://repo1.maven.org/maven2/axis/axis-saaj/1.4/axis-saaj-1.4.pom
Source8:        axis-schema-1.4.pom
Patch0:         unimplemented-dom3-methods.patch
Patch1:         axis-1.4-gcc44_build.patch
Patch2:         axis-manifest.patch
Patch3:         axis-ant-build.patch
Patch4:         axis-encoding.patch
Patch5:         axis-compareto.patch
Patch6:         axis-enum.patch
# PATCH-FIX-UPSTREAM bsc#1103658 CVE-2018-8032 cross-site scripting (XSS) attack in the default servlet/services
Patch7:         axis-CVE-2018-8032.patch
Patch8:         axis-jdk11.patch
# PATCH-FIX-UPSTREAM bsc#1134598 CVE-2012-5784 CVE-2014-3596 missing connection hostname check against X.509 certificate name
Patch9:         axis-CVE-2014-3596.patch
BuildRequires:  ant
BuildRequires:  ant-jdepend
BuildRequires:  antlr
BuildRequires:  apache-commons-httpclient
BuildRequires:  apache-commons-logging
BuildRequires:  gnu-jaf
BuildRequires:  jakarta-commons-discovery
BuildRequires:  java-devel >= 1.8
BuildRequires:  javamail
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  log4j-mini
BuildRequires:  servletapi5
BuildRequires:  unzip
BuildRequires:  wsdl4j
BuildRequires:  xerces-j2
Requires:       apache-commons-httpclient
Requires:       apache-commons-logging
Requires:       jaf
Requires:       jakarta-commons-discovery
Requires:       java
Requires:       javamail
Requires:       jaxp_parser_impl
Requires:       log4j
Requires:       wsdl4j
Obsoletes:      %{name}-javadoc
BuildArch:      noarch

%description
Apache Axis is an implementation of the SOAP ("Simple Object Access
Protocol") submission to W3C.

%package manual
Summary:        Manual for axis
Group:          Documentation/Other

%description manual
Manual for axis

%prep
%setup -q -n %{name}-1_4

%patch0 -p1
%patch1 -p1 -b gcc44-build
%patch2
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

# Remove provided binaries
find . "(" -name "*.jar" -o -name "*.zip" -o -name "*.class" ")" -delete
rm -rf src/org/apache/axis/enum
rm -f src/org/apache/axis/providers/java/CORBAProvider.java
rm -f src/org/apache/axis/deployment/wsdd/providers/WSDDJavaCORBAProvider.java
rm -f src/org/apache/axis/providers/java/EJBProvider.java
rm -f src/org/apache/axis/deployment/wsdd/providers/WSDDJavaEJBProvider.java

cp %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%build
[ -z "$JAVA_HOME" ] && export JAVA_HOME=%{_jvmdir}/java
CLASSPATH=$(build-classpath wsdl4j commons-discovery commons-httpclient3 commons-logging log4j activation javamail servletapi5)
export CLASSPATH=$CLASSPATH:$(build-classpath oro junit jdepend jimi xml-security jsse httpunit jms castor 2>/dev/null)
export OPT_JAR_LIST="ant/ant-nodeps"
ant -Dcompile.ime=true \
    -Dwsdl4j.jar=$(build-classpath wsdl4j) \
    -Dcommons-discovery.jar=$(build-classpath commons-discovery) \
    -Dcommons-logging.jar=$(build-classpath commons-logging) \
    -Dcommons-httpclient.jar=$(build-classpath commons-httpclient3) \
    -Dlog4j-core.jar=$(build-classpath log4j) \
    -Dactivation.jar=$(build-classpath jaf) \
    -Dmailapi.jar=$(build-classpath javamail/mailapi) \
    -Dxerces.jar=$(build-classpath jaxp_parser_impl) \
    -Dservlet.jar=$(build-classpath servletapi5) \
    -Dregexp.jar=$(build-classpath oro 2>/dev/null) \
    -Djunit.jar=$(build-classpath junit 2>/dev/null) \
    -Djimi.jar=$(build-classpath jimi 2>/dev/null) \
    -Djsse.jar=$(build-classpath jsse/jsse 2>/dev/null) \
    -Dant.build.javac.source=8 -Dsource=8 \
    -Dant.build.javac.target=8 -Dtarget=8 \
    clean compile

%install
### Jar files
install -d -m 755 %{buildroot}%{_javadir}/%{name}
pushd build/lib
   install -m 644 axis.jar axis-ant.jar saaj.jar jaxrpc.jar \
           %{buildroot}%{_javadir}/%{name}
popd

# POMs
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -m 644 %{SOURCE4} %{buildroot}%{_mavenpomdir}/JPP.%{name}-axis.pom
%add_maven_depmap JPP.%{name}-axis.pom %{name}/axis.jar
install -m 644 %{SOURCE5} %{buildroot}%{_mavenpomdir}/JPP.%{name}-axis-ant.pom
%add_maven_depmap JPP.%{name}-axis-ant.pom %{name}/axis-ant.jar
install -m 644 %{SOURCE6} %{buildroot}%{_mavenpomdir}/JPP.%{name}-jaxrpc.pom
%add_maven_depmap JPP.%{name}-jaxrpc.pom %{name}/jaxrpc.jar
install -m 644 %{SOURCE7} %{buildroot}%{_mavenpomdir}/JPP.%{name}-saaj.pom
%add_maven_depmap JPP.%{name}-saaj.pom %{name}/saaj.jar
#install -m 644 %{S:8} $RPM_BUILD_ROOT%%{_mavenpomdir}/JPP.%%{name}-axis-schema.pom
# % add_maven_depmap JPP.%%{name}-axis-schema.pom %%{name}/axis-schema.jar

%files
%license LICENSE
%doc README release-notes.html changelog.html
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%{_mavenpomdir}/*.pom
%{_datadir}/maven-metadata/%{name}.xml

%files manual
%doc docs/*

%changelog
