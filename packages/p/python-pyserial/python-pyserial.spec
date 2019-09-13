#
# spec file for package python-pyserial
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
Name:           python-pyserial
Version:        3.4
Release:        0
Summary:        Python Serial Port Extension
License:        Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pyserial/pyserial
Source:         https://files.pythonhosted.org/packages/source/p/pyserial/pyserial-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Requires(post): update-alternatives
Requires(preun): update-alternatives
Provides:       python-serial = %{version}
Obsoletes:      python-serial < %{version}
BuildArch:      noarch
%python_subpackages

%description
Python Serial Port Extension for Win32, Linux, BSD, Jython, IronPython

%package -n %{name}-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       python2-pyserial-doc = %{version}
Provides:       python3-pyserial-doc = %{version}

%description -n %{name}-doc
Documentation, examples, and help files for %{name}.

%prep
%setup -q -n pyserial-%{version}

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

mv %{buildroot}%{_bindir}/miniterm.py %{buildroot}%{_bindir}/miniterm
%python_clone -a %{buildroot}%{_bindir}/miniterm
rm documentation/_build/doctrees/environment.pickle

%{python_expand sed -i '1{/#!/d}' %{buildroot}%{$python_sitelib}/serial/tools/miniterm.py
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%python_exec test/run_all_tests.py

%post
%python_install_alternative miniterm

%preun
%python_uninstall_alternative miniterm

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.rst
%python_alternative miniterm
%{python_sitelib}/serial/
%{python_sitelib}/pyserial-%{version}-py*.egg-info

%files -n %{name}-doc
%doc examples/
%doc documentation/_build/*

%changelog
