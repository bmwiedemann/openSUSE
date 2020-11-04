#
# spec file for package jakarta-commons-discovery
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define short_name commons-discovery
Name:           jakarta-commons-discovery
Version:        0.4
Release:        0
Summary:        Jakarta Commons Discovery
License:        Apache-2.0
Group:          Development/Libraries/Java
Url:            http://jakarta.apache.org/commons/discovery.html
Source0:        http://www.apache.org/dist/jakarta/commons/discovery/source/commons-discovery-0.4-src.tar.gz
BuildRequires:  ant
BuildRequires:  commons-logging >= 1.0.4
BuildRequires:  java-devel
BuildRequires:  javapackages-tools
BuildRequires:  junit >= 3.7
Requires:       commons-logging >= 1.0.4
Provides:       %{short_name} = %{version}
Obsoletes:      %{short_name} < %{version}
#XXX: temporary fix to make axis auto dependencies work, need to revork package
Provides:       osgi(org.apache.commons.discovery)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Discovery component is about discovering, or finding,
implementations for pluggable interfaces.  Pluggable interfaces are
specified with the intent that multiple implementations are, or will
be, available to provide the service described by the interface.
Discovery provides facilities for finding and instantiating classes and
for lifecycle management of singleton (factory) classes.

%package javadoc
Summary:        Javadoc for jakarta-commons-discovery
Group:          Development/Libraries/Java
Requires(pre):  coreutils

%description javadoc
The Discovery component is about discovering, or finding,
implementations for pluggable interfaces.  Pluggable interfaces are
specified with the intent that multiple implementations are, or will
be, available to provide the service described by the interface.
Discovery provides facilities for finding and instantiating classes,
and for lifecycle management of singleton (factory) classes.

This package contains the javadoc documentation for the Jakarta Commons
Discovery Package.

%prep
%setup -q -n commons-discovery-%{version}-src
chmod u+w .

%build
ant \
  -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
  -Djunit.jar=%(find-jar junit) \
  -Dlogger.jar=%(find-jar commons-logging) \
  test.discovery dist

%install
# jar
mkdir -p %{buildroot}%{_javadir}
cp -p dist/%{short_name}.jar %{buildroot}%{_javadir}/%{short_name}.jar
(cd %{buildroot}%{_javadir} && ln -s %{short_name}.jar %{name}.jar)
# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/api/* %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc LICENSE.txt
%{_javadir}/*

%files javadoc
%defattr(0644,root,root,0755)
%doc %{_javadocdir}/%{name}

%changelog
