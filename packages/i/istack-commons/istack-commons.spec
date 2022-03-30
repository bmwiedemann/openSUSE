#
# spec file for package istack-commons
#
# Copyright (c) 2022 SUSE LLC
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


Name:           istack-commons
Version:        3.0.7
Release:        0
Summary:        Common code for some Glassfish projects
License:        CDDL-1.1 AND GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            https://istack-commons.java.net
Source0:        https://github.com/javaee/jaxb-%{name}/archive/%{version}-RELEASE.tar.gz
BuildRequires:  java-devel >= 9
BuildRequires:  maven-local
BuildRequires:  mvn(args4j:args4j)
BuildRequires:  mvn(com.sun.codemodel:codemodel)
BuildRequires:  mvn(dom4j:dom4j)
BuildRequires:  mvn(javax.activation:javax.activation-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.java:jvnet-parent:pom:)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-api)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-connector-basic)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-impl)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-spi)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-transport-file)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-transport-wagon)
BuildRequires:  mvn(org.apache.maven.resolver:maven-resolver-util)
BuildRequires:  mvn(org.apache.maven.shared:file-management)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-http-lightweight)
BuildRequires:  mvn(org.apache.maven:maven-compat)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-settings)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-io)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.jsoup:jsoup)
BuildRequires:  mvn(org.tukaani:xz)
BuildArch:      noarch

%description
Code shared between JAXP, JAXB, SAAJ, and JAX-WS projects.

%package maven-plugin
Summary:        Istack-commons Maven Mojo
Group:          Development/Libraries/Java

%description maven-plugin
This package contains the istack-commons Maven Mojo.

%package -n import-properties-plugin
Summary:        Istack-commons import properties plugin
Group:          Development/Libraries/Java

%description -n import-properties-plugin
This package contains the istack-commons import properties Maven Mojo.

%package buildtools
Summary:        Istack-commons buildtools
Group:          Development/Libraries/Java

%description buildtools
This package contains istack-commons buildtools.

%package runtime
Summary:        Istack-commons runtime
Group:          Development/Libraries/Java

%description runtime
This package contains istack-commons runtime.

%package soimp
Summary:        Istack-commons soimp
Group:          Development/Libraries/Java

%description soimp
This package contains istack-commons soimp.

%package test
Summary:        Istack-commons test
Group:          Development/Libraries/Java

%description test
This package contains istack-commons test.

%package tools
Summary:        Istack-commons tools
Group:          Development/Libraries/Java

%description tools
This package contains istack-commons tools.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jaxb-%{name}-%{version}-RELEASE

# Remove bundled jar files:
find . -name '*.jar' -print -delete
find . -name '*.class' -print -delete

pushd %{name}

%pom_remove_plugin org.glassfish.copyright:glassfish-copyright-maven-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin

%pom_add_dep javax.activation:javax.activation-api runtime

# backward compatibility symlinks
%{mvn_file} com.sun.istack:%{name}-buildtools %{name}-buildtools %{name}/%{name}-buildtools
%{mvn_file} com.sun.istack:%{name}-runtime %{name}-runtime %{name}/%{name}-runtime
%{mvn_file} com.sun.istack:%{name}-soimp %{name}-soimp %{name}/%{name}-soimp
%{mvn_file} com.sun.istack:%{name}-test %{name}-test %{name}/%{name}-test
%{mvn_file} com.sun.istack:%{name}-tools %{name}-tools %{name}/%{name}-tools

popd

%build
pushd %{name}
%{mvn_build} -f -j -s -- -Dproject.build.sourceEncoding=UTF-8
popd

%install
pushd %{name}
%mvn_install
popd

%files -f %{name}/.mfiles-istack-commons
%dir %{_javadir}/%{name}
%license %{name}/Licence.txt

%files -n %{name}-maven-plugin -f %{name}/.mfiles-%{name}-maven-plugin
%license %{name}/Licence.txt

%files -n import-properties-plugin -f %{name}/.mfiles-import-properties-plugin
%license %{name}/Licence.txt

%files buildtools -f %{name}/.mfiles-istack-commons-buildtools
%license %{name}/Licence.txt

%files runtime -f %{name}/.mfiles-istack-commons-runtime
%license %{name}/Licence.txt

%files soimp -f %{name}/.mfiles-istack-commons-soimp
%license %{name}/Licence.txt

%files test -f %{name}/.mfiles-istack-commons-test
%license %{name}/Licence.txt

%files tools -f %{name}/.mfiles-istack-commons-tools
%license %{name}/Licence.txt

%if 0
%files javadoc -f %{name}/.mfiles-javadoc
%license %{name}/Licence.txt
%endif

%changelog
