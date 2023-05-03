#
# spec file for package python-blockdiag
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


%{?sle15_python_module_pythons}
Name:           python-blockdiag
Version:        3.0.0
Release:        0
Summary:        Program to generate block-diagram images from text
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://blockdiag.com/
Source:         https://files.pythonhosted.org/packages/source/b/blockdiag/blockdiag-%{version}.tar.gz
# PATCH-FIX-UPSTREAM python-blockdiag-nose-to-pytest.patch gh#blockdiag/blockdiag#131 pgajdos@suse.com
# Remove the last silly dependency on nose
Patch0:         python-blockdiag-nose-to-pytest.patch
BuildRequires:  %{python_module Pillow >= 3}
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module funcparserlib >= 1.0.0~a0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module webcolors}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 3
Requires:       python-funcparserlib >= 1.0.0~a0
Requires:       python-setuptools
Requires:       python-webcolors
Requires(post): update-alternatives
Requires(preun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module reportlab}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module pytest}
# /SECTION
%if 0%{?suse_version} || 0%{?fedora_version} >= 24
Recommends:     ghostscript
Recommends:     python-Wand
Recommends:     python-reportlab
%endif
%python_subpackages

%description
The blockdiag package generates block-diagram image files
from spec-text files.

%prep
%autosetup -p1 -n blockdiag-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/blockdiag

%post
%python_install_alternative blockdiag

%postun
%python_uninstall_alternative blockdiag

%check
pushd src
# other disabled tests:
# [    9s] WARNING: Could not retrieve: http://blockdiag.com/favicon.ico
# [    9s] WARNING: Could not retrieve: http://upload.wikimedia.org/wikipedia/commons/9/9b/Scalable_Vector_Graphics_Circle2.svg
# [    9s] WARNING: Could not retrieve: http://people.sc.fsu.edu/~jburkardt/data/eps/circle.eps
%pytest -k 'not (test_app_cleans_up_images or test_node_attribute or test_setup_inline_svg_is_true_with_multibytes)'
popd

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%python_alternative %{_bindir}/blockdiag
%{python_sitelib}/blockdiag
%{python_sitelib}/blockdiag-%{version}*-info

%changelog
