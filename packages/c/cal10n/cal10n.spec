#
# spec file for package cal10n
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cal10n
Version:        0.7.7
Release:        0
Summary:        Compiler assisted localization library (CAL10N)
License:        MIT
Group:          Development/Libraries/Java
Url:            http://cal10n.qos.ch
Source0:        http://cal10n.qos.ch/dist/cal10n-%{version}.tar.gz
Source1:        build.xml-0.7.7.tar.xz
Patch0:         cal10n-0.7.7-sourcetarget.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  javapackages-tools
BuildRequires:  junit
BuildRequires:  xz
Requires:       java
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

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
%setup -q
tar -xf %{SOURCE1}
%patch0 -p1
find . -name "*.jar" | xargs rm

# bnc#759912
rm -rf docs cal10n-site
cat > README.SUSE <<EOF

The documentation under Creative Commons Attribution-NonCommercial-ShareAlike
2.5 License is not suitable for Linux distributors, so it has been removed.

You may find the online version at
http://cal10n.qos.ch/manual.html

EOF

%build
for dir in cal10n-api
do
  pushd $dir
  export CLASSPATH=$(build-classpath \
                     junit \
                     ):target/classes:target/test-classes
  ant -Dmaven.mode.offline=true package javadoc \
      -Dmaven.test.skip=true \
      -lib %{_datadir}/java
  popd
done

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}/%{name}
install -m 644 cal10n-api/target/cal10n-api-%{version}.jar \
        %{buildroot}%{_javadir}/%{name}/cal10n-api-%{version}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom
install -pm 644 %{name}-api/pom.xml %{buildroot}%{_mavenpomdir}/%{name}-api.pom
%add_maven_depmap %{name}-api.pom %{name}/cal10n-api-%{version}.jar

# javadoc
pushd cal10n-api
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}-%{version}
cp -pr target/site/apidocs*/* %{buildroot}%{_javadocdir}/%{name}-%{version}/
rm -rf target/site/api*
popd
%fdupes -s %{buildroot}%{_javadocdir}/%{name}-%{version}

%files
%defattr(0644,root,root,0755)
%doc README.SUSE
%dir %{_javadir}/%{name}
%{_javadir}/%{name}/%{name}*.jar
%{_mavenpomdir}/*
%if %{defined _maven_repository}
%{_mavendepmapfragdir}/%{name}
%else
%{_datadir}/maven-metadata/%{name}.xml*
%endif

%files javadoc
%defattr(-,root,root,-)
%{_javadocdir}/%{name}-%{version}

%changelog
