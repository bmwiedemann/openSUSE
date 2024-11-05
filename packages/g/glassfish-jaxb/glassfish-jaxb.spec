#
# spec file for package glassfish-jaxb
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


# The automatic requires would be java-headless >= 9, but the
# binaries are java 8 compatible
%define __requires_exclude java-headless
Name:           glassfish-jaxb
Version:        2.3.1
Release:        0
Summary:        JAXB Reference Implementation
License:        CDDL-1.1 OR GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            https://jaxb.java.net
Source0:        https://github.com/javaee/jaxb-v2/archive/%{version}.tar.gz
Patch0:         txw2-args4j.patch
Patch1:         glassfish-jaxb-timestamp.patch
BuildRequires:  java-devel >= 9
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(com.sun.istack:istack-commons-runtime)
BuildRequires:  mvn(com.sun.istack:istack-commons-tools)
BuildRequires:  mvn(com.sun.xml.dtd-parser:dtd-parser)
BuildRequires:  mvn(com.sun.xml.fastinfoset:FastInfoset)
BuildRequires:  mvn(com.sun.xsom:xsom)
BuildRequires:  mvn(javax.activation:javax.activation-api)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)
BuildRequires:  mvn(net.java.dev.msv:msv-core)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.jvnet.staxex:stax-ex)
BuildRequires:  mvn(relaxngDatatype:relaxngDatatype)
BuildRequires:  mvn(xml-resolver:xml-resolver)
Requires:       %{name}-bom = %{version}-%{release}
Requires:       %{name}-bom-ext = %{version}-%{release}
Requires:       %{name}-codemodel = %{version}-%{release}
Requires:       %{name}-codemodel-annotation-compiler = %{version}-%{release}
Requires:       %{name}-codemodel-parent = %{version}-%{release}
Requires:       %{name}-external-parent = %{version}-%{release}
Requires:       %{name}-jxc = %{version}-%{release}
Requires:       %{name}-parent = %{version}-%{release}
Requires:       %{name}-relaxng-datatype = %{version}-%{release}
Requires:       %{name}-rngom = %{version}-%{release}
Requires:       %{name}-runtime = %{version}-%{release}
Requires:       %{name}-runtime-parent = %{version}-%{release}
Requires:       %{name}-txw-parent = %{version}-%{release}
Requires:       %{name}-txw2 = %{version}-%{release}
Requires:       %{name}-txwc2 = %{version}-%{release}
Requires:       %{name}-xjc = %{version}-%{release}
Requires:       %{name}-xsom = %{version}-%{release}
Requires:       java-headless >= 1.8
#!BuildRequires: glassfish-dtd-parser
#!BuildRequires: glassfish-fastinfoset
#!BuildRequires: istack-commons-runtime
#!BuildRequires: istack-commons-tools
#!BuildRequires: stax-ex
#!BuildRequires: xmlstreambuffer
#!BuildRequires: xsom
BuildArch:      noarch

%description
GlassFish JAXB Reference Implementation.

%package codemodel
Summary:        Codemodel Core
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description codemodel
The core functionality of the CodeModel java source code generation
library.

%package codemodel-annotation-compiler
Summary:        Codemodel Annotation Compiler
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description codemodel-annotation-compiler
The annotation compiler ant task for the CodeModel java source code
generation library.

%package bom
Summary:        JAXB BOM
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description bom
JAXB Bill of Materials (BOM)

%package bom-ext
Summary:        JAXB BOM with all dependencies
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description bom-ext
JAXB Bill of Materials (BOM) with all dependencies.

%package codemodel-parent
Summary:        Codemodel parent POM
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description codemodel-parent
This package contains codemodel parent POM.

%package external-parent
Summary:        JAXB External parent POM
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description external-parent
JAXB External parent POM.

%package jxc
Summary:        JAXB schema generator
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description jxc
The tool to generate XML schema based on java classes.

%package parent
Summary:        JAXB parent POM
Group:          Development/Libraries/Java

%description parent
This package contains parent POM.

%package runtime
Summary:        JAXB Runtime
Group:          Development/Libraries/Java
Requires:       glassfish-fastinfoset
Requires:       istack-commons-runtime
Requires:       java-headless >= 1.8
Requires:       stax-ex

%description runtime
JAXB (JSR 222) Reference Implementation

%package runtime-parent
Summary:        JAXB Runtime parent POM
Group:          Development/Libraries/Java

%description runtime-parent
This package contains Runtime parent POM.

%package txw-parent
Summary:        JAXB TXW parent POM
Group:          Development/Libraries/Java

%description txw-parent
This package contains TXW parent POM.

%package xjc
Summary:        JAXB XJC
Group:          Development/Libraries/Java
Requires:       glassfish-dtd-parser
Requires:       istack-commons-tools
Requires:       java-headless >= 1.8

%description xjc
JAXB Binding Compiler. Contains source code needed for binding
customization files into java sources. In other words: the tool to
generate java classes for the given xml representation.

%package rngom
Summary:        RELAX NG Object Model/Parser
Group:          Development/Libraries/Java

%description rngom
This package contains RELAX NG Object Model/Parser.

%package relaxng-datatype
Summary:        RelaxNG Datatype
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description relaxng-datatype
This package contains RelaxNG Datatype.

%package txw2
Summary:        TXW2 Runtime
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description txw2
TXW is a library that allows you to write XML documents.

%package txwc2
Summary:        TXW2 Compiler
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description txwc2
JAXB schema generator. The tool to generate XML schema based on java
classes.

