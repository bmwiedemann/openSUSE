#
# spec file for package python-recommonmark
#
# Copyright (c) 2020 SUSE LLC
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
%define oldpython python
Name:           python-recommonmark
Version:        0.6.0
Release:        0
Summary:        Python docutils-compatibility bridge to CommonMark
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/rtfd/recommonmark
Source:         https://files.pythonhosted.org/packages/source/r/recommonmark/recommonmark-%{version}.tar.gz
#Source0:        https://github.com/rtfd/recommonmark/archive/%%{version}.tar.gz#/recommonmark-%%{version}.tar.gz
Patch0:         sphinx2.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-CommonMark >= 0.7.3
Requires:       python-Sphinx >= 1.3.1
Requires:       python-docutils >= 0.11
Requires(post): update-alternatives
Requires(preun): update-alternatives
Provides:       python-reCommonMark = %{version}
Obsoletes:      python-reCommonMark < %{version}
BuildArch:      noarch
# SECTION tests
BuildRequires:  %{python_module CommonMark >= 0.7.3}
BuildRequires:  %{python_module Sphinx >= 1.3.1}
BuildRequires:  %{python_module docutils >= 0.11}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module pytest}
# /SECTION tests
%ifpython2
Obsoletes:      %{oldpython}-reCommonMark < %{version}
Provides:       %{oldpython}-reCommonMark = %{version}
%endif
%python_subpackages

%description
A python docutils-compatibility bridge to CommonMark.

This allows you to write CommonMark inside of Docutils & Sphinx projects.

Documentation is available on Read the Docs:
http://recommonmark.readthedocs.org

%prep
%setup -q -n recommonmark-%{version}
%patch0 -p1
# Remove upstream's egg-info
rm -rf %{pypi_name}.egg-info
# find and remove unneeded shebangs
find recommonmark -name "*.py" | xargs sed -i '1 {/^#!/ d}'

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/cm2html
%python_clone -a %{buildroot}%{_bindir}/cm2latex
%python_clone -a %{buildroot}%{_bindir}/cm2man
%python_clone -a %{buildroot}%{_bindir}/cm2pseudoxml
%python_clone -a %{buildroot}%{_bindir}/cm2xetex
%python_clone -a %{buildroot}%{_bindir}/cm2xml

%check
# gh#readthedocs/recommonmark#200
%pytest -k 'not (test_integration or test_code or test_headings or test_image or test_links or test_lists)'

%post
%{python_install_alternative cm2man cm2latex cm2xetex cm2pseudoxml cm2html cm2xml}

%preun
%python_uninstall_alternative cm2man

%files %{python_files}
%license license.md
%python_alternative %{_bindir}/cm2html
%python_alternative %{_bindir}/cm2latex
%python_alternative %{_bindir}/cm2man
%python_alternative %{_bindir}/cm2pseudoxml
%python_alternative %{_bindir}/cm2xetex
%python_alternative %{_bindir}/cm2xml
%{python_sitelib}/recommonmark/
%{python_sitelib}/recommonmark-%{version}-py*.egg-info
%doc README.md CHANGELOG.md

%changelog
