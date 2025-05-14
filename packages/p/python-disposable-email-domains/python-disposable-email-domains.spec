#
# spec file for package python-disposable-email-domains
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


Name:           python-disposable-email-domains
Version:        0.0.126
Release:        0
Summary:        A set of disposable email domains
# the "Homepage" link on PyPi is not the source repository for the PyPI tarball and is licensed under CC
# https://github.com/disposable-email-domains/disposable-email-domains/issues/346
# hence, the 3 lines under this comment (including "Source") are in one of the 2 coherent states and if you change one of them you have to change all three
License:        MIT
URL:            https://github.com/disposable-email-domains/python-disposable-email-domains
Source:         https://files.pythonhosted.org/packages/source/d/disposable-email-domains/disposable_email_domains-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Suggests:       python-check-manifest
BuildArch:      noarch
%python_subpackages

%description
A set of disposable email domains

%prep
%autosetup -p1 -n disposable_email_domains-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/disposable_email_domains
%{python_sitelib}/disposable_email_domains-%{version}.dist-info

%changelog
