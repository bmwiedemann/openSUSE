#
# spec file for package flute
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


Name:           flute
Version:        1.3.0
Release:        0
Summary:        Java CSS parser using SAC
# The entire source code is W3C except ParseException.java which is LGPLv2+
License:        W3C and LGPL-2.1+
Group:          Development/Libraries/Java
Url:            http://www.w3.org/Style/CSS/SAC/
Source0:        http://downloads.sourceforge.net/jfreereport/%{name}-%{version}-OOo31.zip
BuildRequires:  ant
BuildRequires:  java-devel
BuildRequires:  jpackage-utils
BuildRequires:  sac
BuildRequires:  unzip
Requires:       java
Requires:       jpackage-utils
Requires:       sac
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A Cascading Style Sheets parser using the Simple API for CSS, for Java.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -c
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib sac

%build
ant \
    -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6 \
    jar javadoc

%install

mkdir -p %{buildroot}%{_javadir}
cp -p build/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp build/api %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc COPYRIGHT.html
%{_javadir}/*.jar

%files javadoc
%defattr(0644,root,root,0755)
%doc COPYRIGHT.html
%{_javadocdir}/%{name}

%changelog
