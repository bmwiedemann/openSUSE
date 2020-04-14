#
# spec file for package lucene
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


Name:           lucene
Version:        8.5.0
Release:        0
Summary:        Text search engine
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://lucene.apache.org/
Source0:        https://archive.apache.org/dist/lucene/java/%{version}/%{name}-%{version}-src.tgz
Source1:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-queryparser/%{version}/lucene-queryparser-%{version}.pom
Source2:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-join/%{version}/lucene-join-%{version}.pom
Source3:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-queries/%{version}/lucene-queries-%{version}.pom
Source4:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-classification/%{version}/lucene-classification-%{version}.pom
Source6:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-codecs/%{version}/lucene-codecs-%{version}.pom
Source7:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-backward-codecs/%{version}/lucene-backward-codecs-%{version}.pom
Source8:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-grouping/%{version}/lucene-grouping-%{version}.pom
Source9:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-highlighter/%{version}/lucene-highlighter-%{version}.pom
Source10:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-memory/%{version}/lucene-memory-%{version}.pom
Source11:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-misc/%{version}/lucene-misc-%{version}.pom
Source12:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-sandbox/%{version}/lucene-sandbox-%{version}.pom
Source13:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-spatial3d/%{version}/lucene-spatial3d-%{version}.pom
Source14:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-monitor/%{version}/lucene-monitor-%{version}.pom
Source15:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-analyzers-common/%{version}/lucene-analyzers-common-%{version}.pom
Source16:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-analyzers-smartcn/%{version}/lucene-analyzers-smartcn-%{version}.pom
Source17:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-analyzers-stempel/%{version}/lucene-analyzers-stempel-%{version}.pom
Source18:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-core/%{version}/lucene-core-%{version}.pom
Patch0:         0001-Disable-ivy-settings.patch
Patch1:         0002-Dependency-generation.patch
Patch2:         lucene-java8compat.patch
Patch3:         lucene-osgi-manifests.patch
Patch4:         lucene-missing-dependencies.patch
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
BuildRequires:  regexp
BuildRequires:  zip

%description
Apache Lucene is a full-text search engine written entirely in Java.
It offers fuzzy search based on edit (Levenshtein) distance,
incremental indexing, ranked searching, field-based searches and
multi-index searches.

%package core
Summary:        Text search engine
Group:          Development/Libraries/Java
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}
Obsoletes:      %{name}-facet < %{version}-%{release}
Obsoletes:      %{name}-spatial < %{version}-%{release}
BuildArch:      noarch

%description core
Apache Lucene is a full-text search engine written entirely in Java.
It offers fuzzy search based on edit (Levenshtein) distance,
incremental indexing, ranked searching, field-based searches and
multi-index searches.

%files core -f .mfiles-core
%license LICENSE.txt
%doc CHANGES.txt README.txt

%package queryparser
Summary:        Queryparser module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.lucene:lucene-queries)
Requires:       mvn(org.apache.lucene:lucene-sandbox)
BuildArch:      noarch

%description queryparser
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "queryparser" module for lucene.

%files queryparser -f .mfiles-queryparser

%package join
Summary:        Join module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
BuildArch:      noarch

%description join
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "join" module for lucene.

%files join -f .mfiles-join

%package queries
Summary:        Queries module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
BuildArch:      noarch

%description queries
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "queries" module for lucene.

%files queries -f .mfiles-queries

%package classification
Summary:        Classification module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-analyzers-common)
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.lucene:lucene-grouping)
Requires:       mvn(org.apache.lucene:lucene-queries)
BuildArch:      noarch

%description classification
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "classification" module for Lucene.

%files classification -f .mfiles-classification

%package codecs
Summary:        Codecs module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
BuildArch:      noarch

%description codecs
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "codecs" module for Lucene.

%files codecs -f .mfiles-codecs

%package backward-codecs
Summary:        Backward-codecs module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
BuildArch:      noarch

%description backward-codecs
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "backward-codecs" module for Lucene.

%files backward-codecs -f .mfiles-backward-codecs

%package grouping
Summary:        Grouping module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.lucene:lucene-queries)
BuildArch:      noarch

%description grouping
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "grouping" module for Lucene.

%files grouping -f .mfiles-grouping

%package highlighter
Summary:        Highlighter module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.lucene:lucene-join)
Requires:       mvn(org.apache.lucene:lucene-memory)
BuildArch:      noarch

%description highlighter
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "highlighter" module for Lucene.

%files highlighter -f .mfiles-highlighter

%package memory
Summary:        Memory module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
BuildArch:      noarch

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
BuildArch:      noarch

