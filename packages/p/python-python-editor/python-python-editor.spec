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
Version:        1.0.4+git13
Release:        0
Summary:        Python library to programmatically open an editor and capture the result
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/fmoo/python-editor
Source:         python-editor-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# tests
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-mock}

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
sed -i 's|__VERSION__ = .*|__VERSION__ = "%{version}"|' setup.py

%build
find -type f -exec chmod 644 {} +
%pyproject_wheel

%install
%pyproject_install
%python_expand sed -i -e '/^#!\/usr\/bin\/env/d' %{buildroot}%{$python_sitelib}/editor.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%check
%python_expand pytest test_editor.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/editor.py
%{python_sitelib}/python_editor-%{version}.dist-info/
%pycache_only %{python_sitelib}/__pycache__/editor*

%changelog
