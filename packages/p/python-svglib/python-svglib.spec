#
# spec file for package python-svglib
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-svglib
Version:        1.1.0
Release:        0
Summary:        Python library for reading and converting SVG
License:        LGPL-3.0-only
URL:            https://github.com/deeplook/svglib
Source:         https://files.pythonhosted.org/packages/source/s/svglib/svglib-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module cssselect2 >= 0.2.0}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module reportlab}
BuildRequires:  %{python_module tinycss2 >= 0.6.0}
BuildRequires:  yudit
# /SECTION
Requires:       python-cssselect2 >= 0.2.0
Requires:       python-lxml
Requires:       python-reportlab
Requires:       python-tinycss2 >= 0.6.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Pure Python library for reading and converting SVG.

%prep
%setup -q -n svglib-%{version}
# Remove hashbang
sed -i '1{/^#!/d}' svglib/svglib.py

%build
%python_build

%install
%python_install
%{python_clone -a %{buildroot}%{_bindir}/svg2pdf}
%{python_clone -a %{buildroot}%{_mandir}/man1/svg2pdf.1}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Skip several tests needing files from internet
%pytest -rs -k 'not (TestWikipediaFlags or TestOtherFiles or (TestW3CSVG and test_convert_pdf_png))'

%post
%{python_install_alternative svg2pdf svg2pdf.1%{ext_man}}

%postun
%python_uninstall_alternative svg2pdf

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/svg2pdf
%python_alternative %{_mandir}/man1/svg2pdf.1%{ext_man}
%{python_sitelib}/svglib*/

%changelog
