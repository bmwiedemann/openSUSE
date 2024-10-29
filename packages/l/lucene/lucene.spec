#
# spec file for package lucene
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


Name:           lucene
Version:        8.11.4
Release:        0
Summary:        Text search engine
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://lucene.apache.org/
Source0:        https://archive.apache.org/dist/lucene/java/%{version}/%{name}-%{version}-src.tgz
Source1:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analyzers-common/%{version}/lucene-analyzers-common-%{version}.pom
Source2:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analyzers-icu/%{version}/lucene-analyzers-icu-%{version}.pom
Source3:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analyzers-phonetic/%{version}/lucene-analyzers-phonetic-%{version}.pom
Source4:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analyzers-smartcn/%{version}/lucene-analyzers-smartcn-%{version}.pom
Source5:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-analyzers-stempel/%{version}/lucene-analyzers-stempel-%{version}.pom
Source6:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-backward-codecs/%{version}/lucene-backward-codecs-%{version}.pom
Source7:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-classification/%{version}/lucene-classification-%{version}.pom
Source8:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-codecs/%{version}/lucene-codecs-%{version}.pom
Source9:        https://repo1.maven.org/maven2/org/apache/lucene/lucene-core/%{version}/lucene-core-%{version}.pom
Source10:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-grouping/%{version}/lucene-grouping-%{version}.pom
Source11:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-facet/%{version}/lucene-facet-%{version}.pom
Source12:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-expressions/%{version}/lucene-expressions-%{version}.pom
Source13:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-highlighter/%{version}/lucene-highlighter-%{version}.pom
Source14:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-join/%{version}/lucene-join-%{version}.pom
Source15:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-memory/%{version}/lucene-memory-%{version}.pom
Source16:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-monitor/%{version}/lucene-monitor-%{version}.pom
Source17:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-parent/%{version}/lucene-parent-%{version}.pom
Source18:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-queries/%{version}/lucene-queries-%{version}.pom
Source19:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-queryparser/%{version}/lucene-queryparser-%{version}.pom
Source20:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-misc/%{version}/lucene-misc-%{version}.pom
Source21:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-sandbox/%{version}/lucene-sandbox-%{version}.pom
Source22:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-spatial3d/%{version}/lucene-spatial3d-%{version}.pom
Source23:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-spatial-extras/%{version}/lucene-spatial-extras-%{version}.pom
Source24:       https://repo1.maven.org/maven2/org/apache/lucene/lucene-suggest/%{version}/lucene-suggest-%{version}.pom
Patch0:         0001-Disable-ivy-settings.patch
Patch1:         0002-Dependency-generation.patch
Patch2:         lucene-osgi-manifests.patch
Patch3:         lucene-missing-dependencies.patch
Patch4:         lucene-nodoclint.patch
Patch5:         lucene-timestamps.patch
Patch6:         s2-geometry-library-java-2.0.0.patch
BuildRequires:  ant >= 1.6
BuildRequires:  ant-junit >= 1.6
BuildRequires:  antlr-java
BuildRequires:  antlr4-java
BuildRequires:  apache-commons-beanutils
BuildRequires:  apache-commons-codec
BuildRequires:  apache-commons-collections
BuildRequires:  apache-commons-digester
BuildRequires:  apache-commons-logging
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  hppc
BuildRequires:  icu4j
BuildRequires:  ivy-local
BuildRequires:  java-devel >= 1.8
BuildRequires:  javacc
BuildRequires:  javapackages-local >= 6
BuildRequires:  junit
BuildRequires:  objectweb-asm
BuildRequires:  regexp
BuildRequires:  s2-geometry-library-java
BuildRequires:  spatial4j
BuildRequires:  zip
#!BuildIgnore:  xerces-j2

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
BuildArch:      noarch

%description queryparser
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "queryparser" module for lucene.

%files queryparser -f .mfiles-queryparser

%package join
Summary:        Join module for lucene
Group:          Development/Libraries/Java
BuildArch:      noarch

%description join
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "join" module for lucene.

%files join -f .mfiles-join

%package queries
Summary:        Queries module for lucene
Group:          Development/Libraries/Java
BuildArch:      noarch

%description queries
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "queries" module for lucene.

%files queries -f .mfiles-queries

%package classification
Summary:        Classification module for lucene
Group:          Development/Libraries/Java
BuildArch:      noarch

%description classification
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "classification" module for Lucene.

%files classification -f .mfiles-classification

%package codecs
Summary:        Codecs module for lucene
Group:          Development/Libraries/Java
BuildArch:      noarch

%description codecs
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "codecs" module for Lucene.

%files codecs -f .mfiles-codecs

%package backward-codecs
Summary:        Backward-codecs module for lucene
Group:          Development/Libraries/Java
BuildArch:      noarch

%description backward-codecs
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "backward-codecs" module for Lucene.

%files backward-codecs -f .mfiles-backward-codecs

%package expressions
Summary:        Lucene Expressions
Group:          Development/Libraries/Java
BuildArch:      noarch

%description expressions
Dynamically computed values to sort/facet/search based on a pluggable
grammar.

%files expressions -f .mfiles-expressions

