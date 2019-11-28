#
# spec file for package truth
#
# Copyright (c) 2019 SUSE LLC
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


Name:           truth
Version:        0.24
Release:        0
Summary:        An assertion framework for Java unit tests
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/google/truth
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(com.google.auto.value:auto-value)
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(com.google.guava:guava)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.sonatype.oss:oss-parent:pom:)
BuildArch:      noarch

%description
Truth is a library provides alternative ways to express assertions in
unit tests. It can be used as a replacement for JUnit's assertions or FEST
or it can be used alongside where other approaches seem more suitable.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :gwt-maven-plugin core
%pom_remove_dep :gwt-user core
%pom_remove_dep :guava-gwt core
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId[text()='maven-compiler-plugin']]/pom:configuration" "
          <testExcludes>
            <exclude>**/gwt/*.java</exclude>
          </testExcludes>" core

%build
%{mvn_build} -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md
%dir %{_javadir}/%{name}
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
