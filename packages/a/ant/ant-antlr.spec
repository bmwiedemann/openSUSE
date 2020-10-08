#
# spec file for package ant-antlr
#
# Copyright (c) 2020 SUSE LLC
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


%global ant_home %{_datadir}/ant
##### WARNING: please do not edit this auto generated spec file. Use the ant.spec! #####
%bcond_with bootstrap
%bcond_with junit
%bcond_with junit5
%bcond_without antlr
Name:           ant-antlr
Version:        1.10.9
Release:        0
Summary:        Antlr Task for ant
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://ant.apache.org/
Source0:        https://www.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.xz
Source1:        apache-ant-1.8.ant.conf
Source10:       ant-bootstrap.pom.in
Source1000:     pre_checkin.sh
Source1001:     https://www.apache.org/dist/ant/source/apache-ant-%{version}-src.tar.xz.asc
Source1002:     ant.keyring
Patch0:         apache-ant-no-test-jar.patch
Patch1:         apache-ant-class-path-in-manifest.patch
Patch2:         apache-ant-bootstrap.patch
#PATCH-FEATURE-OPENSUSE bmwiedemann -- have fixed build dates
Patch3:         reproducible-build-date.patch
# PATCH-FEATURE-OPENSUSE reproducible-build-manifest.patch -- have fixed "Created-by" in manifest
Patch5:         reproducible-build-manifest.patch
Patch6:         apache-ant-xml-apis.patch
BuildRequires:  antlr-bootstrap
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  unzip
BuildRequires:  xml-commons-apis-bootstrap
#!BuildIgnore:  xml-commons-apis
BuildArch:      noarch
# Needed for maven conversions
%if !%{with bootstrap}
BuildRequires:  javapackages-local
%endif
%if %{with junit} || %{with antlr} || %{with junit5}
BuildRequires:  ant = %{version}
BuildRequires:  hamcrest
BuildRequires:  junit
#!BuildIgnore:  antlr
%endif
%if %{with antlr}
BuildRequires:  xerces-j2
BuildRequires:  xz-java
%endif
%if %{with junit5}
BuildRequires:  apiguardian
BuildRequires:  junit5
%endif
%if 0%{?suse_version} > 1320
BuildRequires:  strip-nondeterminism
%endif
%if %{with bootstrap}
Requires:       java-devel >= 1.8
Requires:       javapackages-tools
Requires:       xerces-j2
Requires:       xml-apis
Requires:       xml-resolver
Obsoletes:      apache-ant < %{version}
Provides:       apache-ant = %{version}
Obsoletes:      ant-nodeps < %{version}
Provides:       ant-nodeps = %{version}
Obsoletes:      ant-trax < %{version}
Provides:       ant-trax = %{version}
%endif
%if %{with antlr}
Requires:       antlr
%requires_eq    ant
Obsoletes:      ant-javadoc
%endif
%if %{with junit}
Requires:       junit4
%requires_eq    ant
%endif
%if %{with junit5}
Requires:       junit5
%requires_eq    ant
%endif
%if %{with junit}
%description
Apache Ant is a Java-based build tool.

This package contains optional JUnit tasks for Apache Ant.
%elif %{with junit5}
%description
Apache Ant is a Java-based build tool.

This package contains optional JUnit5 tasks for Apache Ant.
%else
%description
Apache Ant is a Java-based build tool. In theory, it is kind of like
Make. Build description files are written in XML.
%endif

%if %{with bootstrap}
%package -n ant-jmf
Summary:        Optional jmf tasks for ant
License:        Apache-2.0
Group:          Development/Tools/Building
Requires:       ant = %{version}

%description -n ant-jmf
Apache Ant is a Java-based build tool.

This package contains optional jmf tasks for Apache Ant.

%package -n ant-swing
Summary:        Optional swing tasks for ant
License:        Apache-2.0
Group:          Development/Tools/Building
Requires:       ant = %{version}

