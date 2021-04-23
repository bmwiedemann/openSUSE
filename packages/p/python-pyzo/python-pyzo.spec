#
# spec file for package python-pyzo
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
%define         skip_python2 1
Name:           python-pyzo
Version:        4.10.2
Release:        0
Summary:        Python IDE for scientific computing
License:        BSD-3-Clause
URL:            https://github.com/pyzo/pyzo
Source:         https://files.pythonhosted.org/packages/source/p/pyzo/pyzo-%{version}.tar.gz
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
Requires:       hicolor-icon-theme
Requires:       python-qt5
Requires:       pyzologo
BuildArch:      noarch
%python_subpackages

%description
Pyzo is a computing environment based on Python. Pyzo is a Python IDE
aimed at interactivity, and consists of an editor, a shell, and a set
of tools.

%package     -n pyzo
Summary:        Python IDE for scientific computing
Requires:       python3-pyzo = %{version}

%description -n pyzo
Pyzo is a computing environment based on Python. Pyzo is a Python IDE
aimed at interactivity, and consists of an editor, a shell, and a set
of tools.

%package     -n pyzologo
Summary:        Icons for Pyzo

%description -n pyzologo
Icons used by pyzo

%prep
%setup -q -n pyzo-%{version}
sed -i -e '/^#!\//, 1d' pyzo/*.py
sed -i -e '/^#!\//, 1d' pyzo/codeeditor/_test.py
sed -i -e '/^#!\//, 1d' pyzo/pyzokernel/guisupport.py

%build
%python_build

%install
%python_install
pushd pyzo/resources/
%suse_update_desktop_file pyzo Development Science IDE NumericalAnalysis
install -m 644 -Dt %{buildroot}%{_datadir}/applications pyzo.desktop
popd

pushd pyzo/resources/appicons
for f in pyzologo*.png ; do
    echo ${f}
    r="$(basename ${f:8} .png)"
    echo ${r}
    install -m 644 -Dt %{buildroot}%{_datadir}/icons/hicolor/${r}x${r}/apps/pyzologo.png ${f}
done

popd

%python_expand %fdupes %{buildroot}%{$python_sitelib}

# weirdly installed stuff
rm %{buildroot}%{_prefix}/LICENSE.md
rm %{buildroot}%{_prefix}/README.md
mv %{buildroot}%{_prefix}/pyzo* %{buildroot}%{python_sitelib}/pyzo/util/
chmod +x %{buildroot}%{python_sitelib}/pyzo/util/pyzolauncher.py

%check
# the only test which is in the upstream testsuite
# no need to download github tarball just because of this
export PYTHONPATH=%{buildroot}%{$python_sitelib}
%python_exec -c 'import pyzo; assert pyzo.__version__'

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/*

%files -n pyzo
%license LICENSE.md
%{_datadir}/applications/pyzo.desktop
%{_bindir}/pyzo

%files -n pyzologo
%{_datadir}/icons/hicolor/*/apps/pyzologo.png

%changelog
