#
# spec file for package apache-commons-io
#
# Copyright (c) 2020 SUSE LLC
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


%define base_name       io
%define short_name      commons-%{base_name}
%bcond_with tests
Name:           apache-%{short_name}
Version:        2.7
Release:        0
Summary:        Utilities to assist with developing IO functionality
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://commons.apache.org/%{base_name}
Source0:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
Source1:        https://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz.asc
Source2:        %{name}-build.xml
BuildRequires:  ant >= 1.6
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
Provides:       %{short_name} = %{version}-%{release}
Provides:       jakarta-%{short_name} = %{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{version}-%{release}
BuildArch:      noarch
%if %{with tests}
BuildRequires:  ant-junit
%endif

%description
Commons-IO contains utility classes, stream implementations,
file filters, and endian classes. It is a library of utilities
to assist with developing IO functionality.

%package        javadoc
Summary:        API documentation for %{name}
Group:          Documentation/HTML

%description    javadoc
This package provides %{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
cp %{SOURCE2} build.xml

%pom_remove_parent

%build
%{ant} \
	-Dcompiler.source=1.8 \
%if %{without tests }
	-Dtest.skip=true \
%endif
    jar javadoc

%install
# jars
install -d -m 0755 %{buildroot}%{_javadir}
install -p -m 0644 target/%{short_name}-%{version}.jar \
  %{buildroot}%{_javadir}/%{short_name}.jar
ln -sf %{short_name}.jar %{buildroot}%{_javadir}/%{name}.jar
# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/%{short_name}.pom
%add_maven_depmap %{short_name}.pom %{short_name}.jar -a "org.apache.commons:commons-io"
# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt
%{_javadir}/%{name}.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
