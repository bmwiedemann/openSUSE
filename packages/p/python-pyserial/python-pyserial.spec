#
# spec file for package python-pyserial
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?sle15_python_module_pythons}
Name:           python-pyserial
Version:        3.5
Release:        0
Summary:        Python Serial Port Extension
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pyserial/pyserial
Source:         https://files.pythonhosted.org/packages/source/p/pyserial/pyserial-%{version}.tar.gz
# PATCH-FIX-UPSTREAM - pyserial/pyserial#757 - Replace deprecated unittest.findTestCases function
Patch1:         https://github.com/pyserial/pyserial/pull/757.patch#/replace-deprecated-unittest-function.patch
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(preun): update-alternatives
%endif
Provides:       python-serial = %{version}
Obsoletes:      python-serial < %{version}
BuildArch:      noarch
%python_subpackages

%description
Python Serial Port Extension for Win32, Linux, BSD, Jython, IronPython

%if 0%{?suse_version} > 1500
%package -n %{name}-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       python2-pyserial-doc = %{version}
Provides:       python3-pyserial-doc = %{version}

%description -n %{name}-doc
Documentation, examples, and help files for %{name}.
%endif

%prep
%autosetup -p1 -n pyserial-%{version}

# Unnecessary
rm serial/tools/list_ports_windows.py \
  serial/tools/list_ports_osx.py \
  serial/win32.py \
  serial/serialwin32.py

# Requires .Net/IronPython, and especially System.IO.Ports which is troublesome
rm serial/serialcli.py

# Requires Jython with JavaComm
rm serial/serialjava.py

find serial -type f -not -name 'miniterm.py' -exec sed -i '1{/#!/d}' {} +
find serial -type f -not -name 'miniterm.py' -exec chmod a-x {} +

touch test/__init__.py

%build
%python_build
make %{?_smp_mflags} -C documentation html && rm documentation/_build/html/.buildinfo # Build HTML documentation
sed -i -e "1{s|^#![[:space:]]*\/.*bin.*$|#!%{_bindir}/python3|}" examples/*.py

%install
%python_install

%python_clone -a %{buildroot}%{_bindir}/pyserial-miniterm
%python_clone -a %{buildroot}%{_bindir}/pyserial-ports
rm documentation/_build/doctrees/environment.pickle

%{python_expand sed -i '1{/#!/d}' %{buildroot}%{$python_sitelib}/serial/tools/miniterm.py
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%python_exec test/run_all_tests.py

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative pyserial-miniterm
%python_libalternatives_reset_alternative pyserial-ports

%post
%python_install_alternative pyserial-miniterm
%python_install_alternative pyserial-ports

%preun
%python_uninstall_alternative pyserial-miniterm
%python_uninstall_alternative pyserial-ports

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.rst
%python_alternative pyserial-miniterm
%python_alternative pyserial-ports
%{python_sitelib}/serial/
%{python_sitelib}/pyserial-%{version}-py*.egg-info

%if 0%{?suse_version} > 1500
%files -n %{name}-doc
%endif
%doc examples/
%doc documentation/_build/*

%changelog
