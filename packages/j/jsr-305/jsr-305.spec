#
# spec file for package jsr-305
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


%global svn_revision 51
%global svn_date 20130910
Name:           jsr-305
Version:        0.1+%{svn_date}
Release:        0
Summary:        Correctness annotations for Java code
# The majority of code is BSD-licensed, but some Java sources
# are licensed under CC-BY license, see: $ grep -r Creative .
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            http://code.google.com/p/jsr-305/
# There has been no official release yet.  This is a snapshot of the Subversion
# repository as of 10 Sep 2013.  Use the following commands to generate the
# tarball:
#   svn export -r %{svn_revision} http://%{name}.googlecode.com/svn/trunk %{name}
#   tar -czvf %{name}-%{svn_date}svn.tgz %{name}
Source0:        jsr-305-%{svn_date}svn.tgz
Source1:        jsr-305-ri-build.xml
# File containing URL to CC-BY license text
Source2:        NOTICE-CC-BY.txt
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  javapackages-local
BuildArch:      noarch

%package javadoc
Summary:        Javadoc documentation for %{name}
Group:          Documentation/HTML

%description
This package contains reference implementations, test cases, and other
documents for Java Specification Request 305: Annotations for Software Defect
Detection.

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n %{name}
cp -a %{SOURCE1} ri/build.xml
cp %{SOURCE2} NOTICE-CC-BY
dos2unix sampleUses/pom.xml

# do not build sampleUses module - it causes Javadoc generation to fail
%pom_disable_module sampleUses

for module in ri tcl sampleUses proposedAnnotations; do
  %pom_remove_parent ${module}
done

%build
export OPT_JAR_LIST=:
export CLASSPATH=
pushd ri
%{ant} -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
       -Dversion=%{version} -Djava.javadoc=%{_javadocdir}/java
popd

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 ri/jsr-305-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/jsr305.jar

# poms
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
install -pm 0644 ri/pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a com.google.code.findbugs:jsr305

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr ri/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license ri/LICENSE NOTICE-CC-BY
%{_javadir}/jsr305.jar

%files javadoc
%license ri/LICENSE NOTICE-CC-BY
%{_javadocdir}/%{name}

%changelog
