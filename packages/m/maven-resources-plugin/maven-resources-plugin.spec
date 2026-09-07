#
# spec file for package maven-resources-plugin
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


Name:           maven-resources-plugin
Version:        3.5.0
Release:        0
Summary:        Maven Resources Plugin
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://maven.apache.org/plugins/maven-resources-plugin
Source0:        https://repo1.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  apache-commons-lang3
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  maven-filtering >= 3.5.0
BuildRequires:  maven-lib
BuildRequires:  maven-plugin-annotations
BuildRequires:  maven-plugin-plugin
BuildRequires:  plexus-interpolation
BuildRequires:  plexus-utils
BuildRequires:  sisu-plexus
BuildRequires:  unzip
BuildRequires:  xmvn-connector
BuildRequires:  xmvn-install
BuildRequires:  xmvn-minimal
BuildRequires:  xmvn-resolve
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugins:pom:)
Obsoletes:      %{name}-bootstrap
BuildArch:      noarch

%description
The Resources Plugin handles the copying of project resources
to the output directory.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q
cp %{SOURCE1} build.xml

# Remove all dependencies with scope test, since a raw xmvn does not hide them
%pom_remove_dep -r :::test:

%build
mkdir -p lib
build-jar-repository -s lib \
    atinject \
    commons-lang3 \
    jsoup/jsoup\
    maven-filtering/maven-filtering \
    maven/maven-artifact \
    maven/maven-core \
    maven/maven-model \
    maven/maven-plugin-api \
    maven/maven-resolver-provider \
    maven-plugin-tools/maven-plugin-annotations \
    maven-plugin-tools/maven-plugin-plugin \
    maven-plugin-tools/maven-plugin-tools-annotations \
    maven-plugin-tools/maven-plugin-tools-api \
    maven-plugin-tools/maven-plugin-tools-generators \
    maven-resolver/maven-resolver-api \
    maven-resolver/maven-resolver-util \
    objectweb-asm/asm-all \
    org.eclipse.sisu.plexus \
    plexus/archiver \
    plexus-classworlds \
    plexus/interpolation \
    plexus/utils \
    plexus/xml \
    qdox \
    slf4j/api \
    velocity-engine/velocity-engine-core \
    xmvn
%{ant} -Dtest.skip=true jar javadoc

%{mvn_artifact} pom.xml target/%{name}-%{version}.jar

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
