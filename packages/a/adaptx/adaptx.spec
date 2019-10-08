#
# spec file for package adaptx
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


Name:           adaptx
Version:        0.9.13
Release:        0
Summary:        XSLT Processor Written in Java
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            http://castor.exolab.org/
Source0:        %{name}-%{version}-src.tar.bz2
# svn export http://svn.codehaus.org/castor/adaptx
Patch0:         %{name}-%{version}-xsl.patch
Patch1:         %{name}-%{version}-icedtea-build.patch
BuildRequires:  ant >= 1.6
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  log4j12
BuildRequires:  xerces-j2
BuildRequires:  xml-apis
Requires:       log4j12
Requires:       xerces-j2
Requires:       xml-apis
BuildArch:      noarch

%description
AdaptX is an extensible stylesheet language (XSL) processor.

%package javadoc
Summary:        Javadoc for adaptx
Group:          Development/Libraries/Java

%description javadoc
This package contains the javadoc documentation for AdaptX.

%package doc
Summary:        Documentation for adaptx
Group:          Development/Libraries/Java

%description doc
This package contains the documentation for AdaptX.

%prep
%setup -q -n %{name}-%{version}-src
# remove CVS internal files
for dir in `find . -type d -name CVS`; do rm -rf $dir; done
# remove all binary libs
for j in $(find . -name "*.jar"); do
	mv $j $j.no
done
%patch0
%patch1

%build
perl -p -i -e 's|classic|modern|' src/build.xml
export CLASSPATH=$(build-classpath xml-apis log4j12/log4j-12 xerces-j2)
ant -Dant.build.javac.source=8 -Dant.build.javac.target=8 -buildfile src/build.xml jar javadoc
CLASSPATH=$CLASSPATH:dist/adaptx_%{version}.jar
ant -Dant.build.javac.source=8 -Dant.build.javac.target=8 -buildfile src/build.xml doc

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/%{name}_%{version}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -sf ${jar} ${jar/-%{version}/}; done)
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/doc/javadoc/* %{buildroot}%{_javadocdir}/%{name}
rm -rf build/doc/javadoc

%files
%defattr(0664,root,root,0755)
%doc src%{_sysconfdir}/{CHANGELOG,contributors.html,LICENSE}
%{_javadir}/*

%files javadoc
%defattr(0664,root,root,0755)
%{_javadocdir}/%{name}

%files doc
%defattr(0664,root,root,0755)
%doc build/doc/*

%changelog
