#
# spec file for package xml-stylebook
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


Name:           xml-stylebook
Version:        1.0~b3_xalan2
Release:        0
Summary:        Apache XML Stylebook
License:        Apache-1.1
URL:            https://xml.apache.org/
Source0:        %{name}-%{version}.tar.xz
Patch0:         %{name}-image-printer.patch
Patch1:         %{name}-build-javadoc.patch
BuildRequires:  ant
BuildRequires:  dejavu-fonts
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.8
BuildRequires:  javapackages-local
BuildRequires:  xerces-j2
BuildRequires:  xml-commons-apis-bootstrap
Requires:       xerces-j2
Requires:       xml-apis
BuildArch:      noarch

%description
Apache XML Stylebook is a HTML documentation generator.

%package       javadoc
Summary:        API documentation for %{name}

%description   javadoc
%{summary}.

%package       demo
Summary:        Examples for %{name}
Requires:       %{name} = %{version}

%description   demo
Examples demonstrating the use of %{name}.

%prep
%setup -q
%patch -P 0
%patch -P 1

%build
%{ant} \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 \
    -Dversion-xalan-2=%{version} \
    -Dclasspath=$(build-classpath xml-apis xerces-j2)

# Build the examples (this serves as a good test suite)
pushd docs
java -classpath "$(build-classpath xml-apis xerces-j2):../bin/stylebook-%{version}.jar" \
  org.apache.stylebook.StyleBook "targetDirectory=../results" book.xml ../styles/apachexml
popd

%install
# jars
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 bin/stylebook-%{version}.jar \
  %{buildroot}%{_javadir}/%{name}.jar

# javadoc
install -dm 0755 %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

# examples
install -dm 0755 %{buildroot}%{_datadir}/%{name}
cp -pr docs %{buildroot}%{_datadir}/%{name}
cp -pr styles %{buildroot}%{_datadir}/%{name}
cp -pr results %{buildroot}%{_datadir}/%{name}
%fdupes -s %{buildroot}%{_datadir}/%{name}

%files
%license LICENSE.txt
%{_javadir}/%{name}.jar

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}

%files demo
%{_datadir}/%{name}

%changelog
