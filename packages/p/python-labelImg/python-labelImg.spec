#
# spec file for package python-labelImg
#
# Copyright (c) 2021 SUSE LLC
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
%define         skip_python2 1
Name:           python-labelImg
Version:        1.8.4
Release:        0
Summary:        Graphical image annotation tool
License:        MIT
URL:            https://github.com/tzutalin/labelImg
Source:         https://github.com/tzutalin/labelImg/archive/v%{version}.tar.gz
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  xvfb-run
Requires:       python-lxml
Requires:       python-qt5
Provides:       labelImg
BuildArch:      noarch
%python_subpackages

%description
LabelImg is a graphical image annotation tool and label object bounding boxes in images.

%prep
%setup -q -n labelImg-%{version}

%build
# Fix rpm runtime dependency rpmlint error replace the shebang in all the scripts with %%{_bindir}/python3
find . -name "*.py" -exec sed -i 's|#!%{_bindir}/env python|#!%{_bindir}/python3|' {} ";"
%make_build qt5py3
export LC_ALL=C.utf-8
%python_build

%install
export LC_ALL=C.utf-8
%python_install
# Fix permissions
%python_expand chmod 0755 %{buildroot}%{$python_sitelib}/labelImg/labelImg.py
%python_clone -a %{buildroot}%{_bindir}/labelImg
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
export LC_ALL=C.utf-8
%python_expand PYTHONPATH=%{buildroot}/%{$python_sitelib} xvfb-run -a $python -m unittest discover tests -v

%post
%python_install_alternative labelImg

%postun
%python_uninstall_alternative labelImg

%files %{python_files}
%license LICENSE
%doc README.rst CONTRIBUTING.rst
%python_alternative %{_bindir}/labelImg
%{python_sitelib}/*

%changelog
