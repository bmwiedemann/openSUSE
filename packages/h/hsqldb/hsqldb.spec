#
# spec file for package hsqldb
#
# Copyright (c) 2020 SUSE LLC
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           hsqldb
Version:        2.4.1
Release:        0
Summary:        HyperSQL Database Engine
License:        BSD-3-Clause
Group:          Productivity/Databases/Servers
URL:            http://hsqldb.org/
Source0:        http://downloads.sourceforge.net/hsqldb/%{name}-%{version}.zip
Source1:        hsqldb-1.8.0-standard.cfg
Source2:        hsqldb-1.8.0-standard-server.properties
Source3:        hsqldb-1.8.0-standard-webserver.properties
Source4:        hsqldb-1.8.0-standard-sqltool.rc
Source5:        http://www.hsqldb.org/repos/org/hsqldb/hsqldb/%{version}/hsqldb-%{version}.pom
# Custom systemd files - talking with upstream about incorporating them, see
# http://sourceforge.net/projects/hsqldb/forums/forum/73673/topic/5367103
Source6:        hsqldb.systemd
Source7:        hsqldb-wrapper
Source8:        hsqldb-post
Source9:        hsqldb-stop
# Javadoc fails to create since apidocs folder is deleted and not recreated
Patch0:         %{name}-apidocs.patch
# Package org.hsqldb.cmdline was only compiled with java 1.5
Patch1:         %{name}-cmdline.patch
# Jdk10's javadoc ends up in error when a remote url cannot be reached
Patch2:         hsqldb-2.4.1-javadoc10.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  glassfish-servlet-api
BuildRequires:  java-devel >= 1.8
# Needed for maven conversions
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  servletapi5
BuildRequires:  unzip
BuildRequires:  pkgconfig(systemd)
Requires:       java >= 1.8
Requires:       servletapi5
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%systemd_requires

%description
HSQLdb is a relational database engine written in JavaTM , with a JDBC
driver, supporting a subset of ANSI-92 SQL. It offers a small (about
100k), fast database engine which offers both in memory and disk based
tables. Embedded and server modes are available. Additionally, it
includes tools such as a minimal web server, in-memory query and
management tools (can be run as applets or servlets, too) and a number
of demonstration examples.

Downloaded code should be regarded as being of production quality. The
product is currently being used as a database and persistence engine in
many Open Source Software projects and even in commercial projects and
products! In it's current version it is extremely stable and reliable.
It is best known for its small size, ability to execute completely in
memory and its speed. Yet it is a completely functional relational
database management system that is completely free under the Modified
BSD License. Yes, that's right, completely free of cost or
restrictions!

%package manual
Summary:        Manual for %{name}
Group:          Documentation/Other

%description manual
Manual for %{name}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%package demo
Summary:        Demo for %{name}
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description demo
Demonstrations and samples for %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

# set right permissions
find . -name "*.sh" -exec chmod 755 {} +

# remove all _notes directories
find . -name _notes -exec rm -rf {} +

# remove all binary libs
find . -name "*.jar" -exec rm -f {} +
find . -name "*.class" -exec rm -f {} +
find . -name "*.war" -exec rm -f {} +
find . -name "*.zip" -exec rm -f {} +

# correct silly permissions
chmod -R go=u-w *

# Fix doc location
sed -i -e 's/doc-src/doc/g' build/build.xml
sed -i -e 's|doc/apidocs|%{_javadocdir}/%{name}|g' index.html

%patch0 -p1
%patch1 -p1
%patch2 -p2

%build
pushd build
export JAVA_TOOL_OPTIONS="-Dfile.encoding=UTF8 -Dant.build.javac.source=1.7 -Dant.build.javac.target=1.7"
ant hsqldb javadoc -Dservletapi.lib=$(build-classpath glassfish-servlet-api)
popd

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# systemd
install -d -m 755 %{buildroot}%{_unitdir}
install -d -m 755 %{buildroot}%{_libexecdir}/%{name}
install -m 644 %{SOURCE6} %{buildroot}%{_unitdir}/%{name}.service
install -m 755 %{SOURCE7} %{buildroot}%{_libexecdir}/%{name}/%{name}-wrapper
install -m 755 %{SOURCE8} %{buildroot}%{_libexecdir}/%{name}/%{name}-post
install -m 755 %{SOURCE9} %{buildroot}%{_libexecdir}/%{name}/%{name}-stop

