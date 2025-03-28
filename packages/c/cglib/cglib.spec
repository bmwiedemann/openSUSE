#
# spec file for package cglib
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


%global tarball_name RELEASE_3_3_0
Name:           cglib
Version:        3.3.0
Release:        0
Summary:        Code Generation Library
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/cglib/cglib
Source0:        https://github.com/cglib/cglib/archive/refs/tags/%{tarball_name}.tar.gz
Source1:        %{name}-%{version}-build.tar.xz
BuildRequires:  ant >= 1.6
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  objectweb-asm >= 5
Provides:       %{name}-nohook = %{version}-%{release}
Obsoletes:      %{name}-nohook < %{version}-%{release}
BuildArch:      noarch

%description
cglib is a powerful, high performance and quality Code Generation
Library, It is used to extend JAVA classes and implements interfaces at
runtime.

%package javadoc
Summary:        Code Generation Library
Group:          Documentation/HTML

%description javadoc
cglib is a powerful, high performance and quality Code Generation
Library, It is used to extend JAVA classes and implements interfaces at
runtime.

%prep
%setup -q -n %{name}-%{tarball_name} -a1

%pom_disable_module cglib-nodep
%pom_disable_module cglib-integration-test
%pom_disable_module cglib-jmh
%pom_xpath_set pom:packaging 'bundle' cglib
%pom_xpath_inject pom:build/pom:plugins '<plugin>
                                           <groupId>org.apache.felix</groupId>
                                           <artifactId>maven-bundle-plugin</artifactId>
                                           <version>1.4.0</version>
                                           <extensions>true</extensions>
                                           <configuration>
                                             <instructions>
                                               <Bundle-SymbolicName>net.sf.cglib.core</Bundle-SymbolicName>
                                               <Export-Package>net.*</Export-Package>
                                               <Import-Package>org.apache.tools.*;resolution:=optional,*</Import-Package>
                                             </instructions>
                                           </configuration>
                                         </plugin>' cglib
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-jarsigner-plugin cglib-sample
%pom_remove_plugin -r :maven-javadoc-plugin

%pom_remove_dep -r junit:junit

%build
mkdir -p lib
build-jar-repository -s -p lib objectweb-asm/asm ant/ant ant/ant-launcher
%{ant} \
    -Dtest.skip=true \
    -Dcompiler.target=1.8 -Dcompiler.source=1.8 \
    package javadoc

%install

# jars
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 %{name}/target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
install -pm 0644 %{name}-sample/target/%{name}-sample-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}-sample.jar

# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%mvn_install_pom %{name}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar -a "net.sf.cglib:cglib,cglib:cglib-full,cglib:cglib-nodep,org.sonatype.sisu.inject:cglib"
%mvn_install_pom %{name}-sample/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}-sample.pom
%add_maven_depmap %{name}/%{name}-sample.pom %{name}/%{name}-sample.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r %{name}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc
%{_javadocdir}/%{name}

%changelog
