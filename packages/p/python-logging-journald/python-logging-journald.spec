#
# spec file for package python-logging-journald
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-logging-journald
Version:        0.6.5
Release:        0
Summary:        Pure python logging handler for writing logs to the journald using native protocol
License:        MIT
URL:            https://github.com/mosquito/logging-journald
Source:         https://files.pythonhosted.org/packages/source/l/logging_journald/logging_journald-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Pure python logging handler for writing logs to the journald using native protocol

%prep
%setup -q -n logging_journald-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%{python_sitelib}/logging_journald.py
%pycache_only %{python_sitelib}/__pycache__/*.pyc
%{python_sitelib}/logging_journald-%{version}.dist-info

%changelog
