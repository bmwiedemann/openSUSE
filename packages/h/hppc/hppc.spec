#
# spec file for package hppc
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


Name:           hppc
Version:        0.7.1
Release:        0
Summary:        High Performance Primitive Collections for Java
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://labs.carrotsearch.com/hppc.html
Source0:        https://github.com/carrotsearch/hppc/archive/%{version}.tar.gz
Patch0:         hppc-timestamp.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(org.antlr:antlr4)
BuildRequires:  mvn(org.antlr:antlr4-maven-plugin)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.velocity:velocity)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
#!BuildRequires: log4j stringtemplate4
BuildArch:      noarch

%description
Fundamental data structures (maps, sets, lists, stacks, queues) generated for
combinations of object and primitive types to conserve JVM memory and speed
up execution.

%package templateprocessor
Summary:        HPPC Template Processor
Group:          Development/Libraries/Java

%description templateprocessor
Template Processor and Code Generation for HPPC.

%package javadoc
Summary:        Javadoc for HPPC
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for HPPC.

%prep
%setup -q
%patch -P 0 -p1

find . -name "*.class" -print -delete
find . -name "*.jar" -print -delete

# Unavailable deps
%pom_disable_module %{name}-benchmarks
%pom_remove_plugin :junit4-maven-plugin
%pom_remove_plugin :forbiddenapis
%pom_remove_plugin :junit4-maven-plugin hppc
# Unneeded task
%pom_remove_plugin -r :maven-assembly-plugin

%pom_add_dep javax.annotation:javax.annotation-api hppc

%pom_xpath_set "pom:project/pom:properties/pom:maven.compiler.source" "1.8"
%pom_xpath_set "pom:project/pom:properties/pom:maven.compiler.target" "1.8"

%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId='maven-plugin-plugin']/pom:configuration" "
  <goalPrefix>hppc-template-processor</goalPrefix>" hppc-template-processor

# Convert from dos to unix line ending
for file in CHANGES.txt; do
 sed -i.orig 's|\r||g' $file
 touch -r $file.orig $file
 rm $file.orig
done

%{mvn_file} :%{name} %{name}
%{mvn_package} :%{name}::esoteric:
%{mvn_file} :%{name}-template-processor %{name}-templateprocessor
%{mvn_package} :%{name}-template-processor %{name}-templateprocessor

%build
%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc CHANGES.txt README.txt
%license LICENSE.txt NOTICE.txt

%files templateprocessor -f .mfiles-%{name}-templateprocessor
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt

%changelog
