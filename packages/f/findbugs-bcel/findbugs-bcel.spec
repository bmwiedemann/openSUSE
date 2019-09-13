#
# spec file for package findbugs-bcel
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global basever 6.0
%global findbugsver 20140707svn1547656
# This is a version of BCEL that has been modified by the findbugs team.  They
# added some new functionality and also did some performance optimizations of
# the base code.  I am not producing a new manual, since we already have a
# bcel-manual package and the findbugs team did not patch the manual.  However,
# the javadoc package is necessary to show the changes in the API created by
# the findbug team's work.
Name:           findbugs-bcel
Version:        %{basever}~%{findbugsver}
Release:        0
Summary:        Byte Code Engineering Library with findbugs extensions
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/proper/commons-bcel/
# This archive was created with:
#   $ svn export http://svn.apache.org/repos/asf/commons/proper/bcel/trunk -r 1547656 bcel-6.0
#   $ tar -Jcf bcel-20140707svn1547656.tar.xz bcel-6.0
Source0:        bcel-%{findbugsver}.tar.xz
Source1:        http://central.maven.org/maven2/com/google/code/findbugs/bcel-findbugs/%{basever}/bcel-findbugs-%{basever}.pom
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  xz
Requires:       java >= 1.8
Requires:       javapackages-tools
BuildArch:      noarch

%description
This is a version of Apache's Byte Code Engineering Library (BCEL) that has
been modified by the findbugs developers.  The modifications add some new
functionality, and also introduce a number of performance optimizations to
address findbugs performance problems.  Some of the performance optimizations
induce API changes, so this version of BCEL is not compatible with the vanilla
upstream version.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
%{summary} package.

%prep
%setup -q -n bcel-%{basever}

%build
mkdir classes
javac -g -d classes -source 8 -target 8 -encoding ISO8859-1 $(find src/main/java -type f -name '*.java' | xargs)
jar cf findbugs-bcel.jar -C classes org

mkdir javadoc
javadoc -notimestamp -classpath classes -source 8 -encoding ISO8859-1 -d javadoc \
  $(find src/main/java -type f -name '*.java' | xargs)

%install
# jar and pom
mkdir -p %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 findbugs-bcel.jar %{buildroot}%{_javadir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar -a "com.google.code.findbugs:bcel"
# javadoc
mkdir -p %{buildroot}%{_javadocdir}
cp -a javadoc %{buildroot}%{_javadocdir}/findbugs-bcel
%fdupes -s %{buildroot}%{_javadocdir}/findbugs-bcel

%files -f .mfiles
%license LICENSE.txt
%doc NOTICE.txt README.txt

%files javadoc
%license LICENSE.txt
%doc NOTICE.txt
%{_javadocdir}/findbugs-bcel*

%changelog
