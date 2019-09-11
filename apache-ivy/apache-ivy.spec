#
# spec file for package apache-ivy
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


%bcond_without  ssh
%bcond_without  vfs
Name:           apache-ivy
Version:        2.4.0
Release:        0
Summary:        Java-based dependency manager
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            http://ant.apache.org/ivy/
Source0:        %{name}-%{version}-src.tar.gz
Source1:        ivy.1
Source2:        http://repo1.maven.org/maven2/org/apache/ivy/ivy/%{version}/ivy-%{version}.pom
Patch0:         apache-ivy-2.4.0-jdk9.patch
Patch1:         apache-ivy-global-settings.patch
BuildRequires:  ant
BuildRequires:  bouncycastle
BuildRequires:  commons-httpclient
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  jsch
BuildRequires:  oro
Provides:       ivy = %{version}-%{release}
Obsoletes:      ivy < %{version}-%{release}
BuildArch:      noarch
%if %{with vfs}
BuildRequires:  apache-commons-vfs2
%endif
%if %{with ssh}
BuildRequires:  jsch-agent-proxy-connector-factory
BuildRequires:  jsch-agent-proxy-core
BuildRequires:  jsch-agent-proxy-jsch
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
%patch0 -p1
%patch1 -p1

cp %{SOURCE2} pom.xml

%pom_remove_parent .

#TODO: return back when bouncycastle-pgp will be available
rm -fr src/java/org/apache/ivy/plugins/signer/bouncycastle

# Remove prebuilt documentation
rm -rf doc build/doc

# Port from commons-vfs 1.x to 2.x
%if %{with vfs}
sed -i "s/commons.vfs/&2/" {src,test}/java/org/apache/ivy/plugins/repository/vfs/*
%else
sed -i /commons-vfs/d ivy.xml
sed '/vfs.*=.*org.apache.ivy.plugins.resolver.VfsResolver/d' -i \
        src/java/org/apache/ivy/core/settings/typedef.properties
rm -rf src/java/org/apache/ivy/plugins/repository/vfs
rm -rf src/java/org/apache/ivy/plugins/resolver/VfsResolver.java
%endif

%if %{without ssh}
rm -r src/java/org/apache/ivy/plugins/repository/{ssh,sftp}
rm src/java/org/apache/ivy/plugins/resolver/*{Ssh,SFTP}*.java
%endif

%build
# Craft class path
mkdir -p lib
build-jar-repository lib ant ant/ant-nodeps oro jsch commons-httpclient
export CLASSPATH=$(build-classpath ant ant/ant-nodeps oro jsch commons-httpclient)
%if %{with vfs}
build-jar-repository lib commons-vfs2
export CLASSPATH=${CLASSPATH}:$(build-classpath commons-vfs2)
%endif
%if %{with ssh}
build-jar-repository lib jsch.agentproxy.core \
                         jsch.agentproxy.connector-factory \
                         jsch.agentproxy.jsch
export CLASSPATH=${CLASSPATH}:$(build-classpath jsch.agentproxy.core jsch.agentproxy.connector-factory jsch.agentproxy.jsch)
%endif

# Build
ant -Dtarget.ivy.version=%{version} /localivy /offline jar javadoc

%install
# Code
install -d %{buildroot}%{_javadir}/%{name}
install -p -m644 build/artifact/jars/ivy.jar %{buildroot}%{_javadir}/ivy.jar
ln -sf ../ivy.jar %{buildroot}%{_javadir}/%{name}/ivy.jar

install -d -m 0755 %{buildroot}/%{_mavenpomdir}/
install -m 0644 pom.xml %{buildroot}/%{_mavenpomdir}/JPP-ivy.pom
# Maven depmap
%add_maven_depmap JPP-ivy.pom ivy.jar

# API Documentation
install -d %{buildroot}%{_javadocdir}/%{name}
cp -rp build/doc/reports/api/. %{buildroot}%{_javadocdir}/%{name}
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
%doc README
%config %{_sysconfdir}/ant.d/%{name}
%{_javadir}/%{name}
%attr(755,root,root) %{_bindir}/*
%attr(644,root,root) %{_mandir}/man1/*

%files javadoc
%{_javadocdir}/*

%changelog
