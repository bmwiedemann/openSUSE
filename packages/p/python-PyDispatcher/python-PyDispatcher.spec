#
# spec file for package python-PyDispatcher
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


Name:           python-PyDispatcher
Version:        2.0.7
Release:        0
Summary:        Multi-producer-multi-consumer signal dispatching mechanism
License:        BSD-3-Clause
URL:            https://github.com/mcfletch/pydispatcher
Source:         https://files.pythonhosted.org/packages/source/P/PyDispatcher/PyDispatcher-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Dispatcher mechanism for creating event models.

PyDispatcher is an enhanced version of Patrick K. O’Brien’s original
dispatcher.py module. It provides the Python programmer with a robust
mechanism for event routing within various application contexts.

Included in the package are the robustapply and saferef modules, which
provide the ability to selectively apply arguments to callable objects and
to reference instance methods using weak-references.

%prep
%setup -q -n PyDispatcher-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license license.txt
%{python_sitelib}/pydispatch
%{python_sitelib}/[Pp]y[Dd]ispatcher-%{version}*-info

%changelog
