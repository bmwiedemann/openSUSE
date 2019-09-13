#
# spec file for package powermock
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


%global desc \
PowerMock is a framework that extend other mock libraries\
such as EasyMock with more powerful capabilities. PowerMock uses a\
custom classloader and bytecode manipulation to enable mocking of\
static methods, constructors, final classes and methods, private\
methods, removal of static initializers and more.
Name:           powermock
Version:        1.6.5
Release:        0
Summary:        A Java mocking framework
# Note: api-mockito subpackage is ASL 2.0 and MIT, the rest is ASL 2.0
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/jayway/powermock
Source0:        https://github.com/jayway/%{name}/archive/%{name}-%{version}.tar.gz
Patch0:         fix-build.patch
Patch1:         0001-Fix-junit3-compat.patch
# powermock contains forked version of mockito
# this is the same patch as in mockito to fix incompatibility with our cglib
Patch2:         0002-Setting-naming-policy.patch
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(cglib:cglib-nodep)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.javassist:javassist)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(org.testng:testng)
BuildArch:      noarch

%description
%{desc}

%package common
Summary:        Common files for PowerMock
License:        Apache-2.0
Group:          Development/Libraries/Java

%description common
%{desc}

This package contains common files for all PowerMock modules.

%package reflect
Summary:        Reflection module of PowerMock
License:        Apache-2.0
Group:          Development/Libraries/Java
Requires:       %{name}-common = %{version}-%{release}

%description reflect
%{desc}

This package contains the reflection module of PowerMock.

%package core
Summary:        Core module of PowerMock
License:        Apache-2.0
Group:          Development/Libraries/Java
Requires:       %{name}-common = %{version}-%{release}

%description core
%{desc}

This package contains the core module of PowerMock.

%package junit4
Summary:        JUnit4 common module of PowerMock
License:        Apache-2.0
Group:          Development/Libraries/Java
Requires:       %{name}-common = %{version}-%{release}

%description junit4
%{desc}

This package contains the JUnit4 module of PowerMock.

%package api-support
Summary:        PowerMock API support module
License:        Apache-2.0
Group:          Development/Libraries/Java
Requires:       %{name}-common = %{version}-%{release}

%description api-support
%{desc}

This package contains support code for the PowerMock API extensions.

%package api-mockito
Summary:        PowerMock Mockito API module
# Bundles forked mockito, which is under MIT
License:        Apache-2.0 AND MIT
Group:          Development/Libraries/Java
Requires:       %{name}-common = %{version}-%{release}
Provides:       bundled(mockito) = 2.0

%description api-mockito
%{desc}

This package contains the PowerMock Mockito API extension.

%package api-easymock
Summary:        PowerMock EasyMock API module
License:        Apache-2.0
Group:          Development/Libraries/Java
Requires:       %{name}-common = %{version}-%{release}

%description api-easymock
%{desc}

This package contains the PowerMock EasyMock API extension.

%package testng
Summary:        PowerMock module for TestNG
License:        Apache-2.0
Group:          Development/Libraries/Java
Requires:       %{name}-common = %{version}-%{release}

%description testng
%{desc}

This package contains the PowerMock TestNG extension.

%package javadoc
Summary:        JavaDocs for %{name}
License:        Apache-2.0
Group:          Documentation/HTML

%description javadoc
%{desc}

This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1

# bundled sources of various libraries
rm -r modules/module-impl/agent
# there is forked mockito, which contains bundled cglib and asm
rm -r api/mockito2/src/main/java/org/powermock/api/mockito/repackaged/{cglib,asm}

find -name '*.java' | xargs sed -i 's/org\.mockito\.cglib/net.sf.cglib/g;
                                    s/org\.powermock\.api\.mockito\.repackaged\.cglib/net.cf.cglib/g;
                                    s/org\.powermock\.api\.mockito\.repackaged\.asm/org.objectweb.asm/g'

# Assumes different JUnit version
rm modules/module-impl/junit4-common/src/test/java/org/powermock/modules/junit4/common/internal/impl/JUnitVersionTest.java

# Disable modules that we cannot build (yet).
%pom_disable_module module-test modules
%pom_disable_module junit4-legacy modules/module-impl
%pom_disable_module junit4-rule-agent modules/module-impl
%pom_disable_module junit3 modules/module-impl
%pom_disable_module testng-agent modules/module-impl
%pom_disable_module agent modules/module-impl
%pom_disable_module examples
%pom_disable_module release
%pom_disable_module classloading-xstream classloading
%pom_disable_module mockito2 api

%pom_remove_plugin :rat-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-javadoc-plugin']/pom:executions"

%{mvn_package} :powermock-core core
%{mvn_package} :powermock-classloading-base core
%{mvn_package} :powermock-classloading-objenesis core
%{mvn_package} :powermock-module-junit4 junit4
%{mvn_package} :powermock-module-junit4-rule junit4
%{mvn_package} :powermock-module-junit4-common junit4
%{mvn_package} :powermock-api-mockito api-mockito
%{mvn_package} :powermock-api-mockito-common api-mockito
%{mvn_package} :powermock-api-support api-support
%{mvn_package} :powermock-api-easymock api-easymock
%{mvn_package} :powermock-reflect reflect
%{mvn_package} :powermock-module-testng testng
%{mvn_package} :powermock-module-testng-common testng

%{mvn_package} org.powermock.tests: __noinstall

# poms are not needed by anything
%{mvn_package} ::pom: __noinstall

%build
%{mvn_build} -f -- -Dsource=6

%install
%mvn_install
fdupes -s %{buildroot}%{_javadocdir}

%files common
%dir %{_javadir}/%{name}
%license LICENSE.txt

%files reflect -f .mfiles-reflect

%files core -f .mfiles-core

%files junit4 -f .mfiles-junit4

%files api-support -f .mfiles-api-support

%files api-mockito -f .mfiles-api-mockito
%license api/mockito2/src/main/java/org/powermock/api/mockito/repackaged/Mockito-LICENSE.txt

%files api-easymock -f .mfiles-api-easymock

%files testng -f .mfiles-testng

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
