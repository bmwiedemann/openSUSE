#
# spec file for package python-rarfile
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-rarfile
Version:        3.0
Release:        0
Summary:        RAR Archive Reader for Python
License:        ISC
Group:          Development/Languages/Python
Url:            https://rarfile.readthedocs.org/
Source0:        https://pypi.io/packages/source/r/rarfile/rarfile-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Sphinx >= 1.3
Requires:       bsdtar
Recommends:     unrar
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
This is a Python module for RAR archive reading. It supports both RAR
2.x and 3.x archives, multi volume archives, Unicode filenames,
password-protected archives, archive and file comments. The archive
parsing and non-compressed files are handled in pure Python code, for
compressed files, the "unrar" utility is run.

%package doc
Summary:        RAR Archive Reader for Python (Documentation)
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
Python module for RAR archive reading.

This package contains technical documentation.

%prep
%setup -q -n rarfile-%{version}

%build
%python_build
make %{?_smp_mflags} -C doc html
rm doc/_build/html/.buildinfo
sed -i 's/\r$//' doc/_build/html/objects.inv

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%doc LICENSE
%pycache_only %{python_sitelib}/__pycache__/rarfile.*.py*
%{python_sitelib}/rarfile.py*
%{python_sitelib}/rarfile-%{version}-py%{python_version}.egg-info

%files %{python_files doc}
%defattr(-,root,root,-)
%doc LICENSE doc/_build/html/

%changelog
