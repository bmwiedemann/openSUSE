#
# spec file for package tomcat11
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define app_name tomcat
%define jspspec_major 4
%define jspspec_minor 0
%define jspspec %{jspspec_major}.%{jspspec_minor}
%define servletspec_major 6
%define servletspec_minor 1
%define servletspec %{servletspec_major}.%{servletspec_minor}
%define elspec_major 6
%define elspec_minor 0
%define elspec %{elspec_major}.%{elspec_minor}
%define major_version 11
%define minor_version 0
%define micro_version 13
%define java_major 1
%define java_minor 17
%define java_version %{java_major}.%{java_minor}
%define packdname apache-tomcat-%{version}-src
# FHS 2.3 compliant tree structure - http://www.pathname.com/fhs/2.3/
%global basedir /srv/%{app_name}
%define appdir %{basedir}/webapps
%define bindir %{_datadir}/%{app_name}/bin
%define confdir %{_sysconfdir}/%{app_name}
%define homedir %{_datadir}/%{app_name}
%define libdir %{_javadir}/%{app_name}
%define logdir %{_localstatedir}/log/%{app_name}
%define cachedir %{_localstatedir}/cache/%{app_name}
%define tempdir %{cachedir}/temp
%define workdir %{cachedir}/work
%define tomcatappdir %{_datadir}/%{app_name}/%{app_name}-webapps
%define javac_target 17
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           %{app_name}%{major_version}
Version:        %{major_version}.%{minor_version}.%{micro_version}
Release:        0
Summary:        Apache Servlet/JSP/EL Engine, RI for Servlet %{servletspec}/JSP %{jspspec}/EL %{elspec} API
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://tomcat.apache.org
Source0:        https://archive.apache.org/dist/%{app_name}/%{app_name}-%{major_version}/v%{version}/src/%{packdname}.tar.gz
Source1:        %{app_name}.conf
Source3:        %{app_name}.sysconfig
Source4:        %{app_name}.wrapper
Source5:        %{app_name}.logrotate
Source6:        %{app_name}-digest.script
Source7:        %{app_name}-tool-wrapper.script
Source11:       %{app_name}.service
Source20:       %{app_name}-jsvc.service
Source21:       %{app_name}-functions
Source30:       %{app_name}-preamble
Source31:       %{app_name}-server
Source32:       %{app_name}-named.service
Source100:      valve.xslt
Source101:      allowLinking.xslt
Source1000:     %{app_name}-rpmlintrc
Source1001:     https://archive.apache.org/dist/%{app_name}/%{app_name}-%{major_version}/v%{version}/src/%{packdname}.tar.gz.asc
Source1002:     %{app_name}.keyring
# #PATCH-FIX-UPSTREAM: from jpackage.org package
Patch0:         %{app_name}-bootstrap-MANIFEST.MF.patch
# #PATCH-FIX-UPSTREAM: from jpackage.org package
Patch1:         %{app_name}-%{app_name}-users-webapp.patch
# # PATCH-FIX-OPENSUSE: build javadoc with the same java source level as the class files
Patch2:         %{app_name}-javadoc.patch
# # PATCH-FIX-OPENSUSE: include all necessary aqute-bnd jars
Patch3:         %{app_name}-osgi-build.patch
# PATCH-FIX-OPENSUSE: build against our ecj that does not have CompilerOptions.VERSION_16
Patch4:         %{app_name}-jdt.patch
# # PATCH-FIX-OPENSUSE: set ajp connector secreteRequired to false by default to avoid tomcat not starting
Patch5:         %{app_name}-secretRequired-default.patch
Patch6:         %{app_name}-fix_catalina.patch
Patch7:         %{app_name}-logrotate_everything.patch
BuildRequires:  ant
BuildRequires:  ant-antlr
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-daemon
BuildRequires:  apache-commons-dbcp
BuildRequires:  apache-commons-pool2
BuildRequires:  aqute-bnd
BuildRequires:  ecj
BuildRequires:  fdupes
BuildRequires:  findutils
BuildRequires:  jakarta-taglibs-standard
BuildRequires:  java-devel >= 17
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  osgi-annotation
BuildRequires:  osgi-compendium
BuildRequires:  osgi-core
BuildRequires:  pkgconfig
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  tomcat-jakartaee-migration >= 1.0.7
BuildRequires:  unzip
BuildRequires:  wsdl4j
BuildRequires:  zip
BuildRequires:  pkgconfig(systemd)
Requires:       %{name}-lib = %{version}-%{release}
Requires:       apache-commons-daemon
Requires:       apache-commons-dbcp
Requires:       apache-commons-logging
Requires:       apache-commons-pool2
Requires:       java >= %{java_version}
Requires:       libtcnative-1-0 >= 1.2.38
Requires:       logrotate
Requires(post): %fillup_prereq
Requires(post): libxslt-tools
# for runuser
Requires(post): util-linux
Requires(pre):  shadow
Conflicts:      %{app_name}-implementation
Provides:       %{app_name}-implementation = %{version}
Provides:       group(tomcat)
Provides:       user(tomcat)
BuildArch:      noarch
%systemd_ordering

