#
# spec file for package apache-commons-vfs2
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


%global base_name vfs2
%global short_name commons-%{base_name}
%bcond_with cifs
%bcond_with mina
%bcond_without ssh
Name:           apache-%{short_name}
Version:        2.10.0
Release:        0
Summary:        Commons Virtual File System
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/vfs/
Source0:        https://archive.apache.org/dist/commons/vfs/source/commons-vfs-%{version}-src.tar.gz
Source1:        %{short_name}-build.tar.xz
BuildRequires:  ant
BuildRequires:  apache-commons-collections4
BuildRequires:  apache-commons-compress
BuildRequires:  apache-commons-httpclient
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang3
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-net > 2
BuildRequires:  fdupes
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-core
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch
%if %{with cifs}
BuildRequires:  jcifs
%endif
%if %{with mina}
BuildRequires:  mvn(org.apache.mina:mina-core)
%endif
%if %{with ssh}
BuildRequires:  jsch
%endif

%description
Commons VFS provides a single API for accessing various
different file systems. It presents a uniform view of the
files from various different sources, such as the files on
local disk, on an HTTP server, or inside a Zip archive.
Some of the features of Commons VFS are:
* A single consistent API for accessing files of different
 types.
* Support for numerous file system types.
* Caching of file information. Caches information in-JVM,
 and optionally can cache remote file information on the
 local file system.
* Event delivery.
* Support for logical file systems made up of files from
 various different file systems.
* Utilities for integrating Commons VFS into applications,
 such as a VFS-aware ClassLoader and URLStreamHandlerFactory.
* A set of VFS-enabled Ant tasks.

%package ant
Summary:        Development files for Commons VFS
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}

%description ant
This package enables support for the Commons VFS ant tasks.

%package examples
Summary:        Commons VFS Examples
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}

%description examples
VFS is a Virtual File System library - Examples.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n commons-vfs-%{version} -a1

# Disable unwanted module
%pom_disable_module commons-vfs2-distribution

# Fix ant gId
%pom_change_dep -r :ant org.apache.ant:

# Remove webdav client
%pom_remove_dep -r org.apache.jackrabbit:
%pom_disable_module commons-vfs2-jackrabbit1
%pom_disable_module commons-vfs2-jackrabbit2

# Remove http5 client
%pom_remove_dep -r org.apache.httpcomponents.client5:httpclient5
rm -r commons-vfs2/src/{main,test}/java/org/apache/commons/vfs2/provider/http5
rm -r commons-vfs2/src/{main,test}/java/org/apache/commons/vfs2/provider/http5s

# ftpserver is not available
%if %{without ftp}
%pom_remove_dep -r :ftpserver-core
rm -r commons-vfs2/src/{main,test}/java/org/apache/commons/vfs2/provider/ftps
%endif

# jcifs not packaged and also export controlled in the US
%if %{without cifs}
%pom_remove_dep :jcifs
%endif

# mina is not available
%if %{without mina}
%pom_remove_dep :mina-core
%endif

%build
mkdir -p lib
build-jar-repository -s lib \
  ant \
  commons-collections4 \
  commons-compress \
  commons-httpclient \
  commons-io \
  commons-lang3 \
  commons-logging \
  commons-net \
  httpcomponents/httpclient \
  httpcomponents/httpcore
%if %{with ssh}
build-jar-repository -s lib \
  jsch
%endif

ant \
  -Dtest.skip=true \
  package javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 %{short_name}/target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -sf %{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
install -pm 0644 %{short_name}-examples/target/%{short_name}-examples-%{version}.jar %{buildroot}%{_javadir}/%{short_name}-examples.jar
ln -sf %{short_name}-examples.jar %{buildroot}%{_javadir}/%{name}-examples.jar
# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} %{short_name}/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar
%{mvn_install_pom} %{short_name}-examples/pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}-examples.pom
%add_maven_depmap %{short_name}-examples.pom %{short_name}-examples.jar -f examples
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/%{short_name}-examples
cp -pr %{short_name}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
cp -pr %{short_name}-examples/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/%{short_name}-examples/
%fdupes -s %{buildroot}%{_javadocdir}

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "ant commons-logging commons-vfs" > commons-vfs
install -p -m 644 commons-vfs %{buildroot}%{_sysconfdir}/ant.d/commons-vfs

%files -f .mfiles
%doc README.md RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt
%{_javadir}/%{name}.jar

%files examples -f .mfiles-examples
%{_javadir}/%{name}-examples.jar

%files javadoc
%license LICENSE.txt NOTICE.txt
%{_javadocdir}/%{name}

%files ant
%config %{_sysconfdir}/ant.d/commons-vfs

%changelog
