#
# spec file for package cpptasks
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


Name:           cpptasks
Version:        1.0b5
Release:        0
Summary:        Compile and link task
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://ant-contrib.sourceforge.net/
Source0:        http://downloads.sourceforge.net/ant-contrib/%{name}-%{version}.tar.gz
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  jpackage-utils
BuildRequires:  junit
Requires:       ant
Requires:       java >= 1.8
BuildArch:      noarch

%description
This ant task can compile various source languages and produce
executables, shared libraries and static libraries. Compiler adaptors
are currently available for several C/C++ compilers, FORTRAN,
MIDL and Windows Resource files.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/Other

%description    javadoc
Javadoc documentation for %{summary}.

%prep
%setup -q
find . -name '*.jar' -type f -delete -print

%build
export OPT_JAR_LIST="ant/ant-junit junit"
export CLASSPATH=""
%{ant} \
     -Djavac.source=8 -Djavac.target=8 \
     jars javadocs

%install
# jars
install -Dpm 644 target/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
install -dm 755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/javadocs/* %{buildroot}%{_javadocdir}/%{name}-%{version}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} %{buildroot}%{_javadocdir}/%{name} # ghost symlink

mkdir -p %{buildroot}%{_sysconfdir}/ant.d
echo "cpptasks" > %{buildroot}%{_sysconfdir}/ant.d/cpptasks

%files
%{_javadir}/*.jar
%config %{_sysconfdir}/ant.d/%{name}

%files javadoc
%doc %{_javadocdir}/%{name}-%{version}
%doc %{_javadocdir}/%{name}

%changelog
