#
# spec file for package jisp2
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%{!?make_build:%global make_build make %{?_smp_mflags}}
Name:           jisp2
Version:        2.5.1
Release:        0
Summary:        The Java Indexed Serialization Package
License:        Libpng
Group:          Development/Libraries/Java
URL:            https://www.coyotegulch.com/jisp/
Source0:        jisp-2.5.1-source.tar.bz2
Patch0:         jisp2-2.5.1-java5-enum.patch
Patch1:         jisp2-2.5.1-javac-flags.patch
Patch2:         jisp2-2.5.1-reproducible-jar-mtime.patch
# jisp-3.0.0 won't work with jakarta-turbine-jcs
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  make
Requires:       javapackages-tools
BuildArch:      noarch

%description
Jisp uses B-Tree and hash indexes for keyed access to variable-length
serialized objects stored in files.

%package demo
Summary:        The Java Indexed Serialization Package
Group:          Development/Libraries/Java

%description demo
Jisp uses B-Tree and hash indexes for keyed access to variable-length
serialized objects stored in files.

%package javadoc
Summary:        The Java Indexed Serialization Package
Group:          Development/Libraries/Java

%description javadoc
Jisp uses B-Tree and hash indexes for keyed access to variable-length
serialized objects stored in files.

%prep
%setup -q -n jisp-%{version}
%patch -P 0 -p1
sed -i -e 's/\r$//g' svfl.txt
%patch -P 1 -b .java-cflags
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
%patch -P 2 -p1
%endif

%build
export CLASSPATH=
%make_build JAVAC_FLAGS=" -target 1.8 -source 1.8"
%make_build jars
%make_build docs

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 jisp.jar \
  %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr docs/* %{buildroot}%{_javadocdir}/%{name}
# demo
install -dm 0755 %{buildroot}%{_datadir}/%{name}/lib
install -pm 0644 jisp-demo.jar %{buildroot}%{_datadir}/%{name}/lib
install -pm 0644 *.java %{buildroot}%{_datadir}/%{name}
install -pm 0644 *.txt %{buildroot}%{_datadir}/%{name}

%files
%doc svfl.txt
%{_javadir}/%{name}.jar

%files demo
%{_datadir}/%{name}

%files javadoc
%{_javadocdir}/%{name}

%changelog
