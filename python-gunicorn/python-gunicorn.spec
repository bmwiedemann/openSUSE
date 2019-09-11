#
# spec file for package python-gunicorn
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
Name:           python-gunicorn
Version:        19.9.0
Release:        0
Summary:        WSGI HTTP Server for UNIX
License:        MIT
Group:          Development/Languages/Python
URL:            http://gunicorn.org
Source:         https://files.pythonhosted.org/packages/source/g/gunicorn/gunicorn-%{version}.tar.gz
Patch0:         pytest5.patch
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx
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
%patch0 -p1
# remove version pinning for test requirements
sed -i 's/==.*//' requirements_test.txt
sed -i -e '/cover/d' requirements_test.txt

%build
%python_build
sphinx-build -b html -d docs/build/doctrees docs/source docs/build/html

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/gunicorn
%python_clone -a %{buildroot}%{_bindir}/gunicorn_paster
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%post
%python_install_alternative gunicorn
%python_install_alternative gunicorn_paster

%postun
%python_uninstall_alternative gunicorn
%python_uninstall_alternative gunicorn_paster

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/gunicorn
%python_alternative %{_bindir}/gunicorn_paster
%{python_sitelib}/*

%files -n python-gunicorn-doc
%license LICENSE
%doc README.rst NOTICE THANKS docs/build/html

%changelog
