#
# spec file for package python-netutils
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
Name:           python-netutils
Version:        1.2.0
Release:        0
Summary:        Common helper functions useful in network automation
License:        Apache-2.0
URL:            https://netutils.readthedocs.io
Source:         https://github.com/networktocode/netutils/archive/refs/tags/v%{version}.tar.gz#/netutils-%{version}.tar.gz
BuildRequires:  %{python_module jinja2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Python library that is a collection of objects for common network automation tasks.

%prep
%setup -q -n netutils-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand %fdupes %{buildroot}%{$python_sitelib}
rm -f %{buildroot}%{$python_sitelib}/{CHANGELOG.md,LICENSE,README.md}
}

%check
# test_is_fqdn_resolvable, test_fqdn_to_ip, test_tcp_ping: needs internet connection
# test_sphinx_build: needs Sphinx, which is a huge dependency just for the one test
%pytest -k "not (test_is_fqdn_resolvable or test_fqdn_to_ip or test_tcp_ping or test_sphinx_build)"

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/netutils
%{python_sitelib}/netutils-%{version}*-info

%changelog