# rchsqldb link
install -d -m 0755 %{buildroot}/%{_sbindir}/
ln -sf service %{buildroot}/%{_sbindir}/rc%{name}

# sysconfig
install -d -m 0755 %{buildroot}/%{_sysconfdir}
install -m 0644 %{SOURCE1} %{buildroot}/%{_sysconfdir}/%{name}.conf

# serverconfig
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}
install -m 644 %{SOURCE2} %{buildroot}%{_localstatedir}/lib/%{name}/server.properties
install -m 644 %{SOURCE3} %{buildroot}%{_localstatedir}/lib/%{name}/webserver.properties
install -m 600 %{SOURCE4} %{buildroot}%{_localstatedir}/lib/%{name}/sqltool.rc

# lib
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}/lib

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -r doc/apidocs/* %{buildroot}%{_javadocdir}/%{name}

# data
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}/data

# demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}/sample
rm -f sample/%{name}.init
install -m 644 sample/* %{buildroot}%{_datadir}/%{name}/sample

# manual
install -d -m 755 %{buildroot}%{_docdir}/%{name}-%{version}
cp -pr doc/* %{buildroot}%{_docdir}/%{name}-%{version}
cp -p index.html %{buildroot}%{_docdir}/%{name}-%{version}

cd ..
# Maven metadata
install -pD -T -m 644 %{SOURCE5} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap

pushd %{buildroot}%{_localstatedir}/lib/%{name}/lib
    # build-classpath can not be used as the jar is not
    # yet present during the build
    ln -s %{_javadir}/hsqldb.jar hsqldb.jar
    ln -s $(build-classpath glassfish-servlet-api) servletapi5.jar
popd

%fdupes -s %{buildroot}

%pre
# Add the "hsqldb" user and group
# we need a shell to be able to use su - later
if [ `getent group %{name}` ]; then
    : OK group hsqldb already present
else
    %{_sbindir}/groupadd -r %{name} 2> /dev/null || :
fi
if [ `getent passwd %{name}` ]; then
    : OK user hsqldb already present
else
    %{_sbindir}/useradd -r -g %{name} -c "Hsqldb" -s /bin/sh \
    -d %{_localstatedir}/lib/%{name} %{name} 2> /dev/null || :
fi
%service_add_pre %{name}.service

%post
%{fillup_only %{name}}
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%defattr(0644,root,root,0755)
%dir %{_docdir}/%{name}-%{version}
%doc %{_docdir}/%{name}-%{version}/hsqldb_lic.txt
%{_javadir}/*
%{_sbindir}/rc%{name}
%{_unitdir}/%{name}.service
%dir %{_libexecdir}/%{name}/
%attr(0755,root,root) %{_libexecdir}/%{name}/%{name}-post
%attr(0755,root,root) %{_libexecdir}/%{name}/%{name}-stop
%attr(0755,root,root) %{_libexecdir}/%{name}/%{name}-wrapper
%{_localstatedir}/lib/%{name}/lib
%attr(0700,hsqldb,hsqldb) %{_localstatedir}/lib/%{name}/data
%attr(0644,root,root) %{_localstatedir}/lib/%{name}/server.properties
%attr(0644,root,root) %{_localstatedir}/lib/%{name}/webserver.properties
%attr(0600,hsqldb,hsqldb) %{_localstatedir}/lib/%{name}/sqltool.rc
%dir %{_localstatedir}/lib/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%dir %{_mavenpomdir}
%{_mavenpomdir}/*
%{_datadir}/maven-metadata/%{name}.xml

%files manual
%defattr(0644,root,root,0755)
%exclude %doc %{_docdir}/%{name}-%{version}/hsqldb_lic.txt
%doc %{_docdir}/%{name}-%{version}

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}

%files demo
%defattr(-,root,root,0755)
%{_datadir}/%{name}

%changelog
