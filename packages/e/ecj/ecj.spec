#
# spec file for package ecj
#
# Copyright (c) 2023 SUSE LLC
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


%global eclipse_ver 4.23
%global bundle_ver 3.29.0
%global jar_ver %{eclipse_ver}
%global drop R-%{jar_ver}-202203080310
Name:           ecj
Version:        %{eclipse_ver}
Release:        0
Summary:        Eclipse Compiler for Java
License:        EPL-2.0 AND GPL-2.0-only WITH Classpath-exception-2.0
Group:          Development/Libraries/Java
URL:            https://www.eclipse.org
Source0:        https://download.eclipse.org/eclipse/downloads/drops4/%{drop}/ecjsrc-%{jar_ver}.jar
Source1:        https://repo1.maven.org/maven2/org/eclipse/jdt/ecj/%{bundle_ver}/ecj-%{bundle_ver}.pom
# Extracted from https://download.eclipse.org/eclipse/downloads/drops4/%%{drop}/ecj-%%{jar_ver}.jar
Source2:        MANIFEST.MF
Patch0:         ecj-rpmdebuginfo.patch
BuildRequires:  ant
BuildRequires:  java-devel >= 11
BuildRequires:  javapackages-local >= 6
BuildRequires:  unzip
BuildArch:      noarch

%description
ECJ is the Java bytecode compiler of the Eclipse Platform.  It is also known as
the JDT Core batch compiler.

%prep
%setup -q -c
%patch0 -p1

# Specify encoding
sed -i -e '/compilerarg/s/Xlint:none/Xlint:none -encoding cp1252/' build.xml

mkdir -p scripts/binary/META-INF/
cp %{SOURCE2} scripts/binary/META-INF/MANIFEST.MF

%build
%{ant}

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 ecj.jar %{buildroot}%{_javadir}/%{name}/ecj.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}/ecj.pom
%add_maven_depmap %{name}/ecj.pom %{name}/ecj.jar -a "org.eclipse.jdt:core,org.eclipse.jdt.core.compiler:ecj,org.eclipse.tycho:org.eclipse.jdt.core,org.eclipse.tycho:org.eclipse.jdt.compiler.apt"

# Install the ecj wrapper script
%jpackage_script org.eclipse.jdt.internal.compiler.batch.Main '' '' ecj ecj true

# Install manpage
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 -p ecj.1 %{buildroot}%{_mandir}/man1/ecj.1

%files -f .mfiles
%license about.html
%{_bindir}/ecj
%{_mandir}/man1/ecj*

%changelog
