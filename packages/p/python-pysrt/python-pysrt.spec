#
# spec file for package python-pysrt
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
Name:           python-pysrt
Version:        1.1.2
Release:        0
Summary:        SubRip (.srt) subtitle parser and writer
License:        GPL-3.0-only
URL:            https://github.com/byroot/pysrt
Source0:        https://files.pythonhosted.org/packages/source/p/pysrt/pysrt-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-chardet
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
BuildArch:      noarch
%python_subpackages

%description
pysrt is a python library to search and download subtitles.
It comes with an easy to use CLI suitable for direct use or cron jobs.

%prep
%setup -q -n pysrt-%{version}
# Remove shebang from non-executable file
sed -e '1d' -i pysrt/commands.py

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/srt
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative srt

%postun
%python_uninstall_alternative srt

%files %{python_files}
%doc README.rst
%python_alternative %{_bindir}/srt
%{python_sitelib}/pysrt
%{python_sitelib}/pysrt-%{version}-py%{python_version}.egg-info

%changelog
