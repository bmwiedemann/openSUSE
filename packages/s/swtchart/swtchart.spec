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
BuildRequires:  eclipse-swt
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  tycho
#!BuildIgnore:  libjawt.so(SUNWprivate_1.1)
#!BuildIgnore:  libjawt.so(SUNWprivate_1.1)(64bit)
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
# Create the poms
xmvn -o org.eclipse.tycho:tycho-pomgenerator-plugin:generate-poms -DgroupId=org.swtchart
%{mvn_package} "::pom::" __noinstall
%{mvn_package} :org.swtchart.example* __noinstall

%{mvn_file} :{*} @1 %{name}/@1

%build
%{mvn_build} -f -- \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-Dmaven.compiler.release=6
%else
	-Dsource=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

install -dm 0755 -p %{buildroot}%{_javadir}
install -pm 0644 org.swtchart/target/org.swtchart*.jar %{buildroot}%{_javadir}/org.swtchart.jar
%fdupes -s %{buildroot}%{_datadir}

%files -f .mfiles
%{_javadir}

%files javadoc -f .mfiles-javadoc

%changelog
