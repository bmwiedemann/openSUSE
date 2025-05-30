#
# spec file for package python-imbox
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


Name:           python-imbox
Version:        0.9.8
Release:        0
Summary:        Python IMAP for Human beings
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/martinrusev/imbox
Source:         https://files.pythonhosted.org/packages/source/i/imbox/imbox-%{version}.tar.gz
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-chardet
%python_subpackages

%description
Python library for reading IMAP mailboxes and converting email content to machine readable data

%prep
%setup -q -n imbox-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/imbox
%{python_sitelib}/imbox-%{version}*-info

%changelog
