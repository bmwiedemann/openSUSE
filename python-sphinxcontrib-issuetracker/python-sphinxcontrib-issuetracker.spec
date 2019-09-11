#
# spec file for package python-sphinxcontrib-issuetracker
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
%bcond_with     test
Name:           python-sphinxcontrib-issuetracker
Version:        0.11
Release:        0
Summary:        Sphinx integration with different issuetrackers
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            http://packages.python.org/sphinxcontrib-issuetracker
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-issuetracker/sphinxcontrib-issuetracker-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx >= 1.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 1.1
Requires:       python-requests >= 1.1
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 1.1}
BuildRequires:  python-mock
%endif
%python_subpackages

%description
A Sphinx extension to reference issues in issue trackers, either explicitly
with an "issue" role or optionally implicitly by issue ids like ``#10`` in
plaintext.

%prep
%setup -q -n sphinxcontrib-issuetracker-%{version}

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
%doc CREDITS README.rst CHANGES.rst
%{python_sitelib}/sphinxcontrib/issuetracker/
%{python_sitelib}/sphinxcontrib_issuetracker-%{version}-py*-nspkg.pth
%{python_sitelib}/sphinxcontrib_issuetracker-%{version}-py*.egg-info

%changelog
