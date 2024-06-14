#
# spec file for package plexus-cipher
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


Name:           plexus-cipher
Version:        2.1.0
Release:        0
Summary:        Plexus Cipher: encryption/decryption Component
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/%{name}
Source0:        https://github.com/codehaus-plexus/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildRequires:  sisu-inject
BuildArch:      noarch

%description
Plexus Cipher: encryption/decryption Component

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE1} build.xml

# replace %{version}-SNAPSHOT with %{version}
%pom_xpath_set pom:project/pom:version %{version}

%build
mkdir -p lib
build-jar-repository -s lib atinject org.eclipse.sisu.inject

%{ant} compile
%{ant} jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/plexus
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/plexus/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/plexus
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/plexus/%{name}.pom
%add_maven_depmap plexus/%{name}.pom plexus/%{name}.jar -a org.sonatype.plexus:%{name}
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE.txt NOTICE.txt

%changelog
