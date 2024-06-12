#
# spec file for package guava
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


Name:           guava
Version:        33.2.1
Release:        0
Summary:        Google Core Libraries for Java
License:        Apache-2.0 AND CC0-1.0
Group:          Development/Libraries/Java
URL:            https://github.com/google/guava
Source0:        https://github.com/google/guava/archive/v%{version}.tar.gz
Source1:        %{name}-build.tar.xz
BuildRequires:  ant
BuildRequires:  checker-qual
BuildRequires:  fdupes
BuildRequires:  google-errorprone-annotations >= 2.21.0
BuildRequires:  j2objc-annotations
BuildRequires:  javapackages-local >= 6
BuildRequires:  jsr-305
BuildRequires:  junit
BuildArch:      noarch

%description
Guava is a suite of core and expanded libraries that include
utility classes, Google's collections, io classes, and much
much more.
This project is a complete packaging of all the Guava libraries
into a single jar.  Individual portions of Guava can be used
by downloading the appropriate module and its dependencies.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%package testlib
Summary:        The guava-testlib artifact
Group:          Development/Libraries/Java

%description testlib
guava-testlib provides additional functionality for conveninent unit testing

%prep
%setup -q -a1

find . -name '*.jar' -delete

%pom_disable_module guava-gwt
%pom_disable_module guava-tests

%pom_remove_plugin -r :animal-sniffer-maven-plugin

%pom_xpath_inject /pom:project/pom:build/pom:plugins/pom:plugin/pom:configuration/pom:instructions "<_nouses>true</_nouses>" guava/pom.xml

%pom_remove_dep -r :listenablefuture
%pom_remove_dep -r :failureaccess

%pom_change_dep -r :error_prone_annotations :::provided
%pom_change_dep -r :j2objc-annotations :::provided
%pom_change_dep -r org.checkerframework: :::provided

%build
mkdir -p lib
build-jar-repository -s lib junit jsr-305 google-errorprone/annotations checker-qual j2objc-annotations
%{ant} -Dproject.version=%{version} -Dtest.skip=true package javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 %{name}/target/%{name}-%{version}*.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
install -pm 0644 %{name}-testlib/target/%{name}-testlib-%{version}*.jar %{buildroot}%{_javadir}/%{name}/%{name}-testlib.jar

# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} %{name}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# We integrated this artifact in our main package
%{mvn_install_pom} futures/failureaccess/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/failureaccess.pom
%add_maven_depmap %{name}/failureaccess.pom %{name}/%{name}.jar
%{mvn_install_pom} %{name}-testlib/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-testlib.pom
%add_maven_depmap %{name}/%{name}-testlib.pom %{name}/%{name}-testlib.jar -f %{name}-testlib

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r %{name}/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/%{name}
cp -r %{name}-testlib/target/site/apidocs %{buildroot}%{_javadocdir}/%{name}/%{name}-testlib
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc CONTRIBUTORS README*
%license LICENSE

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%files testlib -f .mfiles-guava-testlib

%changelog
