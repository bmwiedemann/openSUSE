#
# spec file for package python-XStatic-jquery-ui
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-XStatic-jquery-ui
Version:        1.13.0.2
Release:        0
Summary:        jQuery UI repackaged for the XStatic standard
License:        MIT
URL:            https://jqueryui.com/
Source:         https://files.pythonhosted.org/packages/source/X/XStatic-jquery-ui/xstatic_jquery_ui-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/jquery/jquery-ui/master/LICENSE.txt
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-XStatic-jQuery
BuildArch:      noarch
%python_subpackages

%description
jquery-ui javascript library packaged for setuptools (easy_install) / pip.

You can find more info about the xstatic packaging way in the package `XStatic`.

%prep
%setup -q -n xstatic_jquery_ui-%{version}
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}/%{_prefix}

%files %{python_files}
%doc README.txt
%license LICENSE.txt
%dir %{python_sitelib}/xstatic
%dir %{python_sitelib}/xstatic/pkg
%{python_sitelib}/xstatic/pkg/jquery_ui
%{python_sitelib}/[Xx][Ss]tatic[-_]jquery[-_]ui-%{version}.dist-info

%changelog
