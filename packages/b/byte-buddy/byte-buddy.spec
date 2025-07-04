#
# spec file for package byte-buddy
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


Name:           byte-buddy
Version:        1.17.6
Release:        0
Summary:        Runtime code generation for the Java virtual machine
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://bytebuddy.net/
Source0:        https://github.com/raphw/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
Patch0:         0001-Avoid-bundling-asm.patch
BuildRequires:  fdupes
BuildRequires:  jurand
BuildRequires:  maven-local
BuildRequires:  mvn(codes.rafael.modulemaker:modulemaker-maven-plugin)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(net.java.dev.jna:jna)
BuildRequires:  mvn(net.java.dev.jna:jna-platform)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-resolver-provider)
BuildRequires:  mvn(org.eclipse.aether:aether-api)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.ow2.asm:asm) >= 9.7.1
BuildRequires:  mvn(org.ow2.asm:asm-commons)
BuildRequires:  mvn(org.sonatype.plexus:plexus-build-api)
BuildArch:      noarch

%description
Byte Buddy is a code generation and manipulation library for creating and
modifying Java classes during the runtime of a Java application and without the
help of a compiler. Other than the code generation utilities that ship with the
Java Class Library, Byte Buddy allows the creation of arbitrary classes and is
not limited to implementing interfaces for the creation of runtime proxies.
Furthermore, Byte Buddy offers a convenient API for changing classes either
manually, using a Java agent or during a build.

%package agent
Summary:        Byte Buddy Java agent
Group:          Development/Libraries/Java

%description agent
The Byte Buddy Java agent allows to access the JVM's HotSwap feature.

%package maven-plugin
Summary:        Byte Buddy Maven plugin
Group:          Development/Libraries/Java

%description maven-plugin
A plugin for post-processing class files via Byte Buddy in a Maven build.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch -P0 -p1

# Remove Windows-specific resources
rm -rf %{name}-agent/src/main/resources/win32-x86{,-64}

# Don't ship android or benchmark modules
%pom_disable_module %{name}-android
%pom_disable_module %{name}-android-test
%pom_disable_module %{name}-benchmark

# Don't ship gradle plugin
%pom_disable_module %{name}-gradle-plugin

# Remove check plugins unneeded by RPM builds
%pom_remove_plugin :jacoco-maven-plugin
%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin :pitest-maven
%pom_remove_plugin :coveralls-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin
%pom_remove_plugin :jitwatch-jarscan-maven-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin org.sonatype.central:central-publishing-maven-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

# Avoid circular dependency
%pom_remove_plugin :byte-buddy-maven-plugin %{name}-dep

# Not interested in shading sources (causes NPE on old versions of shade plugin)
%pom_xpath_set pom:createSourcesJar false %{name}

# Drop build dep on findbugs annotations, used only by the above check plugins
%pom_remove_dep -r :findbugs-annotations
%{java_remove_annotations} %{name}-{agent,dep,maven-plugin} -n SuppressFBWarnings

%pom_remove_dep org.ow2.asm:asm-deprecated
%pom_remove_dep codes.rafael.asmjdkbridge:asm-jdk-bridge %{name}-dep

%pom_remove_plugin -r :maven-shade-plugin

%pom_add_dep org.apache.maven:maven-resolver-provider:\${version.maven}:provided \
    byte-buddy-maven-plugin

%{mvn_package} :byte-buddy-parent __noinstall

%build
%{mvn_build} -f -s -- \
    -Dsource=8

%install
%mvn_install
%if %{without bootstrap}
%fdupes -s %{buildroot}%{_javadocdir}
%endif

%files -f .mfiles-%{name} -f .mfiles-%{name}-dep
%doc README.md release-notes.md
%license LICENSE NOTICE

%files agent -f .mfiles-%{name}-agent
%license LICENSE NOTICE

%files maven-plugin -f .mfiles-%{name}-maven-plugin

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
