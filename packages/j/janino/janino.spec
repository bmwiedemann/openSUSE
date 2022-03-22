#
# spec file for package janino
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


Name:           janino
Version:        3.1.6
Release:        0
Summary:        An embedded Java compiler
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://janino-compiler.github.io/janino
Source0:        https://github.com/janino-compiler/janino/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
Requires:       commons-compiler = %{version}-%{release}
Requires:       javapackages-tools
BuildArch:      noarch

%description
Janino is a super-small, super-fast Java compiler.

The "JANINO" implementation of the "commons-compiler" API: Super-small,
super-fast, independent from the JDK's "tools.jar".

%package     -n commons-compiler
Summary:        Commons Compiler
Group:          Development/Libraries/Java

%description -n commons-compiler
The "commons-compiler" API, including the "IExpressionEvaluator",
"IScriptEvaluator", "IClassBodyEvaluator" and "ISimpleCompiler" interfaces.

%package     -n commons-compiler-jdk
Summary:        Commons Compiler JDK
Group:          Development/Libraries/Java

%description -n commons-compiler-jdk
The "JDK" implementation of the "commons-compiler" API that uses the
JDK's Java compiler (JAVAC) in "tools.jar".

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description    javadoc
API documentation for %{name}.

%prep

%autosetup

find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

pushd %{name}-parent
  %pom_xpath_remove pom:maven.compiler.source
  %pom_xpath_remove pom:maven.compiler.target
  %pom_xpath_remove pom:maven.compiler.executable
  %pom_xpath_remove pom:maven.compiler.fork

  %pom_remove_plugin :nexus-staging-maven-plugin
  %pom_remove_plugin :maven-jarsigner-plugin
  %pom_remove_plugin :maven-javadoc-plugin
  %pom_remove_plugin :maven-source-plugin

  %pom_disable_module ../commons-compiler-tests

  %{mvn_package} :%{name}-parent __noinstall
popd

%build

pushd %{name}-parent
  %{mvn_build} -fs -- -Dmaven.compiler.source=8 -Dmaven.compiler.target=8
popd

%install

pushd %{name}-parent
  %mvn_install
  %fdupes -s %{buildroot}%{_javadocdir}

  %jpackage_script org.codehaus.commons.compiler.samples.CompilerDemo "" "" %{name}/janino:%{name}/commons-compiler janinoc true
popd

%files -f %{name}-parent/.mfiles-%{name}
%license LICENSE
%{_bindir}/janinoc

%files -n commons-compiler -f %{name}-parent/.mfiles-commons-compiler
%license LICENSE

%files -n commons-compiler-jdk -f %{name}-parent/.mfiles-commons-compiler-jdk
%license LICENSE

%files javadoc -f %{name}-parent/.mfiles-javadoc
%license LICENSE

%changelog
