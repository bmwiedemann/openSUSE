#
# spec file for package python-JPype1
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


%bcond_without  test
# https://build.opensuse.org/package/show/Java:packages/h2database is not in Factory
%bcond_with     test_jdbc
%{?sle15_python_module_pythons}
Name:           python-JPype1
Version:        1.5.1
Release:        0
Summary:        Python to Java bridge
License:        Apache-2.0
URL:            https://github.com/jpype-project/jpype
Source:         https://files.pythonhosted.org/packages/source/j/jpype1/jpype1-%{version}.tar.gz
Patch0:         JPype1-java8compat.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  ant
BuildRequires:  ca-certificates-mozilla
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  java-devel >= 9
BuildRequires:  javapackages-tools
BuildRequires:  python-rpm-macros
Requires:       java-headless >= 1.8
Recommends:     python-numpy
Suggests:       python-typing_extensions
ExcludeArch:    %{ix86} armv7
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module jedi}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions}
%if %{with test_jdbc}
BuildRequires:  h2database
BuildRequires:  hsqldb
BuildRequires:  sqlite-jdbc
%endif
# /SECTION
%endif
%python_subpackages

%description
A Python to Java bridge.

%prep
%autosetup -p1 -n jpype1-%{version}
# Avoid build dependency on PyInstaller
rm jpype/_pyinstaller/test_jpype_pyinstaller.py

%build
ant -f native/build.xml jar
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with test}
%check
ant -f test/build.xml compile

# JClassTestCase.testAsArray fails on i586
# https://github.com/jpype-project/jpype/issues/1029
skip_tests="(JClassTestCase and testAsArray)"

# v1.4.1: https://github.com/jpype-project/jpype/issues/1116
skip_tests+=" or (HtmlTestCase and testClass)"

%if %{without test_jbdc}
skip_tests+=" or test_sql_h2 or test_sql_hsqldb or test_sql_sqlite"
%endif

export CLASSPATH=${PWD}/test/classes:%{_libdir}/java/sqlite-jdbc.jar:%{_localstatedir}/lib/hsqldb/lib/hsqldb.jar:%{_datadir}/java/h2database/h2.jar:%{_datadir}/java/jts/jts-core.jar:%{_datadir}/java/osgi-service-jdbc/org.osgi.service.jdbc.jar
%pytest_arch -rs -k "not ($skip_tests)"

%endif

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitearch}/jpype
%{python_sitearch}/org.jpype.jar
%{python_sitearch}/_jpype*.so
%{python_sitearch}/jpype1-%{version}.dist-info

%changelog
