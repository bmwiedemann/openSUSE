#
# spec file for package python-markdown-word-count
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-markdown-word-count
Version:        0.1.0
Release:        0
Summary:        Word counter for raw Markdown files
License:        MIT
URL:            https://github.com/gandreadis/markdown-word-count
Source:         https://files.pythonhosted.org/packages/source/m/markdown-word-count/markdown_word_count-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Word counter for raw Markdown files

%prep
%autosetup -p1 -n markdown_word_count-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/mwc
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v tests

%post
%python_install_alternative mwc

%postun
%python_uninstall_alternative mwc

%files %{python_files}
%python_alternative %{_bindir}/mwc
%{python_sitelib}/mwc
%{python_sitelib}/markdown_word_count-%{version}.dist-info

%changelog
