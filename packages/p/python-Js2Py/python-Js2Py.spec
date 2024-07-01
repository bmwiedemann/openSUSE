#
# spec file for package python-Js2Py
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
Name:           python-Js2Py
Version:        0.74
Release:        0
Summary:        JavaScript to Python Translator & JavaScript interpreter
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/PiotrDabkowski/Js2Py
Source:         https://files.pythonhosted.org/packages/source/J/Js2Py/Js2Py-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/PiotrDabkowski/Js2Py/master/LICENSE.md
# PATCH-FIX-OPENSUSE remove-python-six.patch
Patch0:         remove-python-six.patch
# PATCH-FIX-UPSTREAM python312.patch gh#PiotrDabkowski/Js2Py#327
Patch1:         python312.patch
# PATCH-FIX-UPSTREAM CVE-2024-28397.patch gh#PiotrDabkowski/Js2Py#323
Patch2:         CVE-2024-28397.patch
BuildRequires:  %{python_module pyjsparser}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pyjsparser
Requires:       python-tzlocal
BuildArch:      noarch
%python_subpackages

%description
Translates JavaScript to Python code. Js2Py is able to translate and
execute virtually any JavaScript code. Js2Py, basically an
implementation of the JavaScript core, is written in pure Python.

%prep
%autosetup -p1 -n Js2Py-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd tests
touch node_failed.txt
%{python_expand #
PYTHONPATH=%{buildroot}%{$python_sitelib} $python run.py
}
popd

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/js2py
%{python_sitelib}/Js2Py-%{version}*-info

%changelog
