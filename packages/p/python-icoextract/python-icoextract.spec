#
# spec file for package python-icoextract
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


%{?sle15_python_module_pythons}
Name:           python-icoextract
Version:        0.1.5
Release:        0
Summary:        Extract icons from Windows PE files (.exe/.dll)
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/jlu5/icoextract
Source:         https://github.com/jlu5/icoextract/archive/%{version}/icoextract-%{version}.tar.gz
# BuildRequires:  %%{python_module devel}
BuildRequires:  %{python_module pefile}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  mingw32-cross-binutils
BuildRequires:  mingw32-cross-gcc
BuildRequires:  mingw64-cross-gcc
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
Requires:       python-pefile
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-Pillow
BuildArch:      noarch
%python_subpackages

%description
icoextract is an icon extractor for Windows PE files (.exe/.dll), written in
Python. It also includes a thumbnailer script (exe-thumbnailer) for Linux
desktops.

%prep
%setup -q -n icoextract-%{version}

find . -name \*.py -exec sed -i -e '1{\@^#!%{_bindir}/env python@d}' '{}' \;

%build
%pyproject_wheel

%install
%pyproject_install
mkdir -p %{buildroot}%{_datadir}/thumbnailers/
cp exe-thumbnailer.thumbnailer %{buildroot}%{_datadir}/thumbnailers/
%python_clone -a %{buildroot}%{_bindir}/exe-thumbnailer
%python_clone -a %{buildroot}%{_bindir}/icoextract
%python_clone -a %{buildroot}%{_bindir}/icolist
%python_clone -a %{buildroot}%{_datadir}/thumbnailers/exe-thumbnailer.thumbnailer
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd tests
%make_build
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python test_extract.py
$python test_thumbnailer.py
}

%post
update-alternatives --install \
    %{_datadir}/thumbnailers/exe-thumbnailer.thumbnailer \
    exe-thumbnailer.thumbnailer \
    %{_datadir}/thumbnailers/exe-thumbnailer.thumbnailer-%{python_version} %{python_version_nodots}
%python_install_alternative exe-thumbnailer
%python_install_alternative icoextract
%python_install_alternative icolist

%postun
[ -f %{_datadir}/thumbnailers/exe-thumbnailer.thumbnailer-%{python_version} ] || update-alternatives --remove \
    exe-thumbnailer.thumbnailer \
    %{_datadir}/thumbnailers/exe-thumbnailer.thumbnailer-%{python_version}
%python_uninstall_alternative exe-thumbnailer
%python_uninstall_alternative icoextract
%python_uninstall_alternative icolist

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/icoextract
%{python_sitelib}/icoextract-%{version}*-info
%python_alternative %{_bindir}/exe-thumbnailer
%python_alternative %{_bindir}/icoextract
%python_alternative %{_bindir}/icolist
%dir %{_datadir}/thumbnailers
%python_alternative %{_datadir}/thumbnailers/exe-thumbnailer.thumbnailer

%changelog
