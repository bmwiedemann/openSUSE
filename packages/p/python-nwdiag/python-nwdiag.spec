#
# spec file for package python-nwdiag
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
Name:           python-nwdiag
Version:        1.0.4
Release:        0
Summary:        Generator for network diagram images from text
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            http://blockdiag.com/
Source:         https://files.pythonhosted.org/packages/source/n/nwdiag/nwdiag-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-blockdiag >= 1.5.0
Requires:       python-setuptools
Suggests:       python-reportlab
Suggests:       python-docutils
Suggests:       python-nose
Suggests:       python-reportlab
Suggests:       python-docutils
BuildArch:      noarch

%python_subpackages

%description
nwdiag generates network diagram images from text.

%prep
%setup -q -n nwdiag-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%python3_only %{_bindir}/nwdiag
%python3_only %{_bindir}/rackdiag
%python3_only %{_bindir}/packetdiag
%{python_sitelib}/*

%changelog
