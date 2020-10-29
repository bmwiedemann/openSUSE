#
# spec file for package python-xcffib
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
%define skip_python2 1
Name:           python-xcffib
Version:        0.10.1
Release:        0
Summary:        A drop in replacement for xpyb, an XCB python binding
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/tych0/xcffib
Source:         https://files.pythonhosted.org/packages/source/x/xcffib/xcffib-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.1.0}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  libxcb-devel
BuildRequires:  python-rpm-macros
BuildRequires:  xeyes
BuildRequires:  xvfb-run
Requires:       python-cffi >= 1.1.0
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
The xcffib package is intended to be a (mostly) drop-in
replacement for xpyb.

%prep
%setup -q -n xcffib-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} xvfb-run nosetests-%{$python_bin_suffix} -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/xcffib/
%{python_sitelib}/xcffib-%{version}-py*.egg-info

%changelog
