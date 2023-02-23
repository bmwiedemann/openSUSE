#
# spec file for package python-bottle
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-bottle
Version:        0.12.24
Release:        0
Summary:        WSGI framework for small web applications
License:        MIT
URL:            https://bottlepy.org/
Source:         https://files.pythonhosted.org/packages/source/b/bottle/bottle-%{version}.tar.gz
Source1:        http://bottlepy.org/docs/0.12/bottle-docs.pdf
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Bottle is a micro-framework for small web applications. It offers
request dispatching (routes) with URL parameter support, templates, a
built-in HTTP server, and adapters for many third party WSGI/HTTP
servers and template engines. This is all in a single file and with
no dependencies other than the Python Standard Library.

%package -n %{name}-doc
Summary:        Documentation for %{name}
Provides:       %{python_module bottle-doc = %{version}}

%description -n %{name}-doc
Bottle is a micro-framework for small web applications. It offers
request dispatching (routes) with URL parameter support, templates, a
built-in HTTP server, and adapters for many third party WSGI/HTTP
servers and template engines. This is all in a single file and with
no dependencies other than the Python Standard Library.

This subpackage contains the PDF documentation for %{name}.

%prep
%setup -q -n bottle-%{version}

cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/bottle.py

%check
%pyunittest -v

%post
%python_install_alternative bottle.py

%postun
%python_uninstall_alternative bottle.py

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/bottle.py
%{python_sitelib}/bottle.py*
%pycache_only %{python_sitelib}/__pycache__
%{python_sitelib}/bottle-%{version}-py%{python_version}.egg-info

%files -n %{name}-doc
%doc bottle-docs.pdf

%changelog
