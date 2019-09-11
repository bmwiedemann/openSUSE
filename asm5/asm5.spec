#
# spec file for package asm5
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


%global base_name asm
%global compat_versions 5.0,5.0.1,5.0.2,5.0.3,5.0.4,5.1,5.2
Name:           %{base_name}5
Version:        5.2
Release:        0
Summary:        Java bytecode manipulation framework
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            http://asm.objectweb.org/
Source:         %{base_name}-%{version}.tar.bz2
Patch0:         %{base_name}-%{version}-sourcetarget.patch
Patch1:         %{base_name}-%{version}-no_bnd.patch
BuildRequires:  ant
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
%setup -q -n %{base_name}-%{version}
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
    -Dcompile.source=8 -Dcompile.target=8 \
    -Dobjectweb.ant.tasks.path=$(build-classpath objectweb-anttask) \
    dist.version jar jdoc

%install
install -d -m 755 %{buildroot}/%{_javadir}/%{name}
# jars
install -m 644 output/dist/lib/*jar %{buildroot}/%{_javadir}/%{name}
(cd %{buildroot}%{_javadir}/%{name} && for jar in *-%{version}.jar; do mv ${jar} ${jar/-%{version}/}; done)

install -m 644 output/dist/lib/all/asm-all-%{version}.jar \
    %{buildroot}%{_javadir}/%{name}-all.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}/%{name}

install -pm 644 output/dist/lib/all/asm-all-%{version}.pom %{buildroot}%{_mavenpomdir}/%{name}-all.pom
%add_maven_depmap %{name}-all.pom %{name}-all.jar -v %{compat_versions}

install -pm 644 output/dist/lib/asm-%{version}.pom %{buildroot}%{_mavenpomdir}/%{name}/asm.pom
%add_maven_depmap %{name}/asm.pom %{name}/asm.jar -v %{compat_versions}

install -pm 644 output/dist/lib/asm-parent-%{version}.pom %{buildroot}%{_mavenpomdir}/%{name}/asm-parent.pom
%add_maven_depmap %{name}/asm-parent.pom -v %{compat_versions}

for i in analysis commons tree util xml; do
	install -pm 644 output/dist/lib/asm-${i}-%{version}.pom %{buildroot}%{_mavenpomdir}/%{name}/asm-${i}.pom
	%add_maven_depmap %{name}/asm-${i}.pom %{name}/asm-${i}.jar -v %{compat_versions}
done

# javadoc
install -d -m 755 %{buildroot}/%{_javadocdir}/%{name}-%{version}
cp -pr output/dist/doc/javadoc/user/* %{buildroot}/%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}/%{_javadocdir}/%{name}
%fdupes -s %{buildroot}
%fdupes -s examples/

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
