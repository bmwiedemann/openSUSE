#
# spec file for package tomcat
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2000-2009, JPackage Project
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


%define jspspec 2.3
%define servletspec 4.0
%define elspec 3.0
%define major_version 9
%define minor_version 0
%define micro_version 106
%define packdname apache-tomcat-%{version}-src
# FHS 2.3 compliant tree structure - http://www.pathname.com/fhs/2.3/
%global basedir /srv/%{name}
%define appdir %{basedir}/webapps
%define bindir %{_datadir}/%{name}/bin
%define confdir %{_sysconfdir}/%{name}
%define homedir %{_datadir}/%{name}
%define libdir %{_javadir}/%{name}
%define logdir %{_localstatedir}/log/%{name}
%define cachedir %{_localstatedir}/cache/%{name}
%define tempdir %{cachedir}/temp
%define workdir %{cachedir}/work
%define tomcatappdir %{_datadir}/%{name}/tomcat-webapps
%define javac_target 1.8
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           tomcat
Version:        %{major_version}.%{minor_version}.%{micro_version}
Release:        0
Summary:        Apache Servlet/JSP/EL Engine, RI for Servlet 4.0/JSP 2.3/EL 3.0 API
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://tomcat.apache.org
Source0:        https://archive.apache.org/dist/tomcat/tomcat-%{major_version}/v%{version}/src/%{packdname}.tar.gz
Source1:        %{name}-%{major_version}.%{minor_version}.conf
Source3:        %{name}-%{major_version}.%{minor_version}.sysconfig
Source4:        %{name}-%{major_version}.%{minor_version}.wrapper
Source5:        %{name}-%{major_version}.%{minor_version}.logrotate
Source6:        %{name}-%{major_version}.%{minor_version}-digest.script
Source7:        %{name}-%{major_version}.%{minor_version}-tool-wrapper.script
Source11:       %{name}-%{major_version}.%{minor_version}.service
Source20:       %{name}-%{major_version}.%{minor_version}-jsvc.service
Source21:       tomcat-functions
Source30:       tomcat-preamble
Source31:       tomcat-server
Source32:       tomcat-named.service
Source100:      valve.xslt
Source101:      allowLinking.xslt
Source1000:     tomcat-rpmlintrc
Source1001:     https://archive.apache.org/dist/tomcat/tomcat-%{major_version}/v%{version}/src/%{packdname}.tar.gz.asc
Source1002:     https://downloads.apache.org/tomcat/tomcat-9/KEYS#/%{name}.keyring
#PATCH-FIX-UPSTREAM: from jpackage.org package
Patch0:         %{name}-%{major_version}.%{minor_version}-bootstrap-MANIFEST.MF.patch
#PATCH-FIX-UPSTREAM: from jpackage.org package
Patch1:         %{name}-%{major_version}.%{minor_version}-tomcat-users-webapp.patch
# PATCH-FIX-SLE: Change security manager default policies bnc#891264
Patch2:         %{name}-%{major_version}.%{minor_version}-sle.catalina.policy.patch
# PATCH-FIX-OPENSUSE: build javadoc with the same java source level as the class files
Patch3:         %{name}-%{major_version}.%{minor_version}-javadoc.patch
# PATCH-FIX-OPENSUSE: include all necessary aqute-bnd jars
Patch4:         tomcat-9.0-osgi-build.patch
# PATCH-FIX-OPENSUSE: build against our ecj that does not have CompilerOptions.VERSION_16
Patch5:         %{name}-%{major_version}.%{minor_version}-jdt.patch
# PATCH-FIX-OPENSUSE: set ajp connector secreteRequired to false by default to avoid tomcat not starting
Patch6:         tomcat-9.0.75-secretRequired-default.patch
Patch7:         tomcat-9.0-fix_catalina.patch
Patch8:         tomcat-9.0-logrotate_everything.patch
Patch9:         tomcat-9.0-build-with-java-11.patch
BuildRequires:  ant >= 1.8.1
BuildRequires:  ant-antlr
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-daemon
BuildRequires:  apache-commons-dbcp >= 2.0
BuildRequires:  apache-commons-pool2
BuildRequires:  aqute-bnd >= 5.2
BuildRequires:  aqute-bndlib >= 5.2
BuildRequires:  ecj >= 4.4.0
BuildRequires:  fdupes
BuildRequires:  findutils
BuildRequires:  geronimo-jaf-1_0_2-api
BuildRequires:  geronimo-jaxrpc-1_1-api
BuildRequires:  geronimo-qname-1_1-api
BuildRequires:  geronimo-saaj-1_1-api
BuildRequires:  jakarta-taglibs-standard >= 1.1
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  pkgconfig
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  unzip
BuildRequires:  wsdl4j
BuildRequires:  zip
BuildRequires:  pkgconfig(systemd)
Requires:       %{name}-lib = %{version}-%{release}
Requires:       apache-commons-daemon
Requires:       apache-commons-dbcp
Requires:       apache-commons-logging
Requires:       apache-commons-pool2
Requires:       java >= 1.8
Requires(post): %fillup_prereq
Requires(post): libxslt-tools
# for runuser
Requires(post): util-linux
Requires(pre):  shadow
Recommends:     libtcnative-1-0 >= 1.1.24
Recommends:     logrotate
Conflicts:      %{name}-implementation
Provides:       %{name}-implementation = %{version}
Provides:       group(tomcat)
Provides:       user(tomcat)
BuildArch:      noarch
%systemd_ordering

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