%description sandbox
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "sandbox" module for Lucene.

%files sandbox -f .mfiles-sandbox

%package spatial3d
Summary:        Spatial3d module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
BuildArch:      noarch

%description spatial3d
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "spatial3d" module for Lucene.

%files spatial3d -f .mfiles-spatial3d

%package monitor
Summary:        Spatial module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-analyzers-common)
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.lucene:lucene-memory)
Requires:       mvn(org.apache.lucene:lucene-queryparser)
BuildArch:      noarch

%description monitor
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "monitor" module for Lucene.

%files monitor -f .mfiles-monitor

%package analyzers-common
Summary:        Analyzers-common module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
Provides:       %{name}-analysis = %{version}-%{release}
Obsoletes:      %{name}-analysis < %{version}-%{release}
BuildArch:      noarch

%description analyzers-common
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "analyzers-common" module for Lucene.

%files analyzers-common -f .mfiles-analyzers-common

%package analyzers-smartcn
Summary:        Analyzers-smartcn module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-analyzers-common)
Requires:       mvn(org.apache.lucene:lucene-core)
BuildArch:      noarch

%description analyzers-smartcn
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "analyzers-smartcn" module for Lucene.

%files analyzers-smartcn -f .mfiles-analyzers-smartcn

%package analyzers-stempel
Summary:        Analyzers-stempel module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-analyzers-common)
Requires:       mvn(org.apache.lucene:lucene-core)
BuildArch:      noarch

%description analyzers-stempel
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "analyzers-stempel" module for Lucene.

%files analyzers-stempel -f .mfiles-analyzers-stempel

%if 0
%package facet
Summary:        Facet module for lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.lucene:lucene-queries)
BuildArch:      noarch

%description facet
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "facet" module for Lucene.

%files facet -f .mfiles-facet

%package analyzers-icu
Summary:        Lucene ICU Analysis Components
Group:          Development/Libraries/Java
Requires:       mvn(com.ibm.icu:icu4j)
Requires:       mvn(org.apache.lucene:lucene-analyzers-common)
Requires:       mvn(org.apache.lucene:lucene-core)
BuildArch:      noarch

%description analyzers-icu
Provides integration with ICU (International Components for Unicode) for
stronger Unicode and internationalization support.

%files analyzers-icu -f .mfiles-analyzers-icu

%package analyzers-kuromoji
Summary:        Lucene Kuromoji Japanese Morphological Analyzer
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-analyzers-common)
Requires:       mvn(org.apache.lucene:lucene-core)
BuildArch:      noarch

%description analyzers-kuromoji
Lucene Kuromoji Japanese Morphological Analyzer.

%files analyzers-kuromoji -f .mfiles-analyzers-kuromoji

%package analyzers-morfologik
Summary:        Lucene Morfologik Polish Lemmatizer
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-analyzers-common)
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.carrot2:morfologik-fsa)
Requires:       mvn(org.carrot2:morfologik-polish)
Requires:       mvn(org.carrot2:morfologik-stemming)
BuildArch:      noarch

%description analyzers-morfologik
A dictionary-driven lemmatizer for Polish (includes morphosyntactic
annotations).

%files analyzers-morfologik -f .mfiles-analyzers-morfologik

%package analyzers-phonetic
Summary:        Lucene Phonetic Filters
Group:          Development/Libraries/Java
Requires:       mvn(commons-codec:commons-codec)
Requires:       mvn(org.apache.lucene:lucene-analyzers-common)
Requires:       mvn(org.apache.lucene:lucene-core)
BuildArch:      noarch

%description analyzers-phonetic
Provides phonetic encoding via Commons Codec.

%files analyzers-phonetic -f .mfiles-analyzers-phonetic

%package analyzers-uima
Summary:        Lucene UIMA Analysis Components
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-analyzers-common)
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.uima:Tagger)
Requires:       mvn(org.apache.uima:WhitespaceTokenizer)
Requires:       mvn(org.apache.uima:uimaj-core)
BuildArch:      noarch

%description analyzers-uima
Lucene Integration with UIMA for extracting metadata from arbitrary (text)
fields and enrich document with features extracted from UIMA types (language,
sentences, concepts, named entities, etc.).

%files analyzers-uima -f .mfiles-analyzers-uima

