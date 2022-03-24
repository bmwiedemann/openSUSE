#
# spec file for package python-logreduce
#
# Copyright (c) 2022 SUSE LLC
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
# CLI tool, no module
%define pythons python3
Name:           python-logreduce
Version:        0.6.1
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
sed -i '1{/^#!/d}' logreduce/cmd.py

# CherryPy 10.1 and lower requires nose in cherrypy/test/helper.py needed by test_api.py
# As of logreduce 0.5.2, upstream doesnt restrict the cherrypy version,
# so remove test_api.py (which has only two tests) if any python has older CherryPy
%{python_expand if $python -c 'import cherrypy,sys,distutils.version; sys.exit(distutils.version.LooseVersion(cherrypy.__version__) < distutils.version.LooseVersion("10.2"))' ; then
  rm -f logreduce/tests/test_api.py
fi}

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/logreduce/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
# not sure where to report
sed -i 's:from mock:from unittest.mock:' logreduce/tests/test_download.py
%pytest

%files %{python_files}
%license LICENSE
%doc ChangeLog README.rst
%{_bindir}/logreduce
%{python_sitelib}/*

%changelog
