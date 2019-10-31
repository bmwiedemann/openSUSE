#
# spec file for package jctools
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


Name:           jctools
Version:        2.1.2
Release:        0
Summary:        Java Concurrency Tools for the JVM
License:        Apache-2.0
URL:            https://jctools.github.io/JCTools/
Source0:        https://github.com/JCTools/JCTools/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.github.javaparser:javaparser-core)
BuildRequires:  mvn(com.google.guava:guava-testlib)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-all)
BuildRequires:  mvn(org.ow2.asm:asm-util)
# uses sun.misc.Unsafe
BuildConflicts: java-devel >= 9
BuildArch:      noarch

%description
This project aims to offer some concurrent data structures
currently missing from the JDK:

° SPSC/MPSC/SPMC/MPMC Bounded lock free queues
° SPSC/MPSC Unbounded lock free queues
° Alternative interfaces for queues
° Offheap concurrent ring buffer for ITC/IPC purposes
° Single Writer Map/Set implementations
° Low contention stats counters
° Executor

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

%package parent
Summary:        JCTools Parent POM

%description parent
JCTools Parent POM.

%prep
%setup -q -n JCTools-%{version}
# Cleanup
find . -name '*.class' -print -delete
find . -name '*.jar' -print -delete

# Remove failure-prone tests (race condition?)
rm jctools-core/src/test/java/org/jctools/queues/MpqSanityTestMpscCompound.java
rm jctools-core/src/test/java/org/jctools/queues/atomic/AtomicMpqSanityTestMpscCompound.java

%pom_xpath_set pom:project/pom:version %{version}
%pom_xpath_set -r pom:parent/pom:version %{version} %{name}-{build,core,channels,experimental}

# Remove plugins unnecessary for RPM builds
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :coveralls-maven-plugin
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :maven-source-plugin %{name}-core
%pom_remove_plugin :maven-javadoc-plugin %{name}-core

# Unavailable deps
%pom_disable_module %{name}-benchmarks
%pom_disable_module %{name}-concurrency-test

# Modern asm deps
%pom_change_dep ":asm-all" ":asm-util" jctools-{channels,experimental}

# Add OSGi support
for mod in core experimental; do
 %pom_xpath_set "pom:project/pom:packaging" bundle %{name}-${mod}
 %pom_add_plugin org.apache.felix:maven-bundle-plugin:2.3.7 %{name}-${mod} '
 <extensions>true</extensions>
 <executions>
   <execution>
     <id>bundle-manifest</id>
     <phase>process-classes</phase>
     <goals>
       <goal>manifest</goal>
     </goals>
   </execution>
 </executions>
 <configuration>
  <excludeDependencies>true</excludeDependencies>
 </configuration>'
done

# No need to package internal build tools
%{mvn_package} :jctools-build __noinstall

%build
%{mvn_build} -s -f

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-%{name}-core
%doc README.md
%license LICENSE

%files channels -f .mfiles-%{name}-channels

%files experimental -f .mfiles-%{name}-experimental

%files javadoc -f .mfiles-javadoc
%license LICENSE

%files parent -f .mfiles-%{name}-parent
%license LICENSE

%changelog
