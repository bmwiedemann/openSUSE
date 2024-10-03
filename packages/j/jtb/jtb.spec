#
# spec file for package jtb
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2000-2005, JPackage Project
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


Name:           jtb
Version:        1.5.1
Release:        0
Summary:        JTB: Java Tree Builder
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://github.com/jtb-javacc/JTB
Source0:        %{name}-%{version}.tar.xz
Patch0:         build-fix.patch
Patch1:         jtb-javac-encoding.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javacc
BuildRequires:  javapackages-local >= 6
Requires:       javapackages-tools
BuildArch:      noarch

%description
JTB is a syntax tree builder to be used with the JavaCC
(Java Compiler Compiler) parser generator.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1

%build
# Build first the bootstrap jar from the pregenerated sources
mkdir -p target/classes
javac \
    -d target/classes \
    -proc:none \
    -encoding utf-8 \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
    --release 8 \
%else
    -source 1.8 \
    -target 1.8 \
%endif
    $(find src/main/java -name \*.java && \
    find target/generated-sources -name \*.java | xargs)
# no need to bother with timestamp, since we are not
# distributing this one, so use the short options
jar -cf %{name}-bootstrap.jar -C target/classes .

# Build now the release including the regeneration of
ant \
    build_new_jtb_jar \
    -Dno_code_coverage=true \
    -Djtb_ok_jar=%{name}-bootstrap.jar \
    -Djavacc_ok_jar=$(find-jar javacc) \
    -Djtb_new_jar=target/%{name}-%{version}.jar

# Generate javadoc
mkdir -p target/site/apidocs
javadoc \
    -d target/site/apidocs \
    -source 1.8 \
    -encoding utf-8 \
    -notimestamp \
    $(find src/main/java -name \*.java && \
    find target/generated-sources -name \*.java | xargs)

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a edu.ucla.cs.compilers:jtb

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

# command-line script
%jpackage_script EDU.purdue.jtb.JTB '' '' jtb %{name} true

%files -f .mfiles
%{_bindir}/%{name}
%doc README.md

%files javadoc
%{_javadocdir}/%{name}

%changelog