%package xsom
Summary:        XSOM
Group:          Development/Libraries/Java
Requires:       java-headless >= 1.8

%description xsom
XML Schema Object Model (XSOM) is a Java library that allows
applications to easily parse XML Schema documents and inspect
information in them. It is expected to be useful for applications
that need to take XML Schema as an input.

%package javadoc
Summary:        Javadocs for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jaxb-v2-%{version}

%patch -P 0
%patch -P 1 -p1

pushd jaxb-ri

%pom_disable_module xjc bundles
%pom_disable_module jxc bundles
%pom_disable_module ri bundles
%pom_disable_module osgi bundles

# Make javax.activation an optional dep
%pom_xpath_inject "pom:configuration/pom:instructions" "
<Import-Package>javax.activation;resolution:=optional,*</Import-Package>" bundles/runtime

%pom_remove_dep com.sun.xml.bind:jaxb-release-documentation bundles/ri
%pom_remove_dep com.sun.xml.bind:jaxb-samples bundles/ri

%pom_change_dep com.sun.org.apache.xml.internal:resolver xml-resolver:xml-resolver xjc
perl -pi -e 's#com\.sun\.org\.apache\.xml\.internal\.resolver#org\.apache\.xml\.resolver#g' xjc/src/main/java/com/sun/tools/xjc/CatalogUtil.java

%pom_remove_plugin :gfnexus-maven-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

%if %{?pkg_vcmp:%pkg_vcmp maven-antrun-plugin >= 3}%{!?pkg_vcmp:0}
sed -i -e 's#tasks\>#target\>#g' xjc/pom.xml jxc/pom.xml
%endif

%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:source" "1.8"
%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration/pom:target" "1.8"
%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:executions/pom:execution[pom:id[text()='base-compile']]/pom:configuration/pom:source" "1.8" . jxc
%pom_xpath_set "pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:executions/pom:execution[pom:id[text()='base-compile']]/pom:configuration/pom:target" "1.8" . jxc
%pom_xpath_set "pom:project/pom:properties/pom:base.java.level" "8"

%{mvn_alias} org.glassfish.jaxb:jaxb-xjc "com.sun.xml.bind:jaxb-xjc"
%{mvn_alias} :jaxb-jxc :jaxb-jxc-jdk9
%{mvn_alias} :jaxb-xjc :jaxb-xjc-jdk9

# Package OSGi version of runtime with the non-OSGi version
%{mvn_package} com.sun.xml.bind:jaxb-impl jaxb-runtime

# Don't install bundles parent pom
%{mvn_package} com.sun.xml.bind.mvn:jaxb-bundles __noinstall

popd

%build
pushd jaxb-ri
%{mvn_build} -f -j -s -- \
    -Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Ddev -DbuildNumber=unknown
popd

%install
pushd jaxb-ri
%mvn_install
popd

%files
%license jaxb-ri/License.txt jaxb-ri/License.html
%doc jaxb-ri/licenceheader.txt

%files codemodel -f jaxb-ri/.mfiles-codemodel
%license jaxb-ri/License.txt jaxb-ri/License.html
%doc jaxb-ri/licenceheader.txt

%files codemodel-annotation-compiler -f jaxb-ri/.mfiles-codemodel-annotation-compiler

%files bom -f jaxb-ri/.mfiles-jaxb-bom
%license jaxb-ri/License.txt jaxb-ri/License.html
%doc jaxb-ri/licenceheader.txt

%files bom-ext -f jaxb-ri/.mfiles-jaxb-bom-ext

%files codemodel-parent -f jaxb-ri/.mfiles-jaxb-codemodel-parent

%files external-parent -f jaxb-ri/.mfiles-jaxb-external-parent

%files jxc -f jaxb-ri/.mfiles-jaxb-jxc
%license jaxb-ri/License.txt jaxb-ri/License.html
%doc jaxb-ri/licenceheader.txt

%files parent -f jaxb-ri/.mfiles-jaxb-parent

%files runtime -f jaxb-ri/.mfiles-jaxb-runtime
%license jaxb-ri/License.txt jaxb-ri/License.html
%doc jaxb-ri/licenceheader.txt

%files runtime-parent -f jaxb-ri/.mfiles-jaxb-runtime-parent

%files txw-parent -f jaxb-ri/.mfiles-jaxb-txw-parent

%files xjc -f jaxb-ri/.mfiles-jaxb-xjc

%files rngom -f jaxb-ri/.mfiles-rngom
%license jaxb-ri/License.txt jaxb-ri/License.html
%doc jaxb-ri/licenceheader.txt

%files relaxng-datatype -f jaxb-ri/.mfiles-relaxng-datatype
%license jaxb-ri/License.txt jaxb-ri/License.html
%doc jaxb-ri/licenceheader.txt

%files txw2 -f jaxb-ri/.mfiles-txw2
%license jaxb-ri/License.txt jaxb-ri/License.html
%doc jaxb-ri/licenceheader.txt

%files txwc2 -f jaxb-ri/.mfiles-txwc2
%license jaxb-ri/License.txt jaxb-ri/License.html
%doc jaxb-ri/licenceheader.txt

%files xsom -f jaxb-ri/.mfiles-xsom
%license jaxb-ri/License.txt jaxb-ri/License.html
%doc jaxb-ri/licenceheader.txt

%if 0
%files javadoc -f jaxb-ri/.mfiles-javadoc
%license jaxb-ri/License.txt jaxb-ri/License.html
%doc jaxb-ri/licenceheader.txt
%endif

%changelog