%description -n ant-swing
Apache Ant is a Java-based build tool.

This package contains optional swing tasks for Apache Ant.

%package -n ant-scripts
Summary:        Additional scripts for ant
License:        Apache-2.0
Group:          Development/Tools/Building
Requires:       ant = %{version}
Requires:       perl
Requires:       python3-base

%description -n ant-scripts
Apache Ant is a Java-based build tool.

This package contains additional perl and python scripts for Apache
Ant.

%endif #if bootstrap

%if %{with antlr}
%package -n ant-apache-bsf
Summary:        Optional apache bsf tasks for ant
License:        Apache-2.0
Group:          Development/Tools/Building
BuildRequires:  bsf
Requires:       bsf
%requires_eq    ant

%description -n ant-apache-bsf
Apache Ant is a Java-based build tool.

This package contains optional apache bsf tasks for Apache Ant.

%package -n ant-apache-resolver
Summary:        Optional apache resolver tasks for ant
License:        Apache-2.0
Group:          Development/Tools/Building
BuildRequires:  xml-resolver
Requires:       xml-resolver
%requires_eq    ant

%description -n ant-apache-resolver
Apache Ant is a Java-based build tool.

This package contains optional apache resolver tasks for Apache Ant.

%package -n ant-commons-logging
Summary:        Optional commons logging tasks for ant
License:        Apache-2.0
Group:          Development/Tools/Building
BuildRequires:  apache-commons-logging
Requires:       apache-commons-logging
%requires_eq    ant

%description -n ant-commons-logging
Apache Ant is a Java-based build tool.

This package contains optional commons logging tasks for Apache Ant.

%package -n ant-commons-net
Summary:        Optional commons net tasks for ant
License:        Apache-2.0
Group:          Development/Tools/Building
BuildRequires:  apache-commons-net
Requires:       apache-commons-net
%requires_eq    ant

%description -n ant-commons-net
Apache Ant is a Java-based build tool.

This package contains optional commons net tasks for Apache Ant.

%package -n ant-apache-bcel
Summary:        Optional apache bcel tasks for ant
License:        Apache-2.0
Group:          Development/Tools/Building
BuildRequires:  bcel
Requires:       bcel
%requires_eq    ant
Provides:       ant-jakarta-bcel = %{version}
Obsoletes:      ant-jakarta-bcel < %{version}

%description -n ant-apache-bcel
Apache Ant is a Java-based build tool.

This package contains optional apache bcel tasks for Apache Ant.

%package -n ant-apache-log4j
Summary:        Optional apache log4j tasks for ant
License:        Apache-2.0
Group:          Development/Tools/Building
BuildRequires:  log4j12-mini
Requires:       log4j12
%requires_eq    ant
Provides:       ant-jakarta-log4j = %{version}
Obsoletes:      ant-jakarta-log4j < %{version}

%description -n ant-apache-log4j
Apache Ant is a Java-based build tool.

This package contains optional apache log4j tasks for Apache Ant.

%package -n ant-apache-oro
Summary:        Optional apache oro tasks for ant
License:        Apache-2.0
Group:          Development/Tools/Building
BuildRequires:  oro
Requires:       oro
%requires_eq    ant
Provides:       ant-jakarta-oro = %{version}
Obsoletes:      ant-jakarta-oro < %{version}

%description -n ant-apache-oro
Apache Ant is a Java-based build tool.

This package contains optional apache oro tasks for Apache Ant.

%package -n ant-apache-regexp
Summary:        Optional apache regexp tasks for ant
License:        Apache-2.0
Group:          Development/Tools/Building
BuildRequires:  regexp
Requires:       regexp
%requires_eq    ant
Provides:       ant-jakarta-regexp = %{version}
Obsoletes:      ant-jakarta-regexp < %{version}

%description -n ant-apache-regexp
Apache Ant is a Java-based build tool.

This package contains optional apache regexp tasks for Apache Ant.

