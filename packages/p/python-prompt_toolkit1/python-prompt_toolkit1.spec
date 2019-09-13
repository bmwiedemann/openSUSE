#
# spec file for package python-prompt_toolkit1
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         oldpython python
%bcond_without  test
Name:           python-prompt_toolkit1
Version:        1.0.15
Release:        0
Summary:        Library for building interactive command lines in Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jonathanslenders/python-prompt-toolkit
Source:         https://files.pythonhosted.org/packages/source/p/prompt_toolkit/prompt_toolkit-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.9.0
Requires:       python-wcwidth
Recommends:     python-Pygments
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wcwidth}
%endif
%ifpython2
Obsoletes:      %{oldpython}-python-prompt-toolkit < %{version}
Provides:       %{oldpython}-python-prompt-toolkit = %{version}
%endif
Provides:       python-prompt_toolkit = %{version}
Conflicts:      python-prompt_toolkit >= 2
%python_subpackages

%description
Prompt toolkit is a library for building interactive command
lines in Python.

%prep
%setup -q -n prompt_toolkit-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
py.test-%{$python_bin_suffix}
}
%endif

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst README.rst CHANGELOG
%{python_sitelib}/prompt_toolkit*

%changelog