%package benchmark
Summary:        Lucene Benchmarking Module
Group:          Development/Libraries/Java
Requires:       mvn(com.ibm.icu:icu4j)
Requires:       mvn(net.sourceforge.nekohtml:nekohtml)
Requires:       mvn(org.apache.commons:commons-compress)
Requires:       mvn(org.apache.lucene:lucene-analyzers-common)
Requires:       mvn(org.apache.lucene:lucene-codecs)
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.lucene:lucene-facet)
Requires:       mvn(org.apache.lucene:lucene-highlighter)
Requires:       mvn(org.apache.lucene:lucene-join)
Requires:       mvn(org.apache.lucene:lucene-memory)
Requires:       mvn(org.apache.lucene:lucene-queries)
Requires:       mvn(org.apache.lucene:lucene-queryparser)
Requires:       mvn(org.apache.lucene:lucene-spatial-extras)
Requires:       mvn(org.locationtech.spatial4j:spatial4j)
Requires:       mvn(xerces:xercesImpl)
BuildArch:      noarch

%description benchmark
Lucene Benchmarking Module.

%files benchmark -f .mfiles-benchmark

%package demo
Summary:        Lucene Demo Module
Group:          Development/Libraries/Java
Requires:       mvn(javax.servlet:servlet-api)
Requires:       mvn(org.apache.lucene:lucene-analyzers-common)
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.lucene:lucene-expressions)
Requires:       mvn(org.apache.lucene:lucene-facet)
Requires:       mvn(org.apache.lucene:lucene-queries)
Requires:       mvn(org.apache.lucene:lucene-queryparser)
BuildArch:      noarch

%description
Demo for Apache Lucene Java.

%files demo -f .mfiles-demo

%package expressions
Summary:        Lucene Expressions Module
Group:          Development/Libraries/Java
Requires:       mvn(org.antlr:antlr4-runtime)
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.ow2.asm:asm)
Requires:       mvn(org.ow2.asm:asm-commons)
BuildArch:      noarch

%description expressions
Dynamically computed values to sort/facet/search on based on a pluggable
grammar.

%files expressions -f .mfiles-expressions

%package replicator
Summary:        Lucene Replicator Module
Group:          Development/Libraries/Java
Requires:       mvn(commons-logging:commons-logging)
Requires:       mvn(javax.servlet:javax.servlet-api)
Requires:       mvn(org.apache.httpcomponents:httpclient)
Requires:       mvn(org.apache.httpcomponents:httpcore)
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.lucene:lucene-facet)
Requires:       mvn(org.eclipse.jetty:jetty-continuation)
Requires:       mvn(org.eclipse.jetty:jetty-http)
Requires:       mvn(org.eclipse.jetty:jetty-io)
Requires:       mvn(org.eclipse.jetty:jetty-server)
Requires:       mvn(org.eclipse.jetty:jetty-servlet)
Requires:       mvn(org.eclipse.jetty:jetty-util)
BuildArch:      noarch

%description replicator
Lucene Replicator Module.

%files replicator -f .mfiles-replicator

%package spatial-extras
Summary:        Spatial Strategies for Apache Lucene
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-core)
Requires:       mvn(org.apache.lucene:lucene-spatial3d)
Requires:       mvn(org.locationtech.spatial4j:spatial4j)
BuildArch:      noarch

%description spatial-extras
Spatial Strategies for Apache Lucene.

%files spatial-extras -f .mfiles-spatial-extras

%package suggest
Summary:        Lucene Suggest Module
Group:          Development/Libraries/Java
Requires:       mvn(org.apache.lucene:lucene-analyzers-common)
Requires:       mvn(org.apache.lucene:lucene-core)
BuildArch:      noarch

%description suggest
Lucene Suggest Module.

%files suggest -f .mfiles-suggest

%package test-framework
Summary:        Apache Lucene Java Test Framework
Group:          Development/Libraries/Java
Requires:       mvn(com.carrotsearch.randomizedtesting:randomizedtesting-runner)
Requires:       mvn(junit:junit)
Requires:       mvn(org.apache.lucene:lucene-codecs)
Requires:       mvn(org.apache.lucene:lucene-core)
BuildArch:      noarch

%description test-framework
Apache Lucene Java Test Framework.

%files test-framework -f .mfiles-test-framework

%endif

%prep
%setup -q

%patch0 -p2
%patch1 -p2
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export CLASSPATH=$(build-classpath commons-digester jtidy junit regexp)
export OPT_JAR_LIST=:
%{ant} \
  -Djavacc.home=%{_bindir}/javacc \
  -Djavacc.jar=%{_javadir}/javacc.jar \
  -Djavacc.jar.dir=%{_javadir} \
  -Djavadoc.link=%{_javadocdir}/java \
  -Dversion=%{version} \
  -Divy.mode=local -Divy.available=true