ATTENTION: This tomcat is built with java 1.8.0.

%package admin-webapps
Summary:        The host manager and manager web applications for Apache Tomcat
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}-%{release}
Requires(post): libxslt-tools
# for runuser
Requires(post): util-linux
Conflicts:      %{name}-implementation-admin-webapps
Provides:       %{name}-implementation-admin-webapps = %{version}

%description admin-webapps
The host manager and manager web-based applications for Apache Tomcat.

%package embed
Summary:        Libraries for Embedding Apache Tomcat
Group:          Productivity/Networking/Web/Servers
Conflicts:      %{name}-implementation-embed
Provides:       %{name}-implementation-embed = %{version}

%description embed
Embeddeding support (various libraries) for Apache Tomcat.

%package docs-webapp
Summary:        The "docs" web application for Apache Tomcat
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}-%{release}
Requires(post): libxslt-tools
# for runuser
Requires(post): util-linux
Conflicts:      %{name}-implementation-docs-webapp
Provides:       %{name}-implementation-docs-webapp = %{version}

%description docs-webapp
The documentation of web application for Apache Tomcat.

%package el-3_0-api
Summary:        Expression Language v3.0 API
Group:          Development/Libraries/Java
Requires(post): update-alternatives
Requires(preun): update-alternatives
Conflicts:      %{name}-implementation-el-api
Provides:       %{name}-el-%{elspec}-api = %{version}-%{release}
Provides:       el_3_0_api = %{version}-%{release}
Provides:       el_api = %{elspec}
Obsoletes:      el_api < %{elspec}
Obsoletes:      tomcat-el-2_2-api
Provides:       %{name}-implementation-el-api = %{version}

%description el-3_0-api
Expression Language API version 3.0.

%package javadoc
Summary:        Javadoc generated documentation for Apache Tomcat
Group:          Documentation/HTML
Conflicts:      %{name}-implementation-javadoc
Provides:       %{name}-implementation-javadoc = %{version}
BuildArch:      noarch

%description javadoc
Javadoc generated documentation files for Apache Tomcat.

%package jsp-2_3-api
Summary:        Apache Tomcat JSP API implementation classes
Group:          Productivity/Networking/Web/Servers
Requires:       mvn(org.apache.tomcat:tomcat-el-api)
Requires:       mvn(org.apache.tomcat:tomcat-servlet-api)
Requires(post): update-alternatives
Requires(postun): update-alternatives
Conflicts:      %{name}-implementation-jsp-api
Provides:       %{name}-implementation-jsp-api = %{version}
Provides:       %{name}-jsp-%{jspspec}-api
Provides:       jsp = %{jspspec}
Provides:       jsp23
Obsoletes:      jsp < %{jspspec}
Obsoletes:      tomcat-jsp-2_2-api

%description jsp-2_3-api
Apache Tomcat JSP API implementation classes version 2.3

%package jsvc
Summary:        Apache jsvc wrapper for Apache Tomcat as separate service
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}-%{release}
Requires:       apache-commons-daemon-jsvc
Conflicts:      %{name}-implementation-jsvc
Provides:       %{name}-implementation-jsvc = %{version}
%systemd_ordering

%description jsvc
Systemd service and wrapper scripts to start tomcat with jsvc,
which allows tomcat to perform some privileged operations
(e.g. bind to a port < 1024) and then switch identity to a non-privileged user.

%package lib
Summary:        Libraries needed to run the Tomcat Web container
Group:          Productivity/Networking/Web/Servers
Requires:       %{name}-el-%{elspec}-api = %{version}-%{release}
Requires:       %{name}-jsp-%{jspspec}-api = %{version}-%{release}
Requires:       %{name}-servlet-%{servletspec}-api = %{version}-%{release}
Requires(post): ecj >= 4.4
Requires(preun): coreutils
Conflicts:      %{name}-implementation-lib
Provides:       jakarta-commons-dbcp-tomcat5 = 1.4
Obsoletes:      jakarta-commons-dbcp-tomcat5 < 1.4
Provides:       %{name}-implementation-lib = %{version}

%description lib
Libraries required to successfully run the Tomcat Web container

