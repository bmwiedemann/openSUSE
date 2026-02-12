#
# spec file for package python-MechanicalSoup
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
Name:           python-MechanicalSoup
Version:        1.4.0
Release:        0
Summary:        A Python library for automating interaction with websites
License:        MIT
URL:            https://github.com/hickford/MechanicalSoup
Source:         https://files.pythonhosted.org/packages/source/m/mechanicalsoup/mechanicalsoup-%{version}.tar.gz
Source100:      python-MechanicalSoup.rpmlintrc
# PATCH-FIX-UPSTREAM fix-unclosed-textarea.patch -- gh#MechanicalSoup/MechanicalSoup#454
Patch0:         fix-unclosed-textarea.patch
BuildRequires:  %{python_module beautifulsoup4 >= 4.7}
BuildRequires:  %{python_module httpbin}
BuildRequires:  %{python_module jsonschema >= 2.5.1}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-httpbin}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.22.0}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-beautifulsoup4 >= 4.7
Requires:       python-certifi
Requires:       python-lxml
Requires:       python-requests >= 2.22.0
Requires:       python-urllib3
Recommends:     python-httpbin
Recommends:     python-jsonschema >= 2.5.1
BuildArch:      noarch
%python_subpackages

%description
A Python library for automating interaction with websites.
MechanicalSoup automatically stores and sends cookies,
follows redirects, and can follow links and submit forms.
It doesn't do Javascript.

The Mechanize library is incompatible with Python 3 and development
is inactive. MechanicalSoup provides a similar API to it, built on
Python giants Requests (for http sessions) and BeautifulSoup (for
document navigation).

%prep
%autosetup -p1 -n mechanicalsoup-%{version}
# do not require cov/xdist/etc
sed -i -e '/addopts/d' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/MechanicalSoup/MechanicalSoup/issues/299 test_enctype_and_file_submit
%pytest -k 'not test_enctype_and_file_submit'

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/mechanicalsoup
%{python_sitelib}/[Mm]echanical[Ss]oup-%{version}*info

%changelog
