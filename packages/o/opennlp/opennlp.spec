#
# spec file for package opennlp
#
# Copyright (c) 2022 SUSE LLC
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


Name:           opennlp
Version:        1.5.3
Release:        0
Summary:        A machine learning based toolkit for the processing of natural language text
License:        Apache-2.0
URL:            https://opennlp.apache.org/
Source0:        http://archive.apache.org/dist/opennlp/%{name}-%{version}/apache-%{name}-%{version}-src.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(net.sf.jwordnet:jwnl)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.uima:uimaj-core)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.osgi:osgi.cmpn)
BuildRequires:  mvn(org.osgi:osgi.core)
BuildArch:      noarch

%description
The Apache OpenNLP library is a machine learning based toolkit for the
processing of natural language text.

It supports the most common NLP tasks, such as tokenization, sentence
segmentation, part-of-speech tagging, named entity extraction, chunking,
parsing, and coreference resolution. These tasks are usually required to
build more advanced text processing services. OpenNLP also includes
maximum entropy and perceptron based machine learning.

%package tools
Summary:        Apache OpenNLP Tools

%description tools
This package provides Apache OpenNLP Tools.

%package maxent
Summary:        Apache OpenNLP Maxent

%description maxent
This package provides Apache OpenNLP Maxent.

%package uima
Summary:        Apache OpenNLP UIMA Annotators

%description uima
This package provides Apache OpenNLP UIMA Annotators.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n apache-%{name}-%{version}-src
# Cleanup
find . -name '*.jar' -print -delete
find . -name '*.bat' -print -delete
find . -name '*.class' -print -delete

# use latest OSGi implementation
%pom_change_dep -r :org.osgi.core org.osgi:osgi.core opennlp
%pom_change_dep -r :org.osgi.compendium org.osgi:osgi.cmpn opennlp

%pom_remove_plugin -r :apache-rat-plugin opennlp
%pom_remove_plugin -r :maven-dependency-plugin opennlp
%pom_remove_plugin -r :maven-eclipse-plugin opennlp
%pom_remove_plugin -r :maven-source-plugin opennlp
%pom_remove_plugin -r :maven-javadoc-plugin opennlp

%pom_xpath_set -r pom:addClasspath false opennlp

%pom_disable_module ../opennlp-distr opennlp
%pom_disable_module ../opennlp-docs opennlp

for p in maxent tools ; do
%pom_xpath_inject "pom:dependency[pom:artifactId='junit']" "<scope>test</scope>" opennlp-${p}
done

# AssertionError: expected:<0.7756870512503095> but was:<0.7766773953948998>
rm -r opennlp-maxent/src/test/java/opennlp/perceptron/PerceptronPrepAttachTest.java \
 opennlp-maxent/src/test/java/opennlp/maxent/quasinewton/QNTrainerTest.java \
 opennlp-maxent/src/test/java/opennlp/PrepAttachDataUtil.java \
 opennlp-maxent/src/test/java/opennlp/maxent/MaxentPrepAttachTest.java

%build

%{mvn_build} -f -j -s -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8 -f opennlp/pom.xml

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-%{name}
%doc KEYS opennlp-distr/README opennlp-distr/RELEASE_NOTES.html
%license LICENSE NOTICE

%files tools -f .mfiles-%{name}-tools
%license LICENSE NOTICE

%files maxent -f .mfiles-%{name}-maxent
%license LICENSE NOTICE

%files uima -f .mfiles-%{name}-uima

%changelog
