#
# spec file for package asm3
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define version_str 3_3_2
%define compat_version 3.0,3.1,3.2,3.3,3.3.1,3.3.2
Name:           asm3
Version:        3.3.2
Release:        0
Summary:        Java bytecode manipulation framework
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            http://asm.objectweb.org/
Source:         https://gitlab.ow2.org/asm/asm/-/archive/ASM_%{version_str}/asm-ASM_%{version_str}.tar.bz2
Patch0:         asm-3.3.1-sourcetarget.patch
Patch1:         fix-incorrect-version.patch
BuildRequires:  ant
BuildRequires:  coreutils
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  objectweb-anttask
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
Group:          Development/Libraries/Java

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
%setup -q -n asm-ASM_%{version_str}
%patch0 -p1
%patch1 -p1
# remove all third party jars
find . -iname '*.jar' | xargs rm -rf
# wrong end of line encoding
find examples/ -type 'f' | xargs sed -i -e 's/.$//'
sed -i -e 's/.$//' README.txt LICENSE.txt
mkdir -p test/lib

%build
ant \
    -Dcompile.source=6 -Dcompile.target=6 \
    -Dobjectweb.ant.tasks.path=$(build-classpath objectweb-anttask) \
    jar jdoc

%install
install -d -m 755 %{buildroot}/%{_javadir}/%{name}
# jars
install -m 644 output/dist/lib/*jar %{buildroot}%{_javadir}/%{name}
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}*; do mv ${jar} ${jar/-%{version}/}; done)

install -m 644 output/dist/lib/all/asm-all-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}-all-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do mv ${jar} ${jar/-%{version}/}; done)

# javadoc
install -d -m 755 %{buildroot}/%{_javadocdir}/%{name}-%{version}
cp -pr output/dist/doc/javadoc/user/* %{buildroot}/%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}/%{_javadocdir}/%{name}
%fdupes -s %{buildroot}
%fdupes -s examples/

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{name}

install -pm 644 output/dist/lib/asm-parent-%{version}.pom %{buildroot}%{_mavenpomdir}/%{name}/asm-parent.pom
%add_maven_depmap %{name}/asm-parent.pom -v %{compat_version}

install -pm 644 output/dist/lib/all/asm-all-%{version}.pom %{buildroot}%{_mavenpomdir}/%{name}-all.pom
%add_maven_depmap %{name}-all.pom %{name}-all.jar -v %{compat_version}

install -pm 644 output/dist/lib/asm-%{version}.pom %{buildroot}%{_mavenpomdir}/%{name}/asm.pom
%add_maven_depmap %{name}/asm.pom %{name}/asm.jar -v %{compat_version}

for i in analysis commons tree util xml; do
	install -pm 644 output/dist/lib/asm-$i-%{version}.pom %{buildroot}%{_mavenpomdir}/%{name}/asm-$i.pom
	%add_maven_depmap %{name}/asm-$i.pom %{name}/asm-$i.jar -v %{compat_version}
done

(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}.jar; do ln -s $(readlink ${jar}) ${jar/-%{version}/}; done)
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sL $(readlink ${jar}) ${jar/-%{version}/}; done)

%files -f .mfiles
%license LICENSE.txt
%doc README.txt
%{_javadir}/%{name}*

%files javadoc
%{_javadocdir}/%{name}-%{version}
%{_javadocdir}/%{name}

%files examples
%doc examples/*

%changelog
