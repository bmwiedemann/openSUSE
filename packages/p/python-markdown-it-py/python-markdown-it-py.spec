#
# spec file for package python-markdown-it-py
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


Name:           python-markdown-it-py
Version:        2.2.0
Release:        0
Summary:        Python port of markdown-it Markdown parsing
License:        MIT
URL:            https://github.com/executablebooks/markdown-it-py/
Source:         https://github.com/executablebooks/markdown-it-py/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source:         https://files.pythonhosted.org/packages/source/m/markdown-it-py/markdown-it-py-%%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module flit}
BuildRequires:  %{python_module mdurl}
BuildRequires:  %{python_module pip}
# SECTION tests
BuildRequires:  %{python_module linkify-it-py}
BuildRequires:  %{python_module pytest-regressions}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-mdurl
Requires(post): update-alternatives
Requires(postun):update-alternatives
Suggests:       python-mdit-py-plugins
BuildArch:      noarch
%python_subpackages

%description
This is a Python port of [markdown-it], and some of its associated plugins.

It follows the CommonMark spec for baseline parsing, has a configurable syntax and is pluggable.

%prep
%setup -q -n markdown-it-py-%{version}
sed -i '1{/\/usr\/bin\/env python*/d;}' markdown_it/cli/parse.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/markdown-it
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%post
%python_install_alternative markdown-it

%postun
%python_uninstall_alternative markdown-it

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE LICENSE.markdown-it
%{python_sitelib}/markdown_it
%{python_sitelib}/markdown_it_py-%{version}.dist-info
%python_alternative %{_bindir}/markdown-it

%changelog
