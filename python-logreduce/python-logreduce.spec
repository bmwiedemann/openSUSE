#
# spec file for package python-logreduce
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-logreduce
Version:        0.4.0
Release:        0
Summary:        Log file anomaly extractor
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://logreduce.softwarefactory-project.io/
Source:         https://files.pythonhosted.org/packages/source/l/logreduce/logreduce-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-CherryPy
Requires:       python-PyYAML
Requires:       python-SQLAlchemy
Requires:       python-aiohttp
Requires:       python-alembic
Requires:       python-gear
Requires:       python-numpy
Requires:       python-requests
Requires:       python-scikit-learn
Requires:       python-scipy
Requires:       python-voluptuous
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module CherryPy}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module alembic}
BuildRequires:  %{python_module gear}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module routes}
BuildRequires:  %{python_module scikit-learn}
BuildRequires:  %{python_module scipy}
BuildRequires:  %{python_module voluptuous}
# /SECTION
%python_subpackages

%description
Based on success logs, logreduce highlights useful text in failed logs.
The goal is to save time in finding a failure's root cause.

On average, learning run at 2000 lines per second, and
testing run at 1300 lines per seconds.

logreduce uses a *model* to learn successful logs and detect novelties in
failed logs:

* Random words are manually removed using regular expression
* Then lines are converted to a matrix of token occurrences
  (using **HashingVectorizer**),
* An unsupervised learner implements neighbor searches
  (using **NearestNeighbors**).

%prep
%setup -q -n logreduce-%{version}
sed -i -e 's,flake8.*,,' test-requirements.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m pytest -v

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%python3_only %{_bindir}/logreduce
%python3_only %{_bindir}/logreduce-client
%python3_only %{_bindir}/logreduce-server
%python3_only %{_bindir}/logreduce-worker
%{python_sitelib}/*

%changelog
