#
# spec file for package tanukiwrapper
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2000-2006, JPackage Project
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


Name:           tanukiwrapper
Version:        3.5.35
Release:        0
Summary:        Java Service Wrapper
License:        GPL-2.0-only
Group:          Development/Languages/Java
Url:            http://wrapper.tanukisoftware.org/
Source0:        http://download.sourceforge.net/wrapper/wrapper_%{version}_src.tar.gz
Source1:        wrapper.1
Patch0:         %{name}-additional-makefiles.patch
Patch1:         %{name}-nojavah.patch
BuildRequires:  ant >= 1.6.1
BuildRequires:  ant-junit
BuildRequires:  ant-nodeps >= 1.6.1
BuildRequires:  cunit-devel
BuildRequires:  fdupes
BuildRequires:  glibc-devel
BuildRequires:  java-devel >= 1.6
BuildRequires:  javapackages-tools
BuildRequires:  perl
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis

%description
The Java Service Wrapper is an application which has
evolved out of a desire to solve a number of problems
common to many Java applications:
- Run as a Windows Service or Unix Daemon
- Application Reliability
- Standard, Out of the Box Scripting
- On Demand Restarts
- Flexible Configuration
- Ease Application installations
- Logging

%package javadoc
Summary:        Javadoc documentation for %{name}
Group:          Documentation/Other

%description javadoc
This package contains the javadoc documentation for %{name}

%package manual
Summary:        Manuals for %{name}
Group:          Documentation/Other

%description manual
This package contains the manuals for %{name}

%prep
%setup -q -n wrapper_%{version}_src
%patch0 -p1
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 10}%{!?pkg_vcmp:0}
%patch1 -p1
%endif

find . -name "*.jar" -exec rm -f {} \;
perl -p -i -e 's|-O3|%{optflags}|' src/c/Makefile*
rm -f bin/* build/* conf/* lib/* logs/* test/* src/c/*.o src/c/wrapperinfo.c

%build
export CLASSPATH=$(build-classpath ant junit xerces-j2 xml-commons-apis)
ant \
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
    -Djavac.target.version=1.6 -Djava.specification.version=1.6 \
    -Dbuild.sysclasspath=first -Dbits=%{__isa_bits}

javadoc -notimestamp -source 1.6 -sourcepath src/java -d build/javadoc org.tanukisoftware.wrapper

%install
# jar
mkdir -p %{buildroot}%{_javadir}
install -p -m 0644 lib/wrapper.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
(cd %{buildroot}%{_javadir} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar| sed  "s|-%{version}||g"`; done)

# jni
install -d -m 755 %{buildroot}%{_libdir}
install -p -m 755 lib/libwrapper.so %{buildroot}%{_libdir}

# commands
install -d -m 755 %{buildroot}%{_sbindir}
install -p -m 755 bin/wrapper %{buildroot}%{_sbindir}/%{name}

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -a build/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

# manpage
mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1/%{name}.1

%check
ant \
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
    -Djavac.target.version=1.6 -Djava.specification.version=1.6 \
    -Dbuild.sysclasspath=first -Dbits=%{__isa_bits} \
    test

%files
%doc doc/wrapper-community-license-1.3.txt
%{_sbindir}/%{name}
%{_libdir}/libwrapper.so
%{_javadir}/%{name}*.jar
%{_mandir}/man1/%{name}.1%{?ext_man}

%files javadoc
%{_javadocdir}/%{name}

%files manual
%doc doc/*

%changelog
