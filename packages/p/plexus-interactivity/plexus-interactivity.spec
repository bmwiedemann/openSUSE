#
# spec file for package plexus-interactivity
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


Name:           plexus-interactivity
Version:        1.3
Release:        0
Summary:        Plexus Interactivity Handler Component
License:        MIT
Group:          Development/Libraries/Java
URL:            https://github.com/codehaus-plexus/plexus-interactivity
Source0:        %{name}-%{version}.tar.xz
Source1:        LICENSE.MIT
Source100:      %{name}-build.tar.xz
Patch0:         %{name}-jline2.patch
BuildRequires:  ant
BuildRequires:  atinject
BuildRequires:  fdupes
BuildRequires:  javapackages-local >= 6
BuildRequires:  jline >= 2
BuildRequires:  plexus-utils
BuildRequires:  sisu-inject
BuildArch:      noarch

%description
Plexus contains end-to-end developer tools for writing applications.
At the core is the container, which can be embedded or for an
application server. There are many reusable components for hibernate,
form processing, jndi, i18n, velocity, etc. Plexus also includes an
application server which is like a J2EE application server.

%package javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description javadoc
This package provides %{summary}.

%package api
Summary:        API for %{name}
Group:          Development/Libraries/Java
Obsoletes:      %{name}-jline

%description api
API module for %{name}.

%prep
%setup -q -a100

%patch -P 0 -p1
%pom_change_dep :jline-reader jline:jline:2.10 %{name}-api

cp %{SOURCE1} .

%build
mkdir -p lib
build-jar-repository -s lib atinject jline org.eclipse.sisu.inject plexus/utils
%{ant} package javadoc

%install

# jar
install -dm 0755 %{buildroot}%{_javadir}/plexus
install -pm 0644 %{name}-api/target/%{name}-api-%{version}.jar %{buildroot}%{_javadir}/plexus/interactivity-api.jar

# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/plexus
%{mvn_install_pom} %{name}-api/pom.xml %{buildroot}%{_mavenpomdir}/plexus/interactivity-api.pom
%add_maven_depmap plexus/interactivity-api.pom plexus/interactivity-api.jar -f api

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/api
cp -pr %{name}-api/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/api/

%fdupes -s %{buildroot}%{_javadocdir}

%files api -f .mfiles-api
%license LICENSE.MIT

%files javadoc
%license LICENSE.MIT
%{_javadocdir}/%{name}

%changelog
