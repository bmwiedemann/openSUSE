#
# spec file for package mx4j
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


Name:           mx4j
Version:        3.0.2
Release:        0
Summary:        Open Source Implementation of JMX Java API
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://mx4j.sourceforge.net/
Source0:        mx4j-%{version}-src.tar.bz2
Source1:        mx4j-build.policy
Source2:        CatalogManager.properties
Source3:        http://repo1.maven.org/maven2/mx4j/mx4j/%{version}/mx4j-%{version}.pom
Source4:        http://repo1.maven.org/maven2/mx4j/mx4j-jmx/3.0.1/mx4j-jmx-3.0.1.pom
Source6:        http://repo1.maven.org/maven2/mx4j/mx4j-remote/%{version}/mx4j-remote-%{version}.pom
Source7:        http://repo1.maven.org/maven2/mx4j/mx4j-tools/3.0.1/mx4j-tools-3.0.1.pom
Source8:        http://repo1.maven.org/maven2/mx4j/mx4j-impl/2.1.1/mx4j-impl-2.1.1.pom
Source9:        http://repo1.maven.org/maven2/mx4j/mx4j-rimpl/2.1.1/mx4j-rimpl-2.1.1.pom
Source10:       http://repo1.maven.org/maven2/mx4j/mx4j-rjmx/2.1.1/mx4j-rjmx-2.1.1.pom
Patch0:         mx4j-javaxssl.patch
Patch2:         mx4j-build.patch
Patch3:         mx4j-docbook.patch
Patch5:         mx4j-caucho-build.patch
Patch7:         mx4j-3.0.2-docbook-stylesheet-location.patch
Patch8:         mx4j-3.0.2-sourcetarget.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  antlr
BuildRequires:  apache-commons-logging
BuildRequires:  axis
BuildRequires:  bcel
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  docbook_3
BuildRequires:  jaf
BuildRequires:  java-devel >= 1.6
BuildRequires:  javamail
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  libtool
BuildRequires:  log4j-mini
BuildRequires:  perl
BuildRequires:  servletapi5
BuildRequires:  unzip
BuildRequires:  update-alternatives
BuildRequires:  xalan-j2
BuildRequires:  xerces-j2
BuildConflicts: java-devel >= 11
Requires:       apache-commons-logging >= 1.0.1
Requires:       axis >= 1.1
Requires:       bcel >= 5.0
Requires:       jaf
Requires:       javamail >= 1.2-5jpp
Requires:       jce >= 1.2.2
Requires:       log4j >= 1.2.7
Requires:       xml-apis
Requires:       xml-resolver
Requires(post): update-alternatives
Requires(postun): update-alternatives
Obsoletes:      openjmx < %{version}
Provides:       jmx
Provides:       jmxri
Provides:       openjmx = %{version}
BuildArch:      noarch

%description
OpenJMX is an open source implementation of the Java(TM) Management
Extensions (JMX).

%prep
%setup -q
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch7 -p1
%patch8 -p1
cp %{SOURCE1} build
cp %{SOURCE2} build

cp %{SOURCE3} %{name}-%{version}.pom
cp %{SOURCE4} %{name}-jmx-%{version}.pom
cp %{SOURCE6} %{name}-remote-%{version}.pom
cp %{SOURCE7} %{name}-tools-%{version}.pom
cp %{SOURCE8} %{name}-impl-%{version}.pom
cp %{SOURCE9} %{name}-rimpl-%{version}.pom
cp %{SOURCE10} %{name}-rjmx-%{version}.pom
sed -i "s|<version>3.0.1</version>|<version>%{version}</version>|" %{name}-*-%{version}.pom
sed -i "s|<version>2.1.1</version>|<version>%{version}</version>|" %{name}-*-%{version}.pom

pushd lib
   ln -sf $(build-classpath junit) .
   ln -sf $(build-classpath xml-apis) xml-apis.jar                        || :
   ln -sf $(build-classpath xerces-j2) xercesImpl.jar                     || :
   ln -sf $(build-classpath xalan-j2) xalan.jar                           || :
   ln -sf $(build-classpath xalan-j2-serializer)                          || :
   ln -sf $(build-classpath commons-logging)                              || :
   ln -sf $(build-classpath log4j)                                        || :
   ln -sf $(build-classpath bcel)                                         || :
   ln -sf $(build-classpath axis/axis)                                    || :
   ln -sf $(build-classpath axis/jaxrpc)                                  || :
   ln -sf $(build-classpath axis/saaj)                                    || :
   ln -sf $(build-classpath wsdl4j)                                       || :
   ln -sf $(build-classpath commons-discovery)                            || :
   ln -sf $(build-classpath servletapi5) servlet.jar                      || :
   ln -sf $(build-classpath jython)                                       || :
   ln -sf $(build-classpath jaas)                                         || :
popd

%build
export GC_MAXIMUM_HEAP_SIZE="134217728" #128M
ln -sf $(build-classpath javamail/mail) lib/
ln -sf $(build-classpath activation) lib/
export ANT_OPTS="-Djava.security.manager \
                 -Djava.security.policy=$(pwd)/build/mx4j-build.policy \
                 -Dant.build.javac.source=1.6 \
                 -Dant.build.javac.target=1.6"
