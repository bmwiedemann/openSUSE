#
# spec file for package python-sphinxcontrib-nwdiag
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


Name:           python-sphinxcontrib-nwdiag
Version:        2.0.0
Release:        0
Summary:        Sphinx "nwdiag" extension
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/blockdiag/sphinxcontrib-nwdiag
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-nwdiag/sphinxcontrib-nwdiag-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 0.6
Requires:       python-blockdiag >= 1.5.0
Requires:       python-nwdiag >= 1.0.3
BuildArch:      noarch
%python_subpackages

%description
sphinxcontrib-nwdiag is a Sphinx extension for embedding nwdiag
diagrams. Network diagrams can be embedded with the "nwdiag",
"rackdiag" and "packetdiag" directives.

%prep
%setup -q -n sphinxcontrib-nwdiag-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%dir %{python_sitelib}/sphinxcontrib
%pycache_only %dir %{python_sitelib}/sphinxcontrib/__pycache__
%{python_sitelib}/sphinxcontrib/nwdiag.py
%pycache_only %{python_sitelib}/sphinxcontrib/__pycache__/nwdiag*
%{python_sitelib}/sphinxcontrib/packetdiag.py
%pycache_only %{python_sitelib}/sphinxcontrib/__pycache__/packetdiag*
%{python_sitelib}/sphinxcontrib/rackdiag.py
%pycache_only %{python_sitelib}/sphinxcontrib/__pycache__/rackdiag*
%{python_sitelib}/sphinxcontrib[-_]nwdiag-%{version}*-info
%{python_sitelib}/sphinxcontrib[-_]nwdiag-%{version}*-nspkg.pth

%changelog
