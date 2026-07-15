#
# spec file for package opennlp
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.9.5
Release:        0
Summary:        A machine learning based toolkit for the processing of natural language text
License:        Apache-2.0
URL:            https://opennlp.apache.org/
Source0:        https://archive.apache.org/dist/opennlp/%{name}-%{version}/apache-%{name}-%{version}-src.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.uima:uimaj-core)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.carrot2:morfologik-stemming)
BuildRequires:  mvn(org.carrot2:morfologik-tools)
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
Provides:       %{name}-maxent = %{version}
Obsoletes:      %{name}-maxent < %{version}

%description tools
This package provides Apache OpenNLP Tools.

%package morfologik-addon
Summary:        Apache OpenNLP Morfologik Addon

%description morfologik-addon
This package provides Apache OpenNLP Morfologik Addon.

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
%pom_change_dep -r :org.osgi.core org.osgi:osgi.core
%pom_change_dep -r :org.osgi.compendium org.osgi:osgi.cmpn

%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :maven-eclipse-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :forbiddenapis
%pom_remove_plugin -r :maven-checkstyle-plugin

%pom_xpath_set pom:addClasspath false opennlp-tools

%pom_disable_module opennlp-brat-annotator
%pom_disable_module opennlp-distr
%pom_disable_module opennlp-docs

%build

%{mvn_build} -f -j -s

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-%{name}
%doc KEYS README.md
%license LICENSE NOTICE

%files tools -f .mfiles-%{name}-tools
%license LICENSE NOTICE

%files morfologik-addon -f .mfiles-%{name}-morfologik-addon

%files uima -f .mfiles-%{name}-uima

%changelog
