#
# spec file for package aelfred
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           aelfred
Version:        7.0
Release:        0
Summary:        Java-based XML parser
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            http://saxon.sourceforge.net/aelfred.html
Source0:        http://downloads.sourceforge.net/project/saxon/aelfred/7.0/aelfred7_0.zip
Patch0:         aelfred-icedtea-build.patch
BuildRequires:  ant
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  unzip
BuildArch:      noarch

%description
AElfred is a Java-based XML parser from Microstar Software Ltd. AElfred
is distributed for free (with full source) for both commercial and
non-commercial use.

%package javadoc
Summary:        Java-based XML parser (documentation)
Group:          Development/Libraries/Java

%description javadoc
Javadoc for aelfred.

%package demo
Summary:        Java-based XML parser (demo and samples)
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}

%description demo
Demonstrations and samples for aelfred.

%prep
%setup -q -c
unzip %{name}-source.zip
%patch0

%build
export JAVA_HOME=%{java_home}
export PATH=%{java_home}/bin:$PATH
export CLASSPATH=
cd net
%{javac} -source 8 -target 8 `find . -name \*.java`
%{javadoc} -notimestamp -source 8 -d ../HTML `find . -name \*.java`

%install
# jar
export JAVA_HOME=%{java_home}
cd net
mkdir -p %{buildroot}%{_javadir}
cp -a ../saxon-%{name}.jar \
%{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do \
ln -s ${jar} ${jar/-%{version}/}; done)
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -a ../HTML/* %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%{_javadir}/*

%files javadoc
%defattr(0644,root,root,0755)
%dir %{_javadocdir}/%{name}
%{_javadocdir}/%{name}/*

%changelog