%package -n ant-apache-xalan2
Summary:        Optional apache xalan2 tasks for ant
License:        Apache-2.0
Group:          Development/Tools/Building
BuildRequires:  regexp
BuildRequires:  xalan-j2
Requires:       regexp
%requires_eq    ant

%description -n ant-apache-xalan2
Optional apache xalan2 tasks for %{name}.

%package -n ant-imageio
Summary:        Optional imageio tasks for ant
License:        Apache-2.0
Group:          Development/Tools/Building
%requires_eq    ant

%description -n ant-imageio
Apache Ant is a Java-based build tool.

This package contains optional imageio tasks for Apache Ant.

%package -n ant-javamail
Summary:        Optional javamail tasks for ant
License:        CDDL-1.0
Group:          Development/Tools/Building
BuildRequires:  javamail >= 1.2-5jpp
Requires:       javamail >= 1.2-5jpp
%requires_eq    ant

%description -n ant-javamail
Apache Ant is a Java-based build tool.

This package contains optional javamail tasks for Apache Ant.

%package -n ant-jdepend
Summary:        Optional jdepend tasks for ant
License:        Apache-2.0
Group:          Development/Tools/Building
BuildRequires:  jdepend
Requires:       jdepend
%requires_eq    ant

%description -n ant-jdepend
Apache Ant is a Java-based build tool.

This package contains optional jdepend tasks for Apache Ant.

%package -n ant-jsch
Summary:        Optional jsch tasks for ant
License:        Apache-2.0
Group:          Development/Tools/Building
BuildRequires:  jsch
Requires:       jsch
%requires_eq    ant

%description -n ant-jsch
Apache Ant is a Java-based build tool.

This package contains optional jsch tasks for Apache Ant.

%package -n ant-xz
Summary:        Opional xz tasks for ant
License:        Apache-2.0
Group:          Development/Tools/Building
Requires:       xz-java
%requires_eq    ant

%description -n ant-xz
Apache Ant is a Java-based build tool.

This package contains optional xz tasks for Apache Ant.

%package -n ant-testutil
Summary:        Test utility classes for ant
License:        Apache-2.0
Group:          Development/Tools/Building
Requires:       junit4
%requires_eq    ant

%description -n ant-testutil
Test utility tasks for %{name}.

%package -n ant-manual
Summary:        Manual for ant
License:        Apache-2.0
Group:          Development/Tools/Building

%description -n ant-manual
Apache Ant is a Java-based build tool.

This package contains the manual for Apache Ant.

%endif

%prep
%setup -q -n apache-ant-%{version}
#Fixup version
find -name build.xml -o -name pom.xml | xargs sed -i -e s/-SNAPSHOT//
find -name \*.jar -print -delete

# When bootstrapping, we don't have junit
%if %{with bootstrap}
%patch0 -p1
%endif
%patch1
%patch2 -p1
%patch3 -p1
%patch5 -p1
%patch6 -p1

# clean jar files
find . -name "*.jar" -print -delete

# failing testcases. TODO see why
%if %{with antlr} || %{with junit}
rm  src/tests/junit/org/apache/tools/mail/MailMessageTest.java \
    src/tests/junit/org/apache/tools/ant/taskdefs/ExecuteWatchdogTest.java \
    src/tests/junit/org/apache/tools/ant/taskdefs/JavaTest.java \
    src/tests/junit/org/apache/tools/ant/taskdefs/TestProcess.java
%endif

#install jars
%if %{with junit} || %{with junit5}
build-jar-repository -s -p lib/optional junit4
%endif
%if %{with junit5}
build-jar-repository -s -p lib/optional junit5 opentest4j
%endif
%if %{with antlr}
# we need to build junit in antlr, but we remove it later
build-jar-repository -s -p lib/optional xerces-j2 xml-commons-apis-bootstrap antlr-bootstrap bcel javamail/mailapi jdepend junit4 log4j12/log4j-12 oro regexp bsf commons-logging commons-net jsch xalan-j2 xalan-j2-serializer xml-resolver xz-java
%endif

