#
# spec file for package apache-commons-validator
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


%define short_name commons-validator
Name:           apache-%{short_name}
Version:        1.5.0
Release:        0
Summary:        Apache Commons Validator
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/proper/commons-validator/
Source0:        https://archive.apache.org/dist/commons/validator/source/%{short_name}-%{version}-src.tar.gz
Patch0:         commons-validator-1.5.0-srcencoding.patch
Patch1:         commons-validator-1.5.0-locale.patch
BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  commons-beanutils
BuildRequires:  commons-collections
BuildRequires:  commons-digester >= 1.8
BuildRequires:  commons-logging
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  junit
BuildRequires:  oro
Requires:       commons-beanutils >= 1.5
Requires:       commons-collections
Requires:       commons-digester >= 1.8
Requires:       commons-logging >= 1.0.2
Requires:       oro >= 2.0.6
Provides:       %{short_name} = %{version}-%{release}
Obsoletes:      %{short_name} < %{version}-%{release}
Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{version}-%{release}
BuildArch:      noarch

%description
A common issue when receiving data either electronically or from user
input is verifying the integrity of the data. This work is repetitive
and becomes even more complicated when different sets of validation
rules need to be applied to the same set of data based, for example, on
locale. Error messages may also vary by locale. This package attempts
to address some of these issues and speed development and maintenance
of validation rules.

%package javadoc
Summary:        Javadoc for jakarta-commons-validator
Group:          Documentation/HTML
Requires(pre):  coreutils

%description javadoc
A common issue when receiving data either electronically or from user
input is verifying the integrity of the data. This work is repetitive
and becomes even more complicated when different sets of validation
rules need to be applied to the same set of data based on locale for
example. Error messages may also vary by locale. This package attempts
to address some of these issues and speed development and maintenance
of validation rules.

This package contains the javadoc documentation for the Jakarta Commons
Validator Package.

%prep
%autosetup -p1 -n %{short_name}-%{version}-src

sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' RELEASE-NOTES.txt
sed -i 's/\r//' NOTICE.txt

%pom_remove_parent .

%build
export CLASSPATH=$(build-classpath \
                   commons-collections \
                   commons-logging \
                   commons-digester \
                   commons-beanutils \
                   junit \
                   hamcrest \
                   oro )
ant \
    -Dcompile.source=8 -Dcompile.target=8 \
    -Dskip.download=true -Dbuild.sysclasspath=first \
    dist

%check
export CLASSPATH=$(build-classpath \
                   commons-collections \
                   commons-logging \
                   commons-digester \
                   commons-beanutils \
                   junit \
                   hamcrest \
                   oro )
ant \
    -Dcompile.source=8 -Dcompile.target=8 \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Dskip.download=true -Dbuild.sysclasspath=first \
    test

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -pm 644 dist/%{short_name}-%{version}-SNAPSHOT.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar
# pom
install -d -m 0755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar -a org.apache.commons:%{short_name}
# javadoc
install -d -m 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr dist/docs/api*/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}/%{name}/

%files -f .mfiles
%license LICENSE.txt
%doc NOTICE.txt RELEASE-NOTES.txt
%{_javadir}/%{short_name}.jar

%files javadoc
%license LICENSE.txt
%doc %{_javadocdir}/%{name}

%changelog
