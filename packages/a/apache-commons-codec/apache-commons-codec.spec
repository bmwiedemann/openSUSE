#
# spec file for package apache-commons-codec
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2000-2010, JPackage Project
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


%define base_name  codec
%define short_name commons-%{base_name}
%bcond_with tests
Name:           apache-commons-codec
Version:        1.14
Release:        0
Summary:        Apache Commons Codec Package
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            http://commons.apache.org/codec/
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        %{name}-build.xml
# Data in DoubleMetaphoneTest.java originally has an inadmissible license.
# The author gives MIT in e-mail communication.
Source100:      aspell-mail.txt
# PATCH-FIX-OPENSUSE Avoid spurious timeout in BeiderMorse tests
Patch0:         timeout.patch
BuildRequires:  ant
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
Requires:       java >= 1.8
Provides:       jakarta-%{short_name} = %{version}
Obsoletes:      jakarta-%{short_name} < %{version}
Provides:       %{short_name} = %{version}
Obsoletes:      %{short_name} < %{version}
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit >= 1.7
BuildRequires:  apache-commons-lang3
BuildRequires:  hamcrest-core
BuildRequires:  junit
BuildRequires:  mozilla-nss
%endif

%description
Commons Codec is an attempt to provide definitive implementations of
commonly used encoders and decoders.

%package        javadoc
Summary:        Javadoc for %{name}
Group:          Documentation/HTML
Provides:       jakarta-%{short_name}-javadoc = %{version}
Obsoletes:      jakarta-%{short_name}-javadoc < %{version}
Provides:       %{short_name}-javadoc = %{version}
Obsoletes:      %{short_name}-javadoc < %{version}

%description    javadoc
Javadoc for %{name}.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE1} build.xml
cp %{SOURCE100} aspell-mail.txt
%patch0 -p1

#fixes eof encoding
dos2unix RELEASE-NOTES*.txt LICENSE.txt NOTICE.txt

%pom_remove_parent .

%build
mkdir -p lib
%if %{with tests}
build-jar-repository -s lib junit4 hamcrest/core commons-lang3
%endif
ant \
%if %{without tests}
  -Dtest.skip=true \
%endif
  -Dcompiler.source=1.8 -Dcompiler.target=1.8 \
  jar javadoc

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{short_name}.jar
ln -sf %{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
# poms
# Install pom file
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar -a "%{short_name}:%{short_name}"
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes -s %{buildroot}%{_javadocdir}

%pre javadoc
if [ -L %{_javadocdir}/%{name} ]; then
  rm -f %{_javadocdir}/%{name};
fi

%files -f .mfiles
%license LICENSE.txt
%doc RELEASE-NOTES.txt
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%changelog
