#
# spec file for package cal10n
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_with tests
Name:           cal10n
Version:        0.8.1.10
Release:        0
Summary:        Compiler assisted localization library (CAL10N)
License:        MIT
Group:          Development/Libraries/Java
URL:            http://cal10n.qos.ch
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-build.tar.xz
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  xz
Requires:       java
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-antunit
BuildRequires:  ant-junit
%endif

%description
Compiler Assisted Localization, abbreviated as CAL10N (pronounced as "calion")
is a java library for writing localized (internationalized) messages.
Features:
    * java compiler verifies message keys used in source code
    * tooling to detect errors in message keys
    * native2ascii tool made superfluous, as you can directly encode bundles
      in the most convenient charset, per locale.
    * good performance (300 nanoseconds per key look-up)
    * automatic reloading of resource bundles upon change

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
API documentation for %{name}.

%prep
%setup -q -a1
find . -name "*.jar" -exec rm -f {} \;

# We don't want to depend on ant, since it will be
# present when we try to use the task
%pom_change_dep :ant :::provided %{name}-ant-task

# bnc#759912
rm -rf docs cal10n-site
cat > README.SUSE <<EOF

The documentation under Creative Commons Attribution-NonCommercial-ShareAlike
2.5 License is not suitable for Linux distributors, so it has been removed.

You may find the online version at
http://cal10n.qos.ch/manual.html

EOF

%build
mkdir -p lib
build-jar-repository -s lib \
%if %{with tests}
    ant-antunit \
%endif
    ant/ant
%{ant} \
%if %{without tests}
    -Dtest.skip=true \
%endif
    package javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -m 644 %{name}-api/target/%{name}-api-*.jar \
        %{buildroot}%{_javadir}/%{name}/%{name}-api.jar
install -m 644 %{name}-ant-task/target/%{name}-ant-task-*.jar \
        %{buildroot}%{_javadir}/%{name}/%{name}-ant-task.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom
install -pm 644 %{name}-api/pom.xml %{buildroot}%{_mavenpomdir}/%{name}-api.pom
%add_maven_depmap %{name}-api.pom %{name}/%{name}-api.jar
install -pm 644 %{name}-ant-task/pom.xml %{buildroot}%{_mavenpomdir}/%{name}-ant-task.pom
%add_maven_depmap %{name}-ant-task.pom %{name}/%{name}-ant-task.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
for i in api ant-task; do
  install -dm 0755 %{buildroot}%{_javadocdir}/%{name}/${i}
  cp -pr %{name}-${i}/target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/${i}/
done
%fdupes -s %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc README.SUSE

%files javadoc
%{_javadocdir}/%{name}

%changelog
