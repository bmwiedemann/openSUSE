#
# spec file for package lucene
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


%define jarname lucene-core
Name:           lucene
Version:        6.6.0
Release:        0
Summary:        Text search engine
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://lucene.apache.org/
Source0:        http://www.apache.org/dist/lucene/java/%{version}/%{name}-%{version}-src.tgz
Source1:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-queryparser/%{version}/lucene-queryparser-%{version}.pom
Source2:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-join/%{version}/lucene-join-%{version}.pom
Source3:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-queries/%{version}/lucene-queries-%{version}.pom
Source4:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-classification/%{version}/lucene-classification-%{version}.pom
Source5:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-facet/%{version}/lucene-facet-%{version}.pom
Source6:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-codecs/%{version}/lucene-codecs-%{version}.pom
Source7:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-backward-codecs/%{version}/lucene-backward-codecs-%{version}.pom
Source8:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-grouping/%{version}/lucene-grouping-%{version}.pom
Source9:        http://repo1.maven.org/maven2/org/apache/lucene/lucene-highlighter/%{version}/lucene-highlighter-%{version}.pom
Source10:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-memory/%{version}/lucene-memory-%{version}.pom
Source11:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-misc/%{version}/lucene-misc-%{version}.pom
Source12:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-sandbox/%{version}/lucene-sandbox-%{version}.pom
Source13:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-spatial3d/%{version}/lucene-spatial3d-%{version}.pom
Source14:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-spatial/%{version}/lucene-spatial-%{version}.pom
Source15:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-analyzers-common/%{version}/lucene-analyzers-common-%{version}.pom
Source16:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-analyzers-smartcn/%{version}/lucene-analyzers-smartcn-%{version}.pom
Source17:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-analyzers-stempel/%{version}/lucene-analyzers-stempel-%{version}.pom
Source18:       http://repo1.maven.org/maven2/org/apache/lucene/lucene-core/%{version}/lucene-core-%{version}.pom
BuildRequires:  ant >= 1.6
BuildRequires:  ant-junit >= 1.6
BuildRequires:  antlr-java
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-digester
BuildRequires:  apache-commons-logging
BuildRequires:  apache-ivy
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  java-devel >= 1.8
BuildRequires:  javacc
BuildRequires:  javapackages-local
BuildRequires:  jtidy
BuildRequires:  junit
BuildRequires:  log4j
BuildRequires:  regexp
BuildRequires:  zip
BuildArch:      noarch

%description
Apache Lucene is a full-text search engine written entirely in Java.
It offers fuzzy search based on edit (Levenshtein) distance,
incremental indexing, ranked searching, field-based searches and
multi-index searches.

%files -f .mfiles
%license LICENSE.txt
%doc CHANGES.txt README.txt

%package queryparser
Summary:        Queryparser module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.lucene:lucene-queries)
Requires:       mvn(org.apache.lucene:lucene-sandbox)

%description queryparser
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "queryparser" module for lucene.

%files queryparser -f .mfiles-queryparser

%package join
Summary:        Join module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)

%description join
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "join" module for lucene.

%files join -f .mfiles-join

%package queries
Summary:        Queries module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)

%description queries
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "queries" module for lucene.

%files queries -f .mfiles-queries

%package classification
Summary:        Classification module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.lucene:lucene-grouping)
Requires:       mvn(org.apache.lucene:lucene-queries)

%description classification
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "classification" module for Lucene.

%files classification -f .mfiles-classification

%package facet
Summary:        Facet module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.lucene:lucene-queries)

%description facet
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "facet" module for Lucene.

%files facet -f .mfiles-facet

%package codecs
Summary:        Codecs module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)

%description codecs
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "codecs" module for Lucene.

%files codecs -f .mfiles-codecs

%package backward-codecs
Summary:        Backward-codecs module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)

%description backward-codecs
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "backward-codecs" module for Lucene.

%files backward-codecs -f .mfiles-backward-codecs

%package grouping
Summary:        Grouping module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.lucene:lucene-queries)

%description grouping
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "grouping" module for Lucene.

%files grouping -f .mfiles-grouping

%package highlighter
Summary:        Highlighter module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-analyzers-common)
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.lucene:lucene-join)
Requires:       mvn(org.apache.lucene:lucene-memory)
Requires:       mvn(org.apache.lucene:lucene-queries)

%description highlighter
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "highlighter" module for Lucene.

%files highlighter -f .mfiles-highlighter

%package memory
Summary:        Memory module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)

%description memory
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "memory" module for Lucene.

%files memory -f .mfiles-memory

%package misc
Summary:        Misc module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)

%description misc
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "misc" module for Lucene.

%files misc -f .mfiles-misc

%package sandbox
Summary:        Sandbox module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)

%description sandbox
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "sandbox" module for Lucene.

%files sandbox -f .mfiles-sandbox

%package spatial3d
Summary:        Spatial3d module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)

%description spatial3d
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "spatial3d" module for Lucene.

%files spatial3d -f .mfiles-spatial3d

