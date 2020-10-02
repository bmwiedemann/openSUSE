#
# spec file for package python-XStatic-jQuery
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
Name:           python-XStatic-jQuery
Version:        3.4.1.0
Release:        0
Summary:        jQuery repackaged for the XStatic standard
License:        MIT
URL:            http://jquery.com/
Source:         https://files.pythonhosted.org/packages/source/X/XStatic-jQuery/XStatic-jQuery-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

%python_subpackages

%description
jQuery javascript library packaged for setuptools (easy_install) / pip.
There are otherwise no changes.

You can find more info about the xstatic packaging way in the package `XStatic`.

%prep
%setup -q -n XStatic-jQuery-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
