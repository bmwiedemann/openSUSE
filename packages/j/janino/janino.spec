#
# spec file for package janino
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2000-2007, JPackage Project
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
Version:        2.7.8
Release:        0
Summary:        An embedded Java compiler
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            http://janino-compiler.github.io/janino
Source0:        http://janino.unkrig.de/download/%{name}-%{version}.zip
Source1:        http://repo1.maven.org/maven2/org/codehaus/%{name}/%{name}-parent/%{version}/%{name}-parent-%{version}.pom
Source2:        http://repo1.maven.org/maven2/org/codehaus/%{name}/commons-compiler/%{version}/commons-compiler-%{version}.pom
Source3:        http://repo1.maven.org/maven2/org/codehaus/%{name}/commons-compiler-jdk/%{version}/commons-compiler-jdk-%{version}.pom
Source4:        http://repo1.maven.org/maven2/org/codehaus/%{name}/%{name}/%{version}/%{name}-%{version}.pom
# removes the de.unkrig.commons.nullanalysis annotations
# http://unkrig.de/w/Unkrig.de
# https://svn.code.sf.net/p/loggifier/code/tags/loggifier_0.9.9.v20140430-1829/de.unkrig.commons.nullanalysis/
Patch0:         %{name}-2.7.8-remove-nullanalysis-annotations.patch
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  unzip
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.codehaus:codehaus-parent:pom:)
BuildArch:      noarch

%description
Janino is a super-small, super-fast Java compiler. Not only can it compile
a set of source files to a set of class files like the JAVAC tool, but also
can it compile a Java expression, block, class body or source file in
memory, load the byte-code and execute it directly in the same JVM. Janino
is not intended to be a development tool, but an embedded compiler for
run-time compilation purposes, e.g. expression evaluators or "server pages"
engines like JSP.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q

find . -name "*.jar" -delete
find . -name "*.class" -delete

for m in commons-compiler \
  commons-compiler-jdk \
  %{name};do
  mkdir -p ${m}/src
  (
    cd ${m}/src/
    unzip -qq  ../../${m}-src.zip
    if [ -f org.codehaus.commons.compiler.properties ]; then
      mkdir -p main/resources
      mv org.codehaus.commons.compiler.properties main/resources
    fi
  )
done

%patch0 -p1

install -m 644 %{SOURCE1} pom.xml
install -m 644 %{SOURCE2} commons-compiler/pom.xml
install -m 644 %{SOURCE3} commons-compiler-jdk/pom.xml
install -m 644 %{SOURCE4} %{name}/pom.xml

%pom_change_dep -r :ant-nodeps :ant

# RHBZ#842604
%pom_xpath_set "pom:plugin[pom:artifactId = 'maven-compiler-plugin']/pom:configuration/pom:source" 1.6
%pom_xpath_set "pom:plugin[pom:artifactId = 'maven-compiler-plugin']/pom:configuration/pom:target" 1.6

dos2unix new_bsd_license.txt README.txt

# Cannot run program "svn"
%pom_remove_plugin :buildnumber-maven-plugin

%pom_remove_plugin :maven-clean-plugin
%pom_remove_plugin :maven-deploy-plugin
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-source-plugin

%build

%{mvn_build} -f -- -Dsource=6

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.txt
%license new_bsd_license.txt

%files javadoc -f .mfiles-javadoc
%license new_bsd_license.txt

%changelog
