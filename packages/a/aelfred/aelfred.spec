#
# spec file for package aelfred
#
# Copyright (c) 2024 SUSE LLC
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


Name:           aelfred
Version:        7.0
Release:        0
Summary:        Java-based XML parser
License:        BSD-3-Clause
Group:          Development/Libraries/Java
URL:            https://saxon.sourceforge.net/aelfred.html
Source0:        http://downloads.sourceforge.net/project/saxon/aelfred/7.0/aelfred7_0.zip
Patch0:         aelfred-icedtea-build.patch
Patch1:         aelfred-javadoc.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  unzip
BuildArch:      noarch

%description
AElfred is a Java-based XML parser from Microstar Software Ltd. AElfred
is distributed for free (with full source) for both commercial and
non-commercial use.

%package javadoc
Summary:        Java-based XML parser (documentation)
Group:          Development/Libraries/Java

%description javadoc
Javadoc for aelfred.

%package demo
Summary:        Java-based XML parser (demo and samples)
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}

%description demo
Demonstrations and samples for aelfred.

%prep
%setup -q -c
rm *.jar
unzip %{name}-source.zip
%patch -P 0
%patch -P 1 -p1

%build
mkdir -p classes
javac -source 8 -target 8 -d classes `find net -name \*.java`
javadoc -notimestamp -source 8 -d HTML `find net -name \*.java`
jar \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 17}%{!?pkg_vcmp:0}
    --date="$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ)" \
%endif
    --create --file=%{name}.jar -C classes .

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 %{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -a HTML/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