%description
Tomcat is the servlet container that is used in the official Reference
Implementation for the Java Servlet and JavaServer Pages technologies.
The Java Servlet and JavaServer Pages specifications are developed by
Sun under the Java Community Process.

ATTENTION: This tomcat is built with java %{java_version}.

%package admin-webapps
Summary:        The host manager and manager web applications for Apache Tomcat
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}-%{release}
Requires(post): libxslt-tools
# for runuser
Requires(post): util-linux
Conflicts:      %{app_name}-implementation-admin-webapps
Provides:       %{app_name}-implementation-admin-webapps = %{version}

%description admin-webapps
The host manager and manager web-based applications for Apache Tomcat.

%package embed
Summary:        Libraries for Embedding Apache Tomcat
Group:          Productivity/Networking/Web/Servers
Conflicts:      %{app_name}-implementation-embed
Provides:       %{app_name}-implementation-embed = %{version}

%description embed
Embeddeding support (various libraries) for Apache Tomcat.

%package docs-webapp
Summary:        The "docs" web application for Apache Tomcat
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}-%{release}
Requires(post): libxslt-tools
# for runuser
Requires(post): util-linux
Conflicts:      %{app_name}-implementation-docs-webapp
Provides:       %{app_name}-implementation-docs-webapp = %{version}

%description docs-webapp
The documentation of web application for Apache Tomcat.

%package el-%{elspec_major}_%{elspec_minor}-api
Summary:        Expression Language v%{elspec} API
Group:          Development/Libraries/Java
Conflicts:      %{app_name}-implementation-el-api
Provides:       %{app_name}-el-%{elspec}-api = %{version}-%{release}
Provides:       %{app_name}-implementation-el-api = %{version}
Provides:       el_%{elspec_major}_%{elspec_minor}_api = %{version}-%{release}
Obsoletes:      %{app_name}-el-2_2-api < %{version}

%description el-%{elspec_major}_%{elspec_minor}-api
Expression Language API version %{elspec}.

%package doc
Summary:        Javadoc generated documentation for Apache Tomcat
Group:          Documentation/HTML
Conflicts:      %{app_name}-implementation-javadoc
Provides:       %{app_name}-implementation-javadoc = %{version}
BuildArch:      noarch

%description doc
Javadoc generated documentation files for Apache Tomcat.

%package jsp-%{jspspec_major}_%{jspspec_minor}-api
Summary:        Apache Tomcat JSP API implementation classes
Group:          Productivity/Networking/Web/Servers
Conflicts:      %{app_name}-implementation-jsp-api
Provides:       %{app_name}-implementation-jsp-api = %{version}
Provides:       %{app_name}-jsp-%{jspspec}-api
Provides:       jsp%{jspspec_major}%{jspspec_minor}
Obsoletes:      %{app_name}-jsp-2_2-api < %{version}

%description jsp-%{jspspec_major}_%{jspspec_minor}-api
Apache Tomcat JSP API implementation classes version %{jspspec}

%package jsvc
Summary:        Apache jsvc wrapper for Apache Tomcat as separate service
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}-%{release}
Requires:       apache-commons-daemon-jsvc
Conflicts:      %{app_name}-implementation-jsvc
Provides:       %{app_name}-implementation-jsvc = %{version}
%systemd_ordering

%description jsvc
Systemd service and wrapper scripts to start tomcat with jsvc,
which allows tomcat to perform some privileged operations
(e.g. bind to a port < 1024) and then switch identity to a non-privileged user.

