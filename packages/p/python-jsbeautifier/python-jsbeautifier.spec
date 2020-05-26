#
# spec file for package python-jsbeautifier
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
Name:           python-jsbeautifier
Version:        1.11.0
Release:        0
Summary:        JavaScript unobfuscator and beautifier
License:        MIT
URL:            https://jsbeautifier.org
Source0:        https://files.pythonhosted.org/packages/source/j/jsbeautifier/jsbeautifier-%{version}.tar.gz
# https://github.com/beautify-web/js-beautify/issues/1674
Source1:        https://raw.githubusercontent.com/beautify-web/js-beautify/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-EditorConfig >= 0.12.2
Requires:       python-setuptools
Requires:       python-six >= 1.13.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module EditorConfig >= 0.12.2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.13.0}
# /SECTION
%python_subpackages

%description
Beautify, unpack or deobfuscate JavaScript. Handles popular online obfuscators.

%prep
%setup -q -n jsbeautifier-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/js-beautify
%{python_expand %fdupes %{buildroot}%{$python_sitelib}}

%check
%pytest jsbeautifier/tests/testindentation.py
%pytest jsbeautifier/tests/generated/tests.py

%post
%python_install_alternative js-beautify

%postun
%python_uninstall_alternative js-beautify

%files %{python_files}
%license LICENSE
%python_alternative %{_bindir}/js-beautify
%{python_sitelib}/jsbeautifier
%{python_sitelib}/jsbeautifier-%{version}-py*.egg-info

%changelog
