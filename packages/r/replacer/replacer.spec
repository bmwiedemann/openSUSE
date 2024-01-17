#
# spec file for package replacer
#
# Copyright (c) 2023 SUSE LLC
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


Name:           replacer
Version:        1.6
Release:        0
Summary:        Replacer Maven Mojo
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/beiliubei/maven-replacer-plugin
# http://code.google.com/p/maven-replacer-plugin/
Source0:        https://github.com/beiliubei/maven-replacer-plugin/archive/%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildRequires:  mvn(xerces:xercesImpl)
BuildArch:      noarch

%description
Maven plugin to replace tokens in a given file with a value.

This plugin is also used to automatically generating PackageVersion.java
in the FasterXML.com project.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n maven-replacer-plugin-%{version}

# remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_remove_plugin :dashboard-maven-plugin
%pom_remove_plugin :maven-assembly-plugin

# remove hard-coded compiler settings
%pom_remove_plugin :maven-compiler-plugin

# trivial port to commons-lang3
%pom_change_dep :commons-lang org.apache.commons:commons-lang3:3.8.1

for i in $(find -name "*.java"); do
    sed -i "s/org.apache.commons.lang./org.apache.commons.lang3./g" $i;
done

%{mvn_file} :%{name} %{name}
%{mvn_alias} :%{name} com.google.code.maven-replacer-plugin:maven-replacer-plugin

%build

%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    -Dmaven.compiler.release=8 \
%endif
    -Dsource=8

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
