#
# spec file for package python-Pydap
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
Name:           python-Pydap
Version:        3.2.2
Release:        0
Summary:        Pure Python Opendap/DODS client and server
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/pydap/pydap
Source:         https://files.pythonhosted.org/packages/source/P/Pydap/Pydap-%{version}.tar.gz
BuildRequires:  %{python_module Jinja2}
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module docopt}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python-singledispatch
Requires:       python-Jinja2
Requires:       python-WebOb
Requires:       python-beautifulsoup4
Requires:       python-docopt
Requires:       python-numpy
Requires:       python-six >= 1.4
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-PasteDeploy
Recommends:     python-WebTest
Recommends:     python-coards
Recommends:     python-flake8
Recommends:     python-gunicorn
Recommends:     python-lxml
Recommends:     python-netCDF4
Recommends:     python-pytest >= 2.8
Recommends:     python-pytest-attrib
Recommends:     python-pytest-cov
Recommends:     python-requests
Recommends:     python-requests-mock
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module PasteDeploy}
BuildRequires:  %{python_module WebTest}
BuildRequires:  %{python_module coards}
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module gunicorn}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module netCDF4}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytest >= 2.8}
BuildRequires:  %{python_module pytest-attrib}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module requests-mock}
BuildRequires:  %{python_module requests}
BuildRequires:  python-mock
BuildRequires:  python3-gsw
# /SECTION
%ifpython3
Recommends:     python-gsw
%endif
%ifpython2
Requires:       python-singledispatch
%endif
%ifpython2
Recommends:     python-mock
%endif
%python_subpackages

%description
Pydap is an implementation of the Opendap/DODS protocol, written from
scratch. You can use Pydap to access scientific data on the internet
without having to download it; instead, you work with special array
and iterable objects that download data on-the-fly as necessary, saving
bandwidth and time. The module also comes with a robust-but-lightweight
Opendap server, implemented as a WSGI application.

%prep
%setup -q -n Pydap-%{version}
rm -f docs/_build/html/.buildinfo
%fdupes docs/_build/html

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/pydap
%python_clone -a %{buildroot}%{_bindir}/dods

%post
%python_install_alternative pydap dods

%postun
%python_uninstall_alternative pydap dods

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python setup.py nosetests || :

%files %{python_files}
%doc CONTRIBUTORS.md NEWS.md README.md docs/_build/html
%license docs/license.rst
%python_alternative %{_bindir}/dods
%python_alternative %{_bindir}/pydap
%{python_sitelib}/Pydap-%{version}-py*.egg-info
%{python_sitelib}/Pydap-%{version}-py*-nspkg.pth
%{python_sitelib}/pydap/

%changelog
