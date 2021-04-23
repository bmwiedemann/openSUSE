#
# spec file for package python-python-fedora
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
%define skip_python2 1
Name:           python-python-fedora
Version:        1.1.0
Release:        0
Summary:        Python modules for interacting with Fedora Services
License:        LGPL-2.1-or-later
URL:            https://github.com/fedora-infra/python-fedora
Source:         https://files.pythonhosted.org/packages/source/p/python-fedora/python-fedora-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-beautifulsoup4
Requires:       python-kitchen
Requires:       python-lockfile
Requires:       python-munch
Requires:       python-openidc-client
Requires:       python-requests
Requires:       python-six >= 1.4.0
Suggests:       python-Beaker
Suggests:       python-Flask
Suggests:       python-Flask_WTF
Suggests:       python-Paste
Suggests:       python-python-openid-cla
Suggests:       python-python-openid-teams
Suggests:       python-python3-openid
Suggests:       python-repoze.who
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Beaker}
BuildRequires:  %{python_module Flask-WTF}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Paste}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module kitchen}
BuildRequires:  %{python_module lockfile}
BuildRequires:  %{python_module munch}
BuildRequires:  %{python_module openidc-client}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-openid-cla}
BuildRequires:  %{python_module python-openid-teams}
BuildRequires:  %{python_module python3-openid}
BuildRequires:  %{python_module repoze.who}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six >= 1.4.0}
# /SECTION
%python_subpackages

%description
Python modules for interacting with Fedora Services.

%prep
%setup -q -n python-fedora-%{version}
sed -i '1{/#!/d}' fedora/client/*.py

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
# test_openidbaseclient.py depends on nose
%pytest --ignore tests/functional/test_openidbaseclient.py

%files %{python_files}
%doc AUTHORS NEWS README.rst
%license COPYING
%{python_sitelib}/*

%changelog
