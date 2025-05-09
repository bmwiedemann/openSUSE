#
# spec file for package jlatexmath
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


Name:           jlatexmath
Version:        1.0.3
Release:        0
Summary:        Java API to display mathematical formulas written in LaTeX
License:        GPL-2.0-or-later
Group:          Development/Libraries/Java
URL:            https://github.com/opencollab/jlatexmath/
Source0:        https://github.com/opencollab/%{name}/archive/refs/tags/%{version}.tar.gz
Source1:        patched_fop.properties
Patch0:         jlatexmath-1.0.3-nosource.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-tools
BuildRequires:  xmlgraphics-fop
Requires:       java >= 1.8
Requires:       javapackages-tools
BuildArch:      noarch

%description
The goal of this Java API is to display mathematical formulas written in LaTeX.
The default encoding is UTF-8 and most of LaTeX commands are available.

JLaTeXMath is a fork of the excellent project JMathTeX.

%package fop
Summary:        FOP plug-in for %{name}
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}-%{release}
Requires:       javapackages-tools
Requires:       xmlgraphics-fop

%description fop
This package contains the FOP plug-in for %{name}.

%package javadoc
Summary:        API Documentation for %{name}
Group:          Documentation/HTML
Requires:       %{name} = %{version}-%{release}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch -P 0 -p1

rm fop.properties
cp -a %{SOURCE1} fop.properties

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# Fix class-path-in-manifest error
sed -i '/class-path/I d' plugin/fop/MANIFEST.MF

%build
ant -Djava_version=1.8 buildJar fop doc

%install

mkdir -p %{buildroot}%{_javadir}
cp -p dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
cp -p dist/%{name}-fop-%{version}.jar %{buildroot}%{_javadir}/%{name}-fop.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp doc/ %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/%{name}.jar
%doc README
%license COPYING
%license LICENSE

%files fop
%{_javadir}/%{name}-fop.jar
%license plugin/fop/COPYING
%license plugin/fop/LICENSE

%files javadoc
%{_javadocdir}/%{name}

%changelog