%package facet
Summary:        Facet module for lucene
Group:          Development/Libraries/Java
BuildArch:      noarch

%description facet
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "facet" module for Lucene.

%files facet -f .mfiles-facet

%package grouping
Summary:        Grouping module for lucene
Group:          Development/Libraries/Java
BuildArch:      noarch

%description grouping
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "grouping" module for Lucene.

%files grouping -f .mfiles-grouping

%package highlighter
Summary:        Highlighter module for lucene
Group:          Development/Libraries/Java
BuildArch:      noarch

%description highlighter
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "highlighter" module for Lucene.

%files highlighter -f .mfiles-highlighter

%package memory
Summary:        Memory module for lucene
Group:          Development/Libraries/Java
BuildArch:      noarch

%description memory
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "memory" module for Lucene.

%files memory -f .mfiles-memory

%package misc
Summary:        Misc module for lucene
Group:          Development/Libraries/Java

%description misc
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "misc" module for Lucene.

%files misc -f .mfiles-misc

%package monitor
Summary:        Spatial module for lucene
Group:          Development/Libraries/Java
BuildArch:      noarch

%description monitor
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "monitor" module for Lucene.

%files monitor -f .mfiles-monitor

%package sandbox
Summary:        Sandbox module for lucene
Group:          Development/Libraries/Java
BuildArch:      noarch

%description sandbox
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "sandbox" module for Lucene.

%files sandbox -f .mfiles-sandbox

%package spatial3d
Summary:        Spatial3d module for lucene
Group:          Development/Libraries/Java
BuildArch:      noarch

%description spatial3d
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "spatial3d" module for Lucene.

%files spatial3d -f .mfiles-spatial3d

%package spatial-extras
Summary:        Spatial Strategies for Apache Lucene
Group:          Development/Libraries/Java
BuildArch:      noarch

%description spatial-extras
Spatial Strategies for Apache Lucene.

%files spatial-extras -f .mfiles-spatial-extras

%package suggest
Summary:        Lucene Suggest Module
Group:          Development/Libraries/Java
BuildArch:      noarch

%description suggest
Lucene Suggest Module.

%files suggest -f .mfiles-suggest

%package analyzers-common
Summary:        Analyzers-common module for lucene
Group:          Development/Libraries/Java
Provides:       %{name}-analysis = %{version}-%{release}
Obsoletes:      %{name}-analysis < %{version}-%{release}
BuildArch:      noarch

%description analyzers-common
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "analyzers-common" module for Lucene.

%files analyzers-common -f .mfiles-analyzers-common

%package analyzers-icu
Summary:        Lucene ICU Analysis Components
Group:          Development/Libraries/Java
BuildArch:      noarch

%description analyzers-icu
Provides integration with ICU (International Components for Unicode) for
stronger Unicode and internationalization support.

%files analyzers-icu -f .mfiles-analyzers-icu

%package analyzers-phonetic
Summary:        Lucene Phonetic Filters
Group:          Development/Libraries/Java
BuildArch:      noarch

%description analyzers-phonetic
Provides phonetic encoding via Commons Codec.

%files analyzers-phonetic -f .mfiles-analyzers-phonetic

%package analyzers-smartcn
Summary:        Analyzers-smartcn module for lucene
Group:          Development/Libraries/Java
BuildArch:      noarch

%description analyzers-smartcn
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "analyzers-smartcn" module for Lucene.

%files analyzers-smartcn -f .mfiles-analyzers-smartcn

%package analyzers-stempel
Summary:        Analyzers-stempel module for lucene
Group:          Development/Libraries/Java
BuildArch:      noarch

%description analyzers-stempel
Apache Lucene is a full-text search engine written entirely in Java.
This package provides the "analyzers-stempel" module for Lucene.

%files analyzers-stempel -f .mfiles-analyzers-stempel

%if 0
%package analyzers-kuromoji
Summary:        Lucene Kuromoji Japanese Morphological Analyzer
Group:          Development/Libraries/Java
BuildArch:      noarch

%description analyzers-kuromoji
Lucene Kuromoji Japanese Morphological Analyzer.

%files analyzers-kuromoji -f .mfiles-analyzers-kuromoji

%package analyzers-morfologik
Summary:        Lucene Morfologik Polish Lemmatizer
Group:          Development/Libraries/Java
BuildArch:      noarch

%description analyzers-morfologik
A dictionary-driven lemmatizer for Polish (includes morphosyntactic
annotations).

%files analyzers-morfologik -f .mfiles-analyzers-morfologik

%package analyzers-nori
Summary:        Lucene Nori Korean Morphological Analyzer
Group:          Development/Libraries/Java
BuildArch:      noarch

%description analyzers-nori
Lucene Nori Korean Morphological Analyzer.

%files analyzers-nori -f .mfiles-analyzers-nori

%package analyzers-opennlp
Summary:        Lucene OpenNLP integration
Group:          Development/Libraries/Java
BuildArch:      noarch

%description analyzers-opennlp
Lucene OpenNLP integration.

%files analyzers-opennlp -f .mfiles-analyzers-opennlp

