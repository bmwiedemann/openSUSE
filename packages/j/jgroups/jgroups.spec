#
# spec file for package jgroups
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


%define _with_repolib 1
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}
%define repodir %{_javadir}/repository.jboss.com/jgroups/2.4.1.SP4-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src
Name:           jgroups
Version:        2.6.10
Release:        0
Summary:        Toolkit for reliable multicast communication
License:        LGPL-2.0-or-later
Group:          Development/Libraries/Java
Url:            http://www.jgroups.org/
# get source zip from sf.net
# unzip -q JGroups-2.6.10.merge.src.zip
# find JGroups-2.6.10.merge.src/ -iname *.jar | xargs rm -rf
# ## bnc#509439
# cd JGroups-2.6.10.merge.src
# rm -rf doc/
# cvs -d:pserver:anonymous@javagroups.cvs.sourceforge.net:/cvsroot/javagroups login
# cvs -z3 -d:pserver:anonymous@javagroups.cvs.sourceforge.net:/cvsroot/javagroups co -P JGroups/doc
# mv JGroups/doc doc/
# rm -rf JGroups
# cd ..
# tar --exclude-vcs -cjf JGroups-2.6.10.merge.src.tar.bz2 JGroups-2.6.10.merge.src/
Source0:        JGroups-%{version}.merge.src.tar.bz2
Source1:        jgroups-component-info.xml
#PATCH-FIX-OPENSUSE: junit.swingui does not exists in junit 4
Patch0:         jgroups-swingui.patch
#PATCH-FIX-OPENSUSE: don't hardcode source so that it can be specified from command-line
Patch1:         jgroups-nosource.patch
BuildRequires:  ant >= 1.6
BuildRequires:  ant-junit
BuildRequires:  apache-commons-logging
BuildRequires:  bsh2
BuildRequires:  fdupes
BuildRequires:  geronimo-jms-1_1-api
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  jaxp_parser_impl
BuildRequires:  junit
BuildRequires:  log4j
BuildRequires:  mx4j
BuildRequires:  xalan-j2
# To use JGroups one needs:
Requires:       apache-commons-logging
Requires:       bsh2
Requires:       geronimo-jms-1_1-api
Requires:       jaxp_parser_impl
Requires:       log4j
Provides:       javagroups = %{version}
Obsoletes:      javagroups < %{version}
BuildArch:      noarch

%description
JGroups is a toolkit for reliable multicast communication. (Note that
this doesn't necessarily mean IP Multicast, JGroups can also use
transports such as TCP). It can be used to create groups of processes
whose members can send messages to each other. The main features include

    * Group creation and deletion. Group members can be spread across
      LANs or WANs
    * Joining and leaving of groups
    * Membership detection and notification about joined/left/crashed members
    * Detection and removal of crashed members
    * Sending and receiving of member-to-group messages (point-to-multipoint)
    * Sending and receiving of member-to-member messages (point-to-point)

To use JGroups one needs:
 commons-logging.jar
 log4j.jar

To run JGroups you need to have an XML parser installed on your system.
If you use JDK 1.4 or higher, you can use the parser that is shipped with it.

If you want to use the JGroups JMS protocol ( org.jgroups.protocols.JMS ),
then you will also need to place jms.jar somewhere in your CLASSPATH.

Place the JAR files somewhere in your CLASSPATH , and you're ready to start
using JGroups.

%if %{with_repolib}
%package repolib
Summary:        Artifacts to be uploaded to a repository library
Group:          Development/Libraries/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio
%endif

%package javadoc
Summary:        Javadoc for jgroups
Group:          Development/Libraries/Java

%description javadoc
JGroups is a toolkit for reliable multicast communication. (Note that
this doesn't necessarily mean IP Multicast, JGroups can also use
transports such as TCP). It can be used to create groups of processes
whose members can send messages to each other. The main features include

    * Group creation and deletion. Group members can be spread across
      LANs or WANs
    * Joining and leaving of groups
    * Membership detection and notification about joined/left/crashed members
    * Detection and removal of crashed members
    * Sending and receiving of member-to-group messages (point-to-multipoint)
    * Sending and receiving of member-to-member messages (point-to-point)

