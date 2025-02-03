#
# spec file for package apache-ivy
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without  httpclient
%bcond_without  oro
%bcond_without  sftp
%bcond_without  vfs
%bcond_with pack200
Name:           apache-ivy
Version:        2.5.3
Release:        0
Summary:        Java-based dependency manager
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://ant.apache.org/ivy/
Source0:        https://archive.apache.org/dist/ant/ivy/%{version}/%{name}-%{version}-src.tar.gz
Source1:        ivy.1
Source2:        https://repo1.maven.org/maven2/org/apache/ivy/ivy/%{version}/ivy-%{version}.pom
Patch0:         apache-ivy-global-settings.patch
Patch1:         apache-ivy-publication-date.patch
Patch2:         apache-ivy-pack200.patch
BuildRequires:  ant
BuildRequires:  bouncycastle-pg
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  jsch
BuildRequires:  oro
Provides:       ivy = %{version}-%{release}
Obsoletes:      ivy < %{version}-%{release}
BuildArch:      noarch
%if %{with pack200}
BuildRequires:  pack200
%else
BuildConflicts: java >= 14
BuildConflicts: java-devel >= 14
BuildConflicts: java-headless >= 14
%endif
%if %{with vfs}
BuildRequires:  apache-commons-vfs2
%endif
%if %{with sftp}
BuildRequires:  jsch-agent-proxy-connector-factory
BuildRequires:  jsch-agent-proxy-core
BuildRequires:  jsch-agent-proxy-jsch
%endif
%if %{with httpclient}
BuildRequires:  httpcomponents-client
%endif
%if %{with oro}
BuildRequires:  oro
%endif

%description
Apache Ivy is a tool for managing (recording, tracking, resolving and
reporting) project dependencies.  It is designed as process agnostic and is
not tied to any methodology or structure. while available as a standalone
tool, Apache Ivy works particularly well with Apache Ant providing a number
of powerful Ant tasks ranging from dependency resolution to dependency
reporting and publication.

%package javadoc
Summary:        API Documentation for ivy
Group:          Documentation/HTML

%description javadoc
JavaDoc documentation for %{name}

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1

cp %{SOURCE2} pom.xml

%pom_remove_dep :jsch.agentproxy

%if %{without httpclient}
%pom_remove_dep :httpclient
rm src/java/org/apache/ivy/util/url/HttpClientHandler.java
%endif

%if %{without oro}
%pom_remove_dep :oro
rm src/java/org/apache/ivy/plugins/matcher/GlobPatternMatcher.java
%endif

%if %{without vfs}
%pom_remove_dep :commons-vfs2
rm src/java/org/apache/ivy/plugins/repository/vfs/VfsRepository.java
rm src/java/org/apache/ivy/plugins/repository/vfs/VfsResource.java
rm src/java/org/apache/ivy/plugins/repository/vfs/ivy_vfs.xml
rm src/java/org/apache/ivy/plugins/resolver/VfsResolver.java
%endif

%if %{without sftp}
%pom_remove_dep :jsch
%pom_remove_dep :jsch.agentproxy.connector-factory
%pom_remove_dep :jsch.agentproxy.jsch
rm src/java/org/apache/ivy/plugins/repository/sftp/SFTPRepository.java
rm src/java/org/apache/ivy/plugins/repository/sftp/SFTPResource.java
rm src/java/org/apache/ivy/plugins/repository/ssh/AbstractSshBasedRepository.java
rm src/java/org/apache/ivy/plugins/repository/ssh/RemoteScpException.java
rm src/java/org/apache/ivy/plugins/repository/ssh/Scp.java
rm src/java/org/apache/ivy/plugins/repository/ssh/SshCache.java
rm src/java/org/apache/ivy/plugins/repository/ssh/SshRepository.java
rm src/java/org/apache/ivy/plugins/repository/ssh/SshResource.java
rm src/java/org/apache/ivy/plugins/resolver/AbstractSshBasedResolver.java
rm src/java/org/apache/ivy/plugins/resolver/SFTPResolver.java
rm src/java/org/apache/ivy/plugins/resolver/SshResolver.java
%endif

%if %{with pack200}
%pom_add_dep io.pack200:pack200:14:provided
%patch -P 2 -p1
%endif

%build
# Craft class path
mkdir -p lib
build-jar-repository -s lib ant ant/ant-nodeps jsch bcprov bcpg
export CLASSPATH=$(build-classpath ant ant/ant-nodeps jsch httpcomponents bcprov bcpg)
%if %{with httpclient}
build-jar-repository -s lib httpcomponents
export CLASSPATH=${CLASSPATH}:$(build-classpath httpcomponents)
%endif
%if %{with oro}
build-jar-repository -s lib oro
export CLASSPATH=${CLASSPATH}:$(build-classpath oro)
%endif
%if %{with vfs}
build-jar-repository -s lib commons-vfs2
export CLASSPATH=${CLASSPATH}:$(build-classpath commons-vfs2)
%endif
%if %{with sftp}
build-jar-repository -s lib jsch.agentproxy.core \
                         jsch.agentproxy.connector-factory \
                         jsch.agentproxy.jsch
export CLASSPATH=${CLASSPATH}:$(build-classpath jsch.agentproxy.core jsch.agentproxy.connector-factory jsch.agentproxy.jsch)
%endif
%if %{with pack200}
build-jar-repository -s lib pack200
export CLASSPATH=${CLASSPATH}:$(build-classpath pack200)
%endif

# Build
%{ant} -v -Dtarget.ivy.version=%{version} -Dbundle.version=%{version} /localivy /offline jar javadoc

%install
# Code
install -d %{buildroot}%{_javadir}/%{name}
install -p -m644 build/artifact/jars/ivy.jar %{buildroot}%{_javadir}/ivy.jar
ln -sf ../ivy.jar %{buildroot}%{_javadir}/%{name}/ivy.jar

install -d -m 0755 %{buildroot}/%{_mavenpomdir}/
%{mvn_install_pom} pom.xml %{buildroot}/%{_mavenpomdir}/JPP-ivy.pom
# Maven depmap
%add_maven_depmap JPP-ivy.pom ivy.jar

# API Documentation
install -d %{buildroot}%{_javadocdir}/%{name}
cp -rp build/reports/api/. %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# Command line script
MAIN_CLASS=`sed -rn 's/^Main-Class: (.*)$/\1/gp' META-INF/MANIFEST.MF | tr -d '\r'`
%jpackage_script "${MAIN_CLASS}" "" "" ant:ant/ant-nodeps:ivy:oro:jsch:commons-httpclient ivy

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ivy" > %{buildroot}%{_sysconfdir}/ant.d/%{name}

# Man page
install -d %{buildroot}%{_mandir}/man1
install %{SOURCE1} %{buildroot}%{_mandir}/man1/ivy.1

%files -f .mfiles
%license LICENSE NOTICE
%doc README.adoc
%config %{_sysconfdir}/ant.d/%{name}
%{_javadir}/%{name}
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_mandir}/man1/*

%files javadoc
%{_javadocdir}/*

%changelog
