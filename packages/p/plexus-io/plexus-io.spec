#
# spec file for package plexus-io
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


Name:           plexus-io
Version:        3.4.2
Release:        0
Summary:        Plexus IO Components
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/%{name}
Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        %{name}-build.xml
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  ant
BuildRequires:  apache-commons-io
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  jsr-305
BuildRequires:  plexus-utils >= 3.3.0
BuildRequires:  sisu-inject
BuildArch:      noarch

%description
Plexus IO is a set of plexus components, which are designed for use
in I/O operations.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE1} build.xml
cp %{SOURCE2} .

%build
mkdir -p lib
build-jar-repository -s lib atinject org.eclipse.sisu.inject plexus/utils commons-io jsr-305

%{ant} \
  jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/plexus
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/plexus/io.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/plexus
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/plexus/io.pom
%add_maven_depmap plexus/io.pom plexus/io.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license NOTICE.txt LICENSE-2.0.txt

%files javadoc
%license NOTICE.txt LICENSE-2.0.txt
%{_javadocdir}/%{name}

%changelog
