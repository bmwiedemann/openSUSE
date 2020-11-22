#
# spec file for package beansbinding
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


Name:           beansbinding
Version:        1.2.1
Release:        0
Summary:        Beans Binding (JSR 295) reference implementation
License:        LGPL-2.0-or-later
Group:          Development/Libraries/Java
Url:            https://beansbinding.dev.java.net/
Source0:        https://beansbinding.dev.java.net/files/documents/6779/73673/beansbinding-%{version}-src.tar.bz2
Patch0:         beansbinding-1.2.1-sourcetarget.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
Requires:       java >= 1.8
BuildArch:      noarch

%description
In essence, Beans Binding (JSR 295) is about keeping two properties
(typically of two objects) in sync. An additional emphasis is placed on
the ability to bind to Swing components, and easy integration with IDEs
such as NetBeans. This project provides the reference implementation.

%package javadoc
Summary:        Beans Binding (JSR 295) reference implementation
Group:          Development/Libraries/Java

%description javadoc
In essence, Beans Binding (JSR 295) is about keeping two properties
(typically of two objects) in sync. An additional emphasis is placed on
the ability to bind to Swing components, and easy integration with IDEs
such as NetBeans. This project provides the reference implementation.

%prep
%setup -q -c
%patch0 -p1
# remove all binary libs
find . -type f \( -iname "*.jar" -o -iname "*.zip" \) -print0 | xargs -t -0 rm -f

%build
ant dist

%install
# jar
install -d -m 755 %{buildroot}%{_javadir}
install -m 644 dist/%{name}.jar %{buildroot}%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/*
%doc license.txt releaseNotes.txt

%files javadoc
%dir %{_javadocdir}/%{name}
%{_javadocdir}/%{name}/*

%changelog
