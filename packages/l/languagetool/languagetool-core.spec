#
# spec file for package languagetool-core
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


%global base_name languagetool
%global hunspell_library %(rpm -q --qf "%%{name}" -f $(readlink -f %{_libdir}/libhunspell.so))
Name:           %{base_name}-core
Version:        4.8
Release:        0
Summary:        Style and Grammar Checker for 25+ Languages - Core package
License:        LGPL-2.1-or-later
URL:            https://languagetool.org
Source0:        https://github.com/languagetool-org/%{base_name}/archive/v%{version}.tar.gz
# In fact a patch, but not applied as such
Source100:      languagetool-system-hunspell.patch.in
# Newer mavens
Patch0:         languagetool-descriptor.patch
Patch1:         languagetool-xgboost-predictor.patch
Patch2:         languagetool-hunspell.patch
Patch3:         languagetool-4.8-lucene-8.patch
Patch4:         languagetool-test-resource.patch
BuildRequires:  fdupes
BuildRequires:  hunspell-devel
BuildRequires:  maven-local
BuildRequires:  mvn(biz.k11i:xgboost-predictor)
BuildRequires:  mvn(ch.qos.logback:logback-classic)
BuildRequires:  mvn(com.carrotsearch:hppc)
BuildRequires:  mvn(com.fasterxml.jackson.core:jackson-databind)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(com.intellij:annotations)
BuildRequires:  mvn(com.optimaize.languagedetector:language-detector)
BuildRequires:  mvn(edu.berkeley.nlp:berkeleylm)
BuildRequires:  mvn(javax.activation:javax.activation-api)
BuildRequires:  mvn(javax.measure:unit-api)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(ml.dmlc:xgboost4j)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.loomchild:segment)
BuildRequires:  mvn(org.apache.commons:commons-csv)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-pool2)
BuildRequires:  mvn(org.apache.commons:commons-text)
BuildRequires:  mvn(org.apache.lucene:lucene-backward-codecs)
BuildRequires:  mvn(org.apache.lucene:lucene-core)
BuildRequires:  mvn(org.carrot2:morfologik-fsa)
BuildRequires:  mvn(org.carrot2:morfologik-fsa-builders)
BuildRequires:  mvn(org.carrot2:morfologik-speller)
BuildRequires:  mvn(org.carrot2:morfologik-stemming)
BuildRequires:  mvn(org.glassfish.jaxb:jaxb-runtime)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(tech.units:indriya)
#!BuildRequires: glassfish-jaxb-runtime
Requires:       glassfish-jaxb-runtime
%requires_eq    %{hunspell_library}
%requires_ge    lucene-backward-codecs
%requires_ge    lucene-core

%description
LanguageTool is a free and open-source grammar checker.
This package contains the core library

%package tests
Summary:        Style and Grammar Checker for 25+ Languages - Core package
BuildArch:      noarch

%description tests
LanguageTool is a free and open-source grammar checker.
This package contains the test-jar for core library

%package javadoc
Summary:        Javadoc for %{name}
BuildArch:      noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{base_name}-%{version}
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%if %{?pkg_vcmp:%pkg_vcmp lucene-core >= 8}%{!?pkg_vcmp:0}
%patch -P 3 -p1
%endif
%patch -P 4 -p1

cat %{SOURCE100} | sed "s#@LIBHUNSPELL@#$(basename $(readlink -e %{_libdir}/libhunspell.so))#g" | patch -p1

pushd %{name}
%{mvn_file} :{*} %{base_name}/@1
%{mvn_package} :::tests: tests
popd

%build
# Remove unneeded dependencies
%pom_xpath_remove pom:project/pom:build/pom:extensions
%pom_xpath_remove pom:project/pom:build/pom:plugins languagetool-core

%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin languagetool-core "
        <executions>
          <execution>
            <goals>
              <goal>test-jar</goal>
            </goals>
          </execution>
        </executions>"

pushd %{name}
%{mvn_build} -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -DskipTests -Dsource=8
popd

%install
pushd %{name}
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}
popd

%files -f %{name}/.mfiles
%license COPYING.txt

%files tests -f %{name}/.mfiles-tests

%files javadoc -f %{name}/.mfiles-javadoc
%license COPYING.txt

%changelog
