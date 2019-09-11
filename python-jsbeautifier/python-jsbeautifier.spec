#
# spec file for package python-jsbeautifier
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        1.10.1
Release:        0
Summary:        JavaScript unobfuscator and beautifier
License:        MIT
Group:          Development/Languages/Python
Url:            http://jsbeautifier.org
Source0:        https://files.pythonhosted.org/packages/source/j/jsbeautifier/jsbeautifier-%{version}.tar.gz
# https://github.com/beautify-web/js-beautify/issues/1674
Source1:        https://raw.githubusercontent.com/beautify-web/js-beautify/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module EditorConfig >= 0.12.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.6.1}
# /SECTION
BuildRequires:  fdupes
Requires:       python-EditorConfig >= 0.12.0
Requires:       python-setuptools
Requires:       python-six >= 1.6.1
BuildArch:      noarch

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
%{python_expand %fdupes %{buildroot}%{$python_sitelib}}

%check
%python_exec setup.py test

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE
%python3_only %{_bindir}/js-beautify
%{python_sitelib}/jsbeautifier
%{python_sitelib}/jsbeautifier-%{version}-py*.egg-info

%changelog
