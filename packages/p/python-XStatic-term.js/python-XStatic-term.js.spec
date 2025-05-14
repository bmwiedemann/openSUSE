#
# spec file for package python-XStatic-term.js
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-XStatic-term.js
Version:        0.0.7.0
Release:        0
Summary:        AngularJS library "term.js" repackaged for the XStatic standard
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/chjj/term.js
Source:         https://files.pythonhosted.org/packages/source/X/XStatic-term.js/XStatic-term.js-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
term.js javascript library packaged for setuptools (easy_install) / pip.
There are otherwise no changes.

* term.js project: `Github chjj/term.js <https://github.com/chjj/term.js>`_
* XStatic package: `Github takluyver/XStatic-termjs <https://github.com/takluyver/XStatic-termjs>`_

You can find more info about the xstatic packaging way in the package `XStatic`.

%prep
%setup -q -n XStatic-term.js-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%dir %{python_sitelib}/xstatic
%dir %{python_sitelib}/xstatic/pkg
%{python_sitelib}/xstatic/pkg/termjs
%{python_sitelib}/[Xx][Ss]tatic[-_]term[._]js-%{version}*-info
%{python_sitelib}/[Xx][Ss]tatic[-_]term[._]js-%{version}*nspkg.pth

%changelog
