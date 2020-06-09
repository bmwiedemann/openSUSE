#
# spec file for package python-responses
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-responses
Version:        0.10.14
Release:        0
Summary:        A utility library for mocking out the `requests` Python library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/getsentry/responses
Source:         https://files.pythonhosted.org/packages/source/r/responses/responses-%{version}.tar.gz
# test requirements
BuildRequires:  %{python_module cookies}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.0
Requires:       python-six
Suggests:       python-pytest
BuildArch:      noarch
%ifpython2
Requires:       python2-cookies
Requires:       python2-mock
%endif
%python_subpackages

%description
A utility library for mocking out the requests Python library.
Check https://github.com/getsentry/responses for more information
about the library.

%prep
%setup -q -n responses-%{version}

%build
export LANG="en_US.UTF8"
export PYTHONIOENCODING="utf_8"
%python_build

%install
export LANG="en_US.UTF8"
export PYTHONIOENCODING="utf_8"
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
