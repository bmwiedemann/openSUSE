#
# spec file for package python-jaraco.text
#
# Copyright (c) 2022 SUSE LLC
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


%define skip_python2 1
Name:           python-jaraco.text
Version:        3.11.0
Release:        0
Summary:        Tools to work with text
License:        MIT
URL:            https://github.com/jaraco/jaraco.text
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco.text/jaraco.text-%{version}.tar.gz
BuildRequires:  %{python_module autocommand}
BuildRequires:  %{python_module importlib_resources if %python-base < 3.9}
BuildRequires:  %{python_module inflect}
BuildRequires:  %{python_module jaraco.context >= 4.1}
BuildRequires:  %{python_module jaraco.functools}
BuildRequires:  %{python_module more-itertools}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if 0%{?python_version_nodots} < 39
Requires:       python-importlib_resources
%endif
Requires:       python-autocommand
Requires:       python-inflect
Requires:       python-jaraco.context >= 4.1
Requires:       python-jaraco.functools
Requires:       python-more-itertools
BuildArch:      noarch
%python_subpackages

%description
This package provides handy routines for dealing with text, such as
wrapping, substitution, trimming, stripping, prefix and suffix removal,
line continuation, indentation, comment processing, identifier processing,
values parsing, case insensitive comparison, and more.

%prep
%setup -q -n jaraco.text-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no pathlib2 in the distro
rm conftest.py
%{python_expand # workaround for gh#jaraco/jaraco.text#10 without pathlib2
if [ %{$python_version_nodots} -lt 310 ]; then
  $python_donttest="or read_newlines or report_newlines"
fi
}
%pytest -k "not (dummyprefix ${$python_donttest})"

%files %{python_files}
%license LICENSE
%doc README.rst CHANGES.rst
%{python_sitelib}/jaraco/text
%{python_sitelib}/jaraco.text-%{version}*-info

%changelog
