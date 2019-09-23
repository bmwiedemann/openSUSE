#
# spec file for package python-PyDispatcher
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-PyDispatcher
Version:        2.0.5
Release:        0
Summary:        Multi-producer-multi-consumer signal dispatching mechanism
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://pydispatcher.sourceforge.net
Source:         https://files.pythonhosted.org/packages/source/P/PyDispatcher/PyDispatcher-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc license.txt
%{python_sitelib}/*

%changelog
