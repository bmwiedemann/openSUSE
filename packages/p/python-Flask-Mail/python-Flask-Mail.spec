#
# spec file for package python-Flask-Mail
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        0.10.0
Release:        0
Summary:        Flask extension for sending email
License:        BSD-3-Clause
URL:            https://github.com/pallets-eco/flask-mail
Source:         https://github.com/pallets-eco/flask-mail/archive/%{version}.tar.gz#/flask_mail-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Test requirements
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module blinker}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module speaklater}
# End of test requirements
Requires:       python-Flask
Requires:       python-blinker
BuildArch:      noarch
%python_subpackages

%description
A Flask extension for sending email messages.

%prep
%autosetup -p1 -n flask-mail-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Skip unicode failing tests
donttest="test_unicode_sender"
%pytest -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/flask_mail
%{python_sitelib}/[Ff]lask_[Mm]ail-%{version}.dist-info

%changelog
