#
# spec file for package appframework
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


Name:           appframework
Version:        1.03
Release:        0
Summary:        Swing Application Framework
License:        LGPL-2.0-or-later
Group:          Development/Libraries/Java
Url:            https://appframework.dev.java.net/
Source0:        https://appframework.dev.java.net/downloads/AppFramework-%{version}-src.tar.bz2
Patch0:         %{name}-%{version}-no-local-storage.diff
Patch1:         %{name}-%{version}-openjdk.diff
Patch2:         %{name}-sourcetarget.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  swing-layout >= 1.0.3
Requires:       java >= 1.8
Requires:       swing-layout >= 1.0.3
BuildArch:      noarch

%description
The JSR-296 Swing Application Framework prototype implementation is a
small set of Java classes that simplify building desktop applications.

%package javadoc
Summary:        Swing Application Framework
Group:          Development/Libraries/Java

%description javadoc
The JSR-296 Swing Application Framework prototype implementation is a
small set of Java classes that simplify building desktop applications.

%prep
%setup -q -n AppFramework-%{version}
# remove all binary libs
find . -name "*.jar" -exec rm -f {} \;
%patch0 -b .sav
%patch1 -p1 -b .sav
%patch2 -p1 -b .sav

%build
ant -Dlibs.swing-layout.classpath=%{_javadir}/swing-layout.jar dist

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/AppFramework-1.03.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/*
%doc COPYING README

%files javadoc
%dir %{_javadocdir}/%{name}
%{_javadocdir}/%{name}/*

%changelog