%package benchmark
Summary:        Lucene Benchmarking Module
Group:          Development/Libraries/Java
BuildArch:      noarch

%description benchmark
Lucene Benchmarking Module.

%files benchmark -f .mfiles-benchmark

%package demo
Summary:        Lucene Demo Module
Group:          Development/Libraries/Java
BuildArch:      noarch

%description
Demo for Apache Lucene Java.

%files demo -f .mfiles-demo

%package expressions
Summary:        Lucene Expressions Module
Group:          Development/Libraries/Java
BuildArch:      noarch

%description expressions
Dynamically computed values to sort/facet/search on based on a pluggable
grammar.

%files expressions -f .mfiles-expressions

%package replicator
Summary:        Lucene Replicator Module
Group:          Development/Libraries/Java
BuildArch:      noarch

%description replicator
Lucene Replicator Module.

%files replicator -f .mfiles-replicator

%package test-framework
Summary:        Apache Lucene Java Test Framework
Group:          Development/Libraries/Java
BuildArch:      noarch

%description test-framework
Apache Lucene Java Test Framework.

%files test-framework -f .mfiles-test-framework

%endif

%prep
%setup -q

%patch -P 0 -p2
%patch -P 1 -p2
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1

cp %{_sourcedir}/%{name}-spatial-extras-%{version}.pom spatial-extras/pom.xml
%pom_change_dep io.sgr:s2-geometry-library-java com.google.geometry:s2-geometry:2.0.0 spatial-extras

%build
ant \
  -Djavacc.home=%{_bindir}/javacc \
  -Djavacc.jar=%{_javadir}/javacc.jar \
  -Djavadoc.link=%{_javadocdir}/java \
  -Dversion=%{version} \
  -Divy.mode=local -Divy.available=true

# DOESN'T BUILD BECAUSE OF MISSING DEPS: replicator analyzers-kuromoji analyzers-morfologik
export modules="queryparser join queries classification codecs backward-codecs grouping highlighter memory misc monitor sandbox spatial3d spatial-extras suggest facet expressions"

for mod in $modules
do
  echo "BUILDING MODULE ${mod}"
  ant -f module-build.xml \
    -Djavacc.home=%{_bindir}/javacc \
    -Djavacc.jar=%{_javadir}/javacc.jar \
    -Djavacc.jar.dir=%{_javadir} \
    -Djavadoc.link=%{_javadocdir}/java \
    -Dversion=%{version} \
    -Divy.mode=local -Divy.available=true \
  jar-$mod
done

export modanalyzers="common icu phonetic smartcn stempel"
pushd analysis
ant \
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

export noarch_modules="core queryparser join queries classification codecs backward-codecs grouping highlighter memory monitor sandbox spatial3d spatial-extras suggest facet expressions"
for mod in $noarch_modules
do
  install -p -m 0644 build/${mod}/%{name}-$mod-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-$mod.jar
  ln -sf %{name}/%{name}-$mod.jar %{buildroot}%{_javadir}/%{name}-$mod.jar
  if [ -f ${mod}/pom.xml ]; then
    %{mvn_install_pom} ${mod}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-${mod}.pom
  else
    %{mvn_install_pom} %{_sourcedir}/%{name}-${mod}-%{version}.pom %{buildroot}%{_mavenpomdir}/%{name}/%{name}-${mod}.pom
  fi
  %add_maven_depmap %{name}/%{name}-${mod}.pom %{name}/%{name}-${mod}.jar -f ${mod}
  echo %{_javadir}/%{name}-$mod.jar >> .mfiles-${mod}
done

export arch_modules="misc"
for mod in $arch_modules
do
  install -p -m 0644 build/${mod}/%{name}-$mod-%{version}.jar %{buildroot}%{_jnidir}/%{name}/%{name}-$mod.jar
  ln -sf %{name}/%{name}-$mod.jar %{buildroot}%{_jnidir}/%{name}-$mod.jar
  %{mvn_install_pom} %{_sourcedir}/%{name}-${mod}-%{version}.pom %{buildroot}%{_mavenpomdir}/%{name}/%{name}-${mod}.pom
  %add_maven_depmap %{name}/%{name}-${mod}.pom %{name}/%{name}-${mod}.jar -f ${mod}
  echo %{_jnidir}/%{name}-$mod.jar >> .mfiles-${mod}
done

export modanalyzers="common icu phonetic smartcn stempel"
for mod in $modanalyzers
do
  install -p -m 0644 build/analysis/$mod/%{name}-analyzers-$mod-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-analyzers-${mod}.jar
  ln -sf %{name}/%{name}-analyzers-$mod.jar %{buildroot}%{_javadir}/%{name}-analyzers-$mod.jar
  %{mvn_install_pom} %{_sourcedir}/lucene-analyzers-${mod}-%{version}.pom %{buildroot}%{_mavenpomdir}/%{name}/%{name}-analyzers-${mod}.pom
  %add_maven_depmap %{name}/%{name}-analyzers-${mod}.pom %{name}/%{name}-analyzers-${mod}.jar -f analyzers-${mod}
  echo %{_javadir}/%{name}-analyzers-$mod.jar >> .mfiles-analyzers-${mod}
done

%changelog
