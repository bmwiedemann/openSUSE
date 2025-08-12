#
# spec file for package python-bottle
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-bottle
Version:        0.13.4
Release:        0
Summary:        WSGI framework for small web applications
License:        MIT
URL:            https://bottlepy.org/
Source:         https://files.pythonhosted.org/packages/source/b/bottle/bottle-%{version}.tar.gz
Source1:        http://bottlepy.org/docs/0.12/bottle-docs.pdf
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
%python_subpackages

%description
Bottle is a micro-framework for small web applications. It offers
request dispatching (routes) with URL parameter support, templates, a
built-in HTTP server, and adapters for many third party WSGI/HTTP
servers and template engines. This is all in a single file and with
no dependencies other than the Python Standard Library.

%if 0%{?suse_version} > 1500
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
%endif

%prep
%autosetup -p1 -n bottle-%{version}
cp %{SOURCE1} .
chmod 644 bottle.py
sed -i '1{ /^#!/d }' bottle.py

%build
%pyproject_wheel

%install
%pyproject_install
rm -rf %{buildroot}%{_bindir}/bottle.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/bottle

%check
%pyunittest -v

%pre
%python_libalternatives_reset_alternative bottle.py
%python_libalternatives_reset_alternative bottle

%post
%python_install_alternative bottle

%postun
%python_uninstall_alternative bottle.py
%python_uninstall_alternative bottle

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/bottle
%{python_sitelib}/bottle.py*
%pycache_only %{python_sitelib}/__pycache__
%{python_sitelib}/bottle-%{version}.dist-info

%if 0%{?suse_version} > 1500
%files -n %{name}-doc
%endif
%doc bottle-docs.pdf

%changelog
