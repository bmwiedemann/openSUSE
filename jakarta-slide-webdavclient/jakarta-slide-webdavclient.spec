#
# spec file for package jakarta-slide-webdavclient
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define _with_repolib 1
%define with_repolib %{?_with_repolib:1}%{!?_with_repolib:0}
%define without_repolib %{!?_with_repolib:1}%{?_with_repolib:0}
%define repodir %{_javadir}/repository.jboss.com/apache-slide/2.1-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src
%define section   devel
%define base_name slide
%define jakarta_version 2.1
Name:           jakarta-slide-webdavclient
Version:        %{jakarta_version}
Release:        0
Summary:        Slide WebDAV client
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://jakarta.apache.org/slide/
Source0:        jakarta-slide-webdavclient-src-2.1.tar.bz2
Source1:        %{name}.sh
Source2:        jakarta-slide-webdavclient-2.2-WebdavResource.java
Source3:        jakarta-slide-webdavclient-component-info.xml
Source4:        http://mirrors.ibiblio.org/pub/mirrors/maven2/slide/slide-webdavlib/2.1/slide-webdavlib-2.1.pom
# FIXME Temporary fix !!!
Patch0:         jakarta-slide-webdavclient-3.0-compat.patch
Patch1:         jakarta-slide-webdavclient-build-jdk16.patch
Patch2:         jakarta-slide-webdavclient-jdk15.patch
Patch3:         jakarta-slide-webdavclient-enum.patch
BuildRequires:  ant >= 1.6
BuildRequires:  ant-antlr
BuildRequires:  antlr
BuildRequires:  fdupes
BuildRequires:  geronimo-j2ee-connector-1_5-api
BuildRequires:  jakarta-commons-httpclient3
BuildRequires:  jakarta-commons-transaction
BuildRequires:  javapackages-tools
BuildRequires:  jdom
BuildRequires:  xml-im-exporter
Requires:       geronimo-j2ee-connector-1_5-api
Requires:       jakarta-commons-httpclient3
Requires:       jakarta-commons-transaction
Requires:       jdom
Requires:       xml-im-exporter
BuildArch:      noarch

%description
Slide includes a fully featured WebDAV client library and command line
client.

%if %{with_repolib}
%package	 repolib
Summary:        Slide WebDAV client
Group:          Development/Libraries/Java

%description	 repolib
Slide includes a fully featured WebDAV client library and command line
client.

%endif

%package        javadoc
Summary:        Slide WebDAV client
Group:          Development/Libraries/Java

%description    javadoc
Slide includes a fully featured WebDAV client library and command line
client.

%prep
%setup -q -n jakarta-slide-webdavclient-src-2.1
find . -name "*.jar" | xargs rm
#for j in $(find . -name "*.jar"); do
#	mv $j $j.no
#done
cp -p %{SOURCE2} clientlib/src/java/org/apache/webdav/lib/WebdavResource.java
%patch0 -b .sav
%patch1 -b .sav
%patch2 -b .sav
%patch3 -p1

%build
export CLASSPATH=$(build-classpath \
antlr \
commons-httpclient3 \
commons-transaction \
geronimo-j2ee-1.4-apis \
jdom \
xml-im-exporter \
)
ant -v -d -Dbuild.sysclasspath=first

%install
install -dm 755 %{buildroot}%{_bindir}
install -pm 755 %{SOURCE1} %{buildroot}%{_bindir}/webdavclient
install -dm 755 %{buildroot}%{_javadir}/%{base_name}
install -pm 644 \
 dist/lib/jakarta-slide-webdavlib-%{jakarta_version}.jar \
 %{buildroot}%{_javadir}/%{base_name}
ln -s jakarta-slide-webdavlib-%{jakarta_version}.jar \
 %{buildroot}%{_javadir}/%{base_name}/%{name}-webdavlib-%{version}.jar
install -pm 644 \
 dist/lib/jakarta-slide-commandline-%{jakarta_version}.jar \
 %{buildroot}%{_javadir}/%{base_name}
ln -s jakarta-slide-commandline-%{jakarta_version}.jar \
 %{buildroot}%{_javadir}/%{base_name}/%{name}-commandline-%{version}.jar
(cd %{buildroot}%{_javadir}/%{base_name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)
(cd %{buildroot}%{_javadir}/%{base_name} && for jar in jakarta-*.jar; do ln -sf ${jar} `echo $jar| sed  "s|jakarta-||g"`; done)
#javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr dist/doc/clientjavadoc/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
# poms
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE4} %{buildroot}%{_mavenpomdir}/JPP.%{name}.pom
#FIXME
# % add_maven_depmap JPP.%{name}.pom %{base_name}/jakarta-slide-webdavlib.jar

%if %{with_repolib}
	install -d -m 755 %{buildroot}%{repodir}
	install -d -m 755 %{buildroot}%{repodirlib}
	install -p -m 644 %{SOURCE3} %{buildroot}%{repodir}/component-info.xml
        tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
        sed -i "s/@TAG@/$tag/g" %{buildroot}%{repodir}/component-info.xml
        sed -i "s/@VERSION@/%{version}-brew/g" %{buildroot}%{repodir}/component-info.xml
	install -d -m 755 %{buildroot}%{repodirsrc}
	install -p -m 644 %{SOURCE2} %{buildroot}%{repodirsrc}
	install -p -m 644 %{PATCH0} %{buildroot}%{repodirsrc}
	install -p -m 644 %{SOURCE0} %{buildroot}%{repodirsrc}
	cp -p %{buildroot}%{_javadir}/slide/jakarta-slide-webdavlib.jar %{buildroot}%{repodirlib}
%endif

%files
%doc LICENSE
%{_javadir}/%{base_name}/*.jar
%attr(0755,root,root) %{_bindir}/webdavclient
%{_mavenpomdir}/*
# % config %{_datadir}/maven-metadata/%{name}.xml*
%dir %{_javadir}/%{base_name}

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}
%if %{with_repolib}
%files repolib
%{repodir}
%dir %{_javadir}/repository.jboss.com
%dir %{_javadir}/repository.jboss.com/apache-%{base_name}
%endif

%changelog
