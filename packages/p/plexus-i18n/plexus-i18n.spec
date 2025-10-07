#
# spec file for package plexus-i18n
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%global parent plexus
%global subname i18n
Name:           %{parent}-%{subname}
Version:        1.0.0
Release:        0
Summary:        Plexus I18N Component
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/plexus-i18n
Source0:        https://repo1.maven.org/maven2/org/codehaus/%{parent}/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  objectweb-asm
BuildRequires:  sisu-inject
BuildRequires:  slf4j
BuildRequires:  unzip
BuildArch:      noarch

%description
Plexus contains end-to-end developer tools for writing applications.
At the core is the container, which can be embedded or for an
application server. There are many reusable components for hibernate,
form processing, jndi, i18n, velocity, etc. Plexus also includes an
application server which is like a J2EE application server.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
cp %{SOURCE1} build.xml

%build
mkdir -p lib
build-jar-repository -s lib \
    atinject \
    objectweb-asm/asm \
    org.eclipse.sisu.inject \
    slf4j/api

%{ant} \
  jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles

%files javadoc
%{_javadocdir}/%{name}

%changelog
