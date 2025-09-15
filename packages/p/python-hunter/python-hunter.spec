#
# spec file for package python-hunter
#
# Copyright (c) 2025 SUSE LLC
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

%{?sle15_python_module_pythons}
Name:           python-hunter
Version:        3.9.0
Release:        0
Summary:        Pytest plugin for coverage reporting
License:        BSD-2-Clause
URL:            https://github.com/ionelmc/python-hunter
Source:         https://files.pythonhosted.org/packages/source/h/hunter/hunter-%{version}.tar.gz
BuildRequires:  %pythons
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module aspectlib}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module process-tests}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module tzdata}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
Hunter is a flexible code tracing toolkit, not for measuring coverage,
but for debugging, logging, inspection and other nefarious purposes.

%prep
%autosetup -p1 -n hunter-%{version}
cat >src/build_tests.py <<EOF
from setuptools import setup
from Cython.Build import cythonize

setup(
    name='Tests',
    ext_modules=cythonize("../tests/*.pyx"),
)
EOF

%build
%pyproject_wheel
export PYTHONDONTWRITEBYTECODE=1
pushd src
%python_exec build_tests.py build_ext
find . -name 'eviltracer.cpython-*-linux-gnu.so' -exec mv "{}" ../tests \;
find . -name 'sample5.cpython-*-linux-gnu.so' -exec mv "{}" ../tests \;
rm build_tests.py
popd

%install
%pyproject_install
%{python_expand \
      rm -r %{buildroot}%{$python_sitearch}/build_tests.py %{buildroot}%{$python_sitearch}/__pycache__
      find %{buildroot}%{$python_sitearch}/hunter \( -name "*.c" -o -name "*.h" \) -delete
%fdupes %{buildroot}%{$python_sitearch}/
}
%python_clone -a %{buildroot}%{_bindir}/hunter-trace

%check
export PYTHONPATH=tests
%pytest_arch -k 'not (test_pdb and (postmortem-ipdb or settrace-ipdb or debugger-ipdb) or test_fullsource_cython or test_source_cython or test_safe_repr or test_profile or test_errorsnooper)' --ignore tests/test_remote.py --ignore tests/test_integration.py

%post
%python_install_alternative hunter-trace

%postun
%python_uninstall_alternative hunter-trace

%files %{python_files}
%python_alternative %{_bindir}/hunter-trace
%license LICENSE
%doc AUTHORS.rst CHANGELOG.rst README.rst
%{python_sitearch}/hunter
%{python_sitearch}/hunter.pth
%{python_sitearch}/hunter-%{version}.dist-info

%changelog