%package manual
Summary:        Manual for jgroups
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description manual
JGroups is a toolkit for reliable multicast communication. (Note that
this doesn't necessarily mean IP Multicast, JGroups can also use
transports such as TCP). It can be used to create groups of processes
whose members can send messages to each other. The main features include

    * Group creation and deletion. Group members can be spread across
      LANs or WANs
    * Joining and leaving of groups
    * Membership detection and notification about joined/left/crashed members
    * Detection and removal of crashed members
    * Sending and receiving of member-to-group messages (point-to-multipoint)
    * Sending and receiving of member-to-member messages (point-to-point)

%prep
%setup -q -n JGroups-%{version}.merge.src
%patch0 -p1
%patch1 -p1
find . -type f -name '*.jar' | xargs rm -f
# this test requires bouncycastle
rm tests/junit/org/jgroups/protocols/ENCRYPTAsymmetricTest.java
%if %{with_repolib}
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/tag=\".*\">/tag=\"$tag\">/g" %{SOURCE1}
%endif

%build
export CLASSPATH=
export OPT_JAR_LIST="ant-launcher ant/ant-junit ant/ant-trax junit xalan-j2 xalan-j2-serializer"
pushd lib
ln -sf $(build-classpath ant) .
ln -sf $(build-classpath ant-launcher) .
ln -sf $(build-classpath ant/ant-junit) .
#BUILD/JGroups-2.4.1.src/lib/bcprov-jdk14-117.jar.no
ln -sf $(build-classpath bsh2/bsh) .
ln -sf $(build-classpath commons-logging) .
ln -sf $(build-classpath geronimo-jms-1.1-api) .
ln -sf $(build-classpath junit) .
ln -sf $(build-classpath log4j) .
ln -sf $(build-classpath mx4j/mx4j-jmx) .
ln -sf $(build-classpath xalan-j2) .
ln -sf $(build-classpath xalan-j2-serializer) .
popd
ant -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 jar javadoc gossip-service jgroups-service

%install
# jar
install -d %{buildroot}%{_javadir}
install -m 644 dist/%{name}-all.jar \
  %{buildroot}%{_javadir}/%{name}-%{version}.jar
install -m 644 dist/%{name}-core.jar \
        %{buildroot}%{_javadir}/%{name}-core-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
# javadoc
install -d %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}/
%fdupes -s %{buildroot}%{_javadocdir}/%{name}-%{version}
(cd %{buildroot}%{_javadocdir} && ln -sf %{name}-%{version} %{name})
# services
install -p -d -m 755 %{buildroot}%{_datadir}/%{name}-%{version}
install -m 644 dist/%{name}*.sar \
        %{buildroot}%{_datadir}/%{name}-%{version}
# docs
install -p -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr doc/* %{buildroot}%{_docdir}/%{name}-%{version}
%if %{with_repolib}
	install -d -m 755 %{buildroot}%{repodir}
	install -d -m 755 %{buildroot}%{repodirlib}
	install -m 755 %{SOURCE1} %{buildroot}%{repodir}/component-info.xml
	install -d -m 755 %{buildroot}%{repodirsrc}
	install -m 755 %{SOURCE0} %{buildroot}%{repodirsrc}
	cp -p %{buildroot}%{_javadir}/jgroups.jar %{buildroot}%{repodirlib}
%endif

%files
%doc CREDITS INSTALL.html README LICENSE
%{_javadir}/%{name}*jar
%{_datadir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files manual
%doc %{_docdir}/%{name}-%{version}
%if %{with_repolib}
%files repolib
%{repodir}
%dir %{_javadir}/repository.jboss.com
%dir %{_javadir}/repository.jboss.com/%{name}
%endif

%changelog
