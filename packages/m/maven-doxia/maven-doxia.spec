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
Version:        1.12.0
Release:        0
Summary:        Content generation framework
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/doxia/
Source0:        https://repo1.maven.org/maven2/org/apache/maven/doxia/doxia/%{version}/doxia-%{version}-source-release.zip
Source1:        %{name}-build.tar.xz
Patch0:         0002-Commons-configuration2.patch
BuildRequires:  ant
BuildRequires:  apache-commons-configuration2
BuildRequires:  apache-commons-lang3
BuildRequires:  apache-commons-text
BuildRequires:  fdupes
BuildRequires:  httpcomponents-client
BuildRequires:  httpcomponents-core
BuildRequires:  javapackages-local
BuildRequires:  modello >= 2.0.0
BuildRequires:  parboiled
BuildRequires:  pegdown
BuildRequires:  plexus-containers-component-annotations
BuildRequires:  plexus-metadata-generator
BuildRequires:  plexus-utils
BuildRequires:  plexus-xml
BuildRequires:  sisu-plexus
BuildRequires:  unzip
BuildRequires:  xmlgraphics-commons
BuildRequires:  xmlgraphics-fop
BuildRequires:  xmlunit
BuildRequires:  xmvn-install
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildArch:      noarch

%description
Doxia is a content generation framework which provides techniques for
generating static and dynamic content. Doxia can be used to generate
static sites in addition to being incorporated into dynamic content
generation systems like blogs, wikis and content management systems.

%package core
Summary:        Core module for %{name}
Group:          Development/Libraries/Java
Obsoletes:      %{name}-module-itext
Obsoletes:      %{name}-module-markdown

%description core
This package provides %{summary}.

%package logging-api
Summary:        Logging-api module for %{name}
Group:          Development/Libraries/Java

%description logging-api
This package provides %{summary}.

%package module-apt
Summary:        APT module for %{name}
Group:          Development/Libraries/Java

%description module-apt
This package provides %{summary}.

%package module-confluence
Summary:        Confluence module for %{name}
Group:          Development/Libraries/Java

%description module-confluence
This package provides %{summary}.

%package module-docbook-simple
Summary:        Simplified DocBook module for %{name}
Group:          Development/Libraries/Java

%description module-docbook-simple
This package provides %{summary}.

%package module-fml
Summary:        FML module for %{name}
Group:          Development/Libraries/Java

%description module-fml
This package provides %{summary}.

%package module-fo
Summary:        FO module for %{name}
Group:          Development/Libraries/Java

%description module-fo
This package provides %{summary}.

%package module-latex
Summary:        Latex module for %{name}
Group:          Development/Libraries/Java

%description module-latex
This package provides %{summary}.

%package module-rtf
Summary:        RTF module for %{name}
Group:          Development/Libraries/Java

%description module-rtf
This package provides %{summary}.

%package module-twiki
Summary:        TWiki module for %{name}
Group:          Development/Libraries/Java

%description module-twiki
This package provides %{summary}.

%package module-xdoc
Summary:        XDoc module for %{name}
Group:          Development/Libraries/Java

%description module-xdoc
This package provides %{summary}.

%package module-xhtml
Summary:        XHTML module for %{name}
Group:          Development/Libraries/Java

%description module-xhtml
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
%setup -q -n doxia-%{version} -a1
%patch -P 0 -p1

# we don't have clirr-maven-plugin
%pom_remove_plugin org.codehaus.mojo:clirr-maven-plugin pom.xml

# complains
%pom_remove_plugin :apache-rat-plugin

# requires network
rm doxia-core/src/test/java/org/apache/maven/doxia/util/XmlValidatorTest.java

%pom_add_dep org.codehaus.plexus:plexus-xml:3.0.0 doxia-core
for i in doxia-module-docbook-simple doxia-module-fml doxia-module-fo doxia-module-itext doxia-module-markdown doxia-module-xdoc doxia-module-xhtml doxia-module-xhtml5; do
  %pom_add_dep org.codehaus.plexus:plexus-xml:3.0.0 doxia-modules/${i}
done

%pom_disable_module doxia-module-itext doxia-modules
%pom_disable_module doxia-module-markdown doxia-modules

%{mvn_package} :doxia __noinstall
%{mvn_package} :doxia-modules __noinstall
%{mvn_package} :{*} @1

%build
mkdir -p lib
build-jar-repository -s lib \
    apache-commons-text \
    commons-configuration2 \
    commons-lang3 \
    httpcomponents/httpclient \
    httpcomponents/httpcore \
    org.eclipse.sisu.plexus \
    parboiled/core \
    pegdown \
    plexus-containers/plexus-component-annotations \
    plexus/utils \
    plexus/xml \
    xmlgraphics-commons \
    xmlgraphics-fop

%{ant} -Dtest.skip=true \
    package javadoc

mkdir -p target/site/apidocs

%{mvn_artifact} pom.xml
for i in \
    doxia-logging-api \
    doxia-sink-api \
    doxia-test-docs \
    doxia-core; do
  %{mvn_artifact} ${i}/pom.xml ${i}/target/${i}-%{version}.jar
  if [ -d ${i}/target/site/apidocs ]; then
    cp -r ${i}/target/site/apidocs target/site/apidocs/${i}
  fi
done

%{mvn_artifact} doxia-modules/pom.xml
for i in \
    doxia-module-apt \
    doxia-module-confluence \
    doxia-module-docbook-simple \
    doxia-module-fml \
    doxia-module-fo \
    doxia-module-latex \
    doxia-module-rtf \
    doxia-module-twiki \
    doxia-module-xdoc \
    doxia-module-xhtml \
    doxia-module-xhtml5; do
  %{mvn_artifact} doxia-modules/${i}/pom.xml doxia-modules/${i}/target/${i}-%{version}.jar
  if [ -d doxia-modules/${i}/target/site/apidocs ]; then
    cp -r doxia-modules/${i}/target/site/apidocs target/site/apidocs/${i}
  fi
done

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files core -f .mfiles-doxia-core

%files logging-api -f .mfiles-doxia-logging-api
%license LICENSE
%doc NOTICE

%files module-apt -f .mfiles-doxia-module-apt

%files module-confluence -f .mfiles-doxia-module-confluence

%files module-docbook-simple -f .mfiles-doxia-module-docbook-simple

%files module-fml -f .mfiles-doxia-module-fml

%files module-fo -f .mfiles-doxia-module-fo

%files module-latex -f .mfiles-doxia-module-latex

%files module-rtf -f .mfiles-doxia-module-rtf

%files module-twiki -f .mfiles-doxia-module-twiki

%files module-xdoc -f .mfiles-doxia-module-xdoc

%files module-xhtml -f .mfiles-doxia-module-xhtml

%files module-xhtml5 -f .mfiles-doxia-module-xhtml5

%files sink-api -f .mfiles-doxia-sink-api

%files test-docs -f .mfiles-doxia-test-docs

%files javadoc -f .mfiles-javadoc
%license LICENSE
%doc NOTICE

%changelog