export OPT_JAR_LIST="ant/ant-junit junit ant/ant-trax jaxp_transform_impl"
export CLASSPATH=$(build-classpath glibj-tools activation javamail/mailapi javamail/smtp \
   jetty4 jython jakarta-commons-logging xml-commons-apis bcel jaas jce \
   log4j jaxp_transform_impl axis/axis axis/jaxrpc axis/saaj \
   xml-resolver xdoclet/xdoclet xdoclet/xdoclet-jmx-module \
   xdoclet/xdoclet-mx4j-module xalan-j2-serializer)
export CLASSPATH=${CLASSPATH}:%{_builddir}/%{name}-%{version}/classes/core:%{_builddir}/%{name}-%{version}/build
cd build
ant compile.jmx compile.rjmx compile.tools compile.examples

%install
install -d -m 755 %{buildroot}%{_javadir}/%{name}
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 644 dist/lib/%{name}-impl.jar %{buildroot}%{_javadir}/%{name}/%{name}-impl-%{version}.jar
install -m 644 dist/lib/%{name}-jmx.jar %{buildroot}%{_javadir}/%{name}/%{name}-jmx-%{version}.jar
install -m 644 dist/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}/%{name}-%{version}.jar
install -m 644 dist/lib/%{name}-tools.jar %{buildroot}%{_javadir}/%{name}/%{name}-tools-%{version}.jar
install -m 644 dist/lib/%{name}-rjmx.jar %{buildroot}%{_javadir}/%{name}/%{name}-rjmx-%{version}.jar
install -m 644 dist/lib/%{name}-rimpl.jar %{buildroot}%{_javadir}/%{name}/%{name}-rimpl-%{version}.jar
install -m 644 dist/lib/%{name}-remote.jar %{buildroot}%{_javadir}/%{name}/%{name}-remote-%{version}.jar
install -d -m 755 %{buildroot}%{_javadir}/%{name}/boa
install -m 644 dist/lib/boa/%{name}-rjmx-boa.jar %{buildroot}%{_javadir}/%{name}/boa/%{name}-rjmx-boa-%{version}.jar
install -m 644 dist/lib/boa/%{name}-rimpl-boa.jar %{buildroot}%{_javadir}/%{name}/boa/%{name}-rimpl-boa-%{version}.jar
install -m 644 dist/lib/boa/%{name}-remote-boa.jar %{buildroot}%{_javadir}/%{name}/boa/%{name}-remote-boa-%{version}.jar
pushd %{buildroot}%{_javadir}/%{name}
   for jar in *-%{version}.jar ; do
      ln -fs ${jar} $(echo $jar | sed "s|-%{version}.jar|.jar|g")
   done
popd

install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 %{name}-%{version}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}.pom
%add_maven_depmap JPP.%{name}-%{name}.pom %{name}/%{name}.jar
install -pm 644 %{name}-jmx-%{version}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-jmx.pom
%add_maven_depmap JPP.%{name}-%{name}-jmx.pom %{name}/%{name}-jmx.jar
install -pm 644 %{name}-remote-%{version}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-remote.pom
%add_maven_depmap JPP.%{name}-%{name}-remote.pom %{name}/%{name}-remote.jar
install -pm 644 %{name}-tools-%{version}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-tools.pom
%add_maven_depmap JPP.%{name}-%{name}-tools.pom %{name}/%{name}-tools.jar
install -pm 644 %{name}-impl-%{version}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-impl.pom
%add_maven_depmap JPP.%{name}-%{name}-impl.pom %{name}/%{name}-impl.jar
install -pm 644 %{name}-rimpl-%{version}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-rimpl.pom
%add_maven_depmap JPP.%{name}-%{name}-rimpl.pom %{name}/%{name}-rimpl.jar
install -pm 644 %{name}-rjmx-%{version}.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP.%{name}-%{name}-rjmx.pom
%add_maven_depmap JPP.%{name}-%{name}-rjmx.pom %{name}/%{name}-rjmx.jar

# alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
ln -sf %{_sysconfdir}/alternatives/jmxri.jar %{buildroot}%{_javadir}/jmxri.jar

%post
%{_sbindir}/update-alternatives --install %{_javadir}/jmxri.jar jmxri %{_javadir}/%{name}/%{name}-jmx.jar 0

%postun
if [ "$1" = "0" ]; then
	%{_sbindir}/update-alternatives --remove jmxri %{_javadir}/%{name}/%{name}-jmx.jar
fi

%files
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/*.jar
%dir %{_javadir}/%{name}/boa
%{_javadir}/%{name}/boa/*.jar
%{_javadir}/jmxri.jar
%ghost %{_sysconfdir}/alternatives/jmxri.jar
%{_mavenpomdir}/JPP.%{name}-%{name}*.pom
%{_mavenpomdir}/*
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml*
%endif

%changelog
