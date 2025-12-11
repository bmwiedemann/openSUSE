#
# spec file for package python-rlPyCairo
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


Name:           python-rlPyCairo
Version:        0.4.0
Release:        0
Summary:        Plugin backend renderer for reportlab.graphicsrenderPM
License:        BSD-3-Clause
URL:            https://hg.reportlab.com/hg-public/rlPyCairo/
Source:         https://files.pythonhosted.org/packages/source/r/rlPyCairo/rlpycairo-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module freetype-py >= 2.3}
BuildRequires:  %{python_module pycairo >= 1.20.0}
# /SECTION
BuildRequires:  fdupes
Supplements:    python-reportlab
Requires:       python-freetype-py >= 2.3
Requires:       python-pycairo >= 1.20.0
Provides:       python-rlpycairo = %{version}
BuildArch:      noarch
%python_subpackages

%description
Plugin backend renderer for reportlab.graphics.renderPM

%prep
%autosetup -p1 -n rlpycairo-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.txt
%{python_sitelib}/rlPyCairo
%{python_sitelib}/rlpycairo-%{version}.dist-info

%changelog
