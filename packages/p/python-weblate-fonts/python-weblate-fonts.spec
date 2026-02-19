#
# spec file for package python-weblate-fonts
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


Name:           python-weblate-fonts
Version:        2026.1
Release:        0
Summary:        Weblate fonts collection
License:        CC0-1.0 AND OFL-1.1
URL:            https://weblate.org/
Source:         https://files.pythonhosted.org/packages/source/w/weblate-fonts/weblate_fonts-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module uv-build}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Fonts used in Weblate.

Sources are available at <https://github.com/WeblateOrg/fonts>.

%prep
%autosetup -p1 -n weblate_fonts-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# no tests

%files %{python_files}
%license LICENSES/CC0-1.0.txt LICENSES/OFL-1.1.txt
%{python_sitelib}/weblate_fonts
%{python_sitelib}/weblate_fonts-%{version}.dist-info

%changelog
