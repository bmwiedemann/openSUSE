#
# spec file for package apache-commons-compress
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


%global base_name       compress
%global short_name      commons-%{base_name}
Name:           apache-%{short_name}
Version:        1.26.1
Release:        0
Summary:        Java API for working with compressed files and archivers
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/proper/commons-compress/
Source0:        https://archive.apache.org/dist/commons/compress/source/%{short_name}-%{version}-src.tar.gz
Source1:        %{name}-build.xml
Patch0:         0001-Remove-Brotli-compressor.patch
Patch1:         0002-Remove-ZSTD-compressor.patch
Patch2:         0003-Remove-Pack200-compressor.patch
BuildRequires:  ant
BuildRequires:  commons-codec
BuildRequires:  commons-io >= 2.14
BuildRequires:  commons-lang3
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  xz-java
Provides:       %{short_name} = %{version}-%{release}
Obsoletes:      %{short_name} < %{version}-%{release}
Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{version}-%{release}
BuildArch:      noarch

%description
The Apache Commons Compress library defines an API for working with
ar, cpio, Unix dump, tar, zip, gzip, XZ, Pack200 and bzip2 files.
In version 1.14 read-only support for Brotli decompression has been added,
but it has been removed from this package.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE1} build.xml

# Unavailable Google Brotli library (org.brotli.dec)
%patch -P 0 -p1
%pom_remove_dep org.brotli:dec
rm -r src/{main,test}/java/org/apache/commons/compress/compressors/brotli

# Unavailable ZSTD JNI library
%patch -P 1 -p1
%pom_remove_dep :zstd-jni
rm -r src/{main,test}/java/org/apache/commons/compress/compressors/zstandard

# Remove support for pack200 which depends on ancient asm:asm:3.2
%patch -P 2 -p1
rm -r src/{main,test}/java/org/apache/commons/compress/harmony
rm -r src/main/java/org/apache/commons/compress/compressors/pack200
rm src/main/java/org/apache/commons/compress/java/util/jar/Pack200.java
rm -r src/test/java/org/apache/commons/compress/compressors/pack200
rm src/test/java/org/apache/commons/compress/java/util/jar/Pack200Test.java

# NPE with jdk10
%pom_remove_plugin :maven-javadoc-plugin

%pom_xpath_remove "pom:profiles/pom:profile[pom:id[text()='java9+']]"

%build
mkdir -p lib
build-jar-repository -s lib xz-java commons-io commons-codec commons-lang3
%{ant} package javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -sf %{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar -a commons:commons-compress,commons-compress:commons-compress
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%{_javadir}/%{name}.jar
%license LICENSE.txt
%doc NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt
%doc NOTICE.txt

%changelog
