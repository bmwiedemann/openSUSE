#
# spec file for package python-cloudflare
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-cloudflare
Version:        2.20.0
Release:        0
Summary:        Python wrapper for the Cloudflare v4 API
License:        MIT
URL:            https://github.com/cloudflare/python-cloudflare
Source:         https://files.pythonhosted.org/packages/source/c/cloudflare/cloudflare-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module jsonlines}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests >= 2.4.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-beautifulsoup4
Requires:       python-jsonlines
Requires:       python-requests >= 2.4.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Python wrapper for the Cloudflare Client API v4.

%prep
%setup -q -n cloudflare-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/cli4
%python_clone -a %{buildroot}%{_mandir}/man1/cli4.1
# remove examples from sitelib
%python_expand rm -rf %{buildroot}%{$python_sitelib}/examples
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# there is one test, but even upstream does not launch it

%post
%python_install_alternative cli4 cli4.1

%postun
%python_uninstall_alternative cli4 cli4.1

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/cli4
%python_alternative %{_mandir}/man1/cli4.1
%{python_sitelib}/CloudFlare
%{python_sitelib}/cli4
%{python_sitelib}/cloudflare-%{version}.dist-info

%changelog