%package servlet-4_0-api
Summary:        Apache Tomcat Servlet API implementation classes
Group:          Productivity/Networking/Web/Servers
Requires(post): update-alternatives
Requires(postun): update-alternatives
Conflicts:      %{name}-implementation-servlet-api
Provides:       %{name}-servlet-%{servletspec}-api = %{version}-%{release}
Provides:       servlet = %{servletspec}
Provides:       servlet31
Provides:       servlet7
Obsoletes:      servlet < %{servletspec}
Obsoletes:      tomcat-servlet-3_0-api
Obsoletes:      tomcat-servlet-3_1-api
Provides:       %{name}-implementation-servlet-api = %{version}

%description servlet-4_0-api
Apache Tomcat Servlet API implementation classes version 3.1

%package webapps
Summary:        ROOT and examples web applications for Apache Tomcat
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}-%{release}
Requires:       jakarta-taglibs-standard >= 1.1
Requires(post): libxslt-tools
# for runuser
Requires(post): util-linux
Conflicts:      %{name}-implementation-webapps
Provides:       %{name}-implementation-webapps = %{version}

%description webapps
The ROOT and examples web applications for Apache Tomcat

%prep
%autosetup -p1 -n %{packdname}

# remove pre-built binaries and windows files
find . -type f \( -name "*.bat" -o -name "*.class" -o -name Thumbs.db -o -name "*.gz" -o \
          -name "*.jar" -o -name "*.war" -o -name "*.zip" \) -print -delete

# remove date from docs
sed -i -e '/build-date/ d' webapps/docs/tomcat-docs.xsl

%build

ln -s $(build-classpath jakarta-taglibs-core) webapps/examples/WEB-INF/lib/jstl.jar
ln -s $(build-classpath jakarta-taglibs-standard) webapps/examples/WEB-INF/lib/standard.jar

export CLASSPATH=
export OPT_JAR_LIST="xalan-j2-serializer"
export ANT_OPTS=-Xmx500M

# we don't care about the tarballs and we're going to replace
# so just create a dummy file for later removal
touch HACK
mkdir -p HACKDIR
touch HACKDIR/build.xml

ant -Dbase.path="." \
    -Dadd.osgi.jar.metadata="true" \
    -Djava.7.home="%{java_home}" \
    -Dbuild.compiler="modern" \
    -Dcommons-collections.jar="$(build-classpath commons-collections)" \
    -Dcommons-daemon.jar="$(build-classpath commons-daemon)" \
    -Dcommons-daemon.native.src.tgz="HACK" \
    -Djasper-jdt.jar="$(build-classpath ecj/ecj)" \
    -Djdt.jar="$(build-classpath ecj/ecj)" \
    -Dtomcat-native.tar.gz="HACK" \
    -Dtomcat-native.home="." \
    -Dcommons-daemon.native.win.mgr.exe="HACK" \
    -Dnsis.exe="HACK" \
    -Djaxrpc-lib.jar="$(build-classpath geronimo-jaxrpc-1.1-api)" \
    -Dwsdl4j-lib.jar="$(build-classpath wsdl4j)" \
    -Dsaaj-api.jar="$(build-classpath geronimo-saaj-1.1-api)" \
    -Dbnd.jar="$(build-classpath aqute-bnd/biz.aQute.bnd)" \
    -Dbnd.dir="%{_javadir}/aqute-bnd" \
    -Dosgiannotation.jar="$(build-classpath osgi-annotation/osgi.annotation)" \
    -Dosgi-annotations.jar="$(build-classpath aqute-bnd/biz.aQute.bnd.annotation)" \
    -Dosgicmpn.jar="$(build-classpath osgi-compendium/osgi.cmpn)" \
	-Dslf4j-api.jar="$(build-classpath slf4j/slf4j-api)" \
    -Dcommons-pool.home="$(build-classpath commons-pool2)" \
    -Dcommons-dbcp.home="$(build-classpath commons-dbcp2)" \
    -Dno.build.dbcp=true \
    -Dversion="%{version}" \
    -Dversion.build="%{micro_version}" \
    deploy javadoc package embed-jars

# remove some jars that we'll replace with symlinks later
rm output/build/bin/commons-daemon.jar \
        output/build/lib/ecj.jar

pushd output/dist/src/webapps/docs/appdev/sample/src
mkdir -p ../web/WEB-INF/classes
javac -source %{javac_target} -target %{javac_target} -cp ../../../../../../../../output/build/lib/servlet-api.jar -d ../web/WEB-INF/classes mypackage/Hello.java
pushd ../web
jar cf ../../../../../../../../output/build/webapps/docs/appdev/sample/sample.war *
popd
popd

