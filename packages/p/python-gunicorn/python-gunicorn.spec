#
# spec file for package python-gunicorn
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-gunicorn
Version:        20.0.4
Release:        0
Summary:        WSGI HTTP Server for UNIX
License:        MIT
Group:          Development/Languages/Python
URL:            https://gunicorn.org
Source:         https://files.pythonhosted.org/packages/source/g/gunicorn/gunicorn-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 3.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
Requires:       python-setuptools >= 3.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork
worker model ported from Ruby's Unicorn_ project. The Gunicorn server is broadly
compatible with various web frameworks.

%package -n python-gunicorn-doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
Provides:       %{python_module gunicorn-doc = %{version}}

%description -n python-gunicorn-doc
Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork
worker model ported from Ruby's Unicorn_ project. The Gunicorn server is broadly
compatible with various web frameworks.

This package contains the documentation.

%prep
%setup -q -n gunicorn-%{version}
# remove version pinning for test requirements
sed -i 's/==.*//' requirements_test.txt
sed -i -e '/cover/d' requirements_test.txt
# do not check coverage
sed -i -e 's/--cov[^ ]*//' -e 's/--cov-report[^ ]*//' setup.cfg

%build
%python_build
sphinx-build -b html -d docs/build/doctrees docs/source docs/build/html

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/gunicorn
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative gunicorn

%postun
%python_uninstall_alternative gunicorn

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/gunicorn
%{python_sitelib}/*

%files -n python-gunicorn-doc
%license LICENSE
%doc README.rst NOTICE THANKS docs/build/html

%changelog

