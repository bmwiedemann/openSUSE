#
# spec file for package python-confusable-homoglyphs
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
Name:           python-confusable-homoglyphs
Version:        3.3.1
Release:        0
Summary:        Detector for confusable use of Unicode homoglyphs
License:        MIT
URL:            https://sr.ht/~valhalla/confusable_homoglyphs/
Source:         https://files.pythonhosted.org/packages/source/c/confusable_homoglyphs/confusable_homoglyphs-%{version}.tar.gz
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%autosetup -p1 -n confusable_homoglyphs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/confusable_homoglyphs
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v tests/

%post
%python_install_alternative confusable_homoglyphs

%postun
%python_uninstall_alternative confusable_homoglyphs

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/confusable_homoglyphs
%{python_sitelib}/confusable_homoglyphs-%{version}.dist-info
%python_alternative %{_bindir}/confusable_homoglyphs

%changelog
