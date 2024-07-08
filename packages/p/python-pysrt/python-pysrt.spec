#
# spec file for package python-pysrt
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


Name:           python-pysrt
Version:        1.1.2
Release:        0
Summary:        SubRip (.srt) subtitle parser and writer
License:        GPL-3.0-only
URL:            https://github.com/byroot/pysrt
Source0:        https://files.pythonhosted.org/packages/source/p/pysrt/pysrt-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#byroot/pysrt#74946098ce136a5b4b1d5766ca573e999c785686
Patch0:         use-assertequal.patch
BuildRequires:  %{python_module chardet}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-chardet
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
pysrt is a python library to search and download subtitles.
It comes with an easy to use CLI suitable for direct use or cron jobs.

%prep
%autosetup -p1 -n pysrt-%{version}
# Remove shebang from non-executable file
sed -e '1d' -i pysrt/commands.py

%build
%pyproject_wheel

%install
%pyproject_install
mv %{buildroot}%{_bindir}/srt %{buildroot}%{_bindir}/pysrt-srt
%python_clone -a %{buildroot}%{_bindir}/pysrt-srt
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative pysrt-srt

%postun
%python_uninstall_alternative pysrt-srt

%files %{python_files}
%doc README.rst
%python_alternative %{_bindir}/pysrt-srt
%{python_sitelib}/pysrt
%{python_sitelib}/pysrt-%{version}.dist-info

%changelog
