#
# spec file for package juniversalchardet
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           juniversalchardet
Version:        1.0.3
Release:        0
Summary:        Encoding detector library
License:        MPL-1.1
Group:          Development/Libraries/Java
URL:            https://code.google.com/archive/p/juniversalchardet/
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/%{name}/%{name}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/com/googlecode/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Patch0:         source-target.patch
Patch1:         automatic-module-name.patch
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local >= 6
BuildArch:      noarch

%description
JUNIVERSALCHARDET is a Java port of 'universalchardet', that is the encoding
detector library of Mozilla.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q -n %{name}
%patch -P 0 -p1
%patch -P 1 -p1

%build
ant dist
javadoc -source 8 -encoding UTF-8 \
    -notimestamp \
    -d target/apidocs \
    -sourcepath src \
    org.mozilla.universalchardet

%install
# jar
install -dm 0755 %{buildroot}%{_javadir}/%{name}
install -pm 0644 dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}/%{name}.jar
# pom
install -dm 0755 %{buildroot}%{_mavenpomdir}/%{name}
%{mvn_install_pom} %{SOURCE1} %{buildroot}%{_mavenpomdir}/%{name}/%{name}.pom
%add_maven_depmap %{name}/%{name}.pom %{name}/%{name}.jar
# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -r target/apidocs/* %{buildroot}%{_javadocdir}/%{name}/
%fdupes %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc readme.txt
%license MPL-1.1.txt

%files javadoc
%{_javadocdir}/%{name}
%license MPL-1.1.txt

%changelog
