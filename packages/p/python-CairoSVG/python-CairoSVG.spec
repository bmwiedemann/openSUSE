#
# spec file for package python-CairoSVG
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
%define skip_python2 1
Name:           python-CairoSVG
Version:        2.6.0
Release:        0
Summary:        A Python SVG converter based on Cairo
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://www.cairosvg.org/
Source:         CairoSVG-%{version}.tar.xz
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module cairocffi}
BuildRequires:  %{python_module cssselect2}
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tinycss2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-cairocffi
Requires:       python-cssselect2
Requires:       python-defusedxml
Requires:       python-tinycss2
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
CairoSVG is a SVG converter based on Cairo. It can export SVG files to PDF,
PostScript and PNG files.

For further information, please visit the CairoSVG website, http://www.cairosvg.org.

%prep
%setup -q -n CairoSVG-%{version}
# remove needless pytest dependencies
sed -i setup.cfg \
    -e '/pytest-runner/d' \
    -e '/--flake8/d' \
    -e '/--isort/d'

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}/%{_bindir}/cairosvg

%check
%pytest

%post
%python_install_alternative cairosvg

%postun
%python_uninstall_alternative cairosvg

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/cairosvg
%{python_sitelib}/*

%changelog
