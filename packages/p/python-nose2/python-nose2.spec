#
# spec file for package python-nose2
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
Name:           python-nose2
Version:        0.15.1
Release:        0
Summary:        The successor to the Python testing framework nose, based on unittest
License:        BSD-2-Clause AND Python-2.0
URL:            https://github.com/nose-devs/nose2
Source:         https://files.pythonhosted.org/packages/source/n/nose2/nose2-%{version}.tar.gz
# Required for testsuite. Bring on python-wheel-wheel
Source1:        https://files.pythonhosted.org/packages/c7/c3/55076fc728723ef927521abaa1955213d094933dc36d4a2008d5101e1af5/wheel-0.42.0-py3-none-any.whl
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools-wheel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-coverage
BuildArch:      noarch
%python_subpackages

%description
nose2 is the successor to nose. It's unittest with plugins.
nose2 is a new project and does not support all of the behaviors of nose.
nose2's purpose is to extend unittest to make testing nicer and easier to understand.

%prep
%autosetup -p1 -n nose2-%{version}
mkdir ../wheels
cp %{SOURCE1} ../wheels

%build
%pyproject_wheel

%install
# -I : work around boo#1201041
%pyproject_install -I
%python_clone -a %{buildroot}%{_bindir}/nose2
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LC_CTYPE=C.UTF8
%{python_expand # nose must test itself in an editable install
$python -m venv editable-%{$python_bin_suffix} --system-site-packages
. editable-%{$python_bin_suffix}/bin/activate
pip install --no-index --find-links /usr/lib/python%{$python_bin_suffix}/wheels  --find-links ../wheels -e .
nose2 -v --pretty-assert
deactivate
}

%post
%python_install_alternative nose2

%postun
%python_uninstall_alternative nose2

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%python_alternative %{_bindir}/nose2
%{python_sitelib}/nose2
%{python_sitelib}/nose2-%{version}.dist-info

%changelog
