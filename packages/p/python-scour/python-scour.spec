#
# spec file for package python-scour
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


%define oldpython python
%bcond_without libalternatives
Name:           python-scour
Version:        0.38.2
Release:        0
Summary:        An SVG scrubber
License:        Apache-2.0
Group:          Productivity/Graphics/Other
URL:            https://github.com/oberstet/scour
Source:         https://github.com/scour-project/scour/archive/v%{version}/scour-%{version}.tar.gz
# https://github.com/scour-project/scour/pull/306
Patch0:         python-scour-no-python2.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module xml}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       alts
Requires:       python-setuptools
Conflicts:      %{oldpython}-scour < 0.37
Provides:       scour = %{version}
BuildArch:      noarch
%ifpython2
Requires:       python-xml
%endif
%python_subpackages

%description
Scour is a Python script that aggressively cleans SVG files, removing
a lot of "cruft" that certain tools or authors embed into their
documents.
The goal of scour is to provide an identically rendered image.

%prep
%autosetup -p1 -n scour-%{version}
# remove unwanted shebang
sed -i '/^#!/ d' scour/{scour.py,yocto_css.py,svg_transform.py}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/scour

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test_scour.py

%pre
%python_libalternatives_reset_alternative scour

%files %{python_files}
%license LICENSE
%doc *.md
%python_alternative %{_bindir}/scour
%{python_sitelib}/scour/
%{python_sitelib}/scour-%{version}*-info

%changelog
