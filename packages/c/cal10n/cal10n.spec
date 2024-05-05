#
# spec file for package cal10n
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "plugins"
%bcond_without plugins
%else
%bcond_with plugins
%endif
%global base_name cal10n
Version:        0.8.1.12
Release:        0
License:        MIT
Group:          Development/Libraries/Java
URL:            https://cal10n.qos.ch
Source0:        %{base_name}-%{version}.tar.xz
Source1:        %{base_name}-build.tar.xz
# https://github.com/qos-ch/cal10n/pull/10
Patch0:         Fix-SupportedSourceVersion-warning.patch
BuildRequires:  fdupes
BuildRequires:  xz
BuildArch:      noarch
%if %{with plugins}
Name:           %{base_name}-maven-plugins
Summary:        Compiler assisted localization library (CAL10N) maven plugins
BuildRequires:  maven-local
BuildRequires:  mvn(ch.qos.cal10n:cal10n-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven.wagon:wagon-ssh)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
%else
Name:           %{base_name}
Summary:        Compiler assisted localization library (CAL10N)
BuildRequires:  ant
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
%endif

%description
%if %{with plugins}
Compiler Assisted Localization, abbreviated as CAL10N (pronounced as "calion")
is a java library for writing localized (internationalized) messages.

This package contains maven plugins
%else
Compiler Assisted Localization, abbreviated as CAL10N (pronounced as "calion")
is a java library for writing localized (internationalized) messages.
Features:
    * java compiler verifies message keys used in source code
    * tooling to detect errors in message keys
    * native2ascii tool made superfluous, as you can directly encode bundles
      in the most convenient charset, per locale.
    * good performance (300 nanoseconds per key look-up)
    * automatic reloading of resource bundles upon change
%endif

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{base_name}-%{version} -a1
%patch -P 0 -p1

# We don't want to depend on ant, since it will be
# present when we try to use the task
%pom_change_dep :ant :::provided %{base_name}-ant-task

%pom_disable_module cal10n-site
%pom_disable_module cal10n-api
%pom_disable_module cal10n-ant-task

%pom_change_dep -r :maven-artifact-manager :maven-core

%pom_remove_plugin -r :maven-source-plugin

# bnc#759912
cat > README.SUSE <<EOF

The documentation under Creative Commons Attribution-NonCommercial-ShareAlike
2.5 License is not suitable for Linux distributors, so it has been removed.

You may find the online version at
http://cal10n.qos.ch/manual.html

EOF

%build
%if %{with plugins}
%{mvn_file} :{*} %{name}/@1

%{mvn_package} :%{base_name}-parent __noinstall

%{mvn_build} -f -- \
	-Dproject.build.outputTimestamp=$(date -u -d @${SOURCE_DATE_EPOCH:-$(date +%%s)} +%%Y-%%m-%%dT%%H:%%M:%%SZ) \
    -Dsource=8 -Dproject.build.sourceEncoding=ISO-8859-1
%else
mkdir -p lib
build-jar-repository -s lib ant/ant
%{ant} package javadoc
%endif

%install
%if %{with plugins}
%mvn_install
%else
install -d -m 0755 %{buildroot}%{_javadir}/%{base_name}
install -d -m 0755 %{buildroot}%{_mavenpomdir}/%{base_name}
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
for i in api ant-task; do
  # jar
  install -m 644 %{base_name}-${i}/target/%{base_name}-${i}-*.jar \
    %{buildroot}%{_javadir}/%{base_name}/%{base_name}-${i}.jar
  # pom
  %{mvn_install_pom} %{base_name}-${i}/pom.xml %{buildroot}%{_mavenpomdir}/%{base_name}/%{base_name}-${i}.pom
  %add_maven_depmap %{base_name}/%{base_name}-${i}.pom %{base_name}/%{base_name}-${i}.jar
  # javadoc
  install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/${i}
  cp -pr %{name}-${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/${i}/
done

%endif
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%if %{with plugins}
%files javadoc -f .mfiles-javadoc
%else
%doc README.SUSE

%files javadoc
%{_javadocdir}/%{name}
%endif

%changelog
