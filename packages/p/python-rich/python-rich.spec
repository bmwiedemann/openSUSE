#
# spec file for package python-rich
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2020-2021, Martin Hauke <mardnh@gmx.de>
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
Name:           python-rich
Version:        13.9.4
Release:        0
Summary:        A Python library for rich text and beautiful formatting in the terminal
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Textualize/rich
Source:         https://files.pythonhosted.org/packages/source/r/rich/rich-%{version}.tar.gz
BuildRequires:  %{python_module dataclasses >= 0.7 if %python-base < 3.7}
BuildRequires:  %{python_module markdown-it-py >= 2.2.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pygments >= 2.13.0}
BuildRequires:  %{python_module typing_extensions >= 4.0.0 if %python-base < 3.9}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-markdown-it-py >= 2.2.0
Requires:       python-pygments >= 2.13.0
Suggests:       python-ipywidgets >= 7.5.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%if 0%{?python_version_nodots} < 39
Requires:       python-typing_extensions >= 4.0.0
%endif
%if 0%{?python_version_nodots} < 37
Requires:       python-dataclasses >= 0.7
%endif
%python_subpackages

%description
Render rich text, tables, progress bars, syntax highlighting,
markdown and more to the terminal.

%prep
%setup -q -n rich-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/rich
%{python_sitelib}/rich-%{version}*-info

%changelog
