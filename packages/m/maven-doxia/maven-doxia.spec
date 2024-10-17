#
# spec file for package maven-doxia
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


Name:           maven-doxia
Version:        2.0.0
Release:        0
Summary:        Content generation framework
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/doxia/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.tar.xz
Source2:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  apache-commons-lang3
BuildRequires:  apache-commons-text
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  jetbrains-annotations
BuildRequires:  modello
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  sisu-inject
BuildRequires:  slf4j
BuildArch:      noarch

%description
Doxia is a content generation framework which provides techniques for
generating static and dynamic content. Doxia can be used to generate
static sites in addition to being incorporated into dynamic content
generation systems like blogs, wikis and content management systems.

%package core
Summary:        Core module for %{name}
Group:          Development/Libraries/Java
# Make the upgrades easier. The last version
# before 2.0.0 was 1.12.0
Obsoletes:      %{name}-logging-api < 1.13
Obsoletes:      %{name}-module-confluence < 1.13
Obsoletes:      %{name}-module-docbook-simple < 1.13
Obsoletes:      %{name}-module-fo < 1.13
Obsoletes:      %{name}-module-itext < 1.13
Obsoletes:      %{name}-module-latex < 1.13
Obsoletes:      %{name}-module-markdown < 1.13
Obsoletes:      %{name}-module-rtf < 1.13
Obsoletes:      %{name}-module-twiki < 1.13
Obsoletes:      %{name}-module-xhtml < 1.13

%description core
This package provides %{summary}.

%package module-apt
Summary:        APT module for %{name}
Group:          Development/Libraries/Java

%description module-apt
This package provides %{summary}.

%package module-fml
Summary:        FML module for %{name}
Group:          Development/Libraries/Java

%description module-fml
This package provides %{summary}.

%package module-xdoc
Summary:        XDoc module for %{name}
Group:          Development/Libraries/Java

%description module-xdoc
This package provides %{summary}.

%package module-xhtml5
Summary:        XHTML5 module for %{name}
Group:          Development/Libraries/Java

%description module-xhtml5
This package provides %{summary}.

%package sink-api
Summary:        Sink-api module for %{name}
Group:          Development/Libraries/Java

%description sink-api
This package provides %{summary}.

%package test-docs
Summary:        Test-docs module for %{name}
Group:          Development/Libraries/Java

%description test-docs
This package provides %{summary}.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -a1
cp %{SOURCE2} LICENSE

%build
mkdir -p lib
build-jar-repository -s lib \
    apache-commons-lang3 \
    apache-commons-text/commons-text \
    atinject \
    commons-io \
    jetbrains-annotations \
    org.eclipse.sisu.inject \
    plexus/utils \
    plexus/xml \
    slf4j/api

ant package javadoc

mkdir -p target/site/apidocs

%install
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}

for i in \
    doxia-sink-api \
    doxia-test-docs \
    doxia-core; do
  install -pm 0644 ${i}/target/${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${i}.jar
  %{mvn_install_pom} ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar -f ${i}
  if [ -d ${i}/target/site/apidocs ]; then
    cp -r ${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${i}
  fi
done

for i in \
    doxia-module-apt \
    doxia-module-fml \
    doxia-module-xdoc \
    doxia-module-xhtml5; do
  install -pm 0644 doxia-modules/${i}/target/${i}-%{version}.jar %{buildroot}%{_javadir}/%{name}/${i}.jar
  %{mvn_install_pom} doxia-modules/${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar -f ${i}
  if [ -d doxia-modules/${i}/target/site/apidocs ]; then
    cp -r doxia-modules/${i}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/${i}
  fi
done

%fdupes -s %{buildroot}%{_javadocdir}

%files core -f .mfiles-doxia-core
%license LICENSE

%files module-apt -f .mfiles-doxia-module-apt

%files module-fml -f .mfiles-doxia-module-fml

%files module-xdoc -f .mfiles-doxia-module-xdoc

%files module-xhtml5 -f .mfiles-doxia-module-xhtml5

%files sink-api -f .mfiles-doxia-sink-api

%files test-docs -f .mfiles-doxia-test-docs

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
