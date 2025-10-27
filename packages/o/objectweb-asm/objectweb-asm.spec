#
# spec file for package objectweb-asm
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define __requires_exclude java-headless
Name:           objectweb-asm
Version:        9.9
Release:        0
Summary:        Java bytecode manipulation framework
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://asm.objectweb.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.tar.xz
Source2:        https://repo1.maven.org/maven2/org/ow2/asm/asm/%{version}/asm-%{version}.pom
Source3:        https://repo1.maven.org/maven2/org/ow2/asm/asm-analysis/%{version}/asm-analysis-%{version}.pom
Source4:        https://repo1.maven.org/maven2/org/ow2/asm/asm-commons/%{version}/asm-commons-%{version}.pom
Source5:        https://repo1.maven.org/maven2/org/ow2/asm/asm-test/%{version}/asm-test-%{version}.pom
Source6:        https://repo1.maven.org/maven2/org/ow2/asm/asm-tree/%{version}/asm-tree-%{version}.pom
Source7:        https://repo1.maven.org/maven2/org/ow2/asm/asm-util/%{version}/asm-util-%{version}.pom
# We still want to create an "all" uberjar, so this is a custom pom to generate it
# TODO: Fix other packages to no longer depend on "asm-all" so we can drop this
Source9:        asm-all.pom
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local >= 6
BuildRequires:  xz
Requires:       java >= 1.8
# For the script
Requires:       javapackages-tools
Obsoletes:      %{name}-examples
BuildArch:      noarch

%description
ASM is a Java bytecode manipulation framework.

It can be used to dynamically generate stub classes or other proxy
classes, directly in binary form, or to dynamically modify classes at
load time, i.e., just before they are loaded into the Java Virtual
Machine.

ASM offers similar functionalities as BCEL or SERP, but is much
smaller.

%package javadoc
Summary:        Java bytecode manipulation framework
Group:          Documentation/HTML

%description javadoc
ASM is a Java bytecode manipulation framework.

It can be used to dynamically generate stub classes or other proxy
classes, directly in binary form, or to dynamically modify classes at
load time, i.e., just before they are loaded into the Java Virtual
Machine.

ASM offers similar functionalities as BCEL or SERP, but is much
smaller.

%package examples
Summary:        Java bytecode manipulation framework
Group:          Development/Libraries/Java

%description examples
ASM is a Java bytecode manipulation framework.

It can be used to dynamically generate stub classes or other proxy
classes, directly in binary form, or to dynamically modify classes at
load time, i.e., just before they are loaded into the Java Virtual
Machine.

ASM offers similar functionalities as BCEL or SERP, but is much
smaller.

%prep
%setup -q -a1
cp %{SOURCE2} asm/pom.xml
cp %{SOURCE3} asm-analysis/pom.xml
cp %{SOURCE4} asm-commons/pom.xml
cp %{SOURCE5} asm-test/pom.xml
cp %{SOURCE6} asm-tree/pom.xml
cp %{SOURCE7} asm-util/pom.xml
# Insert asm-all pom
mkdir -p asm-all
sed 's/@VERSION@/%{version}/g' %{SOURCE9} > asm-all/pom.xml

for i in asm asm-analysis asm-commons asm-tree asm-util asm-all; do
  %pom_remove_parent ${i}
done

%build
%{ant} -Dproject.version=%{version} \
    package javadoc

%install
# jars
install -dm 0755 %{buildroot}/%{_javadir}/%{name}
for i in asm asm-analysis asm-commons asm-tree asm-util asm-all; do
  install -pm 0644 ${i}/target/${i}-%{version}.jar %{buildroot}/%{_javadir}/%{name}/${i}.jar
done

# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
for i in asm asm-analysis asm-commons asm-tree asm-util; do
  %{mvn_install_pom} ${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/${i}.pom
  %add_maven_depmap %{name}/${i}.pom %{name}/${i}.jar
done
%{mvn_install_pom} asm-all/pom.xml %{buildroot}%{_mavenpomdir}/%{name}/asm-all.pom
%add_maven_depmap %{name}/asm-all.pom %{name}/asm-all.jar -a org.ow2.asm:asm-debug-all

# javadoc
install -dm 0755 %{buildroot}/%{_javadocdir}/%{name}
for i in asm asm-analysis asm-commons asm-tree asm-util; do
  cp -pr ${i}/target/site/apidocs %{buildroot}/%{_javadocdir}/%{name}/${i}
done
%fdupes -s %{buildroot}/%{_javadocdir}

# script
%jpackage_script org.objectweb.asm.xml.Processor "" "" %{name}/asm:%{name}/asm-util %{name}-processor true

%files -f .mfiles
%license LICENSE.txt
%{_bindir}/%{name}-processor

%files javadoc
%{_javadocdir}/%{name}

%changelog
