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
Version:        2.5.13
Release:        0
Summary:        A machine learning based toolkit for the processing of natural language text
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://opennlp.apache.org/
Source0:        https://archive.apache.org/dist/opennlp/%{name}-%{version}/apache-%{name}-%{version}-src.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 17
BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.uima:uimaj-core)
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.carrot2:morfologik-stemming)
BuildRequires:  mvn(org.carrot2:morfologik-tools)
BuildRequires:  mvn(org.slf4j:slf4j-api)
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
Group:          Development/Libraries/Java

%description tools
This package provides Apache OpenNLP Tools.

%package morfologik-addon
Summary:        Apache OpenNLP Morfologik Addon
Group:          Development/Libraries/Java

%description morfologik-addon
This package provides Apache OpenNLP Morfologik Addon.

%package uima
Summary:        Apache OpenNLP UIMA Annotators
Group:          Development/Libraries/Java

%description uima
This package provides Apache OpenNLP UIMA Annotators.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n apache-%{name}-%{version}-src
# Cleanup
find . -name '*.jar' -print -delete
find . -name '*.bat' -print -delete
find . -name '*.class' -print -delete

%pom_remove_plugin -r :apache-rat-plugin
%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :maven-eclipse-plugin
%pom_remove_plugin -r :license-maven-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :forbiddenapis
%pom_remove_plugin -r :maven-checkstyle-plugin
%pom_remove_plugin -r :maven-failsafe-plugin

%pom_xpath_set pom:addClasspath false opennlp-tools

%pom_disable_module opennlp-dl
%pom_disable_module opennlp-dl-gpu
%pom_disable_module opennlp-distr
%pom_disable_module opennlp-docs
%pom_disable_module opennlp-tools-models

%build

%{mvn_build} -f -s

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-%{name}
%doc README.md
%license LICENSE NOTICE

%files tools -f .mfiles-%{name}-tools
%license LICENSE NOTICE

%files morfologik-addon -f .mfiles-%{name}-morfologik-addon

%files uima -f .mfiles-%{name}-uima

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
