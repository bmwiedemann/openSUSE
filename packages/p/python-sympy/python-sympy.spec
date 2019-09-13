#
# spec file for package python-sympy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_with     test
Name:           python-sympy
Version:        1.4
Release:        0
Summary:        Computer algebra system (CAS) in Python
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            http://www.sympy.org/
Source0:        https://files.pythonhosted.org/packages/source/s/sympy/sympy-%{version}.tar.gz
Source99:       python-sympy-rpmlintrc
BuildRequires:  %{python_module mpmath >= 0.19}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mpmath >= 0.19
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-jupyter_ipython
Recommends:     python-numpy
Recommends:     python-symengine
BuildArch:      noarch
%python_subpackages

%description
SymPy is a Python library for symbolic mathematics. It aims to become
a full-featured computer algebra system (CAS) while keeping the code
as simple as possible in order to be comprehensible and easily
extensible. SymPy is written entirely in Python and does not require
any external libraries.

%prep
%setup -q -n sympy-%{version}

%{python_expand cp -r examples examples-%{$python_bin_suffix}
find examples-%{$python_bin_suffix} -name "*.py" -exec sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" {} \;
find examples-%{$python_bin_suffix} -name "*.py" -exec sed -i "s|^#! %{_bindir}/env python$|#!%{__$python}|" {} \;
}

%build
%python_build

%install
%python_install

%{python_expand chmod a+x %{buildroot}%{$python_sitelib}/sympy/utilities/tests/diagnose_imports.py
chmod a+x %{buildroot}%{$python_sitelib}/sympy/physics/mechanics/models.py
chmod a+x %{buildroot}%{$python_sitelib}/sympy/benchmarks/bench_symbench.py
sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" %{buildroot}%{$python_sitelib}/sympy/utilities/tests/diagnose_imports.py
sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" %{buildroot}%{$python_sitelib}/sympy/physics/mechanics/models.py
sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" %{buildroot}%{$python_sitelib}/sympy/benchmarks/bench_symbench.py
# Deduplicating files can generate a RPMLINT warning for pyc mtime
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/sympy/utilities/tests/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/sympy/utilities/tests/
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/sympy/physics/mechanics/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/sympy/physics/mechanics/
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/sympy/benchmarks/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/sympy/benchmarks/
%fdupes %{buildroot}%{$python_sitelib}
}

%python_clone -a %{buildroot}%{_bindir}/isympy
%python_clone -a %{buildroot}%{_mandir}/man1/isympy.1

%post
%{python_install_alternative isympy isympy.1%{ext_man} }

%postun
%python_uninstall_alternative isympy

%if %{with test}
%check
export LANG=en_US.UTF-8
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%doc examples-%{python_bin_suffix}/
%python_alternative %{_bindir}/isympy
%python_alternative %{_mandir}/man1/isympy.1%{ext_man}
%{python_sitelib}/sympy
%{python_sitelib}/isympy.py*
%{python_sitelib}/sympy-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__/isympy*.py*

%changelog
