#
# spec file for package plexus-archiver
#
# Copyright (c) 2024 SUSE LLC
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


Name:           plexus-archiver
Version:        4.9.2
Release:        0
Summary:        Plexus Archiver Component
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://codehaus-plexus.github.io/plexus-archiver
Source0:        https://github.com/codehaus-plexus/plexus-archiver/archive/plexus-archiver-%{version}.tar.gz
Source1:        %{name}-build.xml
Patch0:         0001-Remove-support-for-snappy.patch
Patch1:         0002-Remove-support-for-zstd.patch
BuildRequires:  ant
BuildRequires:  apache-commons-compress
BuildRequires:  apache-commons-io
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  jsr-305
BuildRequires:  plexus-io >= 3.2
BuildRequires:  plexus-utils >= 3.3
BuildRequires:  sisu-inject
BuildRequires:  slf4j
BuildRequires:  xz-java
BuildArch:      noarch

%description
Plexus contains end-to-end developer tools for writing applications.
At the core is the container, which can be embedded or for an
application server. There are many reusable components for hibernate,
form processing, jndi, i18n, velocity, etc. Plexus also includes an
application server which is like a J2EE application server.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE1} build.xml

%patch -P 0 -p1
%pom_remove_dep org.iq80.snappy:snappy
rm -rf src/main/java/org/codehaus/plexus/archiver/snappy
rm -rf src/test/java/org/codehaus/plexus/archiver/snappy
rm -f src/main/java/org/codehaus/plexus/archiver/tar/SnappyTarFile.java
rm -f src/main/java/org/codehaus/plexus/archiver/tar/PlexusIoTarSnappyFileResourceCollection.java
rm -r src/test/java/org/codehaus/plexus/archiver/tar/TarSnappyUnArchiverTest.java

%patch -P 1 -p1
%pom_remove_dep com.github.luben:zstd-jni
rm -rf src/main/java/org/codehaus/plexus/archiver/zstd
rm -rf src/test/java/org/codehaus/plexus/archiver/zstd
rm -rf src/main/java/org/codehaus/plexus/archiver/tar/PlexusIoTZstdFileResourceCollection.java
rm -rf src/main/java/org/codehaus/plexus/archiver/tar/ZstdTarFile.java
rm -rf src/main/java/org/codehaus/plexus/archiver/tar/TZstdUnArchiver.java
rm -rf src/main/java/org/codehaus/plexus/archiver/tar/TZstdArchiver.java
rm -rf src/main/java/org/codehaus/plexus/archiver/tar/TarZstdUnArchiver.java
rm -rf src/main/java/org/codehaus/plexus/archiver/tar/PlexusIoTarZstdFileResourceCollection.java
rm -rf src/main/java/org/codehaus/plexus/archiver/tar/TarZstdArchiver.java
rm -rf src/test/java/org/codehaus/plexus/archiver/tar/TarZstdUnArchiverTest.java

%build
mkdir -p lib
build-jar-repository -s lib atinject slf4j/api org.eclipse.sisu.inject jsr-305 commons-compress commons-io plexus/utils plexus/io
%{ant} \
  jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/plexus
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/plexus/archiver.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/plexus
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/plexus/archiver.pom
%add_maven_depmap plexus/archiver.pom plexus/archiver.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE

%files javadoc
%license LICENSE
%{_javadocdir}/%{name}

%changelog
