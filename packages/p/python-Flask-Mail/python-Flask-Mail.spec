#
# spec file for package python-Flask-Mail
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
Name:           python-Flask-Mail
Version:        0.9.1
Release:        0
Summary:        Flask extension for sending email
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/rduplain/flask-mail
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Mail/Flask-Mail-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Test requirements
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module speaklater}
# End of test requirements
Requires:       python-Flask
Requires:       python-blinker
BuildArch:      noarch
%python_subpackages

%description
A Flask extension for sending email messages.

%prep
%setup -q -n Flask-Mail-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
