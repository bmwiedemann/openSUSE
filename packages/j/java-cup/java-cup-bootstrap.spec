#
# spec file for package java-cup-bootstrap
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


##### WARNING: please do not edit this auto generated spec file. Use the java-cup.spec! #####
%global with_bootstrap 1
%define cvs_version        11b
%define real_name   java-cup
%define git_hash d69c832
%define git_date 20210814
%bcond_with                bootstrap
Name:           java-cup-bootstrap
Version:        0.11
Release:        0
Summary:        LALR Parser Generator in Java
License:        HPND
Group:          Development/Libraries/Java
URL:            http://www2.cs.tum.edu/projects/cup/
Source0:        %{real_name}-%{git_hash}.tar.xz
Source1:        %{real_name}-generated-files.tar.xz
Source100:      java-cup-nogit.patch.in
Patch0:         java-cup-no-classpath-in-manifest.patch
Patch1:         java-cup-java8.patch
Patch2:         java-cup-no-cup-no-jflex.patch
Patch3:         java-cup-classpath.patch
BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  xml-commons-apis-bootstrap
BuildRequires:  xml-commons-resolver-bootstrap
#!BuildIgnore:  xalan-j2
#!BuildIgnore:  xerces-j2
#!BuildIgnore:  xml-commons-apis
#!BuildIgnore:  xml-commons-resolver
Obsoletes:      java_cup < %{version}-%{release}
Provides:       java_cup = %{version}-%{release}
BuildArch:      noarch
%if %{without bootstrap}
BuildRequires:  java-cup-bootstrap
BuildRequires:  javapackages-local
BuildRequires:  jflex-bootstrap
Conflicts:      java-cup-bootstrap
%else
Conflicts:      java-cup
%endif

%description
java-cup is a LALR Parser Generator in Java. With v0.11, you can: *
   use CUP in an Ant-Target

* start CUP by a simple command like java -jar java-cup-11a.jar
   myGrammar.cup

* use generic parametrized classes (since Java 1.5) as datatypes for
   non terminals and terminals

* have Your own symbol classes

%if %{without bootstrap}
%package manual
Summary:        LALR Parser Generator in Java
Group:          Development/Libraries/Java

%description manual
java-cup is a LALR Parser Generator in Java. With v0.11, you can: *
   use CUP in an Ant-Target

* start CUP by a simple command like java -jar java-cup-11a.jar
   myGrammar.cup

* use generic parametrized classes (since Java 1.5) as datatypes for
   non

* terminals and terminals

* have Your own symbol classes

%endif

%prep
%setup -q -n %{real_name}-%{git_hash}
cat %{SOURCE100} | sed 's#@GIT_HASH@#%{git_hash}#g' | sed 's#@GIT_DATE@#%{git_date}#g' | patch -p1 -u -l
%patch0 -p1
%patch1 -p1
%if %{with bootstrap}
%setup -q -T -D -a 1 -n %{real_name}-%{git_hash}
%patch2 -p1
%else
%patch3 -p1
%endif
find . -name '*.jar' -print -delete
mkdir -p target/classes

%build
%if %{with bootstrap}
export CLASSPATH=
%else
export CLASSPATH=$(build-classpath java-cup jflex)
%endif
export OPT_JAR_LIST=:
ant

%install
# jar
mkdir -p %{buildroot}%{_javadir}
cp -a target/dist/%{real_name}-%{cvs_version}.jar %{buildroot}%{_javadir}/%{real_name}.jar
cp -a target/dist/%{real_name}-%{cvs_version}-runtime.jar %{buildroot}%{_javadir}/%{real_name}-runtime.jar

%if %{without bootstrap}
# maven data
%add_maven_depmap com.github.vbmacher:%{real_name}:%{cvs_version}-%{git_date} %{real_name}.jar
%add_maven_depmap com.github.vbmacher:%{real_name}-runtime:%{cvs_version}-%{git_date} %{real_name}-runtime.jar
%endif

# compatibility symlinks
(cd %{buildroot}%{_javadir} && ln -s %{real_name}.jar java_cup.jar && ln -s %{real_name}-runtime.jar java_cup-runtime.jar)
mkdir -p %{buildroot}%{_bindir}

%jpackage_script java_cup.Main "" "" %{real_name}:%{real_name}-runtime %{real_name} true

%if %{with bootstrap}
%files
%{_javadir}/%{real_name}*.jar
%else

%files -f .mfiles
%endif
%license licence.txt
%doc changelog.txt
%attr(0755,root,root) %{_bindir}/%{real_name}
%{_javadir}/java_cup*.jar

%if %{without bootstrap}
%files manual
%doc manual.html

%endif

%changelog