%package lib
Summary:        Libraries needed to run the Tomcat Web container
Group:          Productivity/Networking/Web/Servers
Requires:       %{app_name}-el-%{elspec}-api = %{version}-%{release}
Requires:       %{app_name}-jsp-%{jspspec}-api = %{version}-%{release}
Requires:       %{app_name}-servlet-%{servletspec}-api = %{version}-%{release}
Requires:       mvn(org.apache.tomcat:tomcat-websocket-client-api)
Requires(post): ecj >= 4.4
Requires(preun): coreutils
Conflicts:      %{app_name}-implementation-lib
Provides:       %{app_name}-implementation-lib = %{version}
Provides:       jakarta-commons-dbcp-tomcat5 = 1.4
Obsoletes:      jakarta-commons-dbcp-tomcat5 < 1.4

%description lib
Libraries required to successfully run the Tomcat Web container

%package servlet-%{servletspec_major}_%{servletspec_minor}-api
Summary:        Apache Tomcat Servlet API implementation classes
Group:          Productivity/Networking/Web/Servers
Conflicts:      %{app_name}-implementation-servlet-api
Provides:       %{app_name}-implementation-servlet-api = %{version}
Provides:       %{app_name}-servlet-%{servletspec}-api = %{version}-%{release}
Provides:       servlet11
Provides:       servlet60
Obsoletes:      %{app_name}-servlet-3_0-api < %{version}
Obsoletes:      %{app_name}-servlet-3_1-api < %{version}

%description servlet-%{servletspec_major}_%{servletspec_minor}-api
Apache Tomcat Servlet API implementation classes version %{servletspec}

%package webapps
Summary:        ROOT and examples web applications for Apache Tomcat
Group:          Productivity/Networking/Web/Servers
Requires:       %{name} = %{version}-%{release}
Requires:       jakarta-taglibs-standard >= 1.1
Requires(post): libxslt-tools
# for runuser
Requires(post): util-linux
Conflicts:      %{app_name}-implementation-webapps
Provides:       %{app_name}-implementation-webapps = %{version}

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
    -Djava.%{java_minor}.home="%{java_home}" \
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
    -Dosgicore.jar="$( build-classpath osgi-core/osgi.core)" \
    -Dannotation.jar="$(build-classpath aqute-bnd/biz.aQute.bnd.annotation)" \
    -Dosgicmpn.jar="$(build-classpath osgi-compendium/osgi.cmpn)" \
	-Dslf4j-api.jar="$(build-classpath slf4j/slf4j-api)" \
    -Dcommons-pool.home="$(build-classpath commons-pool2)" \
    -Dcommons-dbcp.home="$(build-classpath commons-dbcp2)" \
    -Dmigration-lib.jar="$(build-classpath tomcat-jakartaee-migration)" \
    -Dno.build.dbcp=true \
    -Dversion="%{version}" \
    -Dversion.build="%{micro_version}" \
    deploy javadoc package embed-jars

# remove some jars that we'll replace with symlinks later
rm output/build/bin/commons-daemon.jar \
        output/build/lib/ecj.jar

pushd output/dist/src/webapps/docs/appdev/sample/src
mkdir -p ../web/WEB-INF/classes
javac -source %{java_minor} -target %{javac_target} -cp ../../../../../../../../output/build/lib/servlet-api.jar -d ../web/WEB-INF/classes mypackage/Hello.java
pushd ../web
jar cf ../../../../../../../../output/build/webapps/docs/appdev/sample/sample.war *
popd
popd

%install
# build initial path structure
install -d -m 0755 %{buildroot}%{_bindir}
install -d -m 0755 %{buildroot}%{_sbindir}
install -d -m 0755 %{buildroot}%{_javadocdir}/%{app_name}
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
/bin/echo "%{app_name}-%{major_version}.%{minor_version}.%{micro_version} RPM installed" >> %{buildroot}%{logdir}/catalina.out
install -d -m 0775 %{buildroot}%{homedir}
install -d -m 0775 %{buildroot}%{tempdir}
install -d -m 0775 %{buildroot}%{workdir}
install -d -m 0755 %{buildroot}%{_unitdir}
install -d -m 0755 %{buildroot}%{_libexecdir}/%{app_name}
install -d -m 0755 %{buildroot}%{_fillupdir}

cp -a %{SOURCE100} %{buildroot}%{confdir}
cp -a %{SOURCE101} %{buildroot}%{confdir}