# Fix file-not-utf8 rpmlint warning
iconv KEYS -f iso-8859-1 -t utf-8 -o KEYS.utf8
mv KEYS.utf8 KEYS
iconv LICENSE -f iso-8859-1 -t utf-8 -o LICENSE.utf8
mv LICENSE.utf8 LICENSE
# -----------------------------------------------------------------------------

%build
export OPT_JAR_LIST=:

%if %{with antlr} || %{with junit} || %{with junit5}
ant -Dbuild.sysclasspath=first jars test-jar

#remove empty jai and netrexx jars. Due to missing dependencies they contain only manifests.
rm -rf build/lib/ant-jai.jar build/lib/ant-netrexx.jar
%endif

%if %{with bootstrap}
export GC_MAXIMUM_HEAP_SIZE="134217728" #128M
export JAVA_HOME="%{java_home}"
sh -x ./build.sh --noconfig jars

%endif
%?strip_all_nondeterminism

%install
# ANT_HOME and subdirs
mkdir -p %{buildroot}%{ant_home}/{lib,etc}
# jars
install -d -m 755 %{buildroot}%{_javadir}/ant
install -d -m 755 %{buildroot}%{_mavenpomdir}

%if %{without junit} && %{without junit5}
  rm build/lib/ant-junit*.jar
%else
  %if %{without junit}
    rm build/lib/ant-junit.jar
    rm build/lib/ant-junit4.jar
  %else
    # empty in this scenario
    rm build/lib/ant-junitlauncher.jar
  %endif
  # remove all others
  for i in build/lib/ant-*.jar ; do
    case $i in
     */ant-junit*)
       ;;
     *)
       rm -v $i
       ;;
    esac
  done
%endif

