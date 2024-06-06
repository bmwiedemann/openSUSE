#
# spec file for package python-django-mailer
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


%define skip_python36 1
Name:           python-django-mailer
Version:        2.3.2
Release:        0
Summary:        A reusable Django app for queuing the sending of email
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pinax/django-mailer/
Source:         https://files.pythonhosted.org/packages/source/d/django-mailer/django-mailer-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-lockfile >= 0.8
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module lockfile >= 0.8}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-django}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A reusable Django app for queuing and throttling of email sending, scheduled sending,
consolidation of multiple notifications into single emails and logging of mail failures.

%prep
%autosetup -p1 -n django-mailer-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -v

%files %{python_files}
%doc AUTHORS CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*mailer*/

%changelog
