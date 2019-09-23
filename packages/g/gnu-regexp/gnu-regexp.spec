#
# spec file for package gnu-regexp
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


Name:           gnu-regexp
Version:        1.1.4
Release:        0
Summary:        Java NFA regular expression engine
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Java
Url:            http://www.cacas.org/java/gnu/regexp/
Source0:        ftp://ftp.tralfamadore.com/pub/java/gnu.regexp-%{version}.tar.gz
Source1:        %{name}.build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  gnu-getopt
BuildRequires:  java-devel >= 1.8
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The gnu-regexp package is a pure-Java implementation of a traditional
(non-POSIX) NFA regular expression engine. Its syntax can emulate many
popular development tools, including awk, sed, emacs, perl and grep.
For a relatively complete list of supported and non-supported syntax,
refer to the syntax and usage notes.

%package demo
Summary:        Java NFA regular expression engine (demo and samples)
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}
Requires:       gnu-getopt

%description demo
Demonstrations and samples for Java NFA regular expression engine gnu-regexp.

%package javadoc
Summary:        Java NFA regular expression engine (documentation)
Group:          Development/Libraries/Java

%description javadoc
Javadoc for Java NFA regular expression engine gnu-regexp.

%prep
%setup -q -n gnu.regexp-1.1.4
cp -a %{SOURCE1} build.xml
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;

%build
export CLASSPATH=$(build-classpath gnu.getopt)
ant jar javadoc

%install
# jars
mkdir -p %{buildroot}%{_javadir}
cp -a build/lib/gnu.regexp.jar %{buildroot}%{_javadir}/gnu.regexp-%{version}.jar
(cd %{buildroot}%{_javadir} && ln -sf gnu.regexp-%{version}.jar %{name}-%{version}.jar && \
    for jar in *-%{version}*; do ln -s ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
# demo
mkdir -p %{buildroot}%{_datadir}/gnu.regexp/gnu/regexp/util
cp -a build/classes/gnu/regexp/util/*.class \
  %{buildroot}%{_datadir}/gnu.regexp/gnu/regexp/util
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/gnu.regexp
cp -a build/api/* %{buildroot}%{_javadocdir}/gnu.regexp
%fdupes -s %{buildroot}%{_javadocdir}/gnu.regexp

%files
%defattr(0644,root,root,0755)
%doc COPYING COPYING.LIB README TODO docs/*.html
%{_javadir}/*

%files demo
%defattr(0644,root,root,0755)
%{_datadir}/gnu.regexp

%files javadoc
%defattr(0644,root,root,0755)
%dir %{_javadocdir}/gnu.regexp
%{_javadocdir}/gnu.regexp/*

%changelog
