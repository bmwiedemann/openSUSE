#
# spec file for package plexus-cli
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


Name:           plexus-cli
Version:        1.7
Release:        0
Summary:        Command Line Interface facilitator for Plexus
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/plexus-cli
Source0:        %{name}-%{version}.tar.xz
Source1:        LICENSE-2.0.txt
Source100:      %{name}-build.xml
Patch0:         0001-Do-not-use-commons-cli-deprecated-classes.patch
Patch1:         0002-No-unchecked-operations.patch
BuildRequires:  ant
BuildRequires:  apache-commons-cli
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  plexus-classworlds
BuildRequires:  plexus-utils
BuildRequires:  sisu-plexus
BuildRequires:  xz
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
%patch -P 0 -p1
%patch -P 1 -p1
cp -p %{SOURCE1} .
cp -p %{SOURCE100} build.xml

mkdir -p lib
build-jar-repository -s lib commons-cli plexus/utils plexus/classworlds org.eclipse.sisu.plexus

%build
ant \
  jar javadoc

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/plexus
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/plexus/cli.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/plexus
%{mvn_install_pom} pom.xml %{buildroot}%{_mavenpomdir}/plexus/cli.pom
%add_maven_depmap plexus/cli.pom plexus/cli.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE-2.0.txt

%files javadoc
%license LICENSE-2.0.txt
%{_javadocdir}/%{name}

%changelog