# move things into place
# First copy supporting libs to tomcat lib
pushd output/build
    cp -a bin/*.{jar,xml} %{buildroot}%{bindir}
    cp -a conf/*.{properties,xml} %{buildroot}%{confdir}
    cp -a lib/*.jar %{buildroot}%{libdir}
    cp -a webapps/* %{buildroot}%{tomcatappdir}
popd
# tomcat embedded
pushd output/embed
    cp -a *.jar %{buildroot}%{libdir}
popd

# doc
cp -a output/dist/webapps/docs/api/* %{buildroot}%{_javadocdir}/%{app_name}

sed -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE1} \
    > %{buildroot}%{confdir}/%{app_name}.conf
sed -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE3} \
    > %{buildroot}%{_fillupdir}/sysconfig.%{app_name}
sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE4} \
    > %{buildroot}%{_sbindir}/%{app_name}
sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE11} \
    > %{buildroot}%{_unitdir}/%{app_name}.service
sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE20} \
    > %{buildroot}%{_unitdir}/%{app_name}-jsvc.service
sed -e "s|\@\@\@TCLOG\@\@\@|%{logdir}|g" %{SOURCE5} \
    > %{buildroot}%{_sysconfdir}/logrotate.d/%{app_name}10
sed -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE6} \
    > %{buildroot}%{_bindir}/%{app_name}-digest
sed -e "s|\@\@\@TCHOME\@\@\@|%{homedir}|g" \
   -e "s|\@\@\@TCTEMP\@\@\@|%{tempdir}|g" \
   -e "s|\@\@\@LIBDIR\@\@\@|%{_libdir}|g" %{SOURCE7} \
    > %{buildroot}%{_bindir}/%{app_name}-tool-wrapper

sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE21} \
    > %{buildroot}%{_libexecdir}/%{app_name}/functions
sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE30} \
    > %{buildroot}%{_libexecdir}/%{app_name}/preamble
chmod 0755 %{buildroot}%{_libexecdir}/%{app_name}/preamble
sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE31} \
    > %{buildroot}%{_libexecdir}/%{app_name}/server
chmod 0755 %{buildroot}%{_libexecdir}/%{app_name}/server
sed -e "s|@LIBEXECDIR@|%{_libexecdir}|g" %{SOURCE32} \
    > %{buildroot}%{_unitdir}/%{app_name}@.service

ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{app_name}
ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rc%{app_name}-jsvc

# create jsp and servlet and el API symlinks
pushd %{buildroot}%{_javadir}
   mv %{app_name}/jsp-api.jar %{app_name}-jsp-%{jspspec}-api.jar
   ln -s %{app_name}-jsp-%{jspspec}-api.jar %{app_name}-jsp-api.jar
   mv %{app_name}/servlet-api.jar %{app_name}-servlet-%{servletspec}-api.jar
   ln -s %{app_name}-servlet-%{servletspec}-api.jar %{app_name}-servlet-api.jar
   ln -s %{app_name}-servlet-%{servletspec}-api.jar %{app_name}-servlet.jar
   mv %{app_name}/el-api.jar %{app_name}-el-%{elspec}-api.jar
   ln -s %{app_name}-el-%{elspec}-api.jar %{app_name}-el-api.jar
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
    ln -s ../%{app_name}-jsp-%{jspspec}-api.jar .
    ln -s ../%{app_name}-servlet-%{servletspec}-api.jar .
    ln -s ../%{app_name}-el-%{elspec}-api.jar .
    ln -s $(build-classpath commons-collections) commons-collections.jar
    rm -f commons-dbcp.jar
    ln -s $(build-classpath commons-dbcp2) commons-dbcp2.jar
    ln -s $(build-classpath commons-pool2) commons-pool2.jar
    rm ecj.jar
    ln -s $(build-classpath ecj/ecj) ecj.jar
    ln -s $(build-classpath ecj/ecj) jasper-jdt.jar

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
    %{mvn_install_pom} %{app_name}-$libname.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-$libname.pom
    %add_maven_depmap JPP.%{app_name}-$libname.pom %{app_name}/$libname.jar
done

# servlet-api jsp-api and el-api are not in tomcat subdir, since they are widely re-used elsewhere
%{mvn_install_pom} %{app_name}-jsp-api.pom  %{buildroot}%{_mavenpomdir}/JPP-%{app_name}-jsp-api.pom
%add_maven_depmap JPP-%{app_name}-jsp-api.pom %{app_name}-jsp-api.jar -f jsp-api -a "org.eclipse.jetty.orbit:jakarta.servlet.jsp"

%{mvn_install_pom} %{app_name}-el-api.pom %{buildroot}%{_mavenpomdir}/JPP-%{app_name}-el-api.pom
%add_maven_depmap JPP-%{app_name}-el-api.pom %{app_name}-el-api.jar -f el-api -a "org.eclipse.jetty.orbit:jakarta.el"

%{mvn_install_pom} %{app_name}-servlet-api.pom %{buildroot}%{_mavenpomdir}/JPP-%{app_name}-servlet-api.pom
# Generate a depmap fragment javax.servlet:servlet-api pointing to
# tomcat-servlet-3.0-api for backwards compatibility
# also provide jetty depmap (originally in jetty package, but it's cleaner to have it here
%add_maven_depmap JPP-tomcat-servlet-api.pom tomcat-servlet-api.jar -f servlet-api -a "org.mortbay.jetty:servlet-api"

# two special pom where jar files have different names
%{mvn_install_pom} %{app_name}-tribes.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-catalina-tribes.pom
%add_maven_depmap JPP.%{app_name}-catalina-tribes.pom %{app_name}/catalina-tribes.jar

%{mvn_install_pom} %{app_name}-coyote.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-%{app_name}-coyote.pom
%add_maven_depmap JPP.%{app_name}-%{app_name}-coyote.pom %{app_name}/%{app_name}-coyote.jar

%{mvn_install_pom} %{app_name}-jni.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-%{app_name}-jni.pom
%add_maven_depmap JPP.%{app_name}-%{app_name}-jni.pom %{app_name}/%{app_name}-jni.jar

%{mvn_install_pom} %{app_name}-juli.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-%{app_name}-juli.pom
%add_maven_depmap JPP.%{app_name}-%{app_name}-juli.pom %{app_name}/%{app_name}-juli.jar

%{mvn_install_pom} %{app_name}-jdbc.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-%{app_name}-jdbc.pom
%add_maven_depmap JPP.%{app_name}-%{app_name}-jdbc.pom %{app_name}/%{app_name}-jdbc.jar

%{mvn_install_pom} %{app_name}-dbcp.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-%{app_name}-dbcp.pom
%add_maven_depmap JPP.%{app_name}-%{app_name}-dbcp.pom %{app_name}/%{app_name}-dbcp.jar

%{mvn_install_pom} %{app_name}-api.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-%{app_name}-api.pom
%add_maven_depmap JPP.%{app_name}-%{app_name}-api.pom %{app_name}/%{app_name}-api.jar

%{mvn_install_pom} %{app_name}-util.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-%{app_name}-util.pom
%add_maven_depmap JPP.%{app_name}-%{app_name}-util.pom %{app_name}/%{app_name}-util.jar

%{mvn_install_pom} %{app_name}-util-scan.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-%{app_name}-util-scan.pom
%add_maven_depmap JPP.%{app_name}-%{app_name}-util-scan.pom %{app_name}/%{app_name}-util-scan.jar

%{mvn_install_pom} %{app_name}-websocket-api.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-websocket-api.pom
%add_maven_depmap JPP.%{app_name}-websocket-api.pom %{app_name}/websocket-api.jar

%{mvn_install_pom} %{app_name}-websocket-client-api.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-websocket-client-api.pom
%add_maven_depmap JPP.%{app_name}-websocket-client-api.pom %{app_name}/websocket-client-api.jar

%{mvn_install_pom} %{app_name}-websocket.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-%{app_name}-websocket.pom
%add_maven_depmap JPP.%{app_name}-%{app_name}-websocket.pom %{app_name}/%{app_name}-websocket.jar

%{mvn_install_pom} %{app_name}-embed-core.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-%{app_name}-embed-core.pom
%add_maven_depmap JPP.%{app_name}-%{app_name}-embed-core.pom %{app_name}/%{app_name}-embed-core.jar -f embed

%{mvn_install_pom} %{app_name}-embed-el.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-%{app_name}-embed-el.pom
%add_maven_depmap JPP.%{app_name}-%{app_name}-embed-el.pom %{app_name}/%{app_name}-embed-el.jar -f embed

%{mvn_install_pom} %{app_name}-embed-jasper.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-%{app_name}-embed-jasper.pom
%add_maven_depmap JPP.%{app_name}-%{app_name}-embed-jasper.pom %{app_name}/%{app_name}-embed-jasper.jar -f embed

%{mvn_install_pom} %{app_name}-embed-websocket.pom %{buildroot}%{_mavenpomdir}/JPP.%{app_name}-%{app_name}-embed-websocket.pom
%add_maven_depmap JPP.%{app_name}-%{app_name}-embed-websocket.pom %{app_name}/%{app_name}-embed-websocket.jar -f embed

# replace temporary copy with link
ln -s -f %{bindir}/tomcat-juli.jar %{buildroot}%{libdir}/

# bnc#424675
ln -s %{cachedir}/Catalina %{buildroot}/%{confdir}
rm -rf %{buildroot}/%{confdir}/Catalina
ln -s %{cachedir}/Catalina %{buildroot}/%{confdir}/

# bnc#418664
install -d -m 0755 %{buildroot}/%{_sysconfdir}/ant.d/
echo "tomcat/catalina-ant" > %{buildroot}/%{_sysconfdir}/ant.d/catalina-ant
%fdupes %{buildroot} /srv/%{app_name}
#bnc#565901
ln -sf %{_sbindir}/%{app_name} %{buildroot}/%{bindir}/catalina.sh

%pre
# add the tomcat user and group
getent group tomcat >/dev/null || %{_sbindir}/groupadd -r tomcat
getent passwd tomcat >/dev/null || %{_sbindir}/useradd -c "Apache Tomcat" \
       -g tomcat -s /sbin/nologin -r -d %{homedir} tomcat
%service_add_pre %{app_name}.service

%post
%service_add_post %{app_name}.service
%{fillup_only %{app_name}}
chown -R tomcat:tomcat %{confdir}/server.xml
runuser -u tomcat -g tomcat -- xsltproc --output %{confdir}/server.xml %{confdir}/valve.xslt %{confdir}/server.xml

%preun
%service_del_preun %{app_name}.service

%postun
%service_del_postun %{app_name}.service

%pre jsvc
%service_add_pre %{app_name}-jsvc.service

%post jsvc
%service_add_post %{app_name}-jsvc.service

%preun jsvc
%service_del_preun %{app_name}-jsvc.service

%postun jsvc
%service_del_postun %{app_name}-jsvc.service

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
if [ ! -e %{_datadir}/%{app_name}/webapps/examples ]; then
    ln -sf %{tomcatappdir}/examples %{_datadir}/%{app_name}/webapps/examples
fi
#use the same context.xml for sample war
mkdir -p %{tomcatappdir}/ROOT/META-INF
chown -R tomcat:tomcat %{tomcatappdir}/ROOT/META-INF
runuser -u tomcat -g tomcat -- xsltproc --output %{tomcatappdir}/ROOT/META-INF/context.xml %{confdir}/allowLinking.xslt %{tomcatappdir}/examples/META-INF/context.xml
if [ ! -e %{_datadir}/%{app_name}/webapps/ROOT ]; then
    ln -sf  %{tomcatappdir}/ROOT %{_datadir}/%{app_name}/webapps/ROOT
fi
#use the same context.xml for sample war
mkdir -p %{tomcatappdir}/webapps/sample/META-INF
chown -R tomcat:tomcat %{tomcatappdir}/sample/META-INF
runuser -u tomcat -g tomcat -- xsltproc --output %{tomcatappdir}/sample/META-INF/context.xml %{confdir}/allowLinking.xslt %{tomcatappdir}/examples/META-INF/context.xml
if [ ! -e %{_datadir}/%{app_name}/webapps/sample ]; then
    ln -sf %{tomcatappdir}/sample  %{_datadir}/%{app_name}/webapps/sample
fi

%postun webapps
if [ $1 -eq 0 ]; then # uninstall only
    rm %{tomcatappdir}/ROOT/META-INF/context.xml
    rm %{tomcatappdir}/sample/META-INF/context.xml
fi

%post admin-webapps
chown -R tomcat:tomcat %{tomcatappdir}/manager/META-INF
runuser -u tomcat -g tomcat -- xsltproc --output %{tomcatappdir}/manager/META-INF/context.xml %{confdir}/allowLinking.xslt %{tomcatappdir}/manager/META-INF/context.xml
if [ ! -e %{_datadir}/%{app_name}/webapps/manager ]; then
    ln -sf %{tomcatappdir}/manager %{_datadir}/%{app_name}/webapps/manager
fi

chown -R tomcat:tomcat %{tomcatappdir}/host-manager/META-INF
runuser -u tomcat -g tomcat -- xsltproc --output %{tomcatappdir}/host-manager/META-INF/context.xml %{confdir}/allowLinking.xslt %{tomcatappdir}/host-manager/META-INF/context.xml
if [ ! -e %{_datadir}/%{app_name}/webapps/host-manager ]; then
    ln -sf %{tomcatappdir}/host-manager %{_datadir}/%{app_name}/webapps/host-manager
fi

%post docs-webapp
chown -R tomcat:tomcat %{tomcatappdir}/docs/META-INF
runuser -u tomcat -g tomcat -- xsltproc --output %{tomcatappdir}/docs/META-INF/context.xml %{confdir}/allowLinking.xslt %{tomcatappdir}/docs/META-INF/context.xml
if [ ! -e %{_datadir}/%{app_name}/webapps/docs ]; then
    ln -sf %{tomcatappdir}/docs %{_datadir}/%{app_name}/webapps/docs
fi

%files
%doc {LICENSE,NOTICE,RELEASE*}
%{_bindir}/%{app_name}-digest
%{_bindir}/%{app_name}-tool-wrapper
%{_sbindir}/%{app_name}
%{_unitdir}/%{app_name}.service
%{_sbindir}/rc%{app_name}
%{_unitdir}/%{app_name}@.service
%dir %{_libexecdir}/%{app_name}
%dir %{_localstatedir}/lib/%{app_name}s
%{_libexecdir}/%{app_name}/functions
%{_libexecdir}/%{app_name}/preamble
%{_libexecdir}/%{app_name}/server
#bnc#565901 and bsc#1253460
%config(noreplace) %{bindir}/catalina.sh
%config(noreplace) %{_sysconfdir}/logrotate.d/%{app_name}10
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
%config(noreplace) %{confdir}/conf.d/README
%config(noreplace) %{confdir}/%{app_name}.conf
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
%{homedir}/webapps
%{homedir}/work
%{homedir}/logs
%{homedir}/conf
%{_fillupdir}/sysconfig.%{app_name}
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

%files el-%{elspec_major}_%{elspec_minor}-api -f output/dist/src/res/maven/.mfiles-el-api
%{_javadir}/%{app_name}-el-%{elspec}-api.jar
%{_javadir}/%{app_name}-el-api.jar
%{libdir}/%{app_name}-el-%{elspec}-api.jar

%files doc
%doc %{_javadocdir}/%{app_name}

%files jsp-%{jspspec_major}_%{jspspec_minor}-api -f output/dist/src/res/maven/.mfiles-jsp-api
%{_javadir}/%{app_name}-jsp-%{jspspec}-api.jar
%{_javadir}/%{app_name}-jsp-api.jar

%files lib -f output/dist/src/res/maven/.mfiles
%{libdir}
%dir %{bindir}
%{bindir}/tomcat-juli.jar
%exclude %{libdir}/%{app_name}-el-%{elspec}-api.jar
%exclude %{libdir}/%{app_name}*-embed-*.jar
# bnc#418664
%dir %{_sysconfdir}/ant.d
%config(noreplace) %{_sysconfdir}/ant.d/catalina-ant

%files embed -f output/dist/src/res/maven/.mfiles-embed
%dir %{libdir}

%files servlet-%{servletspec_major}_%{servletspec_minor}-api -f output/dist/src/res/maven/.mfiles-servlet-api
%license LICENSE
%{_javadir}/%{app_name}-servlet-%{servletspec}-api.jar
%{_javadir}/%{app_name}-servlet-api.jar
%{_javadir}/%{app_name}-servlet.jar

%files webapps
%defattr(0644,root,tomcat,0755)
#bnc#520532
%config(noreplace) %{tomcatappdir}/ROOT
%{tomcatappdir}/examples
%config(noreplace) %{tomcatappdir}/examples/META-INF/context.xml
%{tomcatappdir}/sample

%files jsvc
%defattr(755,root,root,0755)
%{_unitdir}/%{app_name}-jsvc.service
%{_sbindir}/rc%{app_name}-jsvc

%changelog
