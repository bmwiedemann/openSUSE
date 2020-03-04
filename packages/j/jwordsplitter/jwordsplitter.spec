#
# spec file for package jwordsplitter
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


Name:           jwordsplitter
Version:        4.4
Release:        0
Summary:        A Java library to split German compound words
License:        Apache-2.0
URL:            https://github.com/danielnaber/%{name}
Source0:        https://github.com/danielnaber/%{name}/archive/v%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
This Java library can split German compound words into smaller parts.
This is especially useful for German words but it can work with all languages,
as long as a dictionary and a class extending AbstractWordSplitter is provided.
So far, only German is supported and a German dictionary is included in the JAR.
Even though it will work for some adjectives it works best for nouns.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :maven-source-plugin

rm -f \
	src/main/resources/de/danielnaber/jwordsplitter/wordsGerman.ser \
	src/main/resources/de/danielnaber/jwordsplitter/all-words.txt

%build
%{mvn_build} -f -- -Dsource=7
# Generate the wordsGerman.ser file
grep -v -f src/main/resources/de/danielnaber/jwordsplitter/removals.txt \
	src/main/resources/de/danielnaber/jwordsplitter/languagetool-dict.txt | cat - \
	src/main/resources/de/danielnaber/jwordsplitter/additions.txt \
	src/main/resources/de/danielnaber/jwordsplitter/germanPrefixes.txt | \
	grep -v "^#" >src/main/resources/de/danielnaber/jwordsplitter/all-words.txt
mkdir -p tmp/de/danielnaber/jwordsplitter
java -cp target/classes de.danielnaber.jwordsplitter.converter.SerializeDict \
	src/main/resources/de/danielnaber/jwordsplitter/all-words.txt \
	tmp/de/danielnaber/jwordsplitter/wordsGerman.ser


%install
%mvn_install
# include the wordGerman.ser in the jar
jar uf %{buildroot}%{_javadir}/%{name}/%{name}.jar -C tmp .
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
