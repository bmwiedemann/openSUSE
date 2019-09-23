#
# spec file for package python-pysrt
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
Name:           python-pysrt
Version:        1.1.1
Release:        0
Summary:        SubRip (.srt) subtitle parser and writer
License:        GPL-3.0
Group:          Development/Languages/Python
Url:            https://github.com/byroot/pysrt
Source0:        https://pypi.io/packages/source/p/pysrt/pysrt-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-chardet
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
%python_exec %{_bindir}/nosetests

%files %{python_files}
%defattr(-,root,root)
%python3_only %{_bindir}/srt
%{python_sitelib}/pysrt
%{python_sitelib}/pysrt-%{version}-py%{python_version}.egg-info

%changelog
