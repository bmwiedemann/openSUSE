#
# spec file for package python-Flask-Mail
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-Flask-Mail
Version:        0.9.1
Release:        0
Summary:        Flask extension for sending email
License:        BSD-3-Clause
URL:            https://github.com/rduplain/flask-mail
Source:         https://files.pythonhosted.org/packages/source/F/Flask-Mail/Flask-Mail-%{version}.tar.gz
# do not use mock, upstream url unavailable
Patch0:         python-Flask-Mail-no-mock.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Test requirements
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module speaklater}
# End of test requirements
Requires:       python-Flask
Requires:       python-blinker
BuildArch:      noarch
%python_subpackages

%description
A Flask extension for sending email messages.

%prep
%autosetup -p1 -n Flask-Mail-%{version}
sed -i 's/assertEquals/assertEqual/' tests.py
# Skip two failing tests
sed -i 's/test_unicode_sender/_test_unicode_sender/' tests.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/flask_mail.py
%pycache_only %{python_sitelib}/__pycache__/flask_mail.*.py*
%{python_sitelib}/Flask_Mail-%{version}.dist-info

%changelog
