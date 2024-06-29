#
# spec file for package python-sympy
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


%{?sle15_python_module_pythons}
# Tests run 7h53m47s in OBS ... so we are switching them off right now
%bcond_with  test
Name:           python-sympy
Version:        1.12.1
Release:        0
Summary:        Computer algebra system (CAS) in Python
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://www.sympy.org/
Source0:        https://files.pythonhosted.org/packages/source/s/sympy/sympy-%{version}.tar.gz
Source99:       python-sympy-rpmlintrc
BuildRequires:  %{python_module mpmath >= 1.1.0 with %python-mpmath < 1.4.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mpmath >= 1.1.0
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-ipython
Recommends:     python-numpy
Recommends:     python-symengine
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
SymPy is a Python library for symbolic mathematics. It aims to become
a full-featured computer algebra system (CAS) while keeping the code
as simple as possible in order to be comprehensible and easily
extensible. SymPy is written entirely in Python and does not require
any external libraries.

%prep
%autosetup -p1 -n sympy-%{version}

sed -i -e '/^#!\//, 1d' sympy/testing/tests/diagnose_imports.py

%{python_expand cp -r examples examples-%{$python_bin_suffix}
find examples-%{$python_bin_suffix} -name "*.py" -exec sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" {} \;
find examples-%{$python_bin_suffix} -name "*.py" -exec sed -i "s|^#! %{_bindir}/env python$|#!%{__$python}|" {} \;
}

%build
%python_build

%install
%python_install

%{python_expand chmod a+x %{buildroot}%{$python_sitelib}/sympy/physics/mechanics/models.py
chmod a+x %{buildroot}%{$python_sitelib}/sympy/physics/optics/polarization.py
chmod a+x %{buildroot}%{$python_sitelib}/sympy/benchmarks/bench_symbench.py
sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" %{buildroot}%{$python_sitelib}/sympy/physics/mechanics/models.py
sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" %{buildroot}%{$python_sitelib}/sympy/physics/optics/polarization.py
sed -i "s|^#!%{_bindir}/env python$|#!%{__$python}|" %{buildroot}%{$python_sitelib}/sympy/benchmarks/bench_symbench.py
}
%{python_compileall}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/isympy
%python_clone -a %{buildroot}%{_mandir}/man1/isympy.1

%post
%{python_install_alternative isympy isympy.1%{ext_man} }

%postun
%python_uninstall_alternative isympy

%if %{with test}
%check
# Don’t even dare to think that the pytest macro could manage
# all complexities hidden in that specific command!
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib} PYTHONDONTWRITEBYTECODE=1
$python -c 'from sympy.testing import runtests ; runtests.run_all_tests()'
}
%endif

%files %{python_files}
%license LICENSE
%doc AUTHORS README.md
%doc examples-%{python_bin_suffix}/
%python_alternative %{_bindir}/isympy
%python_alternative %{_mandir}/man1/isympy.1%{ext_man}
%{python_sitelib}/sympy
%{python_sitelib}/isympy.py*
%{python_sitelib}/sympy-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__/isympy*.py*

%changelog
