#
# spec file for package python-confusable-homoglyphs
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
Name:           python-confusable-homoglyphs
Version:        3.2.0
Release:        0
Summary:        Detector for confusable use of Unicode homoglyphs
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/vhf/confusable_homoglyphs
Source:         https://files.pythonhosted.org/packages/source/c/confusable_homoglyphs/confusable_homoglyphs-%{version}.tar.gz
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A Python module to detect Unicode homoglyphs and homograph attacks.
Homoglyphs are characters that may appear the same but have different
codepoints, meaning or representation, for example U+0041 LATIN
CAPITAL LETTER A ('A') vs. U+0391 GREEK CAPITAL LETTER ALPHA, 'Α'.

%prep
%setup -q -n confusable_homoglyphs-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/confusable_homoglyphs
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%post
%python_install_alternative confusable_homoglyphs

%postun
%python_uninstall_alternative confusable_homoglyphs

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/confusable_homoglyphs

%changelog
