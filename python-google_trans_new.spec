#
# spec file for package python-google_trans_new
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


%define skip_python2 1
Name:           python-google_trans_new
Version:        1.1.9
Release:        0
Summary:        A free and unlimited python tools for google translate api
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/lushan88a/google_trans_new
Source:         https://files.pythonhosted.org/packages/source/g/google_trans_new/google_trans_new-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-requests
Requires:       python-urllib3
BuildArch:      noarch
%python_subpackages

%description
This a free and unlimited python tools for google translate api.

%prep
%autosetup -p1 -n google_trans_new-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%clean

%files %{python_files}
%doc README.md
%{python_sitelib}/google_trans_new
%{python_sitelib}/google_trans_new-%{version}*-info

%changelog
