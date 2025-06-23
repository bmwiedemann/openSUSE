#
# spec file for package python-python-editor
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


Name:           python-python-editor
Version:        1.0.4
Release:        0
Summary:        Python library to programmatically open an editor and capture the result
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/fmoo/python-editor
Source:         https://files.pythonhosted.org/packages/source/p/python-editor/python-editor-%{version}.tar.gz
# PATCH-FIX-UPSTREAM support-python312.patch https://github.com/fmoo/python-editor/commit/5023fafd265add111b29baca59b07f140daf75b7
Patch0:         support-python312.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if 0%{?is_opensuse}
BuildRequires:  nano
%endif
%python_subpackages

%description
python-editor is a library that provides the editor module for
programmatically interfacing with the editor defined in the EDITOR
environment variable.

%prep
%autosetup -p1 -n python-editor-%{version}

%build
find -type f -exec chmod 644 {} +
%pyproject_wheel

%install
%pyproject_install
%python_expand sed -i -e '/^#!\/usr\/bin\/env/d' %{buildroot}%{$python_sitelib}/editor.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

# the example does not look like an unit test
# %%check
# export EDITOR='nano'
# Xpython_exec test.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/editor.py
%{python_sitelib}/python[-_]editor-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/editor*

%changelog