# DOESN'T BUILD BECAUSE OF MISSING DEPS: replicator expressions facet spatial-extras analyzers-kuromoji analyzers-morfologik analyzers-phonetic
export modules="queryparser join queries classification codecs backward-codecs grouping highlighter memory misc sandbox spatial3d monitor"

for mod in $modules
do
  echo "BUILDING MODULE ${mod}"
  %{ant} -f module-build.xml \
    -Djavacc.home=%{_bindir}/javacc \
    -Djavacc.jar=%{_javadir}/javacc.jar \
    -Djavacc.jar.dir=%{_javadir} \
    -Djavadoc.link=%{_javadocdir}/java \
    -Dversion=%{version} \
    -Divy.mode=local -Divy.available=true \
  jar-$mod
done

export modanalyzers="common smartcn stempel"
pushd analysis
%{ant} \
  -Djavacc.home=%{_bindir}/javacc \
  -Djavacc.jar=%{_javadir}/javacc.jar \
  -Djavacc.jar.dir=%{_javadir} \
  -Djavadoc.link=%{_javadocdir}/java \
  -Dversion=%{version} \
  -Divy.mode=local -Divy.available=true \
$modanalyzers

%install
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -d -m 0755 %{buildroot}%{_jnidir}/%{name}

# maven pom dir
install -d -m 0755 %{buildroot}%{_mavenpomdir}/%{name}

export noarch_modules="core queryparser join queries classification codecs backward-codecs grouping highlighter memory sandbox spatial3d monitor"
for mod in $noarch_modules
do
  install -p -m 0644 build/${mod}/%{name}-$mod-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-$mod.jar
  ln -sf %{name}/%{name}-$mod.jar %{buildroot}%{_javadir}/%{name}-$mod.jar
  cp %{_sourcedir}/%{name}-${mod}-%{version}.pom build/${mod}/pom.xml
  %pom_remove_parent build/${mod}
  %pom_xpath_inject "pom:project" "<version>%{version}</version>" build/${mod}
  install -p -m 0644 build/${mod}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-${mod}.pom
  %add_maven_depmap %{name}/%{name}-${mod}.pom %{name}/%{name}-${mod}.jar -f ${mod}
  echo %{_javadir}/%{name}-$mod.jar >> .mfiles-${mod}
done

export arch_modules="misc"
for mod in $arch_modules
do
  install -p -m 0644 build/${mod}/%{name}-$mod-%{version}.jar %{buildroot}%{_jnidir}/%{name}/%{name}-$mod.jar
  ln -sf %{name}/%{name}-$mod.jar %{buildroot}%{_jnidir}/%{name}-$mod.jar
  cp %{_sourcedir}/%{name}-${mod}-%{version}.pom build/${mod}/pom.xml
  %pom_remove_parent build/${mod}
  %pom_xpath_inject "pom:project" "<version>%{version}</version>" build/${mod}
  install -p -m 0644 build/${mod}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-${mod}.pom
  %add_maven_depmap %{name}/%{name}-${mod}.pom %{name}/%{name}-${mod}.jar -f ${mod}
  echo %{_jnidir}/%{name}-$mod.jar >> .mfiles-${mod}
done

export modanalyzers="common smartcn stempel"
for mod in $modanalyzers
do
  install -p -m 0644 build/analysis/$mod/%{name}-analyzers-$mod-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-analyzers-${mod}.jar
  ln -sf %{name}/%{name}-analyzers-$mod.jar %{buildroot}%{_javadir}/%{name}-analyzers-$mod.jar
  cp %{_sourcedir}/lucene-analyzers-${mod}-%{version}.pom build/analysis/$mod/pom.xml
  %pom_remove_parent build/analysis/$mod
  %pom_xpath_inject "pom:project" "<version>%{version}</version>" build/analysis/$mod
  install -p -m 0644 build/analysis/$mod/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-analyzers-${mod}.pom
  %add_maven_depmap %{name}/%{name}-analyzers-${mod}.pom %{name}/%{name}-analyzers-${mod}.jar -f analyzers-${mod}
  echo %{_javadir}/%{name}-analyzers-$mod.jar >> .mfiles-analyzers-${mod}
done

# javadoc DOES NOT BUILD BECAUSE OF MISSING MVN DEPS
# javadoc
#install -d -m 0755 %%{buildroot}%%{_javadocdir}/%%{name}
#cp -pr build/docs/api/* \
#  %%{buildroot}%%{_javadocdir}/%%{name}

%changelog
