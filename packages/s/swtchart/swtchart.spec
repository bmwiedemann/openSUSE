#
# spec file for package swtchart
#
# Copyright (c) 2020 SUSE LLC
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


Name:           swtchart
Version:        0.10.0
Release:        0
Summary:        Chart component based on SWT
License:        EPL-1.0
Group:          Development/Languages/Java
URL:            http://www.swtchart.org/
Source:         %{name}-%{version}.tar.xz
Source1:        build.xml
BuildRequires:  ant
BuildRequires:  eclipse-swt
BuildRequires:  fdupes
BuildRequires:  java-devel
BuildRequires:  javapackages-local
BuildRequires:  sed
BuildRequires:  unzip
BuildArch:      noarch

%description
SWTChart is a chart component which has following basic functionalities.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
Developer documentation of SWT Chart.

%prep
%setup -q

%build
sed "s#SWTJAR#$(build-classpath swt)#g" <%{SOURCE1} >build.xml
sed -i -e '/Classpath/d' org.swtchart/META-INF/MANIFEST.MF
%{ant} -Dant.build.javac.source=1.6 -Dant.build.javac.target=1.6

%install
mkdir -p %{buildroot}%{_javadir}
install org.swtchart.jar %{buildroot}%{_javadir}

%add_maven_depmap org.swtchart:org.swtchart:%{version} org.swtchart.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -r api/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{name}

%changelog
