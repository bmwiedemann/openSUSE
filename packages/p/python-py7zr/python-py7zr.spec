#
# spec file for package python-py7zr
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-py7zr
Version:        0.11.3
Release:        0
Summary:        Library and utility to support 7zip
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/miurahr/py7zr
Source0:        https://files.pythonhosted.org/packages/source/p/py7zr/py7zr-%{version}.tar.gz
BuildRequires:  %{python_module pep517}
BuildRequires:  %{python_module pyannotate}
BuildRequires:  %{python_module pycryptodome}
BuildRequires:  %{python_module pylzma}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module texttable}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest-remotedata}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pycryptodome
Requires:       python-texttable
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
py7zr is a library and utility to support 7zip archive compression, decompression, encryption and decryption written by Python programming language.

%prep
%setup -q -n py7zr-%{version}
find . -type f -name "*.py" -exec sed -i \
       -e '1s|/usr/bin/env python$|/usr/bin/python3|g' \
       -e '1s|/usr/bin/python |/usr/bin/python3 |g' \
       {} \;

sed -i -e 's|setuptools-scm>=3.5.0|setuptools-scm|g' setup.cfg
sed -i -e '/addopts/d' tox.ini

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/py7zr
%python_expand %fdupes %{buildroot}%{$python_sitelib}
for i in __init__.py __main__.py archiveinfo.py callbacks.py cli.py compressor.py helpers.py py7zr.py ; do
  %python_expand chmod +x %{buildroot}%{$python_sitelib}/py7zr/$i
done

%post
%python_install_alternative py7zr

%postun
%python_uninstall_alternative py7zr

%check
# different format of argparse in python3.10
python310_donttest=("-k" "not (test_cli_help or test_cli_no_subcommand)")
%pytest -m "not benchmark" "${$python_donttest[@]}"

%files %{python_files}
%license LICENSE
%doc README.rst Changelog.rst
%{python_sitelib}/py7zr
%{python_sitelib}/py7zr-%{version}*-info
%python_alternative %{_bindir}/py7zr

%changelog
