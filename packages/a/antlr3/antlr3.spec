#
# spec file for package antlr3-java
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


%global flavor @BUILD_FLAVOR@%{nil}
%global antlr_version 3.5.3
%global c_runtime_version 3.4
%global javascript_runtime_version 3.1
%if "%{flavor}" == "bootstrap"
%bcond_without bootstrap
%else
%bcond_with bootstrap
%endif
%if "%{flavor}" == "runtime"
%bcond_without runtime
%else
%bcond_with runtime
%endif
Version:        %{antlr_version}
Release:        0
URL:            https://www.antlr3.org/
Source0:        https://github.com/antlr/antlr3/archive/%{antlr_version}.tar.gz
Patch0:         antlr3-java8-fix.patch
# Generate OSGi metadata
Patch1:         antlr3-osgi-manifest.patch
Patch100:       antlr3-generated_sources.patch
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-enforcer-plugin
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(antlr:antlr)
BuildRequires:  mvn(org.antlr:stringtemplate)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch
%if %{with runtime}
Name:           antlr3-java
Summary:        Java run-time support for ANTLR-generated parsers
License:        BSD-3-Clause
Group:          Development/Libraries/Java

%description
Java run-time support for ANTLR-generated parsers

%else

Summary:        ANother Tool for Language Recognition
License:        BSD-3-Clause
Group:          Development/Libraries/Java
BuildRequires:  unzip
BuildRequires:  mvn(org.antlr:ST4)
BuildRequires:  mvn(org.antlr:antlr-runtime)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.apache.maven:maven-project)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
BuildRequires:  mvn(xerces:dom3-xml-apis)

%if %{with bootstrap}
Name:           antlr3-bootstrap
BuildRequires:  xz
#!BuildRequires: stringtemplate4-bootstrap
%else
Name:           antlr3
BuildRequires:  ant
BuildRequires:  antlr
BuildRequires:  mvn(org.antlr:antlr)
BuildRequires:  mvn(org.antlr:antlr3-maven-plugin)
#!BuildRequires: stringtemplate4
#!BuildRequires: antlr3-bootstrap-tool
%endif

%description
ANother Tool for Language Recognition, is a language tool
that provides a framework for constructing recognizers,
interpreters, compilers, and translators from grammatical
descriptions containing actions in a variety of target languages.

%package     tool
Summary:        ANother Tool for Language Recognition
Group:          Development/Libraries/Java
# Explicit requires for javapackages-tools since antlr3-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools
Requires:       mvn(org.antlr:antlr-runtime) = %{antlr_version}
%if %{without bootstrap}
Conflicts:      antlr3-bootstrap-tool
Provides:       antlr3-bootstrap-tool
%endif

%description tool
ANother Tool for Language Recognition, is a language tool
that provides a framework for constructing recognizers,
interpreters, compilers, and translators from grammatical
descriptions containing actions in a variety of target languages.

%endif

%if %{without boostrap}
%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML
BuildArch:      noarch

%description javadoc
%{summary}.

%endif

%prep
%setup -q -n antlr3-%{antlr_version}
%if %{with bootstrap}
%patch100
%pom_remove_plugin :antlr3-maven-plugin tool
%endif

sed -i "s,\${buildNumber},`cat %{_sysconfdir}/fedora-release` `date`," tool/src/main/resources/org/antlr/antlr.properties
%patch0 -p1
%patch1

# remove pre-built artifacts
find -type f -a -name *.jar -delete
find -type f -a -name *.class -delete

%pom_disable_module antlr3-maven-archetype
%pom_disable_module gunit
%pom_disable_module gunit-maven-plugin
%pom_disable_module antlr-complete

%if %{with runtime}
%pom_disable_module tool
%pom_disable_module antlr3-maven-plugin
%else
%pom_disable_module runtime/Java
%endif

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

# compile for target 1.8
sed -i 's/jsr14/1.8/' antlr3-maven-archetype/src/main/resources/archetype-resources/pom.xml \
                      antlr3-maven-plugin/pom.xml \
                      gunit/pom.xml \
                      gunit-maven-plugin/pom.xml \
                      pom.xml \
                      runtime/Java/pom.xml \
                      tool/pom.xml

# workarounds bug in filtering (Mark invalid)
%pom_xpath_remove pom:resource/pom:filtering

%{mvn_package} :antlr-master __noinstall
%if %{without runtime}
%{mvn_package} : tool
%endif

%{mvn_file} :antlr antlr3
%{mvn_file} :antlr-runtime antlr3-runtime
%{mvn_file} :antlr-maven-plugin antlr3-maven-plugin

%build
%{mvn_build} -f \
%if %{with bootstrap}
	-j \
%endif
    -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=8 \
%endif
    -Dsource=8

%if %{without runtime} &&  %{without bootstrap}

# build ant task
pushd antlr-ant/main/antlr3-task/
export CLASSPATH=$(build-classpath ant)
javac -encoding ISO-8859-1 -source 8 -target 8 antlr3-src/org/apache/tools/ant/antlr/ANTLR3.java
jar cvf ant-antlr3.jar \
  -C antlr3-src org/apache/tools/ant/antlr/antlib.xml \
  -C antlr3-src org/apache/tools/ant/antlr/ANTLR3.class
popd

%endif

%install
%mvn_install
%if %{without bootstrap}
%fdupes -s %{buildroot}%{_javadocdir}
%endif

%if %{without runtime}

mkdir -p %{buildroot}/%{_mandir}
mkdir -p %{buildroot}/%{_datadir}/antlr

%if %{without bootstrap}

# install ant task
install -m 644 antlr-ant/main/antlr3-task/ant-antlr3.jar -D %{buildroot}%{_javadir}/ant/ant-antlr3.jar
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
cat > %{buildroot}%{_sysconfdir}/ant.d/ant-antlr3 << EOF
ant/ant-antlr3 antlr3
EOF

%endif

# install wrapper script
%jpackage_script org.antlr.Tool '' '' 'stringtemplate4/ST4.jar:antlr3.jar:antlr3-runtime.jar' antlr3 true

%files tool -f .mfiles-tool
%license tool/{LICENSE.txt,CHANGES.txt}
%doc README.txt
%{_bindir}/antlr3
%if %{without bootstrap}
%{_javadir}/ant/ant-antlr3.jar
%config(noreplace) %{_sysconfdir}/ant.d/ant-antlr3
%endif

%else

%files -f .mfiles
%license tool/LICENSE.txt

%endif

%if %{without bootstrap}
%files javadoc -f .mfiles-javadoc
%license tool/LICENSE.txt

%endif

%changelog
