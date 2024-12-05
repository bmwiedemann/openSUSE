#
# spec file for package jctools
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


%global srcname JCTools
Name:           jctools
Version:        4.0.5
Release:        0
Summary:        Java Concurrency Tools for the JVM
License:        Apache-2.0
URL:            https://github.com/JCTools/JCTools
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(com.github.javaparser:javaparser-core) >= 3.14.16
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.ow2.asm:asm-all)
BuildArch:      noarch

%description
This project aims to offer some concurrent data structures
currently missing from the JDK:

* SPSC/MPSC/SPMC/MPMC Bounded lock free queues
* SPSC/MPSC Unbounded lock free queues
* Alternative interfaces for queues
* Offheap concurrent ring buffer for ITC/IPC purposes
* Single Writer Map/Set implementations
* Low contention stats counters
* Executor

%package channels
Summary:        JCTools Channel implementations

%description channels
Channel implementations for the
Java Concurrency Tools Library.

%package experimental
Summary:        JCTools Experimental implementations

%description experimental
Experimental implementations for the
Java Concurrency Tools Library.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{srcname}-%{version}

# set correct version in all pom.xml files
%pom_xpath_set pom:project/pom:version %{version}
%pom_xpath_set pom:parent/pom:version %{version} jctools-{build,core,channels,experimental}

# remove plugins unnecessary for RPM builds
%pom_remove_plugin :coveralls-maven-plugin jctools-core
%pom_remove_plugin :jacoco-maven-plugin jctools-core
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-source-plugin jctools-core
%pom_remove_plugin :maven-javadoc-plugin jctools-core

# disable unused modules with unavailable dependencies
%pom_disable_module jctools-benchmarks
%pom_disable_module jctools-concurrency-test

%pom_xpath_set "pom:project/pom:properties/pom:java.version" "1.8"
%pom_xpath_set "pom:project/pom:properties/pom:java.test.version" "1.8"

# Avoid runtime dependency on test-jar
%pom_xpath_set "pom:dependency[pom:scope='compile']/pom:scope" test jctools-experimental
# Deprecated classes "only used for testing" needed for compiling jctools-experimental
mkdir -p jctools-experimental/src/main/java/org/jctools/queues/
cp -r jctools-core/src/test/java/org/jctools/queues/spec jctools-experimental/src/main/java/org/jctools/queues/

# do not install internal build tools
%{mvn_package} :jctools-build __noinstall

# do not install unused parent POM
%{mvn_package} :jctools-parent __noinstall

%build
%{mvn_build} -sf -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-jctools-core
%doc README.md
%license LICENSE

%files channels -f .mfiles-jctools-channels

%files experimental -f .mfiles-jctools-experimental

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
