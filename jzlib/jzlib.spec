#
# spec file for package jzlib
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


Name:           jzlib
Version:        1.1.3
Release:        0
Summary:        Re-implementation of zlib in pure Java
License:        BSD-3-Clause
Group:          Development/Libraries/Java
Url:            http://www.jcraft.com/jzlib/
Source0:        https://github.com/ymnk/jzlib/archive/%{version}.tar.gz
Source1:        %{name}_build.xml
BuildRequires:  ant >= 1.6
BuildRequires:  java-devel
BuildRequires:  javapackages-local
Obsoletes:      %{name}-javadoc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The zlib is designed to be a free, general-purpose, legally
unencumbered -- that is, not covered by any patents -- lossless
data-compression library for use on virtually any computer hardware and
operating system. The zlib was written by Jean-loup Gailly
(compression) and Mark Adler (decompression).

%package        demo
Summary:        Re-implementation of zlib in pure Java
Group:          Development/Libraries/Java

%description    demo
Demo files for %{summary}.

%prep
%setup -q
cp %{SOURCE1} build.xml

# bnc#500524
# be sure that we don't distribute GPL derived code marked as BSD
rm misc/mindtermsrc-v121-compression.patch

%build
ant \
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
    dist

%install
# jar
install -Dpm 644 dist/lib/%{name}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

# pom
install -Dpm 644 pom.xml \
  %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

# examples
install -dm 755 %{buildroot}%{_datadir}/%{name}-%{version}
cp -pr example/* %{buildroot}%{_datadir}/%{name}-%{version}

%files
%defattr(0644,root,root,0755)
%{_javadir}/%{name}.jar
%{_mavenpomdir}/%{name}.pom
%{_datadir}/maven-metadata/%{name}.xml
%doc LICENSE.txt

%files demo
%defattr(0644,root,root,0755)
%doc %{_datadir}/%{name}-%{version}

%changelog
