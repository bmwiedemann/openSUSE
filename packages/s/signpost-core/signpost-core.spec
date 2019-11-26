#
# spec file for package signpost-core
#
# Copyright (c) 2019 SUSE LLC
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


%global githash 3017160f847564879520c564b4bb04abb7b680fe
Name:           signpost-core
Version:        1.2.1.2
Release:        0
Summary:        A simple, light-weight, and modular OAuth client library for the Java platform
License:        Apache-2.0
URL:            https://github.com/mttkay/signpost
Source0:        https://github.com/mttkay/signpost/archive/%{githash}/signpost-%{githash}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
BuildRequires:  fdupes
BuildRequires:  maven-local
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.httpcomponents:httpcore)
BuildArch:      noarch

%description
Signpost is the easy and intuitive solution for signing HTTP messages on the
Java platform in conformance with the OAuth Core 1.0a standard.
Signpost follows a modular and flexible design, allowing you to combine it with
different HTTP messaging layers

%package -n oauth-signpost
Summary:        Parent POM for %{name}

%description -n oauth-signpost
This package contains the Parent POM for %{name}.

%package -n signpost-commonshttp4
Summary:        Signpost Apache HttpClient Supports

%description -n signpost-commonshttp4
Signpost Apache HttpClient Supports.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n signpost-%{githash}

# Remove pre-built JAR and class files
find -name '*.jar' -delete
find -name '*.class' -delete

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

# Unneeded modules
%pom_disable_module signpost-jetty6

# Resolve javadoc doclint problems
%pom_remove_plugin :maven-javadoc-plugin
# Unneeded task
%pom_remove_plugin -r :maven-antrun-plugin
%pom_remove_plugin -r :maven-release-plugin

%{mvn_file} :%{name} %{name}
%{mvn_file} :signpost-commonshttp4 signpost-commonshttp4

%build
%{mvn_build} -s -f \
%if %{?pkg_vcmp:%pkg_vcmp java-devel >= 9}%{!?pkg_vcmp:0}
	-- -Dmaven.compiler.release=6
%endif

%install
%mvn_install
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles-%{name}
%doc README.markdown
%license LICENSE

%files -n oauth-signpost -f .mfiles-oauth-signpost
%license LICENSE

%files -n signpost-commonshttp4 -f .mfiles-signpost-commonshttp4

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