%install
# build initial path structure
install -d -m 0755 %{buildroot}%{_bindir}
install -d -m 0755 %{buildroot}%{_sbindir}
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
install -d -m 0755 %{buildroot}%{_initddir}
install -d -m 0755 %{buildroot}%{_sysconfdir}/logrotate.d
install -d -m 0755 %{buildroot}%{_sysconfdir}/sysconfig
install -d -m 0755 %{buildroot}%{appdir}
install -d -m 0755 %{buildroot}%{tomcatappdir}
install -d -m 0755 %{buildroot}%{bindir}
install -d -m 0775 %{buildroot}%{confdir}
install -d -m 0755 %{buildroot}%{cachedir}/Catalina/localhost
install -d -m 0755 %{buildroot}%{confdir}/conf.d
/bin/echo "Place your custom *.conf files here. Shell expansion is supported." > %{buildroot}%{confdir}/conf.d/README
install -d -m 0755 %{buildroot}%{libdir}
install -d -m 0775 %{buildroot}%{logdir}
/bin/touch %{buildroot}%{logdir}/catalina.out
install -d -m 0775 %{buildroot}%{_localstatedir}/lib/tomcats
/bin/echo "%{name}-%{major_version}.%{minor_version}.%{micro_version} RPM installed" >> %{buildroot}%{logdir}/catalina.out
install -d -m 0775 %{buildroot}%{homedir}
install -d -m 0775 %{buildroot}%{tempdir}
install -d -m 0775 %{buildroot}%{workdir}
install -d -m 0755 %{buildroot}%{_unitdir}
install -d -m 0755 %{buildroot}%{_libexecdir}/%{name}
install -d -m 0755 %{buildroot}%{_fillupdir}

cp -a %{SOURCE100} %{buildroot}%{confdir}
cp -a %{SOURCE101} %{buildroot}%{confdir}

