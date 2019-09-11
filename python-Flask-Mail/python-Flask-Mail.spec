#
# spec file for package python-Flask-Mail
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask-Mail
Version:        0.9.1
Release:        0
License:        BSD-3-Clause
Summary:        Flask extension for sending email
Url:            https://github.com/rduplain/flask-mail
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Mail/Flask-Mail-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
# Test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module speaklater}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module blinker}
# End of test requirements
Requires:       python-blinker
Requires:       python-Flask
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
%python_exec %{_bindir}/nosetests

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
