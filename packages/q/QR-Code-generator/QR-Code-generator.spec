#
# spec file for package QR-Code-generator
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define libcname libqrcodegen1
%define libcppname libqrcodegencpp1

%global pip_version 1.8.0
%global cmake_code_version 1.8.0.cmake3

%{?sle15_python_module_pythons}

Name:           QR-Code-generator
Version:        1.8.0+git17.856ba8a
Release:        0
Summary:        QR Code generator library
License:        MIT
URL:            https://github.com/nayuki/QR-Code-generator
Source0:        %{name}-%{version}.tar.zst
Source1:        qrcodegen-cmake-%cmake_code_version.tar.zst
Source2:        %{name}-build.xml
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  ant
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-local
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  zstd
%python_subpackages

%description
This project aims to be the best, clearest QR Code generator library in multiple languages.
The primary goals are flexible options and absolute correctness.
Secondary goals are compact implementation size and good documentation comments.

%if 0%{?suse_version} < 1500
# this is hack to make rpm happy as %python_subpackage does not work
%package -n python-%{name}
Summary:        QR Code generator python bindings

%description -n python-%{name}
QR Code generator python2 bindings
%endif

%package devel
Summary:        Development files for QR code generator
Requires:       %{libcname}
Requires:       %{libcppname}
Provides:       qrcodegen-devel

%description devel
Development files, headers/libs for QR code generator

%package -n %{libcname}
Summary:        QR Code generator library

%description -n %{libcname}
C QR Code generator library

%package -n %{libcppname}
Summary:        QR Code generator library

%description -n %{libcppname}
C++ QR Code generator library

%package java
Summary:        QR Code generator library - Java

%description java
Java implementation of the QR Code generator library

%package javadoc
Summary:        QR Code generator library - Javadoc

%description javadoc
The Javadoc for the Java implementaion of the QR Code generator library

%prep
%autosetup -p1 -a1
ln -s qrcodegen-cmake-%cmake_code_version/{CMakeLists.txt,cmake} .
cp qrcodegen-cmake-%cmake_code_version/{README.md,LICENSE} .
cp %{SOURCE2} java/build.xml

%build
%cmake

pushd ../python
%pyproject_wheel
popd

pushd ../java
ant jar javadoc
popd

%install
%cmake_install

pushd python
%pyproject_install
popd

pushd java
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/qrcodegen.jar %{buildroot}%{_javadir}/qrcodegen.jar
install -dm 0755 %{buildroot}%{_mavenpomdir}
%mvn_install_pom pom.xml %{buildroot}%{_mavenpomdir}/qrcodegen.pom
%add_maven_depmap qrcodegen.pom qrcodegen.jar
install -dm 0755 %{buildroot}%{_javadocdir}
cp -r target/site/apidocs %{buildroot}%{_javadocdir}/qrcodegen
%fdupes -s %{buildroot}%{_javadocdir}
popd

%ldconfig_scriptlets -n %{libcname}
%ldconfig_scriptlets -n %{libcppname}

%files %{python_files}
%license Readme.markdown
%{python_sitelib}/qrcodegen.py
%pycache_only %{python_sitelib}/__pycache__/qrcodegen.*.pyc
%{python_sitelib}/qrcodegen-%{pip_version}.dist-info

%files -n QR-Code-generator-devel
%license LICENSE Readme.markdown
%doc README.md Readme.markdown
%{_libdir}/cmake/qrcodegencpp/
%{_libdir}/cmake/qrcodegen/
%{_libdir}/libqrcodegen.so
%{_libdir}/libqrcodegencpp.so
%{_includedir}/qrcodegen/
%{_includedir}/qrcodegencpp/
%{_libdir}/pkgconfig/qrcodegencpp.pc
%{_libdir}/pkgconfig/qrcodegen.pc

%files -n %{libcname}
%license Readme.markdown
%{_libdir}/libqrcodegen.so.*

%files -n %{libcppname}
%license Readme.markdown
%{_libdir}/libqrcodegencpp.so.*

%files -n QR-Code-generator-java -f java/.mfiles
%license Readme.markdown

%files -n QR-Code-generator-javadoc
%{_javadocdir}/qrcodegen
%license Readme.markdown

%changelog
