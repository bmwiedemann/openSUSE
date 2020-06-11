#
# spec file for package antlr
#
# Copyright (c) 2020 SUSE LLC
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


%bcond_without python2
Name:           antlr
Version:        2.7.7
Release:        0
Summary:        Another Tool for Language Recognition
License:        GPL-2.0-or-later AND SUSE-Public-Domain AND MIT
Group:          Development/Tools/Other
URL:            https://www.antlr.org/
Source0:        antlr-%{version}.tar.bz2
Source1:        %{name}-build.xml
Source2:        %{name}-script
Source3:        http://repo2.maven.org/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Source1000:     antlr-rpmlintrc
Patch0:         %{name}-jedit.patch
Patch1:         gcc45fix.diff
Patch2:         fix-docpath.diff
BuildRequires:  ant
BuildRequires:  gcc-c++
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  xml-commons-apis
Requires:       %{name}-java
Provides:       %{name}-bootstrap = %{version}
Obsoletes:      %{name}-bootstrap < %{version}
Obsoletes:      %{name}-javadoc
%if %{with python2}
BuildRequires:  python2-base
%endif

%description
ANTLR, Another Tool for Language Recognition, (formerly PCCTS) is a
language tool that provides a framework for constructing recognizers,
compilers, and translators from grammatical descriptions containing C++
or Java actions (you can use PCCTS 1.xx to generate C-based parsers).

%package        java
Summary:        ANother Tool for Language Recognition (Manual)
Group:          Development/Tools/Other
Requires:       java >= 1.8
BuildArch:      noarch

%description    java
ANTLR, Another Tool for Language Recognition, (formerly PCCTS) is a
language tool that provides a framework for constructing recognizers,
compilers, and translators from grammatical descriptions containing C++
or Java actions (you can use PCCTS 1.xx to generate C-based parsers).

This package provides the Java runtime for antlr

%package        manual
Summary:        ANother Tool for Language Recognition (Manual)
Group:          Development/Tools/Other
BuildArch:      noarch

%description    manual
ANTLR, Another Tool for Language Recognition, (formerly PCCTS) is a
language tool that provides a framework for constructing recognizers,
compilers, and translators from grammatical descriptions containing C++
or Java actions (you can use PCCTS 1.xx to generate C-based parsers).

This package provides the manual for antlr.

%package        devel
Summary:        ANother Tool for Language Recognition (c++ runtime)
Group:          Development/Tools/Other
Requires:       antlr

%description    devel
ANTLR, Another Tool for Language Recognition, (formerly PCCTS) is a
language tool that provides a framework for constructing recognizers,
compilers, and translators from grammatical descriptions containing C++
or Java actions (you can use PCCTS 1.xx to generate C-based parsers).

This package provides the C++ runtime (libantlr.a) and a headers files
of antlr

%package -n     python2-%{name}
Summary:        ANother Tool for Language Recognition (python runtime)
Group:          Development/Tools/Other
Requires:       antlr
Provides:       python-%{name}
Obsoletes:      python-%{name}

%description -n  python2-%{name}
Python support for generating your Lexers, Parsers and TreeParsers in Python.
This feature extends the benefits of ANTLR's predicated-LL(k) parsing
technology to the Python language and platform.

ANTLR Python support was contributed (and is to be maintained) by Wolfgang
Haefelinger and Marq Kole.

%prep
%setup -q
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
find . -name "*.exe" -exec rm -f {} \;
find . -name "*.dll" -exec rm -f {} \;
find . -name Makefile.in | xargs chmod 0644
%patch0
cp -p %{SOURCE1} build.xml
#Fix the source so that it compiles with GCC 4.5
%patch1 -p1
#Ensure that the manuals are installed in the correct openSUSE docpath
%patch2
# check for license problematic files:
find | grep "\(ShowString.java$\|StreamConverter.java$\)" && exit 42 || :

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
ant \
    -Dj2se.apidoc=%{_javadocdir}/java \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    jar
%configure --without-examples
make -j1

%if %{with python2}
%py_compile lib/python/antlr
%endif

%install
### jars ###
install -d -m 0755 %{buildroot}%{_javadir}
cp -a work/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}.jar; do ln -s -f ${jar} `echo $jar| sed "s|-%{version}||g"`; done)
# compat symlink
install -d -m 0755 %{buildroot}%{_datadir}/%{name}-%{version}/
ln -s -f %{_javadir}/%{name}-%{version}.jar %{buildroot}%{_datadir}/%{name}-%{version}/%{name}.jar

### pom ###
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 %{SOURCE3} %{buildroot}%{_mavenpomdir}/%{name}-%{version}.pom
%add_maven_depmap %{name}-%{version}.pom %{name}-%{version}.jar -a %{name}:%{name}all -f java

### scripts ###
install -d -m 0755 %{buildroot}%{_bindir}/
install -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}
install -m 0755 scripts/%{name}-config %{buildroot}%{_bindir}/

### python runtime ###
%if %{with python2}
install -d -m 0755 %{buildroot}%{python_sitearch}/%{name}
cp -a lib/python/antlr/* %{buildroot}%{python_sitearch}/%{name}
%endif

### cpp runtime ###
mkdir -p %{buildroot}%{_libdir}
install -m 0755 lib/cpp/src/lib%{name}.a %{buildroot}%{_libdir}
install -d -m 0755 %{buildroot}%{_includedir}/%{name}
install -m 0644 lib/cpp/%{name}/*hpp %{buildroot}%{_includedir}/%{name}

### doc permissions ###
rm doc/{Makefile,Makefile.in}
find doc -type f | xargs chmod 0644

%files
%license LICENSE.txt
%doc README.txt CHANGES.txt
%dir %{_datadir}/%{name}-%{version}
%{_bindir}/antlr
%{_bindir}/antlr-config

%files java
%dir %{_datadir}/%{name}-%{version}
%{_datadir}/%{name}-%{version}/*jar
%{_javadir}/%{name}*.jar
%{_mavenpomdir}/*
%if %{defined _maven_repository}
%config(noreplace) %{_mavendepmapfragdir}/%{name}-java
%else
%{_datadir}/maven-metadata/%{name}-java.xml
%endif

%files manual
%doc doc

%files devel
%{_libdir}/libantlr.a
%{_includedir}/%{name}

%if %{with python2}
%files -n python2-%{name}
%dir %{_datadir}/%{name}-%{version}
%{python_sitearch}/%{name}
%endif

%changelog