# move things into place
# First copy supporting libs to tomcat lib
pushd output/build
    cp -a bin/*.{jar,xml} %{buildroot}%{bindir}
    cp -a conf/*.{policy,properties,xml} %{buildroot}%{confdir}
    cp -a lib/*.jar %{buildroot}%{libdir}
    cp -a webapps/* %{buildroot}%{tomcatappdir}
popd
# tomcat embedded
pushd output/embed
    cp -a *.jar %{buildroot}%{libdir}
popd

# javadoc
cp -a output/dist/webapps/docs/api/* %{buildroot}%{_javadocdir}/%{name}

sed -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE1} \
    > %{buildroot}%{confdir}/%{name}.conf
sed -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE3} \
    > %{buildroot}%{_fillupdir}/sysconfig.%{name}
sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE4} \
    > %{buildroot}%{_sbindir}/%{name}
sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE11} \
    > %{buildroot}%{_unitdir}/%{name}.service
sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE20} \
    > %{buildroot}%{_unitdir}/%{name}-jsvc.service
sed -e "s|\@\@\@TCLOG\@\@\@|%{logdir}|g" %{SOURCE5} \
    > %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
sed -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE6} \
    > %{buildroot}%{_bindir}/%{name}-digest
sed -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE7} \
    > %{buildroot}%{_bindir}/%{name}-tool-wrapper

sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE21} \
    > %{buildroot}%{_libexecdir}/%{name}/functions
sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE30} \
    > %{buildroot}%{_libexecdir}/%{name}/preamble
chmod 0755 %{buildroot}%{_libexecdir}/%{name}/preamble
sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE31} \
    > %{buildroot}%{_libexecdir}/%{name}/server
chmod 0755 %{buildroot}%{_libexecdir}/%{name}/server
sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE32} \
    > %{buildroot}%{_unitdir}/%{name}@.service

ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}
ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{name}-jsvc

# create jsp and servlet and el API symlinks
pushd %{buildroot}%{_javadir}
   mv %{name}/jsp-api.jar %{name}-jsp-%{jspspec}-api.jar
   ln -s %{name}-jsp-%{jspspec}-api.jar %{name}-jsp-api.jar
   mv %{name}/servlet-api.jar %{name}-servlet-%{servletspec}-api.jar
   ln -s %{name}-servlet-%{servletspec}-api.jar %{name}-servlet-api.jar
   ln -s %{name}-servlet-%{servletspec}-api.jar %{name}-servlet.jar
   mv %{name}/el-api.jar %{name}-el-%{elspec}-api.jar
   ln -s %{name}-el-%{elspec}-api.jar %{name}-el-api.jar
popd

pushd output/build
    %{_bindir}/build-jar-repository -s lib commons-collections \
                                        commons-dbcp2 commons-pool2 ecj/ecj 2>&1
    # need to use -p here with b-j-r otherwise the examples webapp fails to
    # load with a java.io.IOException
    %{_bindir}/build-jar-repository -p webapps/examples/WEB-INF/lib \
    taglibs-core.jar taglibs-standard.jar 2>&1
popd

pushd %{buildroot}%{libdir}
    # symlink JSP and servlet and el API jars
    ln -s ../%{name}-jsp-%{jspspec}-api.jar .
    ln -s ../%{name}-servlet-%{servletspec}-api.jar .
    ln -s ../%{name}-el-%{elspec}-api.jar .
    ln -s $(build-classpath commons-collections) commons-collections.jar
    rm -f commons-dbcp.jar
    ln -s $(build-classpath commons-dbcp2) commons-dbcp2.jar
    ln -s $(build-classpath commons-pool2) commons-pool2.jar
    ln -s $(build-classpath ecj/ecj) jasper-jdt.jar
    rm ecj.jar
    ln -s $(build-classpath ecj/ecj) ecj.jar

    # Temporary copy the juli jar here from %%{_datadir}/java/tomcat (for maven depmap)
    cp -a %{buildroot}%{bindir}/tomcat-juli.jar ./
popd

# symlink to the FHS locations where we've installed things
pushd %{buildroot}%{homedir}
    ln -s %{appdir} webapps
    ln -s %{confdir} conf
    ln -s %{libdir} lib
    ln -s %{logdir} logs
    ln -s %{tempdir} temp
    ln -s %{workdir} work
popd

# install sample webapp
mkdir -p %{buildroot}%{tomcatappdir}/sample
pushd %{buildroot}%{tomcatappdir}/sample
jar xf %{buildroot}%{tomcatappdir}/docs/appdev/sample/sample.war
popd

pushd %{buildroot}%{tomcatappdir}/examples/WEB-INF/lib
ln -s -f $(build-classpath jakarta-taglibs-core) jstl.jar
ln -s -f $(build-classpath jakarta-taglibs-standard) standard.jar
popd

rm %{buildroot}%{tomcatappdir}/docs/appdev/sample/sample.war

# Install the maven metadata
install -d -m 0755 %{buildroot}%{_mavenpomdir}
pushd output/dist/src/res/maven
for pom in *.pom; do
    # fix-up version in all pom files
    sed -i 's/@MAVEN.DEPLOY.VERSION@/%{version}/g' $pom
done

# we won't install dbcp, juli-adapters and juli-extras pom files
for libname in annotations-api catalina jasper-el jasper catalina-ha jaspic-api; do
    cp -a %{name}-$libname.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-$libname.pom
    %add_maven_depmap JPP.%{name}-$libname.pom %{name}/$libname.jar
done

# servlet-api jsp-api and el-api are not in tomcat subdir, since they are widely re-used elsewhere
cp -a tomcat-jsp-api.pom %{buildroot}%{_mavenpomdir}/JPP-tomcat-jsp-api.pom
%add_maven_depmap JPP-tomcat-jsp-api.pom tomcat-jsp-api.jar -f jsp-api -a "org.eclipse.jetty.orbit:javax.servlet.jsp"

cp -a tomcat-el-api.pom %{buildroot}%{_mavenpomdir}/JPP-tomcat-el-api.pom
%add_maven_depmap JPP-tomcat-el-api.pom tomcat-el-api.jar -f el-api -a "org.eclipse.jetty.orbit:javax.el"

cp -a tomcat-servlet-api.pom %{buildroot}%{_mavenpomdir}/JPP-tomcat-servlet-api.pom
# Generate a depmap fragment javax.servlet:servlet-api pointing to
# tomcat-servlet-3.0-api for backwards compatibility
# also provide jetty depmap (originally in jetty package, but it's cleaner to have it here
%add_maven_depmap JPP-tomcat-servlet-api.pom tomcat-servlet-api.jar -f servlet-api -a "org.mortbay.jetty:servlet-api"

# two special pom where jar files have different names
cp -a tomcat-tribes.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-catalina-tribes.pom
%add_maven_depmap JPP.%{name}-catalina-tribes.pom %{name}/catalina-tribes.jar

cp -a tomcat-coyote.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-coyote.pom
%add_maven_depmap JPP.%{name}-tomcat-coyote.pom %{name}/tomcat-coyote.jar

cp -a tomcat-jni.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-jni.pom
%add_maven_depmap JPP.%{name}-tomcat-jni.pom %{name}/tomcat-jni.jar

cp -a tomcat-juli.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-juli.pom
%add_maven_depmap JPP.%{name}-tomcat-juli.pom %{name}/tomcat-juli.jar

cp -a tomcat-jdbc.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-jdbc.pom
%add_maven_depmap JPP.%{name}-tomcat-jdbc.pom %{name}/tomcat-jdbc.jar

cp -a tomcat-dbcp.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-dbcp.pom
%add_maven_depmap JPP.%{name}-tomcat-dbcp.pom %{name}/tomcat-dbcp.jar

cp -a tomcat-api.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-api.pom
%add_maven_depmap JPP.%{name}-tomcat-api.pom %{name}/tomcat-api.jar

cp -a tomcat-util.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-util.pom
%add_maven_depmap JPP.%{name}-tomcat-util.pom %{name}/tomcat-util.jar

cp -a tomcat-util-scan.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-util-scan.pom
%add_maven_depmap JPP.%{name}-tomcat-util-scan.pom %{name}/tomcat-util-scan.jar

cp -a tomcat-websocket-api.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-websocket-api.pom
%add_maven_depmap JPP.%{name}-websocket-api.pom %{name}/websocket-api.jar

cp -a tomcat-websocket.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-websocket.pom
%add_maven_depmap JPP.%{name}-tomcat-websocket.pom %{name}/tomcat-websocket.jar

cp -a tomcat-embed-core.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-embed-core.pom
%add_maven_depmap JPP.%{name}-tomcat-embed-core.pom %{name}/tomcat-embed-core.jar -f embed

cp -a tomcat-embed-el.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-embed-el.pom
%add_maven_depmap JPP.%{name}-tomcat-embed-el.pom %{name}/tomcat-embed-el.jar -f embed

cp -a tomcat-embed-jasper.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-embed-jasper.pom
%add_maven_depmap JPP.%{name}-tomcat-embed-jasper.pom %{name}/tomcat-embed-jasper.jar -f embed

cp -a tomcat-embed-websocket.pom %{buildroot}%{_mavenpomdir}/JPP.%{name}-tomcat-embed-websocket.pom
%add_maven_depmap JPP.%{name}-tomcat-embed-websocket.pom %{name}/tomcat-embed-websocket.jar -f embed

# replace temporary copy with link
ln -s -f %{bindir}/tomcat-juli.jar %{buildroot}%{libdir}/

# bnc#424675
ln -s %{cachedir}/Catalina %{buildroot}/%{confdir}
rm -rf %{buildroot}/%{confdir}/Catalina
ln -s %{cachedir}/Catalina %{buildroot}/%{confdir}/

# bnc#418664
install -d -m 0755 %{buildroot}/%{_sysconfdir}/ant.d/
echo "%{name}/catalina-ant" > %{buildroot}/%{_sysconfdir}/ant.d/catalina-ant
%fdupes %{buildroot} /srv/%{name}
#bnc#565901
ln -sf %{_sbindir}/%{name} %{buildroot}/%{bindir}/catalina.sh

# Install update-alternatives content
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/el_api %{buildroot}%{_javadir}/%{name}-el_api.jar
ln -s -f %{_sysconfdir}/alternatives/el_1_0_api %{buildroot}%{_javadir}/%{name}-el_1_0_api.jar
ln -s -f %{_sysconfdir}/alternatives/jsp %{buildroot}%{_javadir}/%{name}-jsp.jar
# To avoid conflicts with servletapi4 and servletapi5 create a link to incorrect /etc/alternatives/servlet.jar.
# It will be changed anyways to the correct symlink by update-alternatives.
ln -s -f %{_sysconfdir}/alternatives/servlet.jar %{buildroot}%{_javadir}/servlet.jar

%pre
# add the tomcat user and group
getent group tomcat >/dev/null || %{_sbindir}/groupadd -r tomcat
getent passwd tomcat >/dev/null || %{_sbindir}/useradd -c "Apache Tomcat" \
	-g tomcat -s /sbin/nologin -r -d %{homedir} tomcat
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service
%{fillup_only %{name}}
chown -R tomcat:tomcat %{confdir}/server.xml
runuser -u tomcat -g tomcat -- xsltproc --output %{confdir}/server.xml %{confdir}/valve.xslt %{confdir}/server.xml

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%pre jsvc
%service_add_pre %{name}-jsvc.service

%post jsvc
%service_add_post %{name}-jsvc.service

%preun jsvc
%service_del_preun %{name}-jsvc.service

%postun jsvc
%service_del_postun %{name}-jsvc.service

%post el-3_0-api
update-alternatives --install %{_javadir}/%{name}-el_api.jar el_api %{_javadir}/%{name}-el-%{elspec}-api.jar 20300
update-alternatives --install %{_javadir}/%{name}-el_1_0_api.jar el_1_0_api %{_javadir}/%{name}-el-%{elspec}-api.jar 20300

%preun el-3_0-api
if [ $1 -eq 0 ] ; then
    update-alternatives --remove el_api %{_javadir}/%{name}-el-%{elspec}-api.jar
    update-alternatives --remove el_1_0_api %{_javadir}/%{name}-el-%{elspec}-api.jar
fi

%post jsp-2_3-api
update-alternatives --install %{_javadir}/%{name}-jsp.jar jsp \
    %{_javadir}/%{name}-jsp-%{jspspec}-api.jar 20200

%postun jsp-2_3-api
if [ $1 -eq 0 ] ; then
    update-alternatives --remove jsp \
        %{_javadir}/%{name}-jsp-%{jspspec}-api.jar
fi

%post servlet-4_0-api
update-alternatives --install %{_javadir}/servlet.jar servlet \
    %{_javadir}/%{name}-servlet-%{servletspec}-api.jar 30000
# Fix for bsc#1092163.
# Keep the /usr/share/java/tomcat-servlet.jar symlink for compatibility.
# In case of update from an older version where /usr/share/java/tomcat-servlet.jar is an alternatives symlink
# the update-alternatives in the new version will cause a rename tomcat-servlet.jar -> servlet.jar.
# This makes sure the tomcat-servlet.jar is recreated if it's missing because of the rename.
if [ ! -f %{_javadir}/%{name}-servlet.jar ]; then
    echo "Recreating symlink %{_javadir}/%{name}-servlet.jar"
    ln -s %{_javadir}/%{name}-servlet-%{servletspec}-api.jar %{_javadir}/%{name}-servlet.jar
fi

%postun servlet-4_0-api
if [ $1 -eq 0 ] ; then
    if [ ! -f %{_sysconfdir}/alternatives/servlet ]; then
        # %{_sysconfdir}/alternatives/servlet was removed on uninstall.
        # Create a broken symlink to make sure update-alternatives works correctly and falls back
        # to servletapi5 or servletapi4 if they're installed.
        ln -s %{_javadir}/%{name}-servlet-%{servletspec}-api.jar %{_sysconfdir}/alternatives/servlet
    fi
    update-alternatives --remove servlet \
        %{_javadir}/%{name}-servlet-%{servletspec}-api.jar
fi

%post lib
# those links are no longer needed
rm -f \
    %{libdir}/\[commons-collections-tomcat5\].jar \
    %{libdir}/\[commons-dbcp-tomcat5\].jar \
    %{libdir}/\[commons-pool-tomcat5\].jar \
    %{libdir}/\[ecj\].jar >/dev/null 2>&1

%post webapps
chown -R tomcat:tomcat %{tomcatappdir}/examples/META-INF
runuser -u tomcat -g tomcat -- xsltproc --output %{tomcatappdir}/examples/META-INF/context.xml %{confdir}/allowLinking.xslt %{tomcatappdir}/examples/META-INF/context.xml
if [ ! -e %{_datadir}/%{name}/webapps/examples ]; then
    ln -sf %{tomcatappdir}/examples %{_datadir}/%{name}/webapps/examples
fi
#use the same context.xml for sample war
mkdir -p %{tomcatappdir}/ROOT/META-INF
chown -R tomcat:tomcat %{tomcatappdir}/ROOT/META-INF
runuser -u tomcat -g tomcat -- xsltproc --output %{tomcatappdir}/ROOT/META-INF/context.xml %{confdir}/allowLinking.xslt %{tomcatappdir}/examples/META-INF/context.xml
if [ ! -e %{_datadir}/%{name}/webapps/ROOT ]; then
    ln -sf  %{tomcatappdir}/ROOT %{_datadir}/%{name}/webapps/ROOT
fi
#use the same context.xml for sample war
mkdir -p %{tomcatappdir}/webapps/sample/META-INF
chown -R tomcat:tomcat %{tomcatappdir}/sample/META-INF
runuser -u tomcat -g tomcat -- xsltproc --output %{tomcatappdir}/sample/META-INF/context.xml %{confdir}/allowLinking.xslt %{tomcatappdir}/examples/META-INF/context.xml
if [ ! -e %{_datadir}/%{name}/webapps/sample ]; then
    ln -sf %{tomcatappdir}/sample  %{_datadir}/%{name}/webapps/sample
fi

%postun webapps
if [ $1 -eq 0 ]; then # uninstall only
    rm %{tomcatappdir}/ROOT/META-INF/context.xml
    rm %{tomcatappdir}/sample/META-INF/context.xml
fi

%post admin-webapps
chown -R tomcat:tomcat %{tomcatappdir}/manager/META-INF
runuser -u tomcat -g tomcat -- xsltproc --output %{tomcatappdir}/manager/META-INF/context.xml %{confdir}/allowLinking.xslt %{tomcatappdir}/manager/META-INF/context.xml
if [ ! -e %{_datadir}/%{name}/webapps/manager ]; then
    ln -sf %{tomcatappdir}/manager %{_datadir}/%{name}/webapps/manager
fi

chown -R tomcat:tomcat %{tomcatappdir}/host-manager/META-INF
runuser -u tomcat -g tomcat -- xsltproc --output %{tomcatappdir}/host-manager/META-INF/context.xml %{confdir}/allowLinking.xslt %{tomcatappdir}/host-manager/META-INF/context.xml
if [ ! -e %{_datadir}/%{name}/webapps/host-manager ]; then
    ln -sf %{tomcatappdir}/host-manager %{_datadir}/%{name}/webapps/host-manager
fi

%post docs-webapp
chown -R tomcat:tomcat %{tomcatappdir}/docs/META-INF
runuser -u tomcat -g tomcat -- xsltproc --output %{tomcatappdir}/docs/META-INF/context.xml %{confdir}/allowLinking.xslt %{tomcatappdir}/docs/META-INF/context.xml
if [ ! -e %{_datadir}/%{name}/webapps/docs ]; then
    ln -sf %{tomcatappdir}/docs %{_datadir}/%{name}/webapps/docs
fi

%files
%doc {LICENSE,NOTICE,RELEASE*}
%{_bindir}/%{name}-digest
%{_bindir}/%{name}-tool-wrapper
%{_sbindir}/%{name}
%{_unitdir}/%{name}.service
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}@.service
%dir %{_libexecdir}/%{name}
%dir %{_localstatedir}/lib/tomcats
%{_libexecdir}/%{name}/functions
%{_libexecdir}/%{name}/preamble
%{_libexecdir}/%{name}/server
#bnc#565901
%{bindir}/catalina.sh
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{basedir}
%dir %{confdir}
%attr(0775,root,tomcat) %dir %{appdir}
%attr(0770,tomcat,tomcat) %dir %{logdir}
%attr(0660,tomcat,tomcat) %{logdir}/catalina.out
%attr(0770,root,tomcat) %dir %{cachedir}
%attr(0775,root,tomcat) %dir %{cachedir}/Catalina

# tomcat group writtable dirs - bnc#625415
%attr(0770,root,tomcat) %dir %{tempdir}
%attr(0770,root,tomcat) %dir %{workdir}
%attr(0775,root,tomcat) %dir %{tomcatappdir}

%{confdir}/Catalina
%dir %{confdir}/conf.d
%{confdir}/conf.d/README
%config(noreplace) %{confdir}/%{name}.conf
%config(noreplace) %{confdir}/*.policy
%config(noreplace) %{confdir}/*.properties
%config(noreplace) %{confdir}/context.xml
%config(noreplace) %{confdir}/server.xml
# keep tomcat-users.xml readable only by root and tomcat group
%attr(0640,root,tomcat) %config(noreplace) %{confdir}/tomcat-users.xml
%config(noreplace) %{confdir}/web.xml
%config(noreplace) %{confdir}/jaspic-providers.xml
%dir %{homedir}
%{bindir}/bootstrap.jar
%{bindir}/catalina-tasks.xml
%{homedir}/lib
%{homedir}/temp
%{homedir}/work
%{homedir}/webapps
%{homedir}/logs
%{homedir}/conf
%{_fillupdir}/sysconfig.%{name}
%{confdir}/allowLinking.xslt
%{confdir}/valve.xslt

%files admin-webapps
%defattr(0644,root,tomcat,0755)
%{tomcatappdir}/host-manager
%config(noreplace) %{tomcatappdir}/host-manager/META-INF/context.xml
%{tomcatappdir}/manager
%config(noreplace) %{tomcatappdir}/manager/META-INF/context.xml

%files docs-webapp
%{tomcatappdir}/docs

%files el-3_0-api -f output/dist/src/res/maven/.mfiles-el-api
%{_javadir}/%{name}-el-%{elspec}-api.jar
%{_javadir}/%{name}-el-api.jar
%{libdir}/%{name}-el-%{elspec}-api.jar
%{_javadir}/%{name}-el_1_0_api.jar
%{_javadir}/%{name}-el_api.jar
%ghost %{_sysconfdir}/alternatives/el_1_0_api
%ghost %{_sysconfdir}/alternatives/el_api

%files javadoc
%doc %{_javadocdir}/%{name}

%files jsp-2_3-api -f output/dist/src/res/maven/.mfiles-jsp-api
%{_javadir}/%{name}-jsp-%{jspspec}-api.jar
%{_javadir}/%{name}-jsp-api.jar
%{_javadir}/%{name}-jsp.jar
%ghost %{_sysconfdir}/alternatives/jsp

%files lib -f output/dist/src/res/maven/.mfiles
%{libdir}
%dir %{bindir}
%{bindir}/tomcat-juli.jar
%exclude %{libdir}/%{name}-el-%{elspec}-api.jar
%exclude %{libdir}/%{name}*-embed-*.jar
# bnc#418664
%dir %{_sysconfdir}/ant.d
%config(noreplace) %{_sysconfdir}/ant.d/catalina-ant

%files embed -f output/dist/src/res/maven/.mfiles-embed
%dir %{libdir}

%files servlet-4_0-api -f output/dist/src/res/maven/.mfiles-servlet-api
%license LICENSE
%{_javadir}/%{name}-servlet-%{servletspec}-api.jar
%{_javadir}/%{name}-servlet-api.jar
%{_javadir}/%{name}-servlet.jar
%{_javadir}/servlet.jar
%ghost %{_sysconfdir}/alternatives/servlet

%files webapps
%defattr(0644,root,tomcat,0755)
#bnc#520532
%config(noreplace) %{tomcatappdir}/ROOT
%{tomcatappdir}/examples
%config(noreplace) %{tomcatappdir}/examples/META-INF/context.xml
%{tomcatappdir}/sample

%files jsvc
%defattr(755,root,root,0755)
%{_unitdir}/%{name}-jsvc.service
%{_sbindir}/rc%{name}-jsvc

%changelog
