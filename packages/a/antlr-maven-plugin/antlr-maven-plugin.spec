#
# spec file for package antlr-maven-plugin
#
# Copyright (c) 2023 SUSE LLC
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


Name:           antlr-maven-plugin
Version:        2.2
Release:        0
Summary:        Maven plugin that generates files based on grammar file(s)
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://mojo.codehaus.org/antlr-maven-plugin/
Source0:        https://repo1.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip
# Modern modello expects to see <models></models>, even if there is only one.
Patch0:         maven-antlr-plugin-2.2-modello-issue.patch
# siteRenderer.createSink doesn't exist anymore
Patch2:         maven-antlr-plugin-2.1-sinkfix.patch
# Fix grammar processing bug (bz 1020312)
Patch3:         0001-MANTLR-34-Fix-NPE-when-building-Jenkins.patch
Patch4:         new-reporting-api.patch
Patch5:         jdk18plus.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.commons:commons-exec)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.reporting:maven-reporting-impl)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-provider-api)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.codehaus.plexus:plexus-i18n)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildArch:      noarch

%description
The Antlr Plugin has two goals:
- antlr:generate Generates file(s) to a target directory based on grammar
  file(s).
- antlr:html Generates Antlr report for grammar file(s).

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch -P 0 -p1 -b .modello
%patch -P 2 -b .sink
%patch -P 3 -p1 -b .fixnpe
%patch -P 4 -p1
%patch -P 5 -p1

%pom_change_dep :maven-project :maven-core:3.9.3

# reporting eventually pulls in another antlr and we'd break with weird errors
%pom_xpath_inject "pom:dependency[pom:artifactId[text()='maven-reporting-impl']]/pom:exclusions" "
        <exclusion>
            <groupId>antlr</groupId>
            <artifactId>antlr</artifactId>
        </exclusion>"

# remove all binary bits
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%{mvn_file} : %{name}

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
