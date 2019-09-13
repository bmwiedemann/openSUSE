#
# spec file for package python-sphinxcontrib-nwdiag
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
Name:           python-sphinxcontrib-nwdiag
Version:        0.9.5
Release:        0
Summary:        Sphinx "nwdiag" extension
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            http://github.com/blockdiag/sphinxcontrib-nwdiag
Source:         https://files.pythonhosted.org/packages/source/s/sphinxcontrib-nwdiag/sphinxcontrib-nwdiag-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