%package spatial
Summary:        Spatial module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)

%description spatial
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "spatial" module for Lucene.

%files spatial -f .mfiles-spatial

%package analyzers-common
Summary:        Analyzers-common module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)

%description analyzers-common
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "analyzers-common" module for Lucene.

%files analyzers-common -f .mfiles-analyzers-common

%package analyzers-smartcn
Summary:        Analyzers-smartcn module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-analyzers-common)
Requires:       mvn(org.apache.lucene:lucene-core)

%description analyzers-smartcn
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "analyzers-smartcn" module for Lucene.

%files analyzers-smartcn -f .mfiles-analyzers-smartcn

%package analyzers-stempel
Summary:        Analyzers-stempel module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-analyzers-common)
Requires:       mvn(org.apache.lucene:lucene-core)

%description analyzers-stempel
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "analyzers-stempel" module for Lucene.

%files analyzers-stempel -f .mfiles-analyzers-stempel

%prep
%setup -q

%build
export CLASSPATH=$(build-classpath commons-digester jtidy junit regexp)
export OPT_JAR_LIST=:
ant \
  -Djavacc.home=%{_bindir}/javacc \
  -Djavacc.jar=%{_javadir}/javacc.jar \
  -Djavacc.jar.dir=%{_javadir} \
  -Djavadoc.link=%{_javadocdir}/java \
  -Dversion=%{version} \
  -Divy.mode=local

# DOESN'T BUILD BECAUSE OF MISSING DEPS: replicator expressions spatial-extras analyzers-kuromoji analyzers-morfologik analyzers-phonetic
export modules="queryparser join queries classification facet codecs backward-codecs grouping highlighter memory misc sandbox spatial3d spatial"

for mod in $modules
do
  ant -f module-build.xml \
    -Djavacc.home=%{_bindir}/javacc \
    -Djavacc.jar=%{_javadir}/javacc.jar \
    -Djavacc.jar.dir=%{_javadir} \
    -Djavadoc.link=%{_javadocdir}/java \
    -Dversion=%{version} \
    -Divy.mode=local \
  jar-$mod
done

export modanalyzers="common smartcn stempel"
pushd analysis
ant \
  -Djavacc.home=%{_bindir}/javacc \
  -Djavacc.jar=%{_javadir}/javacc.jar \
  -Djavacc.jar.dir=%{_javadir} \
  -Djavadoc.link=%{_javadocdir}/java \
  -Dversion=%{version} \
  -Divy.mode=local \
$modanalyzers

%install
install -d -m 0755 %{buildroot}%{_javadir}

# maven pom dir
install -d -m 0755 %{buildroot}%{_mavenpomdir}/

install -p -m 0644 build/core/%{jarname}-%{version}.jar %{buildroot}%{_javadir}/%{jarname}.jar
cp %{_sourcedir}/lucene-core-%{version}.pom build/core/pom.xml
%pom_remove_parent build/core
%pom_xpath_inject "pom:project" "<version>%{version}</version>" build/core
install -p -m 0644 build/core/pom.xml %{buildroot}%{_mavenpomdir}/%{name}-core.pom
%add_maven_depmap %{name}-core.pom lucene-core.jar

export modules="queryparser join queries classification facet codecs backward-codecs grouping highlighter memory misc sandbox spatial3d spatial"
for mod in $modules
do
  install -p -m 0644 build/${mod}/lucene-$mod-%{version}.jar %{buildroot}%{_javadir}/lucene-$mod.jar
  cp %{_sourcedir}/lucene-${mod}-%{version}.pom build/${mod}/pom.xml
  %pom_remove_parent build/${mod}
  %pom_xpath_inject "pom:project" "<version>%{version}</version>" build/${mod}
  install -p -m 0644 build/${mod}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}-${mod}.pom
  %add_maven_depmap %{name}-${mod}.pom lucene-${mod}.jar -f ${mod}
done

export modanalyzers="common smartcn stempel"
for mod in $modanalyzers
do
  install -p -m 0644 build/analysis/$mod/lucene-analyzers-$mod-%{version}.jar %{buildroot}%{_javadir}/lucene-analyzers-${mod}.jar
  cp %{_sourcedir}/lucene-analyzers-${mod}-%{version}.pom build/analysis/$mod/pom.xml
  %pom_remove_parent build/analysis/$mod
  %pom_xpath_inject "pom:project" "<version>%{version}</version>" build/analysis/$mod
  install -p -m 0644 build/analysis/$mod/pom.xml %{buildroot}%{_mavenpomdir}/%{name}-analyzers-${mod}.pom
  %add_maven_depmap %{name}-analyzers-${mod}.pom lucene-analyzers-${mod}.jar -f analyzers-${mod}
done

# javadoc DOES NOT BUILD BECAUSE OF MISSING MVN DEPS
# javadoc
#install -d -m 0755 %%{buildroot}%%{_javadocdir}/%%{name}
#cp -pr build/docs/api/* \
#  %%{buildroot}%%{_javadocdir}/%%{name}

%changelog
