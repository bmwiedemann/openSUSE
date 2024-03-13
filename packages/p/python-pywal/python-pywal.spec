#
# spec file for package python-pywal
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


Name:           python-pywal
Version:        3.3.0
Release:        0
Summary:        Generate and change color-schemes on the fly
License:        MIT
URL:            https://github.com/dylanaraps/pywal
Source:         https://files.pythonhosted.org/packages/source/p/pywal/pywal-%{version}.tar.gz
Source1:        python-pywal.rpmlintrc
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     ImageMagick
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Generate and change color-schemes on the fly

%prep
%autosetup -p1 -n pywal-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/wal
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Forbidden by imagemagick's security policy
%pytest -k 'not test_gen_colors'

%post
%python_install_alternative wal

%postun
%python_uninstall_alternative wal

%files %{python_files}
%doc README.md
%license LICENSE.md
%python_alternative %{_bindir}/wal
%{python_sitelib}/pywal
%{python_sitelib}/pywal-%{version}.dist-info

%changelog
