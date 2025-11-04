#
# spec file for package python-nose2
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-nose2
Version:        0.15.1
Release:        0
Summary:        The successor to the Python testing framework nose, based on unittest
License:        BSD-2-Clause AND Python-2.0
URL:            https://github.com/nose-devs/nose2
Source:         https://files.pythonhosted.org/packages/source/n/nose2/nose2-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Support Python 3.14 multiprocessing and argparse changes
Patch0:         support-python314.patch
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools-wheel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-coverage
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
nose2 is the successor to nose. It's unittest with plugins.
nose2 is a new project and does not support all of the behaviors of nose.
nose2's purpose is to extend unittest to make testing nicer and easier to understand.

%prep
%autosetup -p1 -n nose2-%{version}

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
pip install --no-index --find-links %{_prefix}/lib/python%{$python_bin_suffix}/wheels -e .
nose2 -v --pretty-assert
deactivate
}

%post
%python_install_alternative nose2

%postun
%python_uninstall_alternative nose2

%pre
%python_libalternatives_reset_alternative nose2

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%python_alternative %{_bindir}/nose2
%{python_sitelib}/nose2
%{python_sitelib}/nose2-%{version}.dist-info

%changelog
