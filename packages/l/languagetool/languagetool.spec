#
# spec file for package languagetool
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


Name:           languagetool
Version:        4.8
Release:        0
Summary:        Style and Grammar Checker for 25+ Languages
License:        LGPL-2.1-or-later
URL:            https://languagetool.org
Source0:        https://github.com/languagetool-org/%{name}/archive/v%{version}.tar.gz
# Newer mavens
Patch0:         languagetool-descriptor.patch
Patch1:         languagetool-xgboost-predictor.patch
Patch2:         languagetool-hunspell.patch
Patch3:         languagetool-4.8-lucene-8.patch
Patch4:         languagetool-test-resource.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  xmvn-subst
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(com.auth0:java-jwt)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.hankcs:aho-corasick-double-array-trie)
BuildRequires:  mvn(com.intellij:annotations)
BuildRequires:  mvn(commons-cli:commons-cli)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(de.danielnaber:german-pos-dict)
BuildRequires:  mvn(de.danielnaber:jwordsplitter)
BuildRequires:  mvn(edu.washington.cs.knowitall:opennlp-chunk-models)
BuildRequires:  mvn(edu.washington.cs.knowitall:opennlp-postag-models)
BuildRequires:  mvn(edu.washington.cs.knowitall:opennlp-tokenize-models)
BuildRequires:  mvn(edu.washington.cs.knowitall:openregex)
BuildRequires:  mvn(io.prometheus:simpleclient)
BuildRequires:  mvn(io.prometheus:simpleclient_guava)
BuildRequires:  mvn(io.prometheus:simpleclient_hotspot)
BuildRequires:  mvn(io.prometheus:simpleclient_httpserver)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-collections4)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.opennlp:opennlp-tools)
BuildRequires:  mvn(org.carrot2:morfologik-tools)
BuildRequires:  mvn(org.languagetool:languagetool-core)
BuildRequires:  mvn(org.languagetool:languagetool-core::tests:)
BuildRequires:  mvn(org.languagetool:languagetool-tools)
BuildRequires:  mvn(org.mariadb.jdbc:mariadb-java-client)
BuildRequires:  mvn(org.mybatis:mybatis)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.softcatala:catalan-pos-dict)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
Requires:       apache-commons-cli
Requires:       apache-commons-codec
Requires:       apache-commons-collections4
Requires:       apache-commons-csv
Requires:       apache-commons-io
Requires:       apache-commons-lang3
Requires:       apache-commons-logging
Requires:       apache-commons-pool2
Requires:       apache-commons-text
Requires:       bcel
Requires:       berkeleylm
Requires:       beust-jcommander
Requires:       catalan-pos-dict
Requires:       german-pos-dict
Requires:       glassfish-fastinfoset
Requires:       glassfish-jaxb-api
Requires:       glassfish-jaxb-runtime
Requires:       glassfish-jaxb-txw2
Requires:       guava
Requires:       hamcrest-core
Requires:       hppc
Requires:       indriya
Requires:       istack-commons-runtime
Requires:       jackson-annotations
Requires:       jackson-core
Requires:       jackson-databind
Requires:       jaf
Requires:       jafama
Requires:       java-jwt
Requires:       jetbrains-annotations
Requires:       jna
Requires:       jsr-305
Requires:       junit
Requires:       jwnl
Requires:       jwordsplitter
Requires:       kryo
Requires:       language-detector
Requires:       languagetool-core
Requires:       languagetool-core-tests
Requires:       languagetool-libs = %{version}-%{release}
Requires:       languagetool-tools
Requires:       logback
Requires:       mariadb-java-client
Requires:       minlog
Requires:       morfologik-stemming
Requires:       mybatis
Requires:       objectweb-asm
Requires:       objenesis
Requires:       opennlp-chunk-models
Requires:       opennlp-maxent
Requires:       opennlp-postag-models
Requires:       opennlp-tokenize-models
Requires:       opennlp-tools
Requires:       openregex
Requires:       prometheus-simpleclient-java
Requires:       prometheus-simpleclient-java-common
Requires:       prometheus-simpleclient-java-guava
Requires:       prometheus-simpleclient-java-hotspot
Requires:       prometheus-simpleclient-java-httpserver
Requires:       reflectasm
Requires:       regexp
Requires:       scala
Requires:       segment
Requires:       slf4j
Requires:       stax-ex
Requires:       typesafe-config
Requires:       unit-api
Requires:       uom-lib-common
Requires:       xgboost
Requires:       xgboost-predictor
%requires_ge    lucene-backward-codecs
%requires_ge    lucene-core

%description
LanguageTool is a free and open-source grammar checker.

%package libs
Summary:        Style and Grammar Checker for 25+ Languages (libraries)
BuildArch:      noarch

%description libs
LanguageTool is a free and open-source grammar checker.

This package contains the jar files built by languagetool
project.

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%if %{?pkg_vcmp:%pkg_vcmp lucene-core >= 8}%{!?pkg_vcmp:0}
%patch -P 3 -p1
%endif
%patch -P 4 -p1

# We built these ones in another spec file
%pom_disable_module languagetool-core
%pom_disable_module languagetool-tools

%{mvn_package} :languagetool-parent __noinstall
%{mvn_package} ::zip:: __noinstall

%build

# Remove unneeded dependencies
%pom_xpath_remove pom:project/pom:build/pom:extensions
%pom_xpath_remove pom:project/pom:build/pom:plugins languagetool-core

# The following language modules are disabled because of
# missing dependencies. Later, one can work through them
# package what is needed
%pom_disable_module languagetool-language-modules/zh
%pom_remove_dep -r :language-zh

%pom_disable_module languagetool-language-modules/el
%pom_remove_dep -r :language-el

%pom_disable_module languagetool-language-modules/ja
%pom_remove_dep -r :language-ja

%pom_disable_module languagetool-language-modules/uk
%pom_remove_dep -r :language-uk

%pom_disable_module languagetool-office-extension

%pom_disable_module languagetool-wikipedia
%pom_remove_dep -r :languagetool-wikipedia

%pom_disable_module languagetool-dev

%pom_disable_module languagetool-rpm-package

%{mvn_build} -f -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

install -dm 0755 %{buildroot}%{_datadir}/%{name}
cp -r languagetool-standalone/target/LanguageTool-%{version}/LanguageTool-%{version}/* %{buildroot}%{_datadir}/%{name}
# the file-aggregator creates a file with too restrictive permissions
chmod 0644 %{buildroot}%{_datadir}/%{name}/META-INF/org/languagetool/language-module.properties
xmvn-subst -R %{buildroot} -s %{buildroot}%{_datadir}/%{name}/libs
%fdupes -s %{buildroot}%{_datadir}/%{name}

%files
%{_datadir}/%{name}
%license COPYING.txt
%doc README.md

%files libs -f .mfiles
%license COPYING.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license COPYING.txt
%doc README.md

%changelog
