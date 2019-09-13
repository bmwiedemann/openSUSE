#
# spec file for package jakarta-commons-vfs
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


%define base_name commons-vfs
Name:           jakarta-commons-vfs
Version:        1.0
Release:        0
Summary:        Commons Virtual Filesystem
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://jakarta.apache.org/commons/vfs/
# svn export http://svn.apache.org/repos/asf/jakarta/commons/proper/vfs/tags/vfs-1.0/
Source0:        commons-vfs-1.0-src.tar.bz2
Source1:        commons-vfs-1.0-build.tar.xz
Patch0:         commons-vfs-1.0-project_properties.patch
Patch1:         commons-vfs-1.0-jakarta-commons-httpclient-3.1.patch
BuildRequires:  ant >= 1.6
BuildRequires:  ant-junit
BuildRequires:  fdupes
BuildRequires:  jaf_1_1_api
BuildRequires:  jakarta-commons-codec
BuildRequires:  jakarta-commons-collections
BuildRequires:  jakarta-commons-httpclient3
BuildRequires:  jakarta-commons-logging
BuildRequires:  jakarta-commons-net
BuildRequires:  jakarta-slide-webdavclient
BuildRequires:  javamail
BuildRequires:  javapackages-local
BuildRequires:  jcifs
BuildRequires:  jdom
BuildRequires:  jsch
BuildRequires:  junit
BuildRequires:  oro
BuildRequires:  xml-commons-apis
Requires:       jaf_1_1_api
Requires:       jakarta-commons-codec
Requires:       jakarta-commons-collections
Requires:       jakarta-commons-httpclient3
Requires:       jakarta-commons-logging
Requires:       jakarta-commons-net
Requires:       jakarta-slide-webdavclient
Requires:       javamail
Requires:       jcifs
Requires:       jdom
Requires:       jsch
Requires:       oro
Requires:       xml-commons-apis
BuildArch:      noarch

%description
Commons VFS provides a single API for accessing various different
   file systems. It presents a uniform view of the files from
   various different sources, such as the files on local disk, on an
   HTTP server, or inside a Zip archive. Some of the features of
   Commons VFS are: * A single consistent API for accessing files of
   different types.

%package javadoc
Summary:        Commons Virtual Filesystem
Group:          Development/Libraries/Java

%description javadoc
Commons VFS provides a single API for accessing various different
   file systems. It presents a uniform view of the files from
   various different sources, such as the files on local disk, on an
   HTTP server, or inside a Zip archive. Some of the features of
   Commons VFS are: * A single consistent API for accessing files of
   different types.

%package manual
Summary:        Commons Virtual Filesystem
Group:          Development/Libraries/Java

%description manual
Commons VFS provides a single API for accessing various different
   file systems. It presents a uniform view of the files from
   various different sources, such as the files on local disk, on an
   HTTP server, or inside a Zip archive. Some of the features of
   Commons VFS are: * A single consistent API for accessing files of
   different types.

%prep
%setup -q -n vfs-%{version} -a1
%patch0
%patch1 -p1
find . -name "*.jar" | xargs -t rm

%pom_remove_parent core examples sandbox

%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
export CLASSPATH=$(build-classpath commons-collections commons-httpclient3 commons-logging commons-net jaf_1_1_api javamail/mail jcifs jdom jsch junit slide/jakarta-slide-webdavlib):`pwd`/target/commons-vfs-%{version}.jar:`pwd`/target/test-classes
export OPT_JAR_LIST="junit ant/ant-junit"
ant \
    -Dmaven.build.dir=`pwd`/target \
    -Dmaven.build.outputDir=`pwd`/target \
    -Dmaven.mode.offline=true \
    -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.repo.remote=file:%{_datadir}/maven/repository \
    -Dmaven.javadoc.source=1.4 \
    -Dmaven.home.local=$(pwd)/.maven \
    -Dmaven.test.skip=true \
    -Dmaven.test.error.ignore=true \
    package javadoc

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 target/%{base_name}-%{version}*.jar %{buildroot}%{_javadir}/%{base_name}.jar
ln -sf %{base_name}.jar %{buildroot}%{_javadir}/%{name}.jar
install -m 644 target/%{base_name}-examples-%{version}*.jar %{buildroot}%{_javadir}/%{base_name}-examples.jar
ln -sf %{base_name}-examples.jar %{buildroot}%{_javadir}/%{name}-examples.jar
install -m 644 target/%{base_name}-sandbox-%{version}*.jar %{buildroot}%{_javadir}/%{base_name}-sandbox.jar
ln -sf %{base_name}-sandbox.jar %{buildroot}%{_javadir}/%{name}-sandbox.jar
#pom
mkdir -p %{buildroot}%{_mavenpomdir}
install -m 0644 core/pom.xml %{buildroot}%{_mavenpomdir}/%{base_name}.pom
%add_maven_depmap %{base_name}.pom %{base_name}.jar
install -m 0644 examples/pom.xml %{buildroot}%{_mavenpomdir}/%{base_name}-examples.pom
%add_maven_depmap %{base_name}-examples.pom %{base_name}-examples.jar
install -m 0644 sandbox/pom.xml %{buildroot}%{_mavenpomdir}/%{base_name}-sandbox.pom
%add_maven_depmap %{base_name}-sandbox.pom %{base_name}-sandbox.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}
rm -rf target/site/apidocs
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name}
mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}

%files -f .mfiles
%doc *.txt
%{_javadir}/%{name}*.jar

%files manual
%{_docdir}/%{name}-%{version}

%files javadoc
%{_javadocdir}/%{name}

%changelog