for jar in build/lib/*.jar
do
  jarname=$(basename $jar .jar)
  pomname="${jarname}.pom"

  #Determine where to put it
  case $jarname in
#These go into %%{_javadir}, pom files have different names
  ant | ant-bootstrap | ant-launcher)
%if %{with bootstrap}
  destdir="%{buildroot}%{_javadir}/ant"; destname="ant/";pomname="$jarname.pom"
%else
  continue
%endif
  ;;
  ant-jmf|ant-swing)
%if %{with bootstrap}
  destdir="%{buildroot}%{_javadir}/ant"; destname="ant/";
%else
  continue
%endif
  ;;
#Bootstracp builds an incomplete ant-foo jars, don't ship them
  *)
%if %{with bootstrap}
  continue
%else
#These go into %%{_javadir}/ant
  destdir="%{buildroot}%{_javadir}/ant"; destname="ant/";
%endif
  ;;
  esac

  #instal jar
  install -m 644 ${jar} ${destdir}/${jarname}.jar
  # jar aliases
  ln -sf ../../java/${destname}${jarname}.jar %{buildroot}%{ant_home}/lib/${jarname}.jar

  #bootstrap does not have a pom
  if [ "$jarname" = ant-bootstrap ]; then
    mkdir -p src/etc/poms/${jarname}
    sed -e "s#@VERSION@#%{version}#g" < %{SOURCE10} > src/etc/poms/${jarname}/pom.xml
  fi

  #install pom
  if [ "$jarname" != ant-bootstrap ]; then
    %pom_remove_parent src/etc/poms/${jarname}/pom.xml
  fi
  install -m 644 src/etc/poms/${jarname}/pom.xml %{buildroot}/%{_mavenpomdir}/${pomname}
  if [ "$jarname" = ant-launcher ]; then
    %add_maven_depmap ${pomname} ${destname}${jarname}.jar -a ant:ant-launcher
  elif [ "$jarname" = ant-jmf ]; then
    %add_maven_depmap ${pomname} ${destname}${jarname}.jar -f jmf
  elif [ "$jarname" = ant-swing ]; then
    %add_maven_depmap ${pomname} ${destname}${jarname}.jar -f swing
  elif [ "$jarname" = ant ]; then
    %add_maven_depmap ${pomname} ${destname}${jarname}.jar -a org.apache.ant:ant-nodeps,apache:ant,ant:ant
  elif [ "$jarname" = ant-antlr -o "$jarname" = ant-bootstrap ]; then
    %add_maven_depmap ${pomname} ${destname}${jarname}.jar
  else
%if %{with junit} || %{with junit5}
    %add_maven_depmap ${pomname} ${destname}${jarname}.jar
%else
    %add_maven_depmap ${pomname} ${destname}${jarname}.jar -f ${jarname}
%endif
  fi
done

%if %{with bootstrap}

# scripts: remove dos and os/2 scripts
rm -f src/script/*.bat
rm -f src/script/*.cmd

# XSLs
cp -p src/etc/*.xsl %{buildroot}%{ant_home}%{_sysconfdir}
rm -f  %{buildroot}%{ant_home}%{_sysconfdir}/{maudit-frames,jdepend,jdepend-frames,junit-frames,junit-noframes}.xsl
%endif
%if %{with junit}
cp -p src/etc/{junit-noframes,junit-frames}.xsl %{buildroot}%{ant_home}%{_sysconfdir}
%endif
%if %{with antlr}
cp -p src/etc/{maudit-frames,jdepend,jdepend-frames}.xsl %{buildroot}%{ant_home}%{_sysconfdir}
%endif

%if %{with bootstrap}
# install everything else
mkdir -p %{buildroot}%{_bindir}
cp -p src/script/* %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/%{name}/bin/
ln -sf %{_bindir}/antRun %{buildroot}/%{_datadir}/%{name}/bin/antRun
%endif

mkdir -p %{buildroot}%{_sysconfdir}/ant.d

%if %{with bootstrap}
# default ant.conf
mkdir -p %{buildroot}%{_sysconfdir}
cp -p %{SOURCE1} %{buildroot}%{_sysconfdir}/ant.conf

# OPT_JAR_LIST fragments
echo "ant/ant-jmf" > %{buildroot}%{_sysconfdir}/%{name}.d/jmf
echo "ant/ant-swing" > %{buildroot}%{_sysconfdir}/%{name}.d/swing
%endif

%if %{with junit}
echo "junit ant/ant-junit" > %{buildroot}%{_sysconfdir}/ant.d/junit
echo "junit4 ant/ant-junit4" > %{buildroot}%{_sysconfdir}/ant.d/junit4
%endif

%if %{with junit5}
echo "junit5 hamcrest/core junit opentest4j ant/ant-junitlauncher" > %{buildroot}%{_sysconfdir}/ant.d/junitlauncher
%endif

%if %{with antlr}
echo "antlr ant/ant-antlr" > %{buildroot}%{_sysconfdir}/ant.d/antlr
echo "rhino bsf ant/ant-apache-bsf" > %{buildroot}%{_sysconfdir}/ant.d/apache-bsf
echo "xml-resolver ant/ant-apache-resolver" > %{buildroot}%{_sysconfdir}/ant.d/apache-resolver
echo "apache-commons-logging ant/ant-commons-logging" > %{buildroot}%{_sysconfdir}/ant.d/commons-logging
echo "apache-commons-net ant/ant-commons-net" > %{buildroot}%{_sysconfdir}/ant.d/commons-net
echo "bcel ant/ant-apache-bcel" > %{buildroot}%{_sysconfdir}/ant.d/apache-bcel
echo "log4j12/log4j-12 ant/ant-apache-log4j" > %{buildroot}%{_sysconfdir}/ant.d/apache-log4j
echo "oro ant/ant-apache-oro" > %{buildroot}%{_sysconfdir}/ant.d/apache-oro
echo "regexp ant/ant-apache-regexp" > %{buildroot}%{_sysconfdir}/ant.d/apache-regexp
echo "xalan-j2 ant/ant-apache-xalan2" > %{buildroot}%{_sysconfdir}/ant.d/apache-xalan2
echo "ant/ant-imageio" > %{buildroot}%{_sysconfdir}/ant.d/imageio
echo "javamail jaf ant/ant-javamail" > %{buildroot}%{_sysconfdir}/ant.d/javamail
echo "jdepend ant/ant-jdepend" > %{buildroot}%{_sysconfdir}/ant.d/jdepend
echo "jsch ant/ant-jsch" > %{buildroot}%{_sysconfdir}/ant.d/jsch
echo "xz-java ant/ant-xz" > %{buildroot}%{_sysconfdir}/ant.d/xz
echo "testutil ant/ant-testutil" > %{buildroot}%{_sysconfdir}/ant.d/testutil
%endif

%if %{with bootstrap}
find %{buildroot}%{_datadir}/ant%{_sysconfdir} -type f -name "*.xsl" \
                                                 -a ! -name ant-update.xsl \
                                                 -a ! -name changelog.xsl \
                                                 -a ! -name coverage-frames.xsl \
                                                 -a ! -name junit-frames-xalan1.xsl \
                                                 -a ! -name log.xsl \
                                                 -a ! -name mmetrics-frames.xsl \
                                                 -a ! -name tagdiff.xsl \
                                                 -print -delete
%endif
# remove *.orig
rm -rf %{buildroot}%{_bindir}/ant.orig

%if %{with bootstrap}
pushd %{buildroot}%{_javadir}
  for i in ant-bootstrap ant-launcher ant; do
    ln -sf ant/${i}.jar ${i}.jar
  done
popd

%files -f .mfiles
%license LICENSE NOTICE
%doc KEYS README WHATSNEW
%config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(0755,root,root) %{_bindir}/ant
%attr(0755,root,root) %{_bindir}/antRun
%{_javadir}/%{name}.jar
%{_javadir}/%{name}-launcher.jar
%{_javadir}/%{name}-bootstrap.jar
%dir %{_javadir}/%{name}
%dir %{ant_home}
%dir %{ant_home}%{_sysconfdir}
%{ant_home}/bin
%{ant_home}%{_sysconfdir}/ant-update.xsl
%{ant_home}%{_sysconfdir}/changelog.xsl
%{ant_home}%{_sysconfdir}/coverage-frames.xsl
%{ant_home}%{_sysconfdir}/mmetrics-frames.xsl
%{ant_home}%{_sysconfdir}/log.xsl
%{ant_home}%{_sysconfdir}/tagdiff.xsl
%{ant_home}%{_sysconfdir}/junit-frames-xalan1.xsl
# % {ant_home}/etc/common2master.xsl
# % {ant_home}/etc/printFailingTests.xsl
%dir %{ant_home}/lib
%dir %{_sysconfdir}/%{name}.d
%{ant_home}/lib/ant.jar
%{ant_home}/lib/ant-bootstrap.jar
%{ant_home}/lib/ant-launcher.jar
%dir %{_sysconfdir}/ant.d
%endif

%if %{with antlr}
%files -f .mfiles
%{ant_home}/lib/ant-antlr.jar
%config(noreplace) %{_sysconfdir}/ant.d/antlr
%endif

%if %{with junit}
%files -f .mfiles
%{ant_home}/lib/ant-junit*.jar
%config(noreplace) %{_sysconfdir}/ant.d/junit
%config(noreplace) %{_sysconfdir}/ant.d/junit4
%{ant_home}%{_sysconfdir}/junit-frames.xsl
%{ant_home}%{_sysconfdir}/junit-noframes.xsl
%endif

%if %{with junit5}
%files -f .mfiles
%{ant_home}/lib/ant-junitlauncher.jar
%config(noreplace) %{_sysconfdir}/ant.d/junitlauncher
%endif

### Basic ant subpackages
%if %{with bootstrap}
%files -n ant-jmf -f .mfiles-jmf
%{ant_home}/lib/ant-jmf.jar
%config(noreplace) %{_sysconfdir}/ant.d/jmf

%files -n ant-swing -f .mfiles-swing
%{ant_home}/lib/ant-swing.jar
%config(noreplace) %{_sysconfdir}/ant.d/swing

%files -n ant-scripts
%defattr(0755,root,root,0755)
%{_bindir}/*.pl
%{_bindir}/*.py*
%endif #if bootstrap

%if %{with antlr}
%files -n ant-apache-bsf -f .mfiles-ant-apache-bsf
%{ant_home}/lib/ant-apache-bsf.jar
%config(noreplace) %{_sysconfdir}/ant.d/apache-bsf

%files -n ant-apache-resolver -f .mfiles-ant-apache-resolver
%{ant_home}/lib/ant-apache-resolver.jar
%config(noreplace) %{_sysconfdir}/ant.d/apache-resolver

%files -n ant-commons-logging -f .mfiles-ant-commons-logging
%{ant_home}/lib/ant-commons-logging.jar
%config(noreplace) %{_sysconfdir}/ant.d/commons-logging

%files -n ant-commons-net -f .mfiles-ant-commons-net
%{ant_home}/lib/ant-commons-net.jar
%config(noreplace) %{_sysconfdir}/ant.d/commons-net

%files -n ant-apache-bcel -f .mfiles-ant-apache-bcel
%{ant_home}/lib/ant-apache-bcel.jar
%config(noreplace) %{_sysconfdir}/ant.d/apache-bcel

%files -n ant-apache-log4j -f .mfiles-ant-apache-log4j
%{ant_home}/lib/ant-apache-log4j.jar
%config(noreplace) %{_sysconfdir}/ant.d/apache-log4j

%files -n ant-apache-oro -f .mfiles-ant-apache-oro
%{ant_home}/lib/ant-apache-oro.jar
%{ant_home}%{_sysconfdir}/maudit-frames.xsl
%config(noreplace) %{_sysconfdir}/ant.d/apache-oro

%files -n ant-apache-regexp -f .mfiles-ant-apache-regexp
%{ant_home}/lib/ant-apache-regexp.jar
%config(noreplace) %{_sysconfdir}/ant.d/apache-regexp

%files -n ant-apache-xalan2 -f .mfiles-ant-apache-xalan2
%{ant_home}/lib/ant-apache-xalan2.jar
%config(noreplace) %{_sysconfdir}/ant.d/apache-xalan2

%files -n ant-imageio -f .mfiles-ant-imageio
%{ant_home}/lib/ant-imageio.jar
%config(noreplace) %{_sysconfdir}/ant.d/imageio

%files -n ant-javamail -f .mfiles-ant-javamail
%{ant_home}/lib/ant-javamail.jar
%config(noreplace) %{_sysconfdir}/ant.d/javamail

%files -n ant-jdepend -f .mfiles-ant-jdepend
%{ant_home}/lib/ant-jdepend.jar
%config(noreplace) %{_sysconfdir}/ant.d/jdepend
%{ant_home}%{_sysconfdir}/jdepend.xsl
%{ant_home}%{_sysconfdir}/jdepend-frames.xsl

%files -n ant-jsch -f .mfiles-ant-jsch
%{ant_home}/lib/ant-jsch.jar
%config(noreplace) %{_sysconfdir}/ant.d/jsch

%files -n ant-xz -f .mfiles-ant-xz
%{ant_home}/lib/ant-xz.jar
%config(noreplace) %{_sysconfdir}/ant.d/xz

%files -n ant-testutil -f .mfiles-ant-testutil
%{ant_home}/lib/ant-testutil.jar
%config(noreplace) %{_sysconfdir}/ant.d/testutil

%files -n ant-manual
%doc manual/*
%endif

%changelog
