#
# spec file for package python-sphinx-gallery
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
Name:           python-sphinx-gallery
Version:        0.18.0
Release:        0
Summary:        Sphinx extension that builds an HTML gallery of examples
License:        BSD-3-Clause
URL:            https://github.com/sphinx-gallery/sphinx-gallery
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-gallery/sphinx_gallery-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module Sphinx >= 4}
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Pillow
Requires:       python-Sphinx >= 4
Suggests:       python-numpy
Suggests:       python-graphviz
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A Sphinx extension that builds an HTML gallery of examples from any set of Python scripts.

%prep
%autosetup -p1 -n sphinx_gallery-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# Don't ship tests
%python_expand rm -r %{buildroot}%{$python_sitelib}/sphinx_gallery/tests
%python_clone -a %{buildroot}%{_bindir}/sphinx_gallery_py2jupyter
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Requires network
donttest="test_embed_code_links_get_data"
# Requires jupyterlite_sphinx, long dependency chain and we don't ship it
donttest+=" or test_dummy_image"
%pytest sphinx_gallery/tests -k "not ($donttest)"

%post
%python_install_alternative sphinx_gallery_py2jupyter

%postun
%python_uninstall_alternative sphinx_gallery_py2jupyter

%files %{python_files}
%python_alternative %{_bindir}/sphinx_gallery_py2jupyter
%{python_sitelib}/sphinx_gallery
%{python_sitelib}/sphinx_gallery-%{version}.dist-info

%changelog
